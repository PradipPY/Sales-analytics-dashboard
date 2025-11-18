import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw_sales.csv")

df['revenue'] = df['quantity'] * df['price']

df.groupby('category')['revenue'].sum().plot(kind='bar')
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()
