import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHART_DIR = os.path.join(BASE_DIR, "charts")
os.makedirs(CHART_DIR, exist_ok=True)

monthly = pd.read_csv(os.path.join(BASE_DIR, "monthly_sales_data.csv"))
category = pd.read_csv(os.path.join(BASE_DIR, "category_sales_data.csv"))

plt.figure(figsize=(9, 5))
plt.bar(monthly["Month"], monthly["Sales (₹)"])
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "01_monthly_sales_bar.png"), dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
plt.plot(monthly["Month"], monthly["Sales (₹)"], marker="o")
plt.title("Sales Trend from January to June")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=25, ha="right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "02_sales_trend_line.png"), dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
plt.pie(category["Sales (₹)"], labels=category["Category"], autopct="%1.1f%%", startangle=90)
plt.title("Share of Sales by Product Category")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "03_category_sales_pie.png"), dpi=160)
plt.close()

print("Created 3 charts in:", CHART_DIR)
