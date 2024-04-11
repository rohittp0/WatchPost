import json
import os
from pathlib import Path

FIRST_POST_TEMPLATE = """\
This is the first post in a series of posts that I will be posting on LinkedIn about the project. \
Include what the project is and what I have done so far ( based on diff and project description ).
"""

NEXT_POST_TEMPLATE = """\
This is the next post in a series of posts that I will be posting on LinkedIn about the project. \
Include what I have done since the last post ( based on diff ).
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

SYSTEM_MESSAGE = """\
You are a LinkedIn content creator AI. You have to create a LinkedIn post based on the given prompt. \
Make sure the post is engaging and fun to read, while also being semi-formal. \
Make sure to include Github repo link in the post. Do not directly quote the git diff, write based on it.\
In the first post include an explanation about the project based on the project description. \
If this is not the first post, previous post will be included in the context, use that to maintain continuity.\
The response created should be in plain text format so that it can be easily copied and pasted to LinkedIn post.\
"""

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
