
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap
from langchain_core.output_parsers import StrOutputParser
import re
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig

# --- TEXT CLEANING ---
def clean_text(text):
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# --- PROMPT TEMPLATE ---
prompt_template = PromptTemplate(
    input_variables=["query", "recipes"],
    template="""You are a smart cooking assistant.
The user has the following ingredients: "{query}".

Here are some recipes:
<recipes>
{recipes}
</recipes>

From the recipes above, identify the TWO recipes that best utilize the user's available ingredients mentioned in their query. Consider recipes where the user's ingredients are primary components.

For each of the identified recipes, output the information STRICTLY in the following format. Use the exact delimiters shown:

--- Recipe 1 ---
Title: <title of recipe 1>
Ingredients: <ingredients of recipe 1>
Instructions: <instructions of recipe 1>
--- End Recipe 1 ---

--- Recipe 2 ---
Title: <title of recipe 2>
Ingredients: <ingredients of recipe 2>
Instructions: <instructions of recipe 2>
--- End Recipe 2 ---

Do not include any other text or explanations outside of this specified format.
"""
)

# --- LANGCHAIN SETUP ---
def get_llm():
    model_name = "mistralai/Mistral-7B-Instruct-v0.2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Configure quantization
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype="float16",
        bnb_4bit_use_double_quant=False,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        # quantization_config=bnb_config,
        # device_map="auto",
        max_memory={0: "10GB"},
    )

    # Create a text generation pipeline
    text_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=2048,
        temperature=0.5,
        top_p=0.9,
        do_sample=True,
        return_full_text=False,
    )

    llm = HuggingFacePipeline(pipeline=text_pipeline)
    return llm

def generate_answer_langchain(query, retriever):
    # Step 1: Retrieve docs from ChromaDB
    docs = retriever.invoke(query)
    raw_context = "\n\n".join([doc.page_content for doc in docs])
    cleaned_context = clean_text(raw_context)

    # Step 2: Create the chain
    chain = (
        RunnableMap({
            "query": lambda x: query,
            "recipes": lambda x: cleaned_context
        })
        | prompt_template
        | get_llm()
        | StrOutputParser()
        | RunnableLambda(lambda x: clean_text(x))  # Optional post-cleaning
    )

    # Step 3: Run the chain
    return chain.invoke({})
