import streamlit as st

st.set_page_config(
    page_title="AKTUARIA",
    page_icon="A",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>

/* Import Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */
.stApp{
    background:
    linear-gradient(
        135deg,
        #0F172A 0%,
        #1E1B4B 50%,
        #312E81 100%
    );
}

/* Hilangkan header streamlit */
header{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Navbar */
.navbar{
    display:flex;
    justify-content:space-between;
    align-items:center;

    padding:20px 40px;

    background:rgba(255,255,255,0.05);

    backdrop-filter:blur(12px);

    border-radius:20px;

    margin-bottom:30px;

    border:1px solid rgba(255,255,255,0.08);
}

.logo{
    color:white;
    font-size:28px;
    font-weight:700;
}

.tagline{
    color:#cbd5e1;
    font-size:14px;
}

/* Hero */

.hero{

    text-align:center;

    padding:100px 40px;

    border-radius:30px;

    background:
    rgba(255,255,255,0.05);

    backdrop-filter:blur(15px);

    border:
    1px solid rgba(255,255,255,0.08);
}

.hero-title{

    font-size:70px;

    font-weight:700;

    color:white;

    margin-bottom:10px;
}

.hero-sub{

    color:#cbd5e1;

    font-size:22px;

    max-width:700px;

    margin:auto;

    line-height:1.8;
}

/* Cards */

.card{

    background:
    rgba(255,255,255,0.07);

    backdrop-filter:blur(12px);

    border-radius:24px;

    padding:30px;

    min-height:220px;

    border:
    1px solid rgba(255,255,255,0.08);

    transition:all .3s ease;
}

.card:hover{

    transform:
    translateY(-8px);

    border:
    1px solid #8B5CF6;

    box-shadow:
    0px 0px 30px rgba(
    139,92,246,.4
    );
}

.card-title{

    color:white;

    font-size:24px;

    font-weight:600;

    margin-bottom:15px;
}

.card-desc{

    color:#cbd5e1;

    line-height:1.8;
}

/* Result Card */

.result{

    background:
    rgba(255,255,255,0.08);

    padding:30px;

    border-radius:24px;

    border-left:
    6px solid #8B5CF6;

    margin-top:25px;
}

.result-title{

    color:#a78bfa;

    font-size:14px;

    letter-spacing:2px;
}

.result-value{

    color:white;

    font-size:42px;

    font-weight:700;

    margin-top:10px;
}

/* Button */

.stButton > button{

    width:100%;

    height:55px;

    border:none;

    border-radius:14px;

    background:
    linear-gradient(
    90deg,
    #7C3AED,
    #8B5CF6
    );

    color:white;

    font-weight:600;

    transition:.3s;
}

.stButton > button:hover{

    transform:
    translateY(-3px);

    box-shadow:
    0px 0px 25px rgba(
    139,92,246,.5
    );
}

</style>
""", unsafe_allow_html=True)


# ==========================
# SESSION STATE
# ==========================
if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

if st.session_state.menu == "Dashboard":

    st.markdown("""
    <div class="hero">

    <div class="hero-title">
    AKTUARIA
    </div>

    <div class="hero-sub">
    Membantu merencanakan investasi,
    target keuangan, dana darurat,
    dan dana pensiun secara sederhana.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <div class="card-title">
        Bunga Majemuk
        </div>

        <div class="card-desc">
        Menghitung pertumbuhan investasi
        berdasarkan bunga majemuk.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka", key="bunga"):
            st.session_state.menu = "Bunga"
            st.rerun()
        
    with col2:
        st.markdown("""
        <div class="card">
        <div class="card-title">
        Target Keuangan
        </div>

        <div class="card-desc">
        Menentukan kebutuhan tabungan
        untuk mencapai tujuan finansial.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka", key="target"):
            st.session_state.menu = "Target"
            st.rerun()
        
    with col3:
        st.markdown("""
        <div class="card">
        <div class="card-title">
        Dana Pensiun
        </div>

        <div class="card-desc">
        Merencanakan kebutuhan dana
        untuk masa pensiun.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka", key="pensiun"):
            st.session_state.menu = "Pensiun"
            st.rerun()
        
elif st.session_state.menu == "Bunga":
    if st.button("← Kembali ke Dashboard"):
    st.session_state.menu = "Dashboard"
    st.rerun()

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
        Bunga Majemuk
        </div>

        <div class="hero-sub">
        Menghitung pertumbuhan investasi
        berdasarkan bunga majemuk.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:

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

        hitung = st.button("Hitung")

    if hitung:

        hasil = modal * (1+bunga/100)**waktu

        keuntungan = hasil - modal

        persen = (
            keuntungan/modal*100
            if modal > 0
            else 0
        )

        st.markdown(f"""
        <div class="result">

        <div class="result-title">
        HASIL PERHITUNGAN
        </div>

        <div class="result-value">
        Rp {hasil:,.0f}
        </div>

        <hr>

        <p style="color:white;">
        Keuntungan :
        Rp {keuntungan:,.0f}
        </p>

        <p style="color:white;">
        Pertumbuhan :
        {persen:.2f}%
        </p>

        </div>
        """, unsafe_allow_html=True)

elif st.session_state.menu == "FV":
    if st.button("← Kembali ke Dashboard"):
    st.session_state.menu = "Dashboard"
    st.rerun()

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
        Nilai Masa Depan
        </div>

        <div class="hero-sub">
        Proyeksi nilai investasi
        pada masa mendatang.
        </div>
    </div>
    """, unsafe_allow_html=True)

    pv = st.number_input(
        "Nilai Saat Ini",
        min_value=0.0
    )

    bunga = st.number_input(
        "Suku Bunga (%)",
        min_value=0.0,
        key="fv_bunga"
    )

    tahun = st.number_input(
        "Periode (tahun)",
        min_value=0.0,
        key="fv_tahun"
    )

    if st.button("Hitung Future Value"):

        fv = pv * (1+bunga/100)**tahun

        st.markdown(f"""
        <div class="result">

        <div class="result-title">
        NILAI MASA DEPAN
        </div>

        <div class="result-value">
        Rp {fv:,.0f}
        </div>

        </div>
        """, unsafe_allow_html=True)

elif st.session_state.menu == "Target":
    if st.button("← Kembali ke Dashboard"):
    st.session_state.menu = "Dashboard"
    st.rerun()

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
        Target Keuangan
        </div>

        <div class="hero-sub">
        Tentukan jumlah tabungan yang diperlukan
        untuk mencapai tujuan finansial.
        </div>
    </div>
    """, unsafe_allow_html=True)

    target = st.text_input(
        "Nama Target"
    )

    harga = st.number_input(
        "Harga Target",
        min_value=0.0
    )

    bulan = st.number_input(
        "Jangka Waktu (bulan)",
        min_value=1
    )

    if st.button("Hitung Target"):

        tabungan = harga / bulan

        st.markdown(f"""
        <div class="result">

        <div class="result-title">
        TABUNGAN PER BULAN
        </div>

        <div class="result-value">
        Rp {tabungan:,.0f}
        </div>

        <hr>

        <p style="color:white;">
        Untuk mencapai target
        <b>{target}</b>
        senilai Rp {harga:,.0f}
        dalam {bulan} bulan,
        diperlukan tabungan
        Rp {tabungan:,.0f}
        setiap bulan.
        </p>

        </div>
        """, unsafe_allow_html=True)

elif st.session_state.menu == "Darurat":
    if st.button("← Kembali ke Dashboard"):
    st.session_state.menu = "Dashboard"
    st.rerun()

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
        Dana Darurat
        </div>

        <div class="hero-sub">
        Menghitung kebutuhan dana cadangan
        berdasarkan kondisi keuangan.
        </div>
    </div>
    """, unsafe_allow_html=True)

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

    if st.button("Hitung Dana Darurat"):

        if status == "Belum Menikah":
            faktor = 6

        elif status == "Menikah":
            faktor = 9

        else:
            faktor = 12

        dana = pengeluaran * faktor

        st.markdown(f"""
        <div class="result">

        <div class="result-title">
        DANA DARURAT IDEAL
        </div>

        <div class="result-value">
        Rp {dana:,.0f}
        </div>

        <hr>

        <p style="color:white;">
        Berdasarkan status
        <b>{status}</b>,
        kebutuhan dana darurat ideal
        adalah sebesar
        Rp {dana:,.0f}.
        </p>

        </div>
        """, unsafe_allow_html=True)

elif st.session_state.menu == "Pensiun":
    if st.button("← Kembali ke Dashboard"):
    st.session_state.menu = "Dashboard"
    st.rerun()

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
        Dana Pensiun
        </div>

        <div class="hero-sub">
        Rencanakan kebutuhan dana
        untuk masa pensiun.
        </div>
    </div>
    """, unsafe_allow_html=True)

    usia = st.number_input(
        "Usia Saat Ini",
        min_value=1
    )

    usia_pensiun = st.number_input(
        "Usia Pensiun",
        min_value=usia+1
    )

    target_dana = st.number_input(
        "Target Dana Pensiun",
        min_value=0.0
    )

    if st.button("Hitung Dana Pensiun"):

        sisa_tahun = usia_pensiun - usia

        total_bulan = sisa_tahun * 12

        tabungan = (
            target_dana / total_bulan
            if total_bulan > 0
            else 0
        )

        st.markdown(f"""
        <div class="result">

        <div class="result-title">
        TABUNGAN PER BULAN
        </div>

        <div class="result-value">
        Rp {tabungan:,.0f}
        </div>

        <hr>

        <p style="color:white;">
        Untuk mencapai dana pensiun
        sebesar Rp {target_dana:,.0f}
        pada usia {usia_pensiun} tahun,
        diperlukan tabungan sekitar
        Rp {tabungan:,.0f}
        per bulan.
        </p>

        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<br><br>

<div style="
text-align:center;
color:#94A3B8;
padding:30px;
">

AKTUARIA

<br>

Perhitungan Cerdas untuk Masa Depan

</div>
""", unsafe_allow_html=True)
