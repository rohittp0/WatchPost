import json
import os
from pathlib import Path

FIRST_POST_TEMPLATE = """\
This is the first post in a series of posts that I will be posting on LinkedIn about the project. \
Include what the project is and what I have done so far ( based on diff ).
"""

NEXT_POST_TEMPLATE = """\
This is the next post in a series of posts that I will be posting on LinkedIn about the project. \
Keep the continuity from the previous post. Include what I have done since the last post ( based on diff ).
"""

PROMPT_TEMPLATE = """\
Create a LinkedIn post based on the following git diff. Make the post engaging and fun to read. \
{post_description}

{diff}

Context
=======

Project Description: {project_description}
Github Repo: {repo_url}
Previous Post: {previous_post}
"""

SYSTEM_MESSAGE = ("You are a LinkedIn content creator. "
                  "You should create engaging LinkedIn posts based on the information provided by the user.")
CONFIG = {
    "posts_folder": Path("posts"),
    "diffs_folder": Path("diffs"),
    "repo": json.load(open("repo.json", "r")),
    "slack_file": "slack.json",
    "first_post_template": FIRST_POST_TEMPLATE,
    "next_post_template": NEXT_POST_TEMPLATE,
    "prompt_template": PROMPT_TEMPLATE,
    "system_message": SYSTEM_MESSAGE,
    "base_repo_url": os.environ["CURRENT_REPO_URL"],
    "open_ai_key": os.environ["OPEN_AI_API_KEY"],
    "openai_model": os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
}
