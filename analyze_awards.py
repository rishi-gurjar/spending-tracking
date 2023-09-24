import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('awards.csv')

# Convert 'Start Date' to datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'])

# 1. Total award funding per month over time by "Start Date"
df['Start Month'] = df['Start Date'].dt.to_period('M')  # Extract month and year
monthly_funding = df.groupby('Start Month')['Award Amount'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(monthly_funding['Start Month'].astype(str), monthly_funding['Award Amount'])
plt.title('Total Award Funding Per Month Over Time by Start Date')
plt.xlabel('Start Month')
plt.ylabel('Total Award Amount')
plt.xticks(rotation=45)
plt.show()

# 2. Award funding by month (ignoring the year)
df['Start Month Only'] = df['Start Date'].dt.month  # Extract only the month
monthly_funding_only = df.groupby('Start Month Only')['Award Amount'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(monthly_funding_only['Start Month Only'], monthly_funding_only['Award Amount'])
plt.title('Award Funding by Month')
plt.xlabel('Month')
plt.ylabel('Total Award Amount')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()
