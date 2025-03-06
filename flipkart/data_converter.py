import os
import pandas as pd
from langchain_core.documents import Document

def dataconverter():
    # Get the absolute path dynamically
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/flipkart_product_review.csv"))

    # Debugging: Print the actual path being used
    print(f"Trying to read CSV from: {csv_path}")

    # Load CSV file
    product_data = pd.read_csv(csv_path)
    print("CSV file loaded successfully!")

    # Select relevant columns
    data = product_data[["product_title", "review"]]

    product_list = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        obj = {
            "product_name": row["product_title"],
            "review": row["review"]
        }
        # Append the object inside the loop (fix indentation)
        product_list.append(obj)

    docs = []
    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content=entry['review'], metadata=metadata)
        docs.append(doc)

    return docs
