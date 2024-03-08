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

# Function to display statistics of bike usage by weekday and holiday
def display_bike_usage_statistics(df, title):
    statistik_penggunaan = df.groupby(['weekday', 'holiday']).agg({
        "registered": ["sum", "max", "min"],
        "casual": ["sum", "max", "min"]
    }).reset_index()

    st.write(title)
    st.write(statistik_penggunaan)

# Main part of the Streamlit app
st.title("Bike Rental Dashboard")
st.header("Banyakya Jumlah Sepeda yang disewa pada setiap Musim")
plot_bike_rental_by_weather(jam_df, "Jumlah Sepeda yang Disewa Berdasarkan Musim (Jam)")
plot_bike_rental_by_weather(hari_df, "Jumlah Sepeda yang Disewa Berdasarkan Musim (Hari)")

# Display bike usage statistics by weekday and holiday
display_bike_usage_statistics(jam_df, "Statistik Penggunaan Sepeda (Jam)")
display_bike_usage_statistics(hari_df, "Statistik Penggunaan Sepeda (Hari)")
