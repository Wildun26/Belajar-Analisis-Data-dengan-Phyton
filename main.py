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
    # Sewa Sepeda Menurut Musim
    mapping_musim = {1: "musim panas", 2: "musim gugur"}
    data["label_musim"] = data["musim"].map(mapping_musim)

    jumlah_musim = data.groupby("label_musim")["cnt"].sum().reset_index()
    grafik_jumlah_musim = px.bar(jumlah_musim, x="label_musim",
                              y="cnt", title="Sewa Sepeda Menurut Musim")
    st.plotly_chart(grafik_jumlah_musim, use_container_width=True,
                    height=400, width=600)

with kolom2:
    # Sewa Sepeda Menurut Situasi Cuaca
    jumlah_cuaca = data.groupby("cuaca")["cnt"].sum().reset_index()
    grafik_jumlah_cuaca = px.bar(jumlah_cuaca, x="cuaca",
                               y="cnt", title="Sewa Sepeda Menurut Situasi Cuaca")
    st.plotly_chart(grafik_jumlah_cuaca, use_container_width=True, height=400, width=800)

# Sewa Sepeda per Jam
jumlah_per_jam = data.groupby("jam")["cnt"].sum().reset_index()
grafik_jumlah_per_jam = px.line(
    jumlah_per_jam, x="jam", y="cnt", title="Sewa Sepeda per Jam")
st.plotly_chart(grafik_jumlah_per_jam, use_container_width=True,
                height=400, width=600)

# Suhu vs. Sewa Sepeda
grafik_suhu = px.scatter(data, x="suhu", y="cnt",
                            title="Suhu vs. Sewa Sepeda")
st.plotly_chart(grafik_suhu, use_container_width=True,
                height=400, width=800)
```
