import praw
import json
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_askreddit_posts(limit=50):
    subreddit = reddit.subreddit("AskReddit")
    posts = []

    for post in subreddit.hot(limit=limit):
        posts.append({
            "id": post.id,
            "title": post.title,
            "url": post.url,
            "score": post.score
        })

    with open("cache.json", "w") as f:
        json.dump(posts, f, indent=2)

    print(f"✅ Fetched and saved {len(posts)} AskReddit posts.")

if __name__ == "__main__":
    fetch_askreddit_posts()
