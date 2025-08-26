import streamlit as st

# Bikin judul
st.set_page_config(page_title="Persamaan Linear", layout='centered')
st.title("Persamaan Linear 2D & 3D")
st.sidebar.title("Menu")

# Pilihan Persamaan 
st.sidebar.markdown("Pilih 2D atau 3D di Panel Utama")
option = st.sidebar.selectbox("Pilih Opsi:", ["2D", "3D"])

# Fungsi Tombol
if st.sidebar.button("Mulai Ulang"):
    st.session_state.clear()
    st.experimental_rerun()
    
    # Fungsi Tombol input
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Tentang Aplikasi")
if option == "2D":
    st.sidebar.markdown("""
    - 'A = [[1, 0], [0, 1]]')
    - 'b = [2, 3]'
    - ***Hasil:** (2.0, 3.0)
    """)
else:
    st.sidebar.markdown("""
    - 'A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]'
    - 'b = [2, 3, 4]'
    - ***Hasil:** (2.0, 3.0, 4.0)
    """)

if option == "2D":
    from Persamaan_Linear.Two_D import matriks_2D
    matriks_2D()
else:
    from Persamaan_Linear.Three_D import matriks_3D
    matriks_3D()

# Fungsi bikin footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        👨‍💻 Dibuat oleh <b>Maliki Mayzar</b><br><br>
        <a href="https://github.com/malikimayzar" target="_blank" style="margin-right: 15px;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" 
            width="40" height="40">
        </a>
        <a href="https://instagram.com/malikimayzar" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" 
            width="40" height="40">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
