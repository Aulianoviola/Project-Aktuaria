import streamlit as st

st.set_page_config(
    page_title="AKTUARIA",
    page_icon="A",
    layout="wide"
)

st.markdown("""
<style>

/* =========================
   FONT
========================= */

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */
.stApp{
    background:
    linear-gradient(
        135deg,
        #f8faff 0%,
        #eef2ff 40%,
        #ede9fe 100%
    );
}

/* Hero */
.hero{
    background:white;
    border-radius:35px;
    padding:70px;
    box-shadow:
    0 25px 50px rgba(99,102,241,.10);

    position:relative;
    overflow:hidden;
}

.hero::before{
    content:"";
    position:absolute;

    width:400px;
    height:400px;

    right:-120px;
    top:-120px;

    background:
    radial-gradient(
        circle,
        rgba(139,92,246,.20),
        transparent 70%
    );
}

.hero-title{
    font-size:72px;
    font-weight:800;
    color:#111827;
}

.hero-sub{
    font-size:22px;
    color:#6B7280;
    max-width:700px;
}

/* CARD */
.card{
    background:
    rgba(255,255,255,.8);

    backdrop-filter:blur(20px);

    border-radius:30px;

    padding:30px;

    min-height:240px;

    border:
    1px solid rgba(255,255,255,.8);

    box-shadow:
    0 15px 40px rgba(99,102,241,.08);

    transition:.35s;
}

.card:hover{
    transform:translateY(-8px);
}

.card h3{
    color:#111827;
    font-size:24px;
    font-weight:700;
}

.card p{
    color:#6B7280;
    line-height:1.8;
}

/* Statistic Card */
.stat-card{
    background:white;

    border-radius:25px;

    padding:25px;

    text-align:center;

    box-shadow:
    0 10px 30px rgba(0,0,0,.05);
}

.stat-number{
    font-size:28px;
    font-weight:800;
    color:#4F46E5;
}

.stat-title{
    color:#6B7280;
}

/* Result */
.result{
    background:
    linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );

    border-radius:35px;

    padding:45px;

    color:white;

    box-shadow:
    0 20px 50px rgba(124,58,237,.30);
}

.result-title{
    color:#ddd6fe;
    letter-spacing:2px;
}

.result-value{
    color:white;
    font-size:60px;
    font-weight:800;
}

/* Button */
.stButton > button{

    border:none;

    border-radius:18px;

    height:55px;

    background:
    linear-gradient(
        135deg,
        #6366F1,
        #8B5CF6
    );

    color:white;

    font-weight:600;

    transition:.3s;
}

.stButton > button:hover{

    transform:translateY(-3px);

    box-shadow:
    0 10px 30px rgba(139,92,246,.40);
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
    
    <br>
    
    <div class="hero-sub">
    Kelola investasi, dana darurat, target keuangan,
    dan perencanaan pensiun dalam satu dashboard modern.
    </div>
    
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>BUNGA MAJEMUK</h3>
        
            <p>
            Menghitung pertumbuhan investasi
            berdasarkan bunga majemuk.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="bunga"):
            st.session_state.menu = "Bunga"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>NILAI MASA DEPAN</h3>
        
            <p>
            Proyeksi nilai investasi
            pada masa mendatang.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="fv"):
            st.session_state.menu = "FV"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>TARGET KEUANGAN</h3>
        
            <p>
            Menentukan kebutuhan tabungan
            untuk mencapai tujuan finansial.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="target"):
            st.session_state.menu = "Target"
            st.rerun()
    
    st.write("")
    
    col4,col5 = st.columns(2)
    
    with col4:
        st.markdown("""
        <div class="card">
            <h3>DANA DARURAT</h3>
        
            <p>
            Menghitung kebutuhan dana
            cadangan keuangan.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="darurat"):
            st.session_state.menu = "Darurat"
            st.rerun()
    
    with col5:
        st.markdown("""
        <div class="card">
            <h3>DANA PENSIUN</h3>
        
            <p>
            Perencanaan dana pensiun
            jangka panjang.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="pensiun"):
            st.session_state.menu = "Pensiun"
            st.rerun()
        
    # ==========================
    # FINANCIAL INSIGHT
    # ==========================
    
    st.write("")
    st.write("")
    
    st.markdown("""
    <div class="result">
    
    <div class="result-title">
    FINANCIAL INSIGHT
    </div>
    
    <div class="result-value">
    Konsistensi lebih penting daripada jumlah yang besar di awal.
    </div>
    
    </div>
    """, unsafe_allow_html=True)
        
        
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
