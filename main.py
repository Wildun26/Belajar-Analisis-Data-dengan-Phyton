# Mengimpor Pustaka
import streamlit as st
import pandas as pd
import plotly.express as px

def muat_data():
    data = pd.read_csv("Bike-sharing-dataset/hour.csv")
    return data

data = muat_data()

kolom1, kolom2 = st.columns(2)

with kolom1:
    # Jumlah Berbagi Sepeda Menurut Musim
    mapping_musim = {2: "musim panas", 3: "musim gugur"}
    data["label_musim"] = data["season"].map(mapping_musim)

    jumlah_musim = data.groupby("label_musim")["cnt"].sum().reset_index()
    grafik_jumlah_musim = px.bar(jumlah_musim, x="label_musim",
                              y="cnt", title="Jumlah Berbagi Sepeda Menurut Musim")
    st.plotly_chart(grafik_jumlah_musim, use_container_width=True,
                    height=400, width=600)

with kolom2:
    # Jumlah Berbagi Sepeda Menurut Situasi Cuaca
    jumlah_cuaca = data.groupby("weathersit")["cnt"].sum().reset_index()
    grafik_jumlah_cuaca = px.bar(jumlah_cuaca, x="weathersit",
                               y="cnt", title="Jumlah Berbagi Sepeda Menurut Situasi Cuaca")
    st.plotly_chart(grafik_jumlah_cuaca, use_container_width=True, height=400, width=800)

# Jumlah Berbagi Sepeda per Jam
jumlah_per_jam = data.groupby("hr")["cnt"].sum().reset_index()
grafik_jumlah_per_jam = px.line(
    jumlah_per_jam, x="hr", y="cnt", title="Jumlah Berbagi Sepeda per Jam")
st.plotly_chart(grafik_jumlah_per_jam, use_container_width=True,
                height=400, width=600)

# Kelembapan vs. Jumlah Berbagi Sepeda
grafik_kelembapan = px.scatter(
    data, x="hum", y="cnt", title="Kelembapan vs. Jumlah Berbagi Sepeda")
st.plotly_chart(grafik_kelembapan)

# Suhu vs. Jumlah Berbagi Sepeda
grafik_suhu = px.scatter(data, x="temp", y="cnt",
                            title="Suhu vs. Jumlah Berbagi Sepeda")
st.plotly_chart(grafik_suhu, use_container_width=True,
                height=400, width=800)
