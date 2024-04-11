from openai import OpenAI

from config import CONFIG
from slack import to_slack_json, write_to_file


def init():
    CONFIG["posts_folder"].mkdir(exist_ok=True)

    diff_index = len([*CONFIG["diffs_folder"].iterdir()])
    diff_file = CONFIG["diffs_folder"] / f"{diff_index}.txt"

    post_index = len([*CONFIG["posts_folder"].iterdir()]) + 1
    post_file = CONFIG["posts_folder"] / f"{post_index}.md"
    previous_post_file = CONFIG["posts_folder"] / f"{post_index - 1}.md"

    diff = diff_file.read_text(encoding="utf-8")
    previous_post = previous_post_file.read_text(encoding="utf-8") if previous_post_file.exists() else None

    return {
        "diff": diff,
        "previous_post": previous_post,
        "post": post_file,
    }


def get_prompt(init_data):
    if init_data["previous_post"]:
        post_description = CONFIG["next_post_template"]
    else:
        post_description = CONFIG["first_post_template"]

    return CONFIG["prompt_template"].format(
        post_description=post_description,
        diff=init_data["diff"],
        project_description=CONFIG["repo"]["description"],
        repo_url=CONFIG["repo"]["html_url"],
        previous_post=init_data["previous_post"] or "No previous post",
    )


def main():
    init_data = init()
    prompt = get_prompt(init_data)

    client = OpenAI(api_key=CONFIG["open_ai_key"])
    response = client.chat.completions.create(
        model=CONFIG["openai_model"],
        messages=[
            {"role": "system", "content": CONFIG["system_message"]},
            {"role": "user", "content": prompt},
        ]
    )

    content = response.choices[0].message.content
    init_data["post"].write_text(content, encoding="utf-8")

    slack_json = to_slack_json(
        content,
        init_data["post"],
        CONFIG["repo"]["full_name"],
        CONFIG["base_repo_url"]
    )

    write_to_file(CONFIG["slack_file"], slack_json)


if __name__ == "__main__":
    main()
