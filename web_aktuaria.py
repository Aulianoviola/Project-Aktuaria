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

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* =========================
   BACKGROUND
========================= */

.stApp{
    background:
    linear-gradient(
        180deg,
        #FAF8FD 0%,
        #F6F1FB 100%
    );
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{
    background:
    linear-gradient(
        180deg,
        #6F4BD8,
        #8E6AF0
    );
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* =========================
   HERO
========================= */

.hero{

background-image:
url("https://share.google/VaT3e9S1k2R2ae27p");

background-repeat:no-repeat;

background-position:right center;

background-size:320px;
}
.hero-title{

    font-size:72px;

    font-weight:800;

    color:#2D1F4A;

    line-height:1.1;
}

.hero-sub{

    font-size:22px;

    color:#786F87;

    line-height:1.8;

    max-width:750px;
}

/* =========================
   CARD
========================= */

.card{

    background:white;

    border-radius:28px;

    padding:30px;

    min-height:240px;

    border:1px solid #EEE6FA;

    box-shadow:
    0 10px 25px rgba(0,0,0,.04);

    transition:.3s;

    position:relative;

    overflow:hidden;
}

.card:hover{

    transform:translateY(-6px);

    box-shadow:
    0 20px 40px rgba(111,75,216,.10);
}

/* =========================
   CARD TOP BAR
========================= */

.card-purple{
    border-top:8px solid #7C5CE6;
}

.card-pink{
    border-top:8px solid #FF7BB5;
}

.card-green{
    border-top:8px solid #10B981;
}

.card-gold{
    border-top:8px solid #D4A24C;
}

.card-blue{
    border-top:8px solid #3B82F6;
}

/* =========================
   ICON BOX
========================= */

.icon{

    width:65px;
    height:65px;

    border-radius:18px;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:30px;

    margin-bottom:20px;
}

.icon-purple{
    background:#EFE9FF;
}

.icon-pink{
    background:#FFE8F3;
}

.icon-green{
    background:#DDFBF0;
}

.icon-gold{
    background:#FFF2D8;
}

.icon-blue{
    background:#E3EEFF;
}

/* =========================
   CARD TEXT
========================= */

.card h3{

    color:#2D1F4A;

    font-size:24px;

    font-weight:700;

    margin-bottom:15px;
}

.card p{

    color:#7B728B;

    font-size:15px;

    line-height:1.8;
}

/* =========================
   BADGE
========================= */

.badge{

    display:inline-block;

    background:#F4EEFF;

    color:#6F4BD8;

    padding:8px 14px;

    border-radius:999px;

    font-size:12px;

    font-weight:600;

    margin-bottom:18px;
}

/* =========================
   RESULT CARD
========================= */

.result{

    background:
    linear-gradient(
        135deg,
        #7C5CE6,
        #A78BFA
    );

    border-radius:35px;

    padding:45px;

    color:white;

    box-shadow:
    0 20px 40px rgba(124,92,230,.18);
}

.result-title{

    color:#EDE7FF;

    letter-spacing:2px;

    font-size:14px;

    font-weight:600;

    margin-bottom:10px;
}

.result-value{

    font-size:58px;

    font-weight:800;

    line-height:1.2;

    color:white;
}

/* =========================
   BUTTON
========================= */

.stButton > button{

    width:100%;

    background:
    linear-gradient(
        135deg,
        #6F4BD8,
        #8E6AF0
    ) !important;

    color:white !important;

    border:none !important;

    border-radius:14px !important;

    height:55px !important;

    font-size:15px !important;

    font-weight:600 !important;

    box-shadow:
    0 8px 20px rgba(111,75,216,.20);

    transition:.3s;
}

.stButton > button:hover{

    transform:translateY(-2px);

    background:
    linear-gradient(
        135deg,
        #5E3CC4,
        #7D58EA
    ) !important;
}

/* =========================
   INPUT
========================= */

.stNumberInput input,
.stTextInput input{

    background:white !important;

    border:1px solid #E7DFF5 !important;

    border-radius:15px !important;

    height:52px !important;

    color:#2D1F4A !important;
}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"] > div{

    border-radius:15px !important;

    border:1px solid #E7DFF5 !important;

    min-height:52px !important;
}

/* =========================
   FOOTER
========================= */

.footer{

    text-align:center;

    color:#8D839F;

    padding:30px;

    font-size:14px;
}

/* =========================
   SCROLLBAR
========================= */

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#B79DF5;
    border-radius:999px;
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
        <div class="card card-purple">
            <h3>BUNGA MAJEMUK</h3>
            <p>Menghitung pertumbuhan investasi berdasarkan bunga majemuk.</p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="bunga"):
            st.session_state.menu = "Bunga"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>NILAI MASA DEPAN</h3>
            <p>Proyeksi nilai investasi pada masa mendatang.</p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="fv"):
            st.session_state.menu = "FV"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>TARGET KEUANGAN</h3>
            <p>Menentukan kebutuhan tabungan untuk mencapai tujuan finansial.</p>
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
            <p>Menghitung kebutuhan dana cadangan keuangan.</p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="darurat"):
            st.session_state.menu = "Darurat"
            st.rerun()
    
    with col5:
        st.markdown("""
        <div class="card">
            <h3>DANA PENSIUN</h3>
            <p>Perencanaan dana pensiun jangka panjang.</p>
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
            Menghitung pertumbuhan investasi berdasarkan bunga majemuk.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    left, center, right = st.columns([1,2,1])

    with center:

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

        hitung = st.button(
            "Hitung",
            use_container_width=True
        )

    if hitung:

        hasil = modal * (1+bunga/100)**waktu
        keuntungan = hasil - modal

        persen = (
            keuntungan/modal*100
            if modal > 0
            else 0
        )

        result_col = st.columns([1,2,1])[1]

        with result_col:
            st.markdown(f"""
            <div class="result">

            <div class="result-title">
            HASIL PERHITUNGAN
            </div>

            <div class="result-value">
            Rp {hasil:,.0f}
            </div>

            <hr>

            <p style="color:white;font-size:18px;">
            Keuntungan : Rp {keuntungan:,.0f}
            </p>

            <p style="color:white;font-size:18px;">
            Pertumbuhan : {persen:.2f}%
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

    st.write("")

    left, center, right = st.columns([1,2,1])
    
    with center:
    
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
    
        hitung_fv = st.button(
            "Hitung Future Value",
            use_container_width=True
        )
    
    if hitung_fv:
    
        fv = pv * (1+bunga/100)**tahun
    
        with st.columns([1,2,1])[1]:
    
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

    st.write("")

    left, center, right = st.columns([1,2,1])

    with center:

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
    
        hitung_target = st.button(
            "Hitung Target",
            use_container_width=True
        )
    
    if hitung_target:
    
        tabungan = harga / bulan
    
        with st.columns([1,2,1])[1]:
    
            st.markdown(f"""
            <div class="result">
    
            <div class="result-title">
            TABUNGAN PER BULAN
            </div>
    
            <div class="result-value">
            Rp {tabungan:,.0f}
            </div>
    
            <p style="color:white;margin-top:20px;">
            Target: {target}
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

    st.write("")

    left, center, right = st.columns([1,2,1])

    with center:

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

        hitung_darurat = st.button(
            "Hitung Dana Darurat",
            use_container_width=True
        )

    if hitung_darurat:

        if status == "Belum Menikah":
            faktor = 6

        elif status == "Menikah":
            faktor = 9

        else:
            faktor = 12

        dana = pengeluaran * faktor

        with st.columns([1,2,1])[1]:

            st.markdown(f"""
            <div class="result">

            <div class="result-title">
            DANA DARURAT IDEAL
            </div>

            <div class="result-value">
            Rp {dana:,.0f}
            </div>

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

    st.write("")

    left, center, right = st.columns([1,2,1])
    
    with center:
    
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
    
        hitung_pensiun = st.button(
            "Hitung Dana Pensiun",
            use_container_width=True
        )
    if hitung_pensiun:

        sisa_tahun = usia_pensiun - usia

        total_bulan = sisa_tahun * 12

        tabungan = (
            target_dana / total_bulan
            if total_bulan > 0
            else 0
        )
        with st.columns([1,2,1])[1]:
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
