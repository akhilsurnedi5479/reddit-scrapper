import json
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_topics(input_file="cache.json", output_file="cache.json"):
    with open(input_file, "r") as f:
        posts = json.load(f)

    for post in posts:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  #  Temporary fallback
                messages=[
                    {
                        "role": "system",
                        "content": "You categorize AskReddit questions into topics like funny, serious, weird, relationship, nostalgia, dark, etc."
                    },
                    {
                        "role": "user",
                        "content": f"What category best fits this Reddit question?\n\n'{post['title']}'"
                    }
                ]
            )
            post["topic"] = response.choices[0].message.content.strip().lower()
            time.sleep(1.2)  # 🛑 Prevent hitting rate limits
        except Exception as e:
            print(f"❌ Error on post '{post['title']}': {e}")
            post["topic"] = "uncategorized"

    with open(output_file, "w") as f:
        json.dump(posts, f, indent=2)

    print("✅ Finished labeling posts and saved to cache.")

if __name__ == "__main__":
    classify_topics()
