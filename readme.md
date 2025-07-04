# AskReddit Companion Bot

A fun Streamlit app that scrapes top posts from r/AskReddit, classifies them into topics using GPT, and lets users explore threads by mood or theme.

## 🧰 Tech Stack
- PRAW for Reddit scraping
- OpenAI GPT-4 for topic classification
- Streamlit for interactive UI

## 🚀 How to Run
1. Clone the repo
2. Set your Reddit and OpenAI API keys in `reddit_scraper.py` and `topic_classifier.py`
3. Install dependencies:
pip install -r requirements.txt
4. Fetch and label posts: 
`
python reddit_scraper.py`
`
python topic_classifier.py
`
5. Launch the app: `streamlit run app.py`
`

## 💡 Example Topics
`funny`, `serious`, `relationship`, `nostalgia`, `weird`, `dark`

## 📁 Cache
The `cache.json` file stores the latest posts and topics for fast access.\

`Made this completely using gpt4o`



