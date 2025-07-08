<p align="center">
  <img src="./assets/smartkart.png" alt="SmartKart Banner">
  </p>

<h1 align="center">SmartKart: GNN-Powered In-Store Recommender</h1>

<p align="center">
  A novel recommendation system that combines Graph Neural Network embeddings with in-store smart pathfinding to enhance the retail shopping experience.
</p>

<p align="center">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
    <img src="https://img.shields.io/github/languages/top/anmol0705/SmartKart-Recommendation-System" alt="Top Language">
    <img src="https://img.shields.io/github/repo-size/anmol0705/SmartKart-Recommendation-System" alt="Repo Size">
</p>

---

## 🚀 Core Features

* 🧠 **GNN-Based Embeddings:** Employs a **GraphSAGE** model on the `ogbn-products` dataset to generate powerful item embeddings from co-purchase data.
* ⚡️ **High-Speed Similarity Search:** Integrates **Facebook AI's FAISS** library for efficient, real-time similarity searches to discover related products.
* 🛍️ **Hybrid Recommendation Engine:** A dynamic API that sources candidates from both embedding similarity and trending items, then re-ranks them based on user context (cart, session) and inventory levels.
* 🗺️ **Smart Pathfinding:** Includes a `networkx`-powered module to calculate the most efficient in-store route for a shopper to collect their recommended items.

---

## 🛠️ Technologies Used

This project leverages a modern stack for graph machine learning and data science:

* **Primary Language:** Python
* **ML Frameworks:** PyTorch, PyTorch Geometric
* **Core Libraries:** OGB, FAISS, NumPy, Pandas
* **Pathfinding:** NetworkX
* **Development Environment:** Jupyter Notebook

---

## 📂 Project Structure

The repository is organized for clarity and ease of use, with the main workflow contained in the Jupyter Notebook.

---

```
SmartKart-GNN-Recommender/
├── README.md
├── requirements.txt
├── notebooks/
│   └── SmartKart_Recommendation_System.ipynb   # Main notebook with the end-to-end workflow.
└── src/
    ├── inspect_product_categories.py          # Utility to explore product categories.
    └── pathfinding/
        ├── store_graph.py                     # Defines and implements the smart store pathfinding.
        └── test_pathfinding.py                # Example usage of the pathfinding module.
```
## ⚙️ Getting Started

### Prerequisites

* Python 3.8+
* `pip` and `venv`

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/anmol0705/SmartKart-Recommendation-System](https://github.com/anmol0705/SmartKart-Recommendation-System)
    cd SmartKart-Recommendation-System
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install PyTorch and PyG Dependencies:**
    It's crucial to install the correct versions for your system's architecture (CPU or GPU).

    * **For CPU-only:**
        ```bash
        pip install torch torch-scatter torch-sparse torch-cluster -f [https://data.pyg.org/whl/torch-2.1.0+cpu.html](https://data.pyg.org/whl/torch-2.1.0+cpu.html)
        ```
    * **For GPU (example with CUDA 12.1):**
        ```bash
        pip install torch torch-scatter torch-sparse torch-cluster -f [https://data.pyg.org/whl/torch-2.1.0+cu121.html](https://data.pyg.org/whl/torch-2.1.0+cu121.html)
        ```

4.  **Install remaining packages:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃‍♀️ How to Run

The entire project is designed to be executed from the primary Jupyter Notebook.

> **Start Jupyter Lab or Jupyter Notebook and open `notebooks/SmartKart_Recommendation_System.ipynb`.**

Running the cells sequentially will guide you through the entire process:
1.  **Environment Setup**: Installs all packages.
2.  **Data Loading & Simulation**: Downloads the OGB dataset and simulates user/product data.
3.  **Model Training**: Trains the GraphSAGE model to generate embeddings.
4.  **FAISS Indexing**: Builds a FAISS index for fast similarity lookups.
5.  **Recommendation API**: Defines and tests the final recommendation function.

---

## 🧠 Methodology Pipeline

The recommendation system follows a multi-stage pipeline:

1.  **Data Loading & Subgraphing**: The large `ogbn-products` graph is loaded, and a smaller subgraph is created for efficient prototyping.
2.  **GNN Training**: A GraphSAGE model is trained on the subgraph to predict product categories. Its penultimate layer generates rich 40-dimensional embeddings.
3.  **FAISS Indexing**: The learned embeddings are indexed using `faiss.IndexFlatL2` to enable real-time nearest neighbor searches.
4.  **Hybrid Recommendation**: The `get_recommendations` function fetches candidates from similarity searches and trending products, then re-ranks them using session/cart relevance and inventory data.

---

## 📞 Contact

Anmol - [anmol752005@gmail.com](mailto:anmol752005@gmail.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-anmol-jain-blue)](https://www.linkedin.com/in/anmol-jain0705/)
[![GitHub](https://img.shields.io/badge/GitHub-anmol0705-grey?logo=github)](https://github.com/anmol0705)
