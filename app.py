import gradio as gr
from generate_results import format_recipes
from chroma_utils import get_retriever

import os
import zipfile
import gdown

CHROMA_DIR = "./chroma-db-langchain"  
ZIP_PATH = "chroma_db.zip"

# Access the secret key
DRIVE_FILE_ID = os.getenv("DRIVE_FILE_ID")

def download_and_extract_chroma():
    if not os.path.exists(CHROMA_DIR):  # avoid re-download
        print("Downloading Chroma DB...")
        url = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"
        gdown.download(url, ZIP_PATH, quiet=False)

        print("Extracting...")
        with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(CHROMA_DIR)

        print("Chroma DB ready.")
    else:
        print("Chroma DB already exists, skipping download.")

# Call this once at the beginning
download_and_extract_chroma()



def get_response(query):
    # Call generate_answer_langchain with the retriever and model setup
    retriever = get_retriever()
    
    docs = retriever.invoke(query)
    raw_context = "\n\n".join([doc.page_content for doc in docs])

    return "".join(format_recipes(query, raw_context))

    

article = "Created with 🤎 (and a mixture of mathematics, statistics, and tons of calculations 👩🏽‍🔬) by Arpit Vaghela [GitHub](https://github.com/magnifiques)"

example_list = [
    ["I have tomato and pasta, what should I cook?"],
    ["I have chicken and potatoes, what can I make?"],
    ["I have rice and beans, any recipe ideas?"]
]

# Gradio Interface
demo = gr.Interface(
    fn=get_response,  # Function to call
    inputs="text",     # Input type
    outputs=gr.Textbox(lines=10, label="Suggested Recipes"),   
    title="WhatToCookToday", 
    description="""Welcome to WhatToCookToday! 🍳  
Struggling to decide what to cook with the ingredients you already have?  
we've got you covered.

Just tell us what’s in your kitchen, and we’ll instantly suggest a delicious recipes you can make with those ingredients.  

You don’t need to search endlessly, we turn your pantry into a personalized recipe book!

How to use it:  
- Simply type the ingredients you have, like "I have tomatoes and pasta, what can I cook?"  
- You can list multiple ingredients in any order or phrasing.  
- The assistant will respond with a recipe tailored to what you’ve got.

Example prompts you can try:  
1. "I have tomato and pasta, what should I cook?"  
2. "I have chicken and potatoes, what can I make?"  
3. "I have rice and beans, any recipe ideas?"

⏱️ Fast. 🍲 Simple. 🧠 Smart.
""",  
    article=article,
    examples=example_list,
    live=True
)

if __name__ == "__main__":
    demo.launch(debug=False, # print errors locally?
            share=False)
