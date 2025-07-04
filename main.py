import praw
import pandas as pd

# Set up Reddit API credentials (replace values below)
reddit = praw.Reddit(
    client_id='9yA6EAIM_nxMYzQ9ibLUgw',
    client_secret='vRrnIRIKOxYLpX1dXh3A5MJ59wtfEw',
    user_agent='scrapper-v1 by /u/arrow5479'
)

def scrape_subreddit(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)

    posts_data = []
    for post in subreddit.hot(limit=limit):
        posts_data.append({
            'title': post.title,
            'score': post.score,
            'id': post.id,
            'url': post.url,
            'num_comments': post.num_comments,
            'created_utc': post.created_utc,
            'selftext': post.selftext
        })

    df = pd.DataFrame(posts_data)
    df.to_csv(f"{subreddit_name}_posts.csv", index=False)
    print(f"Scraped {len(df)} posts from r/{subreddit_name} into {subreddit_name}_posts.csv")

# Example usage
if __name__ == '__main__':
    scrape_subreddit('python', limit=50)
