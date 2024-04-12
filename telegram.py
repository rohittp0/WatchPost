from pathlib import Path


def to_telegram_json(post: str, post_file: Path, repo: str, base_repo: str, chat_id: str):
    return {
        "chat_id": chat_id,
        "text": post,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "View on GitHub",
                        "url": f"{base_repo}{repo}/{post_file}"
                    }
                ]
            ]
        }
    }
