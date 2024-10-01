import pandas as pd
import matplotlib.pyplot as plt
import requests

def q06():
    # Step 1: Fetch the product data from the REST API
    api_url = 'https://fakestoreapi.in/api/products'
    response = requests.get(api_url)
    products = response.json()  # Load JSON data

    # Step 2: Load the products into a DataFrame
    df = pd.json_normalize(products['products'])

    # Step 3: Group the data by category and count the number of products in each category
    category_counts = df['category'].value_counts()

    # Step 4: Create a pie chart
    plt.figure()  # Default figure size
    category_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

    # Step 5: Add a title and remove y-axis label for clarity
    plt.title('Product Categories Distribution')
    plt.ylabel('')  # Hide the default y-label

    # Step 6: Save the pie chart as 'pie06.png'
    plt.tight_layout()
    plt.savefig('pie06.png', format='png')
    plt.show()  # Display the pie chart