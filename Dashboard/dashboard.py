import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st

# Load data
jam_df = pd.read_csv("https://raw.githubusercontent.com/NazwaChantika/dashboard-dicoding-streamlit/main/Dashboard/jam.csv")
hari_df = pd.read_csv("https://raw.githubusercontent.com/NazwaChantika/dashboard-dicoding-streamlit/main/Dashboard/hari.csv")


# Function to plot bike rental count by weather situation
def plot_bike_rental_by_weather(df, title):
    musim_df = df.groupby(by="weathersit").cnt.nunique().reset_index()
    musim_df.rename(columns={
        "cnt": "count_sewa"
    }, inplace=True)

    colors = ["#FFA500", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    fig, ax = plt.subplots(figsize=(10,5))
    sb.barplot(
        y="count_sewa",
        x="weathersit",
        data=musim_df.sort_values(by="count_sewa", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title(title, loc="center", fontsize=15)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Banyak Sepeda disewa")
    st.pyplot(fig)

# Function to plot bike usage statistics by weekday and holiday
def plot_bike_usage_statistics(df, title):
     statistik_penggunaan = df.groupby(['weekday', 'holiday']).agg({
        "registered": ["sum", "max", "min"],
        "casual": ["sum", "max", "min"]
    }).reset_index()
    
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

    # Plot registered users
    sb.barplot(x="weekday", y=("registered", "sum"), hue="holiday", data=df, ax=axes[0, 0])
    axes[0, 0].set_title("Registered Users - Total")
    axes[0, 0].set_xlabel("Weekday")
    axes[0, 0].set_ylabel("Total Registered Users")

    # Plot casual users
    sb.barplot(x="weekday", y=("casual", "sum"), hue="holiday", data=df, ax=axes[0, 1])
    axes[0, 1].set_title("Casual Users - Total")
    axes[0, 1].set_xlabel("Weekday")
    axes[0, 1].set_ylabel("Total Casual Users")

    # Plot max registered users
    sb.barplot(x="weekday", y=("registered", "max"), hue="holiday", data=df, ax=axes[1, 0])
    axes[1, 0].set_title("Registered Users - Max")
    axes[1, 0].set_xlabel("Weekday")
    axes[1, 0].set_ylabel("Max Registered Users")

    # Plot max casual users
    sb.barplot(x="weekday", y=("casual", "max"), hue="holiday", data=df, ax=axes[1, 1])
    axes[1, 1].set_title("Casual Users - Max")
    axes[1, 1].set_xlabel("Weekday")
    axes[1, 1].set_ylabel("Max Casual Users")

    plt.tight_layout()
    st.pyplot(fig)

# Plot bike usage statistics for jam_df
st.header("Statistik Penggunaan Sepeda (Jam)")
plot_bike_usage_statistics(statistik_penggunaan_jam, "Statistik Penggunaan Sepeda (Jam)")

# Plot bike usage statistics for hari_df
st.header("Statistik Penggunaan Sepeda (Hari)")
plot_bike_usage_statistics(statistik_penggunaan_hari, "Statistik Penggunaan Sepeda (Hari)")

