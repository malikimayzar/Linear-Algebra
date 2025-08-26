import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt

def tampilkan_sumbu(ax):
    # Panah Sumbu X Y & Z
    ax.quiver(0, 0, 0, 1, 0, 0, color='black', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='black', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='black', arrow_length_ratio=0.1)

    # Label Sumbu 
    ax.text(1.1, 0, 0, 'X', color='black')
    ax.text(0, 1.1, 0, 'Y', color='black')
    ax.text(0, 0, 1.1, 'Z', color='black')

def matriks_3D():
    solusi = None 
    xmin, xmax, ymin, ymax, zmin, zmax = -10, 10, -10, 10, -10, 10

    # Fungsi Masukan Matriks A
    st.markdown("### Masukan Koefisien Matriks A (3x3)")
    ax1 = st.number_input("Masukan Nilai Ax1:")
    ax2 = st.number_input("Masukan Nilai Ax2:")
    ax3 = st.number_input("Masukan Nilai Ax3:")
    ay1 = st.number_input("Masukan Nilai Ay1:")
    ay2 = st.number_input("Masukan Nilai Ay2:")
    ay3 = st.number_input("Masukan Nilai Ay3:")
    az1 = st.number_input("Masukan Nilai Az1:")
    az2 = st.number_input("Masukan Nilai Az2:")
    az3 = st.number_input("Masukan Nilai Az3:")
    A = np.array([[ax1, ax2, ax3],
                  [ay1, ay2, ay3],
                  [az1, az2, az3]])
    
    # Fungsi Masukan Nilai vektor b:
    st.markdown("### Masukan Vektor b (3x1)")
    vektor_b1 = st.number_input("Masukan Nilai b1:")
    vektor_b2 = st.number_input("Masukan Nilai b2:")
    vektor_b3 = st.number_input("Masukan Nilai b3:")
    b = np.array([vektor_b1, vektor_b2, vektor_b3])

    determinan = np.linalg.det(A)
    st.write(f"Determinannya: {determinan:.2f}")

    if determinan != 0:
        x = np.linalg.solve(A, b)
        solusi = x
        st.write(f"Solusi unik (titik potong): {x}")
        buffer = 5
        xmin = min(-10, x[0] - buffer)
        xmax = max( 10, x[0] + buffer)
        ymin = min(-10, x[1] - buffer)
        ymax = max( 10, x[1] + buffer)
        zmin = min(-10, x[2] - buffer)
        zmax = max( 10, x[2] + buffer)
    else:
        #Fungsi Cek Apakah solusi Tak higga atau tak ada solusi
        Ab = np.column_stack((A, b))
        rankA = np.linalg.matrix_rank(A)
        rankAb = np.linalg.matrix_rank(Ab)

        if rankA == rankAb:
            st.write("Solusi Tak hingga (bidang Tumpang Tindih)")
        else:
            st.write("Tidak ada solusi.(garis paralel)")
    # Visualisasi 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    tampilkan_sumbu(ax)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin, zmax)
    ax.grid(True)
    ax.set_box_aspect([1, 1, 1])
    
    # Generatif Nilai x untuk plotting garis
    x, y = np.meshgrid(np.linspace(xmin, xmax, 20),
                       np.linspace(ymin, ymax, 20))
    # Bidang Pertama
    if A[0, 2] != 0:
        z1 = (b[0] - A[0, 0]*x - A[0, 1]*y) / A[0, 2]
        ax.plot_surface(x, y, z1, alpha=0.5, color='r')

    # Bidang Kedua
    if A[1, 2] != 0:
        z2 = (b[1] - A[1, 0]*x - A[1, 1]*y) / A[1, 2]
        ax.plot_surface(x, y, z2, alpha=0.5, color='b')

    # Bidang Ketiga 
    if A[2, 2] != 0:
        z3 = (b[2] - A[2, 0]*x -A[2, 1]*y) / A[2, 2]
        ax.plot_surface(x, y, z3, alpha=0.5, color='g')

    if solusi is not None:
        ax.scatter(solusi[0], solusi[1], solusi[2], color='k',
                   s=80, label=f'solusi ({solusi[0]:.2f},{solusi[1]:.2f}, {solusi[2]:.2f})')
        
        
        
    ax.legend(loc='best')
    st.pyplot(fig)

if __name__ == "__main__":
    matriks_3D()
