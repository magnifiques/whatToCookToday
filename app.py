
import gradio as gr
from langchain_utils import generate_answer_langchain
from chroma_utils import get_retriever

import os
import zipfile
import gdown

CHROMA_DIR = "./chroma-db-langchain"  s
ZIP_PATH = "chroma_db.zip"
DRIVE_FILE_ID = "1rvD_Ic9ojmx3ORaut2jxgagwLn0bE2cJ"

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
    response = generate_answer_langchain(query, retriever)
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
