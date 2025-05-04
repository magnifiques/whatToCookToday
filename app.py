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

    response = format_recipes(raw_context)
    return response

# Gradio Interface
iface = gr.Interface(
    fn=get_response,  # Function to call
    inputs="text",     # Input type
    outputs="text",    # Output type
    title="Smart Cooking Assistant",  # Title of the interface
    description="Ask the assistant for recipes based on available ingredients!"
)

if __name__ == "__main__":
    iface.launch()
