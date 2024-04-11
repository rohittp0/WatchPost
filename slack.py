import json
from pathlib import Path


def to_slack_json(post: str, post_file: Path, repo: str, base_repo: str):
    return {
        "text": f"WatchPost Daily Update for {repo}",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": post
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "View on Github"
                        },
                        "url": f"{base_repo}{repo}/{post_file}"
                    }
                ]
            }
        ]
    }


def write_to_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)
