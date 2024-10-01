import pandas as pd
import matplotlib.pyplot as plt
import requests

def q04(): #Define number of US transactions by states
    # Step 1: Fetch the data from the REST API
    api_url = 'https://fakestoreapi.in/api/products'
    data = requests.get(api_url).json()  # Get and parse the JSON data

    # Step 2: Extract the 'products' field
    products = data['products']

    # Step 3: Create DataFrame from products and extract prices
    df = pd.json_normalize(products)

    # Step 4: Filter products with price less than 4,000
    filtered_data = df[df['price'] < 4000]

    # Step 5: Plot a histogram of product prices
    plt.figure(figsize=(10.4, 6.4))  # Set figure size
    plt.hist(filtered_data['price'], bins=10, color='green', edgecolor='black')

    # Step 6: Add title and labels
    plt.title('Histogram of Product Prices Less Than 4,000')
    plt.xlabel('Price (in USD)')
    plt.ylabel('Number of Products')

    # Step 7: Save and show the histogram
    plt.tight_layout()
    plt.savefig('hit04.png', format='png')
    plt.show()

