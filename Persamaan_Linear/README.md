# 🔢 Persamaan Linear Solver  

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Made with NumPy](https://img.shields.io/badge/Made%20with-NumPy-blue)
![Made with Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)

> Solver interaktif untuk sistem persamaan linear 2D & 3D dengan visualisasi real-time.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![NumPy](https://img.shields.io/badge/NumPy-Array-green)

✨ Fitur:
- 🧮 Solver 2D & 3D – Mendukung sistem persamaan linear 2x2 dan 3x3  
- 📊 Visualisasi Interaktif – Grafik vektor & plot 3D interaktif  
- ⚡ Real-time Calculation – Hasil langsung update saat input berubah  
- 🎯 Multiple Solutions Detection – Deteksi solusi unik, tak hingga, atau tidak ada solusi  
- 📱 Responsive Design – Smooth di desktop & mobile  

🚀 Cara Mulai:
Prerequisites
Python 3.10+

Installation
git clone https://github.com/malikimayzar/Persamaan_Linear.git
cd Persamaan_Linear
pip install -r requirements.txt
streamlit run app.py

🎮 Cara Penggunaan
Untuk Persamaan 2D:
a₁x + b₁y = c₁
a₂x + b₂y = c₂

Pilih 2D di sidebar:
    -Input nilai matriks A dan vektor b
    -Lihat solusi dan visualisasi grafik langsung

Untuk Persamaan 3D
text
a₁x + b₁y + c₁z = d₁
a₂x + b₂y + c₂z = d₂  
a₃x + b₃y + c₃z = d₃
Pilih 3D di sidebar

-Input semua koefisien
-Explore visualisasi 3D yang interaktif

🛠️ Tech Stack:
    -Frontend: Streamlit
    -Computing: NumPy, Matplotlib
    -Visualization: Matplotlib 3D, Quiver Plots

Deployment: Streamlit Cloud

📁 Project Structure
text
Persamaan_Linear/
├── app.py             # Main application
├── Two_D.py           # 2D solver module
├── Three_D.py         # 3D solver module
├── requirements.txt   # Dependencies
├── assets/            # Images & preview
└── README.md          # Documentation

🎯 Contoh Penggunaan:
Untuk Persamaan 2D:
$$
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
$$

Untuk Persamaan 3D:
$$
a_1x + b_1y + c_1z = d_1 \\
a_2x + b_2y + c_2z = d_2 \\
a_3x + b_3y + c_3z = d_3


🤝 Contributing
PR dipersilakan! Untuk perubahan besar, buka issue terlebih dahulu.

📄 License
MIT License - lihat LICENSE file untuk detail.

👨‍💻 Author
Maliki Mayzar
GitHub: @malikimayzar
Instagram: @malikimayzar

### 📊 Preview
**2D Solver Preview**
- Visualisasi garis & titik potong
![Preview 2D](assets/preview_2d.png)

**3D Solver Preview**
- Visualisasi bidang & titik potong 3D
![Preview 3D](assets/preview_3d.png)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://persamaan-linear-ahc7kk2dsnhdhwfcthakh2.streamlit.app/)
