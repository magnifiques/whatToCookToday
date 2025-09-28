# 🍳 WhatToCookToday

**Struggling to decide what to cook with the ingredients you already have? We've got you covered!**

WhatToCookToday is an AI-powered recipe recommendation system that helps you discover delicious recipes based on the ingredients you have in your kitchen. Simply tell us what's available, and we'll instantly suggest personalized recipes you can make right now.

## ✨ Features

- **Smart Ingredient Recognition**: Understands natural language ingredient descriptions
- **Instant Recipe Suggestions**: Get recipe recommendations in seconds
- **Beginner-Friendly Instructions**: Clear, step-by-step cooking guidance
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Real-time Streaming**: Watch recipes appear as they're generated

## 🚀 Live Demo

Try the live application: [WhatToCookToday on Hugging Face Spaces](https://huggingface.co/spaces/vapit/whattocooktoday)

## 🛠️ Tech Stack

- **Frontend**: Gradio with custom CSS styling
- **AI Model**: OpenAI GPT-4o-mini for recipe generation
- **Vector Database**: ChromaDB with Chroma-langchain integration
- **Embeddings**: HuggingFace sentence-transformers/all-MiniLM-L6-v2
- **Database Storage**: Google Drive integration for ChromaDB persistence
- **Deployment**: Hugging Face Spaces

## 🔧 Configuration

### ChromaDB Setup

The application automatically downloads and extracts the ChromaDB from Google Drive on first run. The database contains pre-indexed recipe data for fast retrieval.

## 💡 Usage Examples

**Simple ingredients:**
```
"I have tomato and pasta, what should I cook?"
```

**Multiple ingredients:**
```
"I have chicken, potatoes, and onions, what can I make?"
```

**Pantry staples:**
```
"I have rice and beans, any recipe ideas?"
```

## 🏗️ Architecture

```
User Input → Ingredient Processing → Vector Search (ChromaDB) → 
Recipe Retrieval → GPT-4o Processing → Formatted Recipe Output
```

### Key Components

1. **`app.py`**: Main Gradio interface with custom styling
2. **`generate_results.py`**: OpenAI integration for recipe formatting
3. **`chroma_utils.py`**: ChromaDB operations and vector retrieval
4. **Database**: Pre-indexed recipe collection stored in ChromaDB

## 🎨 Features in Detail

### Smart Recipe Generation
- Uses RAG (Retrieval-Augmented Generation) for contextual recipe suggestions
- Combines vector search with LLM generation for accurate results
- Formats output in clean, readable Markdown

### User Experience
- Real-time streaming responses
- Loading indicators and progress feedback
- Mobile-responsive design
- Example prompts for new users

### Performance
- Efficient vector similarity search
- Cached database operations
- Optimized for fast response times

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for the GPT-4o-mini model
- Hugging Face for embeddings and hosting
- ChromaDB for vector database capabilities
- Gradio for the intuitive web interface

## 📞 Contact

Created with 🤎 (and a mixture of mathematics, statistics, and tons of calculations 👩🏽‍🔬) by **Arpit Vaghela**

- GitHub: [@magnifiques](https://github.com/magnifiques)
- Feel free to reach out for questions or collaborations!

---
