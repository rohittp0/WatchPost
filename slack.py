def to_slack_json(post: str, post_id: int, repo: str, base_repo: str):
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
                        "url": f"{base_repo}{repo}/posts/{post_id}.md"
                    }
                ]
            }
        ]
    }
