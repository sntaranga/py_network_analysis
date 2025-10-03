import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def plot_linergraph(data_set):
    print("hellow")
    print(data_set)

    fig = go.Figure()
    plt.figure(figsize=(12, 6))
    for  ifname in data_set.keys():
        print (f"ifname:{ifname}")
        df_list = data_set[ifname]
        flat_data = df_list[0]
        display(flat_data)
        print(type(flat_data))

        df = pd.DataFrame(flat_data, columns=["timestamp", "speed_mbps"])

        print(type(df))
        print("display")
        display(df)
        anomally = find_anomely(df)
#        df = pd.DataFrame(data_set[ifname])

        plt.plot(df["timestamp"],df["speed_mbps"],label=f"{ifname}",marker='o')
        plt.scatter(anomally[anomally["anomaly"]]["timestamp"], anomally[anomally["anomaly"]]["speed_mbps"],
            color="red", label=f"Anomaly{ifname}",zorder=5 )
        fig.add_trace(go.Scatter(
            x=anomally[anomally["anomaly"]]["timestamp"],
            y=anomally[anomally["anomaly"]]["speed_mbps"],
            mode="markers",
            marker=dict(color="red", size=8),
            name=f"{ifname} Anomaly",
            showlegend=True
        ))

        # Plot main line on top
        fig.add_trace(go.Scatter(
            x=df["timestamp"],
            y=df["speed_mbps"],
            mode="lines+markers",
            name=ifname
        ))
    fig.update_layout(
        title="Speed over Time for Multiple Interfaces",
        xaxis_title="Timestamp",
        yaxis_title="Speed (Mbps)",
        hovermode="x unified"
    )
    fig.show()
    plt.title("Speed over Time ")
    plt.xlabel("Timestamp")
    plt.ylabel("Speed (Mbps)")

    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.show()

def find_anomely(data_set):
    rolling_mean = data_set["speed_mbps"].rolling(window=10).mean()
    rolling_std = data_set["speed_mbps"].rolling(window=10).std()
    data_set["anomaly"] = np.abs(data_set["speed_mbps"] - rolling_mean) > 2 * rolling_std
    print("anomaly")
    display(data_set)
    return data_set
