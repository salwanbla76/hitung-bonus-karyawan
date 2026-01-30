%%writefile app.py
import streamlit as st

# --- INIT --- 
if "slide" not in st.session_state:
  st.session_state.slide = 1

# --- SLIDE 1 ---
if st.session_state.slide == 1:
  col1, col2 = st.columns([2, 2], vertical_alignment="center")

  with col1:
    st.image ("gedung.jpg", caption="Gedung Utama PT Astra", use_container_width=True)

  with col2:
    st.title("Aplikasi Perhitungan Bonus Karyawan")
    st.write("Berdasarkan Kinerja dan Masa Kerja")

    if st.button("Lanjut"):
      st.session_state.slide = 2
      st.rerun()

# --- SLIDE 2 --- 
elif st.session_state.slide == 2:
    st.header("Data Karyawan PT Astra")

    nama = st.text_input("Nama Karyawan")
    gaji = st.text_input("Gaji Pokok")
    lama = st.number_input("Lama Kerja (tahun)", min_value=0)
    kinerja = st.selectbox("Nilai Kinerja", ["A", "B", "C"])

    colA, colB = st.columns(2)

    with colA:
        if st.button("Kembali"):
            st.session_state.slide = 1
            st.rerun()

    with colB:
        if st.button("Hitung"):
          try:
            #mengubah variabel gaji teks mnenjadi angka
            gaji_bersih = int(gaji) if gaji else 0

            st.session_state.nama = nama
            st.session_state.gaji = gaji_bersih
            st.session_state.lama = lama
            st.session_state.kinerja = kinerja
            st.session_state.slide = 3
            st.rerun()

          except ValueError:
            st.error("Gaji wajib diisi!!")

# --- SLIDE 3 ---
elif st.session_state.slide == 3:
    st.header("📊 Hasil Perhitungan")

    gaji = st.session_state.gaji
    lama = st.session_state.lama
    kinerja = st.session_state.kinerja

    if kinerja == "A":
        bonus_p = 0.20
    elif kinerja == "B":
        bonus_p = 0.10
    else:
        bonus_p = 0.05

    if lama >= 5:
        bonus_p += 0.05

    bonus = gaji * bonus_p

    st.success(f"Nama: {st.session_state.nama}")
    st.write(f"Bonus: Rp {bonus: ,.0f}")
    st.write(f"Total Gaji: Rp {gaji + bonus: ,.0f}")

    if st.button("Ulangi"):
        st.session_state.slide = 1
        st.rerun()