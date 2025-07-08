# SmartKart: GNN-Powered In-Store Recommendation & Pathfinding System

This project presents SmartKart, a novel recommendation system designed for a retail environment. It leverages Graph Neural Networks (GNNs) on product co-purchase data to generate powerful item embeddings. These embeddings are then used in a hybrid recommendation engine that provides real-time suggestions and calculates the most efficient in-store path for shoppers to retrieve their recommended items.

The entire end-to-end workflow—from data simulation and model training to final recommendation logic—is detailed and executable in the primary Jupyter Notebook.

---

## 🚀 Features

* **End-to-End Walkthrough:** The project is consolidated into a single, comprehensive Jupyter Notebook (`SmartKart_Recommendation_System.ipynb`).
* **GNN-Based Embeddings:** Utilizes a GraphSAGE model trained on the `ogbn-products` dataset to learn item embeddings that capture complex co-purchase relationships.
* **High-Speed Similarity Search:** Implements Facebook AI's FAISS library for efficient, large-scale similarity searches to find related products in real-time.
* **Hybrid Recommendation Engine:** A sophisticated API that combines candidates from embedding similarity and trending products, then re-ranks them based on cart contents, session activity, and inventory awareness.
* **Smart Pathfinding Module:** Includes a `networkx`-based store graph module to find the most efficient in-store path for shoppers.

---

## 📂 Project Structure

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

---

## ⚙️ Installation

To run the project, first clone the repository and install the necessary dependencies.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/SmartKart-GNN-Recommender.git](https://github.com/your-username/SmartKart-GNN-Recommender.git)
    cd SmartKart-GNN-Recommender
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    This project requires specific PyTorch libraries. It's best to install these first.

    * **For CPU-only systems:**
        ```bash
        pip install torch torch-scatter torch-sparse torch-cluster -f [https://data.pyg.org/whl/torch-2.1.0+cpu.html](https://data.pyg.org/whl/torch-2.1.0+cpu.html)
        pip install -r requirements.txt
        ```
    * **For GPU systems (example with CUDA 12.1):**
        ```bash
        pip install torch torch-scatter torch-sparse torch-cluster -f [https://data.pyg.org/whl/torch-2.1.0+cu121.html](https://data.pyg.org/whl/torch-2.1.0+cu121.html)
        pip install -r requirements.txt
        ```

---

## 🏃‍♀️ How to Run

The entire project is designed to be run from the Jupyter Notebook.

**Start Jupyter Lab or Jupyter Notebook and open `notebooks/SmartKart_Recommendation_System.ipynb`.**

Running the cells sequentially will guide you through the entire process:
1.  **Environment Setup:** Installs all necessary packages.
2.  **Data Loading & Simulation:** Downloads the OGB dataset, creates a subgraph, and simulates user/product data.
3.  **Model Training:** Defines and trains the GraphSAGE model to generate product embeddings.
4.  **FAISS Indexing:** Builds a FAISS index for fast similarity lookups.
5.  **Recommendation API:** Defines and tests the final recommendation function with multiple scenarios.

---

## 🧠 Methodology

The recommendation system is built on a multi-stage pipeline detailed in the notebook:

1.  **Data Loading & Subgraphing:** The large `ogbn-products` graph (2.4M nodes) is loaded, and a smaller, manageable subgraph is created for efficient prototyping.

2.  **GNN Training for Embeddings:** A GraphSAGE model is trained on the subgraph to learn product categories. Its penultimate layer generates rich 40-dimensional embeddings that place co-purchased products close to each other in vector space.

3.  **FAISS Indexing:** The embeddings are indexed using `faiss.IndexFlatL2` for extremely fast nearest neighbor searches, enabling real-time similarity lookups.

4.  **Hybrid Recommendation API:** The final `get_recommendations` function fetches candidates from similarity searches and trending products, then re-ranks them using session/cart relevance and inventory data.

---

## 📞 Contact

Your Name - [anmol752005@gmail.com](mailto:anmol752005@gmail.com)

Project Link: [https://github.com/your-username/SmartKart-GNN-Recommender](https://github.com/your-username/SmartKart-GNN-Recommender)
