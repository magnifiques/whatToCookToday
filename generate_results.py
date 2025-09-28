import re
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def format_recipes(query, raw_context):
    prompt = f"""
    You are a helpful cooking assistant that responds in markdown format.
    The user asked: {query}

    Here are some relevant recipes from the database:
    {raw_context}

    Please:
    1. Summarize their ingredients clearly.
    2. Rewrite the steps in a beginner-friendly, easy-to-follow way.
    3. Keep the tone warm and encouraging, like you're guiding a new cook.
    4. Format your response in proper Markdown with:
       - Use ## for recipe titles
       - Use **bold** for ingredient lists and important notes
       - Use numbered lists (1. 2. 3.) for cooking steps
       - Use - for bullet points when listing ingredients
       - Use > for helpful tips or notes
    
    Example format:
    ## Recipe Name
    
    **Ingredients:**
    - ingredient 1
    - ingredient 2
    
    **Instructions:**
    1. Step one
    2. Step two
    
    > **Tip:** Helpful cooking tip here
    """

    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            stream=True
        )
        
        # Collect all chunks into a single response
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                
        return full_response
                
    except Exception as e:
        return f"Error generating response: {str(e)}"

   
