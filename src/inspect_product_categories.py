# inspect_product_categories.py

import torch
import os.path as osp
import numpy as np
from ogb.nodeproppred import PygNodePropPredDataset

def main():
    """
    Main function to load the ogbn-products dataset and inspect its product categories.
    """
    # Define the root directory where the dataset is stored or will be downloaded.
    # This should be the same path where you previously downloaded the dataset.
    root = osp.join(osp.dirname(osp.realpath(__file__)), 'content')
    # If running directly in a Colab notebook, you might use root = '/content'
    # root = '/content' # Uncomment this if you are running this specific script directly in Colab

    print(f"Attempting to load ogbn-products dataset from: {root}")
    try:
        dataset = PygNodePropPredDataset(name='ogbn-products', root=root)
        data = dataset[0] # Get the first (and only) graph in the dataset
        print("Dataset loaded successfully.")

        # The labels (data.y) in ogbn-products represent product categories.
        # Ensure y is 1D for easier processing of categories.
        product_categories = data.y.squeeze()

        # Get unique product categories and their counts
        unique_categories, counts = torch.unique(product_categories, return_counts=True)

        print(f"\nTotal number of nodes (products): {data.num_nodes}")
        print(f"Total number of edges (co-purchases): {data.num_edges}")
        print(f"Number of unique product categories: {len(unique_categories)}")

        print("\n--- Product Categories and their Counts ---")
        # Sort categories by their ID for consistent output
        sorted_indices = torch.argsort(unique_categories)
        for i in sorted_indices:
            category_id = unique_categories[i].item()
            category_count = counts[i].item()
            print(f"Category ID {category_id}: {category_count} products")

        print("\n--- How to use this information to create a subgraph ---")
        print("To create a smaller graph with only selected item types (categories), you would:")
        print("1. Choose a subset of 'Category IDs' from the list above (e.g., [0, 5, 10]).")
        print("2. Filter the nodes (data.x and data.y) based on these chosen category IDs.")
        print("3. Create a new edge_index that only includes edges between the selected nodes.")
        print("   This typically involves using `torch_geometric.utils.subgraph` or manually filtering edges.")
        print("\nExample (conceptual, not runnable as-is without further implementation):")
        print("selected_category_ids = [0, 1, 2] # Example: select categories 0, 1, and 2")
        print("selected_nodes_mask = torch.isin(data.y.squeeze(), torch.tensor(selected_category_ids, device=data.y.device))")
        print("selected_node_indices = torch.where(selected_nodes_mask)[0]")
        print("# Then use these indices to create a subgraph (similar to the 10k node example)")
        print("# from torch_geometric.utils import subgraph")
        print("# new_edge_index, _, _ = subgraph(selected_node_indices, data.edge_index, relabel_nodes=True)")
        print("# new_x = data.x[selected_node_indices]")
        print("# new_y = data.y[selected_node_indices]")
        print("\nThis approach allows you to control the size of the graph by selecting fewer, or smaller, categories.")

    except Exception as e:
        print(f"An error occurred while loading or inspecting the dataset: {e}")
        print("Please ensure the dataset is fully downloaded and accessible at the specified 'root' path.")
        print("If you are still facing download issues, consider manually downloading the dataset or checking network connectivity.")

if __name__ == "__main__":
    main()