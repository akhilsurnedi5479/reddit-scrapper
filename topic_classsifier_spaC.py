import json
import spacy

# Load a small English model (install with: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

TOPIC_KEYWORDS = {
    "funny": ["joke", "laugh", "funny", "hilarious", "silly", "meme"],
    "relationship": ["wife", "husband", "girlfriend", "boyfriend", "partner", "crush", "relationship"],
    "career": ["job", "boss", "work", "career", "interview", "promotion"],
    "nostalgia": ["childhood", "remember", "memory", "nostalgic", "old days"],
    "serious": ["mental", "health", "depression", "anxiety", "therapy", "trauma"],
    "weird": ["weird", "strange", "creepy", "odd", "unusual"],
    "dark": ["death", "murder", "crime", "dark", "suicide", "abuse"]
}

def classify(title):
    doc = nlp(title.lower())
    for topic, keywords in TOPIC_KEYWORDS.items():
        for word in keywords:
            if word in doc.text:
                return topic
    return "uncategorized"

def classify_topics(input_file="cache.json", output_file="cache2.json"):
    with open(input_file, "r") as f:
        posts = json.load(f)

    for post in posts:
        post["topic"] = classify(post["title"])

    with open(output_file, "w") as f:
        json.dump(posts, f, indent=2)

    print("✅ Classified posts using spaCy and saved to cache.")

if __name__ == "__main__":
    classify_topics()
