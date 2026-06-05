import streamlit as st

st.set_page_config(page_title="Analisis Kinerja Boiler", layout="wide")
st.title("kalkulator spesific Fuel Cosumption (Kcal/kg)")
st.write("Masukkan Data Pembangkit")

coal1 =  st.number_input("Flow Batubara 1 (t/h)", min_value=0.0, value=0.0)
coal2 =  st.number_input("Flow Batubara 2 (t/h)", min_value=0.0, value=0.0)
produksi_listrik = st.number_input("Produksi Listrik (kWh)", min_value=0.0, value=0.0)

if st.button("Hitung Spesific Fuel Cosumption"):
    if produksi_listrik == 0:
        st.error("Produksi listrik tidak boleh 0")
    else:
        coal_total = (coal1+coal2)*1000
        Spesific_Fuel_Cosumption = ((coal1+coal2)*1000)/(produksi_listrik*1000)
        st.success (f"Spesific Fuel Cosumption = {Spesific_Fuel_Cosumption:.4f}kg/kWh")
        st.write(f"Total Konsumsi Batubara ={coal_total:.2f}kg/h")