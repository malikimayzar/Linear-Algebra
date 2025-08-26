import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt

def tampilkan_sumbu(ax):
    # panah sumbu X & Y
    ax.quiver(0, 0, 1, 0, color='black')
    ax.quiver(0, 0, 0, 1, color='black')

    # Label sumbu 
    ax.text(1.1, 0, 'X', color='black')
    ax.text(0, 1.1, 'Y', color='black')

def matriks_2D():
    solusi = None
    xmin, xmax, ymin, ymax = -10, 10, -10, 10

    #Fungsi Masukan Matriks A
    st.markdown("### Masukan Koefisien Matriks A (2x2)")
    ax1 = st.number_input("Masukan Nilai Ax1:")
    ax2 = st.number_input("Masukan Nilai Ax2:")
    ay1 = st.number_input("Masukan Nilai Ay1:")
    ay2 = st.number_input("Masukan Nilai Ay2:")
    A = np.array([[ax1, ax2],
                [ay1, ay2]])

    #Fungsi Masukan vektor b:
    st.markdown("### Masukan Vektor b (2x1)")
    vektor_b1 = st.number_input("Masukan Nilai b1:")
    vektor_b2 = st.number_input("Masukan Nilai b2:")
    b = np.array([vektor_b1, vektor_b2])

    determinan = np.linalg.det(A)
    st.write(f"Determinanya: {determinan:.2f}")

    if determinan != 0:
        x = np.linalg.solve(A, b)
        solusi = x
        st.write(f"Solusi Unik (titik potong): {x}")
        buffer = 5
        xmin = min(-10, x[0] - buffer)
        xmax = max( 10, x[0] + buffer)
        ymin = min(-10, x[1] - buffer)
        ymax = max( 10, x[1] + buffer)

    else:
        # Fungsi Cek Persamaan tak hingga atau tak ada solusi:
        Ab = np.column_stack((A, b))
        rankA = np.linalg.matrix_rank(A)
        rankAb = np.linalg.matrix_rank(Ab)

        if rankA == rankAb:
            st.write("Solusi Tak hingga (garis tumpang tindih)")
        else:
            st.write("Tak ada solisi. (garis Paralel)")

    # Visualisasi
    fig, ax = plt.subplots()
    tampilkan_sumbu(ax)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')

    x_vals = np.linspace(xmin, xmax, 500)

    # Garis pertama
    if A[0, 1] != 0:
        y_vals1 = (b[0] - A[0, 0] * x_vals) / A[0, 1]
        ax.plot(x_vals, y_vals1, 'r-', linewidth=2, label=f'{A[0,0]}x + {A[0,1]}y = {b[0]}')
    elif A[0, 0] != 0:
        ax.axvline(x=b[0]/A[0,0], color='r', linewidth=2, label=f"{A[0,0]}x = {b[0]}")
    else:
        st.warning("Garis pertama tidak valid (A[0,0] dan A[0,1] tidak boleh keduanya nol).")

    # Garis kedua
    if A[1, 1] != 0:
        y_vals2 = (b[1] - A[1, 0] * x_vals) / A[1, 1]
        ax.plot(x_vals, y_vals2, 'b-', linewidth=2, label=f'{A[1,0]}x + {A[1,1]}y = {b[1]}')
    elif A[1, 0] != 0:
        ax.axvline(x=b[1]/A[1,0], color='b', linewidth=2, label=f"{A[1,0]}x = {b[1]}")
    else:
        st.warning("Garis kedua tidak valid (A[1,0] dan A[1,1] tidak boleh keduanya nol).")

    if solusi is not None:
       ax.scatter(solusi[0], solusi[1], color='green', marker='o', s=120, edgecolors='black',
           label=f'Solusi ({solusi[0]:.2f}, {solusi[1]:.2f})')

    ax.legend(loc='best')
    st.pyplot(fig)

if __name__ == "__main__":
    matriks_2D()
        

    


    




    
  


