import pandas as pd

# Load the CSV file
df = pd.read_csv('data01.csv')

# Select specific columns
result = df[['Item Name', '# of Items Sold']]

# Group by "Item Name" and sum the "# of Items Sold"
result = result.groupby('Item Name')['# of Items Sold'].sum().reset_index()

# Save to a new CSV file
result.to_csv('data02.csv')
