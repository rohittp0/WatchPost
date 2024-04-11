import json
import os
from pathlib import Path

from slack import to_slack_json


def main():
    posts_folder = Path("posts")
    posts_folder.mkdir(exist_ok=True)

    post_index = len([*posts_folder.iterdir()]) + 1

    post_file = posts_folder / f"{post_index}.md"
    post = f"# Post {post_index}\n\nHello, World! 🚀\n"

    post_file.write_text(post, encoding="utf-8")
    repo = json.load(open("repo.json"))

    post_json = to_slack_json(
        post,
        post_index,
        repo["full_name"],
        os.environ.get("CURRENT_REPO_URL")
    )

    json.dump(post_json, open("slack.json", "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
