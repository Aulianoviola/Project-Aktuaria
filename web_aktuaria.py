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
radial-gradient(
circle at top right,
rgba(139,92,246,.25),
transparent 30%
),

radial-gradient(
circle at bottom left,
rgba(37,99,235,.20),
transparent 30%
),

linear-gradient(
135deg,
#020014 0%,
#050021 40%,
#090B3F 100%
);

color:white;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{

background:
linear-gradient(
180deg,
#080022,
#12003D
);

border-right:
1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] *{
color:white;
}

/* =========================
   HERO
========================= */

.hero{

background:
linear-gradient(
145deg,
rgba(15,15,50,.95),
rgba(5,5,30,.95)
);

padding:70px;

border-radius:35px;

border:
1px solid rgba(255,255,255,.08);

box-shadow:
0 0 40px rgba(139,92,246,.15);

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

border-radius:50%;

background:
radial-gradient(
circle,
rgba(139,92,246,.25),
transparent 70%
);

filter:blur(40px);
}

.hero-title{

font-size:72px;

font-weight:800;

line-height:1.1;

color:white;
}

.hero-sub{

font-size:22px;

line-height:1.8;

color:#BFC4E0;

max-width:700px;
}

/* =========================
   CARD
========================= */

.card{

background:
linear-gradient(
145deg,
rgba(17,17,60,.95),
rgba(8,8,35,.95)
);

padding:30px;

border-radius:30px;

min-height:240px;

border:
1px solid rgba(255,255,255,.08);

box-shadow:
0 0 20px rgba(0,0,0,.25);

transition:.4s;
}

.card:hover{

transform:
translateY(-8px);

border:
1px solid rgba(139,92,246,.6);

box-shadow:
0 0 35px rgba(139,92,246,.30);
}

/* =========================
   CARD VARIANTS
========================= */

.card-purple{
border-top:5px solid #8B5CF6;
}

.card-pink{
border-top:5px solid #EC4899;
}

.card-blue{
border-top:5px solid #3B82F6;
}

.card-green{
border-top:5px solid #10B981;
}

.card-orange{
border-top:5px solid #F59E0B;
}

/* =========================
   ICON
========================= */

.icon{

width:65px;
height:65px;

display:flex;
align-items:center;
justify-content:center;

font-size:30px;

border-radius:18px;

margin-bottom:20px;
}

.icon-purple{
background:rgba(139,92,246,.15);
}

.icon-pink{
background:rgba(236,72,153,.15);
}

.icon-blue{
background:rgba(59,130,246,.15);
}

.icon-green{
background:rgba(16,185,129,.15);
}

.icon-orange{
background:rgba(245,158,11,.15);
}

/* =========================
   CARD TEXT
========================= */

.card h3{

font-size:24px;

font-weight:700;

color:white;

margin-bottom:15px;
}

.card p{

color:#BFC4E0;

line-height:1.8;
}

/* =========================
   BADGE
========================= */

.badge{

display:inline-block;

padding:8px 15px;

border-radius:999px;

font-size:12px;

font-weight:600;

margin-bottom:15px;

background:
rgba(139,92,246,.15);

color:#C4B5FD;
}

/* =========================
   RESULT
========================= */

.result{

background:
linear-gradient(
135deg,
#7C3AED,
#2563EB
);

border-radius:35px;

padding:45px;

box-shadow:
0 0 40px rgba(124,58,237,.35);
}

.result-title{

font-size:14px;

letter-spacing:2px;

color:#DDD6FE;
}

.result-value{

font-size:60px;

font-weight:800;

color:white;

line-height:1.1;
}

/* =========================
   BUTTON
========================= */

.stButton > button{

width:100%;

height:55px;

border:none !important;

border-radius:14px !important;

font-weight:700;

color:white !important;

background:
linear-gradient(
135deg,
#8B5CF6,
#2563EB
) !important;

box-shadow:
0 0 25px rgba(139,92,246,.30);

transition:.3s;
}

.stButton > button:hover{

transform:
translateY(-3px);

box-shadow:
0 0 35px rgba(37,99,235,.40);
}

/* =========================
   INPUT
========================= */

.stTextInput input,
.stNumberInput input{

background:
rgba(255,255,255,.05) !important;

color:white !important;

border:
1px solid rgba(255,255,255,.10) !important;

border-radius:15px !important;

height:52px !important;
}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"] > div{

background:
rgba(255,255,255,.05) !important;

border:
1px solid rgba(255,255,255,.10) !important;

border-radius:15px !important;

color:white !important;
}

/* =========================
   LABEL
========================= */

label{
color:white !important;
}

/* =========================
   HR
========================= */

hr{
border:
1px solid rgba(255,255,255,.10);
}

/* =========================
   FOOTER
========================= */

.footer{

text-align:center;

padding:30px;

color:#A5AED0;
}

/* =========================
   SCROLLBAR
========================= */

::-webkit-scrollbar{
width:8px;
}

::-webkit-scrollbar-thumb{

background:
linear-gradient(
180deg,
#8B5CF6,
#2563EB
);

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
        <div class="card card-purple">
            <h3>NILAI MASA DEPAN</h3>
            <p>Proyeksi nilai investasi pada masa mendatang.</p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="fv"):
            st.session_state.menu = "FV"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card card-purple">
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
        <div class="card card-purple">
            <h3>DANA DARURAT</h3>
            <p>Menghitung kebutuhan dana cadangan keuangan.</p>
        </div>
        """, unsafe_allow_html=True)
    
        if st.button("Coba Sekarang →", key="darurat"):
            st.session_state.menu = "Darurat"
            st.rerun()
    
    with col5:
        st.markdown("""
        <div class="card card-purple">
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
    st.error("AKU DI SINI")
    st.markdown(
    """
    <div class="hero">
        <div class="hero-title">
            Dana Pensiun
        </div>
    
        <div class="hero-sub">
            Rencanakan kebutuhan dana
            untuk masa pensiun.
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )

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
