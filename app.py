import streamlit as st
import json
import random

st.title("💬 AskReddit Companion Bot")

with open("cache.json", "r") as f:
    posts = json.load(f)

topics = sorted(set(p["topic"] for p in posts))

selected_topic = st.selectbox("Choose a topic", topics)
count = st.slider("How many threads?", 1, 10, 3)

if st.button("Get Threads"):
    filtered = [p for p in posts if p["topic"] == selected_topic]
    chosen = random.sample(filtered, min(count, len(filtered)))

    for post in chosen:
        st.markdown(f"**{post['title']}**  \n[🔗 View thread]({post['url']})  \n👍 Score: {post['score']}")
