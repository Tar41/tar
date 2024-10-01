import pandas as pd
import matplotlib.pyplot as plt

def q03(): #Define number of US transactions by states
    # Step 1: Load data and clean column names
    file_path = r'C:\Users\Asus\Downloads\transactions.csv'  # Adjust the file path
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()  # Clean up column names

    # Step 2: Group by 'cardType' and sum 'transactionAmountUSD'
    total_spending = data.groupby('cardType')['transactionAmountUSD'].sum()

    # Step 3: Plot the total spending by card type as a bar chart
    plt.figure(figsize=(10, 6))  # Set figure size to 10 x 6 inches
    total_spending.sort_values(ascending=False).plot(kind='barh', color='blue')

    # Step 4: Add chart decorations
    plt.title('Total Spending by Card Type')
    plt.xlabel('Total Spending (USD)')
    plt.ylabel('Card Type')

    # Step 5: Save and show the chart
    plt.tight_layout()  # Ensure layout fits well
    plt.savefig('mychart03.png', format='png')  # Save as mychart03.png
    plt.show()  # Show the chart