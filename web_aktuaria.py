import streamlit as st

st.set_page_config(
    page_title="AKTUARIA",
    layout="wide"
)

# ==========================
# CSS
# ==========================
st.markdown("""
<style>

.stApp{
    background-color:#F5F7FA;
}

.main-title{
    color:#1E3A5F;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    color:#6B7280;
    font-size:18px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    border:1px solid #E5E7EB;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom:15px;
}

.result{
    background:#EFF6FF;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #2563EB;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================
menu = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Bunga Majemuk",
        "Nilai Masa Depan",
        "Target Keuangan",
        "Dana Darurat",
        "Dana Pensiun"
    ]
)

# ==========================
# DASHBOARD
# ==========================
if menu == "Dashboard":

    st.markdown(
        '<p class="main-title">AKTUARIA</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Perhitungan Cerdas untuk Masa Depan</p>',
        unsafe_allow_html=True
    )

    col1,col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>Bunga Majemuk</h3>
        Menghitung pertumbuhan investasi berdasarkan bunga majemuk.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Target Keuangan</h3>
        Menentukan tabungan bulanan untuk mencapai tujuan finansial.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Dana Pensiun</h3>
        Merencanakan kebutuhan dana di masa pensiun.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>Nilai Masa Depan</h3>
        Menghitung proyeksi nilai investasi.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Dana Darurat</h3>
        Menghitung kebutuhan dana cadangan.
        </div>
        """, unsafe_allow_html=True)

# ==========================
# BUNGA MAJEMUK
# ==========================
elif menu == "Bunga Majemuk":

    st.title("Bunga Majemuk")

    modal = st.number_input(
        "Modal Awal",
        min_value=0.0
    )

    bunga = st.number_input(
        "Suku Bunga (%)",
        min_value=0.0
    )

    waktu = st.number_input(
        "Lama Investasi (tahun)",
        min_value=0.0
    )

    if st.button("Hitung"):

        hasil = modal * (1+bunga/100)**waktu
        keuntungan = hasil - modal
        persen = (keuntungan/modal)*100 if modal>0 else 0

        st.markdown(f"""
        <div class="result">
        <h3>Hasil Perhitungan</h3>

        Nilai Akhir : Rp {hasil:,.0f}<br>
        Keuntungan : Rp {keuntungan:,.0f}<br>
        Pertumbuhan : {persen:.2f}%
        </div>
        """, unsafe_allow_html=True)

# ==========================
# NILAI MASA DEPAN
# ==========================
elif menu == "Nilai Masa Depan":

    st.title("Nilai Masa Depan")

    pv = st.number_input(
        "Nilai Saat Ini",
        min_value=0.0
    )

    bunga = st.number_input(
        "Suku Bunga (%)",
        min_value=0.0,
        key="fv"
    )

    waktu = st.number_input(
        "Periode (tahun)",
        min_value=0.0,
        key="fv2"
    )

    if st.button("Hitung"):

        fv = pv*(1+bunga/100)**waktu

        st.markdown(f"""
        <div class="result">
        <h3>Nilai Masa Depan</h3>

        Rp {fv:,.0f}
        </div>
        """, unsafe_allow_html=True)

# ==========================
# TARGET KEUANGAN
# ==========================
elif menu == "Target Keuangan":

    st.title("Target Keuangan")

    target = st.text_input("Nama Target")

    harga = st.number_input(
        "Harga Target",
        min_value=0.0
    )

    bulan = st.number_input(
        "Jangka Waktu (bulan)",
        min_value=1
    )

    if st.button("Hitung"):

        tabungan = harga / bulan

        st.markdown(f"""
        <div class="result">
        <h3>Tabungan Bulanan</h3>

        Rp {tabungan:,.0f}
        </div>
        """, unsafe_allow_html=True)

# ==========================
# DANA DARURAT
# ==========================
elif menu == "Dana Darurat":

    st.title("Dana Darurat")

    pengeluaran = st.number_input(
        "Pengeluaran Bulanan",
        min_value=0.0
    )

    status = st.selectbox(
        "Status",
        [
            "Belum Menikah",
            "Menikah",
            "Menikah + Anak"
        ]
    )

    if st.button("Hitung"):

        if status == "Belum Menikah":
            faktor = 6
        elif status == "Menikah":
            faktor = 9
        else:
            faktor = 12

        dana = pengeluaran * faktor

        st.markdown(f"""
        <div class="result">
        <h3>Dana Darurat Ideal</h3>

        Rp {dana:,.0f}
        </div>
        """, unsafe_allow_html=True)

# ==========================
# DANA PENSIUN
# ==========================
elif menu == "Dana Pensiun":

    st.title("Dana Pensiun")

    usia = st.number_input(
        "Usia Saat Ini",
        min_value=1
    )

    pensiun = st.number_input(
        "Usia Pensiun",
        min_value=usia+1
    )

    target = st.number_input(
        "Target Dana Pensiun",
        min_value=0.0
    )

    if st.button("Hitung"):

        sisa_tahun = pensiun - usia
        bulan = sisa_tahun * 12

        tabungan = target / bulan

        st.markdown(f"""
        <div class="result">
        <h3>Kebutuhan Tabungan Bulanan</h3>

        Rp {tabungan:,.0f}
        </div>
        """, unsafe_allow_html=True)
