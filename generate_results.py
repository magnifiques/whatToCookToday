import re
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def format_recipes(query, raw_context):
    prompt = f"""
    You are a helpful cooking assistant.
    The user asked: {query}

    Here are some relevant recipes from the database:
    {raw_context}

    Please:
    1. Summarize their ingredients clearly.
    2. Rewrite the steps in a beginner-friendly, easy-to-follow way.
    3. Keep the tone warm and encouraging, like you're guiding a new cook.
    """



    with client.chat.completions.stream(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    ) as stream:
        for event in stream:
            if event.type == "message.delta":
                yield event.delta  # send partial text to Gradio
