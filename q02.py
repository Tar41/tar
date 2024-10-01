import pandas as pd
import matplotlib.pyplot as plt

def q02(): #Display VISA transaction amounts by shipping country

    # Step 1: Load data and clean column names
    file_path = r'C:\Users\Asus\Downloads\transactions.csv'  # Adjust the file path
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()  # Clean up column names

    # Step 2: Filter for VISA transactions
    visa_data = data[data['cardType'].str.contains('VISA', case=False, na=False)]

    # Step 3: Use .loc to modify shippingCountry and ensure it's uppercase
    visa_data.loc[:, 'shippingCountry'] = visa_data['shippingCountry'].str.upper()

    # Step 4: Group by shipping country and sum transaction amounts
    transaction_amount_by_country = visa_data.groupby('shippingCountry')['transactionAmountUSD'].sum()

    # Step 5: Limit to top 20 countries by transaction amount
    #transaction_amount_by_country = transaction_amount_by_country.nlargest(30)

    # Step 6: Create a horizontal bar chart
    plt.figure(figsize=(20, 10))  # Set the figure size
    transaction_amount_by_country.sort_values().plot(kind='barh', color='green')

    # Step 7: Add title and labels
    plt.title('Top 20 VISA Transaction Amounts by Shipping Country')
    plt.xlabel('Transaction Amount (USD)')
    plt.ylabel('Shipping Country')

    # Step 8: Save the plot with the specified file name
    plt.tight_layout()
    plt.savefig('mychart02.png', format='png')

    # Step 9: Show the plot
    plt.show()