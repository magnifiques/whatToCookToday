# 🍳 WhatToCookToday

**Struggling to decide what to cook with the ingredients you already have? We've got you covered!**

WhatToCookToday is an AI-powered recipe recommendation system that helps you discover delicious recipes based on the ingredients you have in your kitchen. Simply tell us what's available, and we'll instantly suggest personalized recipes you can make right now.

<img width="1208" height="1228" alt="huggingface co_spaces_vapit_whattocooktoday" src="https://github.com/user-attachments/assets/292424a0-24a6-4303-a100-b602c52216e1" />

## 🎯 Problem Solved

**Food Waste & Meal Planning Challenge:**
- **36% of food waste** occurs at the household level due to poor meal planning
- Users struggle to utilize existing ingredients effectively
- Traditional recipe search requires exact ingredient matching

**Our Solution:**
- **Semantic ingredient understanding** that recognizes ingredient relationships and substitutions
- **Context-aware recommendations** based on what users actually have available
- **Reduces food waste** by maximizing utilization of existing ingredients
- **Simplifies meal planning** with instant, personalized recipe suggestions

## 📊 Dataset & Performance

**Food.com Recipe Dataset:**
- **Source**: [Food.com Recipes and Interactions Dataset](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions) from Kaggle
- **Size**: 180K+ real-world recipes with comprehensive metadata
- **Content**: Recipe titles, ingredients, instructions, ratings, nutritional information, and user interactions
- **Processing**: Extensive data cleaning, normalization, and LangChain-compatible document conversion
- **Quality Assurance**: Filtered for completeness, removed duplicates, and standardized formatting

**Technical Performance:**
- **Search Accuracy**: Semantic embeddings enable context-aware matching beyond keyword limitations
- **Response Time**: Sub-second recipe retrieval through optimized vector search
- **Resource Efficiency**: CPU-compatible model optimized for low-resource environments
- **Scalability**: Efficiently handles large-scale dataset with ChromaDB vector operations# 🍳 WhatToCookToday

**Struggling to decide what to cook with the ingredients you already have? We've got you covered!**

WhatToCookToday is an intelligent recipe recommendation system that tackles food waste and meal planning challenges by helping users discover recipes based on their available ingredients. Built with Retrieval-Augmented Generation (RAG) and powered by 180K+ real-world recipes from the Food.com dataset, this system delivers personalized cooking suggestions through advanced semantic search and natural language processing.

## ✨ Features

- **Smart Ingredient Recognition**: Advanced semantic understanding of natural language ingredient descriptions
- **Massive Recipe Database**: 180K+ real-world recipes from Food.com dataset
- **Context-Aware Search**: Dense vector search using semantic embeddings, eliminating keyword matching limitations
- **RAG Implementation**: Retrieval-Augmented Generation with CPU-optimized models for low-resource environments
- **Real-time Processing**: ChromaDB-powered vector database for instant recipe matching
- **Beginner-Friendly Output**: Clear, step-by-step cooking guidance with markdown formatting
- **Responsive Design**: Gradio-based interactive UI optimized for seamless user experience
- **Food Waste Reduction**: Helps minimize waste by suggesting recipes for existing ingredients

## 🚀 Live Demo

Try the live application: [WhatToCookToday on Hugging Face Spaces](https://huggingface.co/spaces/vapit/whattocooktoday)

## 🛠️ Tech Stack

- **Frontend**: Gradio with custom CSS styling for interactive UI
- **AI Model**: OpenAI GPT-4o-mini optimized for CPU-compatible, low-resource environments
- **RAG Architecture**: Retrieval-Augmented Generation for context-aware recipe recommendations
- **Vector Database**: ChromaDB with dense vector search capabilities
- **Embeddings**: HuggingFace sentence-transformers/all-MiniLM-L6-v2 for semantic understanding
- **Data Processing**: LangChain for document conversion and data preprocessing
- **Dataset**: 180K+ recipes from Food.com with comprehensive data cleaning and normalization
- **Database Storage**: Google Drive integration for ChromaDB persistence
- **Deployment**: Hugging Face Spaces for scalable cloud hosting

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/magnifiques/WhatToCookToday.git
   cd WhatToCookToday
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   DRIVE_FILE_ID=your_google_drive_file_id_here
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

   The app will be available at `http://localhost:7860`

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: OpenAI API key for recipe generation
- `DRIVE_FILE_ID`: Google Drive file ID containing the ChromaDB database

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
User Input → Semantic Processing → Dense Vector Search (ChromaDB) → 
Recipe Retrieval (180K+ Food.com recipes) → RAG Processing (GPT-4o-mini) → 
Formatted Recipe Output
```

### Technical Implementation

**RAG (Retrieval-Augmented Generation) Pipeline:**
1. **Data Preprocessing**: 180K+ Food.com recipes cleaned, normalized, and converted to LangChain-compatible documents
2. **Semantic Embeddings**: HuggingFace transformers create dense vector representations of recipes
3. **Vector Storage**: ChromaDB stores and indexes recipe embeddings for efficient similarity search
4. **Retrieval**: Context-aware search matches user ingredients to relevant recipes without keyword limitations
5. **Generation**: CPU-optimized GPT-4o-mini formats retrieved recipes into beginner-friendly instructions

**Key Technical Advantages:**
- **Semantic Understanding**: Goes beyond keyword matching to understand ingredient relationships
- **Scalability**: Efficiently handles large-scale dataset with optimized vector operations
- **Resource Efficiency**: CPU-compatible implementation suitable for various deployment environments
- **Real-time Performance**: ChromaDB enables sub-second recipe retrieval and matching

### Key Components

1. **`app.py`**: Gradio-based interactive UI with custom styling and natural language input support
2. **`generate_results.py`**: RAG implementation with OpenAI integration for context-aware recipe formatting
3. **`chroma_utils.py`**: ChromaDB operations, vector retrieval, and semantic search functionality
4. **Database**: Pre-processed and indexed 180K+ Food.com recipes with semantic embeddings
5. **Data Pipeline**: LangChain-compatible document processing and normalization system

## 🎨 Features in Detail

### Advanced RAG Implementation
- **Retrieval-Augmented Generation** combines the best of both search and generation
- **Context-aware processing** ensures recipes match available ingredients precisely
- **CPU-optimized models** enable deployment in resource-constrained environments
- **Semantic search** understands ingredient relationships and cooking contexts

### Intelligent Data Processing
- **Large-scale dataset handling** with 180K+ Food.com recipes
- **LangChain integration** for seamless document processing and conversion
- **Data normalization** ensures consistent recipe formatting and quality
- **Vector embedding optimization** for efficient similarity search operations

### User Experience Excellence
- **Natural language processing** supports conversational ingredient input
- **Real-time streaming** responses with progress indicators
- **Mobile-responsive design** optimized for all device types
- **Intuitive interface** designed for seamless cooking workflow integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

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
