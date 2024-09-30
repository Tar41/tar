import pandas as pd
import matplotlib.pyplot as plt

def q01():  # Define number of US transactions by states
    # Step 1: Load data and clean column names
    file_path = r'C:\Users\Asus\Downloads\transactions.csv'  # Adjust the file path
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()  # Clean up column names

    # Step 2: Filter for transactions with 'US' as the shipping country
    us_data = data[data['shippingCountry'].str.upper() == 'US']

    # Step 3: Count transactions by shipping state (for US transactions only)
    transactions_by_state = us_data['shippingState'].value_counts()

    # Step 4: Create the bar chart with specified size
    plt.figure(figsize=(20.4, 6.4))  # Set the figure size to 20.4 x 6.4 inches
    transactions_by_state.plot(kind='bar', color='skyblue')

    plt.title('Number of US Transactions by State')
    plt.xlabel('State')
    plt.ylabel('Number of Transactions')
    plt.xticks(rotation=45, ha='right')

    # Step 5: Save the plot with the specified file name
    plt.tight_layout()
    plt.savefig('mychart01.png', format='png')

    # Step 6: Show the plot
    plt.show()
