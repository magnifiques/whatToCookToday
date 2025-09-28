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

    response = ""
    for chunk in format_recipes(query, raw_context):
        response += chunk
        yield response

    

article = "Created with 🤎 (and a mixture of mathematics, statistics, and tons of calculations 👩🏽‍🔬) by Arpit Vaghela [GitHub](https://github.com/magnifiques)"

example_list = [
    ["I have tomato and pasta, what should I cook?"],
    ["I have chicken and potatoes, what can I make?"],
    ["I have rice and beans, any recipe ideas?"]
]

# Gradio Interface
# demo = gr.Interface(
#     fn=get_response,  # Function to call
#     inputs="text",     # Input type
#     outputs=gr.Markdown(label="Suggested Recipes"),   
#     title="WhatToCookToday", 
#     description="""Welcome to WhatToCookToday! 🍳  
# Struggling to decide what to cook with the ingredients you already have?  
# we've got you covered.

# Just tell us what’s in your kitchen, and we’ll instantly suggest a delicious recipes you can make with those ingredients.  

# You don’t need to search endlessly, we turn your pantry into a personalized recipe book!

# How to use it:  
# - Simply type the ingredients you have, like "I have tomatoes and pasta, what can I cook?"  
# - You can list multiple ingredients in any order or phrasing.  
# - The assistant will respond with a recipe tailored to what you’ve got.

# Example prompts you can try:  
# 1. "I have tomato and pasta, what should I cook?"  
# 2. "I have chicken and potatoes, what can I make?"  
# 3. "I have rice and beans, any recipe ideas?"

# ⏱️ Fast. 🍲 Simple. 🧠 Smart.
# """,  
#     article=article,
#     examples=example_list,
#     cache_examples=False,
#     live=False
# )

# if __name__ == "__main__":
#     demo.launch(
#         server_name="0.0.0.0",  
#         server_port=7860,       
#         debug=False,
#         share=True)

# Create a custom Blocks interface for better control
with gr.Blocks(
    title="WhatToCookToday",
    theme=gr.themes.Soft(),
    css="""
    .recipe-output {
        max-height: 600px;
        overflow-y: auto;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: #fafafa;
    }
    """
) as demo:
    
    gr.HTML("""
    <div style="text-align: center; padding: 20px;">
        <h1>🍳 WhatToCookToday</h1>
        <p style="font-size: 18px; color: #666;">
            Struggling to decide what to cook with the ingredients you already have? We've got you covered!
        </p>
    </div>
    """)
    
    gr.Markdown("""
    **How to use:**
    - Simply type the ingredients you have, like "I have tomatoes and pasta, what can I cook?"  
    - You can list multiple ingredients in any order or phrasing.  
    - The assistant will respond with a recipe tailored to what you've got.

    ⏱️ **Fast.** 🍲 **Simple.** 🧠 **Smart.**
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            input_text = gr.Textbox(
                placeholder="Enter your ingredients here... (e.g., 'I have tomatoes and pasta')",
                label="What ingredients do you have?",
                lines=3
            )
            
            submit_btn = gr.Button("🔍 Find Recipes", variant="primary", size="lg")
            
            gr.Examples(
                examples=example_list,
                inputs=input_text,
                label="Try these examples:"
            )
        
        with gr.Column(scale=3):
            output_markdown = gr.Markdown(
                label="Suggested Recipes",
                elem_classes=["recipe-output"],
                container=True,
                value="Your delicious recipes will appear here! 👨‍🍳"
            )
    
    # Add loading behavior
    submit_btn.click(
        fn=lambda: gr.update(value="🔄 **Searching for recipes...** \n\nPlease wait while we find the perfect recipes for your ingredients!", visible=True),
        inputs=None,
        outputs=output_markdown,
        queue=False
    ).then(
        fn=get_response,
        inputs=input_text,
        outputs=output_markdown,
        show_progress=True
    )
    
    # Also allow Enter key submission
    input_text.submit(
        fn=lambda: gr.update(value="🔄 **Searching for recipes...** \n\nPlease wait while we find the perfect recipes for your ingredients!", visible=True),
        inputs=None,
        outputs=output_markdown,
        queue=False
    ).then(
        fn=get_response,
        inputs=input_text,
        outputs=output_markdown,
        show_progress=True
    )
    
    gr.HTML(f"""
    <div style="text-align: center; padding: 20px; margin-top: 30px; border-top: 1px solid #eee;">
        {article}
    </div>
    """)
    
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",  # Important for HF Spaces
        server_port=7860,       # Default port for HF Spaces
        debug=False,
        share=False             # Don't use share=True on HF Spaces
    )