# Network Analysis Assignment Template

# ==========================
# 1. Imports & Setup
# ==========================
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from helpers import plot_linergraph
from sklearn.ensemble import IsolationForest

# Configure plots
sns.set(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams["figure.figsize"] = (12, 6)

# ==========================
# 2. Load Data
# ==========================
# TODO: Replace 'market_data.csv' with actual dataset filename
df = pd.read_csv("speeds.csv")

if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])

# Quick overview
print("Data shape:", df.shape)
print("head")
display(df.head())
print("info")
display(df.info())
print("describe")
display(df.describe())


# split by interfaces

interface_values = df['interface'].unique()
display(interface_values)
columns_to_keep = ['timestamp', 'speed_mbps']
interface_data = {}
for iface in interface_values:
    print(iface)
    print(interface_values[1])
    df1 = df[df['interface'] == iface]
    df_filtered = df1[columns_to_keep]
    print("filterd")
    display(df_filtered)
    if iface not in interface_data:
        interface_data[iface] = []
        interface_data[iface].append(df_filtered)

print("interface data")
print(interface_data)

plot_linergraph(interface_data)

# ==========================
# 3. Data Cleaning / Preprocessing
# ==========================
# Example: parse timestamps if they exist
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])

# Handle missing values
print("Missing values:\n", df.isna().sum())

# ==========================
# 4. Exploratory Analysis
# ==========================
# Example: check distributions
df.hist(bins=50, figsize=(15, 8))
plt.suptitle("Feature Distributions")
plt.show()

# ==========================
# 5. Metric Calculation
# ==========================
# TODO: Define the metric(s) you want to calculate
# Example (placeholder): average spread


if {"ask", "bid"}.issubset(df.columns):
    df["spread"] = df["ask"] - df["bid"]
    avg_spread = df["spread"].mean()
    print("Average Spread:", avg_spread)

# ==========================
# 6. Visualization of Findings
# ==========================
# Example visualization
if "timestamp" in df.columns and "spread" in df.columns:
    df.set_index("timestamp")["spread"].plot(title="Spread Over Time")
    plt.show()


# ==========================
# 7. Conclusion / Insights
# ==========================
# TODO: Summarize findings in markdown cells when presenting




