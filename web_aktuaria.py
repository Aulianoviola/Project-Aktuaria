import streamlit as st
import math

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Kalkulator Aktuaria",
    page_icon="📈",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(
        135deg,
        #050816 0%,
        #0b1026 30%,
        #150f3f 70%,
        #090b18 100%
    );
    color:white;
}

/* Hide Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:white;

    text-shadow:
        0 0 10px #00d4ff,
        0 0 20px #00d4ff,
        0 0 40px #7f5cff;
}

/* Subtitle */
.sub-title{
    text-align:center;
    color:#cfcfcf;
    font-size:18px;
}

/* Hero */
.hero{
    padding:40px;
    border-radius:25px;

    background:rgba(255,255,255,.05);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.1);

    box-shadow:
        0 0 30px rgba(0,212,255,.2);
}

/* Cards */
.card{
    padding:25px;

    border-radius:20px;

    background:rgba(255,255,255,.05);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.08);

    transition:0.4s;

    margin-bottom:20px;
}

.card:hover{
    transform:translateY(-8px);

    box-shadow:
        0 0 20px #00d4ff,
        0 0 40px #7f5cff;
}

/* Buttons */
.stButton>button{

    width:100%;
    border:none;

    border-radius:15px;

    padding:12px;

    color:white;

    font-weight:bold;

    background:
        linear-gradient(
            90deg,
            #7f5cff,
            #00d4ff
        );

    box-shadow:
        0 0 15px #7f5cff,
        0 0 25px #00d4ff;

    transition:.4s;
}

.stButton>button:hover{
    transform:translateY(-5px);
}

/* Inputs */

[data-baseweb="input"]{
    background:rgba(255,255,255,.05);
    border-radius:15px;
}

/* Success Box */
.stAlert{
    border-radius:15px;
}

/* Floating Animation */

@keyframes float{
    0%{
        transform:translateY(0px);
    }

    50%{
        transform:translateY(-8px);
    }

    100%{
        transform:translateY(0px);
    }
}

.float{
    animation:float 3s ease-in-out infinite;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# MENU
# =====================================

if "menu" not in st.session_state:
    st.session_state.menu = "home"

with st.sidebar:

    st.markdown("## 🚀 Navigation")

    if st.button("🏠 Home"):
        st.session_state.menu = "home"

    if st.button("📈 Bunga Majemuk"):
        st.session_state.menu = "bm"

    if st.button("💰 Present Value"):
        st.session_state.menu = "pv"

    if st.button("📊 Future Value"):
        st.session_state.menu = "fv"

    if st.button("🧾 Anuitas"):
        st.session_state.menu = "anuitas"

# =====================================
# HOME
# =====================================

if st.session_state.menu == "home":

    st.markdown("""
    <div class="hero float">

    <h1 class="main-title">
    📈 Kalkulator Aktuaria
    </h1>

    <p class="sub-title">
    Future Value • Present Value • Anuitas • Bunga Majemuk
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1,col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
        <h3>📈 Bunga Majemuk</h3>
        Hitung pertumbuhan investasi dengan bunga majemuk.
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Bunga Majemuk"):
            st.session_state.menu="bm"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="card">
        <h3>💰 Present Value</h3>
        Menghitung nilai sekarang dari nilai masa depan.
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Present Value"):
            st.session_state.menu="pv"
            st.rerun()

    col3,col4 = st.columns(2)

    with col3:

        st.markdown("""
        <div class="card">
        <h3>📊 Future Value</h3>
        Hitung nilai investasi masa depan.
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Future Value"):
            st.session_state.menu="fv"
            st.rerun()

    with col4:

        st.markdown("""
        <div class="card">
        <h3>🧾 Anuitas</h3>
        Perhitungan nilai anuitas.
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Anuitas"):
            st.session_state.menu="anuitas"
            st.rerun()

# =====================================
# BUNGA MAJEMUK
# =====================================

elif st.session_state.menu == "bm":

    st.markdown("# 📈 Bunga Majemuk")

    P = st.number_input("Modal Awal",0.0, value=1000.0)
    r = st.number_input("Bunga (%)",0.0,value=5.0)
    t = st.number_input("Tahun",0.0,value=1.0)

    if st.button("🚀 Hitung"):

        hasil = P*(1+r/100)**t

        st.success(
            f"Hasil Akhir = Rp {hasil:,.2f}"
        )

# =====================================
# PRESENT VALUE
# =====================================

elif st.session_state.menu == "pv":

    st.markdown("# 💰 Present Value")

    fv = st.number_input("Future Value",0.0,100000000.0,10000.0)
    r = st.number_input("Bunga (%)",0.0,100.0,5.0)
    t = st.number_input("Tahun",0.0,100.0,1.0)

    if st.button("🚀 Hitung PV"):

        pv = fv/((1+r/100)**t)

        st.success(
            f"PV = Rp {pv:,.2f}"
        )

# =====================================
# FUTURE VALUE
# =====================================

elif st.session_state.menu == "fv":

    st.markdown("# 📊 Future Value")

    pv = st.number_input("Present Value",0.0,100000000.0,1000.0)
    r = st.number_input("Bunga (%)",0.0,100.0,5.0)
    t = st.number_input("Tahun",0.0,100.0,1.0)

    if st.button("🚀 Hitung FV"):

        fv = pv*((1+r/100)**t)

        st.success(
            f"FV = Rp {fv:,.2f}"
        )

# =====================================
# ANUITAS
# =====================================

elif st.session_state.menu == "anuitas":

    st.markdown("# 🧾 Anuitas")

    pembayaran = st.number_input(
        "Pembayaran per Periode",
        value=1000.0
    )

    bunga = st.number_input(
        "Bunga (%)",
        value=5.0
    )

    periode = st.number_input(
        "Jumlah Periode",
        value=5
    )

    if st.button("🚀 Hitung Anuitas"):

        r = bunga/100

        hasil = pembayaran * (
            (1-(1+r)**(-periode))/r
        )

        st.success(
            f"Nilai Anuitas = Rp {hasil:,.2f}"
        )
