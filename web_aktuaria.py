import streamlit as st
import math

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Kalkulator Matematika Aktuaria",
    page_icon="🔢",
    layout="centered"
)

# =====================================
# SIDEBAR
# =====================================
st.sidebar.markdown("## Menu")

if st.sidebar.button("🏠 Halaman Depan"):
    st.session_state.menu = "home"

if st.sidebar.button("📈 Bunga Majemuk"):
    st.session_state.menu = "Bunga Majemuk"

if st.sidebar.button("💰 Present Value"):
    st.session_state.menu = "Present Value"

if st.sidebar.button("📊 Future Value"):
    st.session_state.menu = "Future Value"

if st.sidebar.button("🧾 Anuitas"):
    st.session_state.menu = "Anuitas"
# =====================================
# DEFAULT MENU
# =====================================
if "menu" not in st.session_state:
    st.session_state.menu = "home"
# =========================================
# HOME
# =========================================
if st.session_state.menu == "home":

    st.title("Kalkulator Matematika Aktuaria")

    st.write("""
    Website Sederhana untuk Membantu Perhitungan Matematika Aktuaria.
    """)

    st.write("## 📌 Pilihan Perhitungan")

    # BARIS PERTAMA
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📈 Bunga Majemuk"):
            st.session_state.menu = "Bunga Majemuk"
            st.rerun()

    with col2:
        if st.button("💰 Present Value"):
            st.session_state.menu = "Present Value"
            st.rerun()

    # BARIS KEDUA
    col3, col4 = st.columns(2)

    with col3:
        if st.button("📊 Future Value"):
            st.session_state.menu = "Future Value"
            st.rerun()

    with col4:
        if st.button("🧾 Anuitas"):
            st.session_state.menu = "Anuitas"
            st.rerun()

# =====================================================
# BUNGA MAJEMUK
# =====================================================
elif st.session_state.menu == "Bunga Majemuk":

    st.header("Perhitungan Bunga Majemuk")

    modal = st.number_input(
        "Modal Awal",
        min_value=0.0,
        value=1000.0
    )

    bunga = st.number_input(
        "Bunga (%)",
        min_value=0.0,
        value=5.0
    )

    waktu = st.number_input(
        "Waktu (tahun)",
        min_value=0.0,
        value=1.0
    )

    if st.button("Hitung Bunga Majemuk"):

        hasil = modal * (1 + bunga / 100) ** waktu

        st.success(f"Hasil Akhir = {hasil:,.2f}")

        st.info(
            f"""
            Rumus:
            
            A = P(1+r)^t
            
            Dengan:
            - P = {modal}
            - r = {bunga/100}
            - t = {waktu}
            """
        )

# =====================================================
# PRESENT VALUE
# =====================================================
elif st.session_state.menu == "Present Value":

    st.header("Perhitungan Present Value")

    fv = st.number_input(
        "Future Value",
        min_value=0.0,
        value=10000.0
    )

    bunga = st.number_input(
        "Bunga (%)",
        min_value=0.0,
        value=5.0,
        key="pv_bunga"
    )

    waktu = st.number_input(
        "Waktu (tahun)",
        min_value=0.0,
        value=1.0,
        key="pv_waktu"
    )

    if st.button("Hitung Present Value"):

        pv = fv / ((1 + bunga / 100) ** waktu)

        st.success(f"Present Value = {pv:,.2f}")

        st.info(
            f"""
            Rumus:
            
            PV = FV / (1+r)^t
            """
        )

# =====================================================
# FUTURE VALUE
# =====================================================
elif st.session_state.menu == "Future Value":

    st.header("Perhitungan Future Value")

    pv = st.number_input(
        "Present Value",
        min_value=0.0,
        value=1000.0
    )

    bunga = st.number_input(
        "Bunga (%)",
        min_value=0.0,
        value=5.0,
        key="fv_bunga"
    )

    waktu = st.number_input(
        "Waktu (tahun)",
        min_value=0.0,
        value=1.0,
        key="fv_waktu"
    )

    if st.button("Hitung Future Value"):

        fv = pv * ((1 + bunga / 100) ** waktu)

        st.success(f"Future Value = {fv:,.2f}")

        st.info(
            f"""
            Rumus:
            
            FV = PV(1+r)^t
            """
        )

# =====================================================
# ANUITAS
# =====================================================
elif st.session_state.menu == "Anuitas":

    st.header("Perhitungan Anuitas")

    pembayaran = st.number_input(
        "Pembayaran per Periode",
        min_value=0.0,
        value=1000.0
    )

    bunga = st.number_input(
        "Bunga (%)",
        min_value=0.1,
        value=5.0,
        key="anuitas_bunga"
    )

    periode = st.number_input(
        "Jumlah Periode",
        min_value=1,
        value=5
    )

    if st.button("Hitung Anuitas"):

        r = bunga / 100

        anuitas = pembayaran * ((1 - (1 + r) ** (-periode)) / r)

        st.success(f"Nilai Anuitas = {anuitas:,.2f}")

        st.info(
            f"""
            Rumus:
            
            A = P[(1-(1+r)^-n)/r]
            """
        )
