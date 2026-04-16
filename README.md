###🏎️ F1 Data Analytics Dashboard (Local API)
Sebuah dashboard analitik Full-Stack yang dirancang untuk mengekstrak, memproses, dan memvisualisasikan data telemetri dan waktu putaran Formula 1 secara end-to-end. Proyek ini mendemonstrasikan implementasi pipeline data yang utuh, mulai dari sumber data mentah hingga visualisasi antarmuka web interaktif menggunakan Semantic HTML.

✨ Update Terbaru: Telemetry Integration
Menambahkan fitur visualisasi data telemetri beresolusi tinggi. Fitur ini menarik data sensor mobil (Kecepatan, Throttle, Putaran Mesin/RPM, dan Tekanan Rem) pada fastest lap seorang pembalap, lalu memetakannya berdasarkan jarak lintasan (Distance). Visualisasi menggunakan multi-axis (sumbu Y ganda) untuk memisahkan skala metrik yang berbeda secara proporsional.

🛠️ Tech Stack
Proyek ini dibangun dengan memisahkan (Separation of Concerns) antara pemrosesan data, penyediaan API, dan antarmuka pengguna:

Data Source: FastF1 (Python Library)

Database: MariaDB / MySQL (Penyimpanan relasional tersentralisasi)

Backend API: Python Flask (Menyajikan data berformat JSON, dilengkapi CORS)

Frontend: Semantic HTML5, Vanilla CSS3 (Grid & Flexbox), Vanilla JavaScript (Fetch API)

Data Visualization: Chart.js

📊 Fitur Utama Saat Ini
Driver Board: Menampilkan daftar pembalap beserta warna identitas tim yang ditarik secara dinamis dari database.

Pace Comparison (Lap Times): Grafik interaktif yang membandingkan fluktuasi waktu putaran pembalap (contoh: Top 3 Finishers) dari awal hingga akhir balapan untuk melihat strategi pit-stop dan degradasi ban.

Telemetry Analysis: Analisis mendalam satu putaran penuh (fastest lap) yang menampilkan kurva sinkron antara Speed (km/h), Throttle (%), Brake (%), dan RPM terhadap posisi di sirkuit.

🚀 Roadmap Pengembangan (What's Next?)
Proyek ini sedang dalam tahap transisi menuju arsitektur Multi-Page Application dengan perombakan desain yang lebih profesional:

[ ] Merancang purwarupa (prototyping) UI/UX sistem navigasi dan tata letak grafis menggunakan Figma.

[ ] Memisahkan halaman berdasarkan kategori (Profil Pembalap, Komparasi Pace, Analisis Telemetri).

[ ] Memperkaya database profil pembalap (Bio, Foto, Kewarganegaraan).

[ ] Memecah visualisasi telemetri ke dalam beberapa canvas yang disusun vertikal (seperti software ATLAS/MoTeC F1 asli) agar lebih mudah dibaca teknisi.

Dibangun sebagai eksplorasi arsitektur Sistem Informasi dan Analisis Data.

Built as a practical exploration of Information Systems architecture and Data Analytics.


###HOW TO INSTAL LIBRARY
 
 ⚙️ Local Setup & Installation

Ensure you have **Python 3.8+** and **MySQL/MariaDB** installed on your machine before running this project.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/f1-dashboard.git](https://github.com/your-username/f1-dashboard.git)
   cd f1-dashboard

2. Create a Virtual Environment (Recommended):
   This ensures project dependencies remain isolated from your global Python environment.
   python -m venv venv

# For Windows users:
venv\Scripts\activate

# For Mac/Linux users:
source venv/bin/activate

3. Install the required Python libraries:
   Run the following command to install all necessary backend and ETL dependencies:
   pip install fastf1 pandas sqlalchemy pymysql flask flask-cors

4. MySQL/MariaDB Database Setup:
  [] Create a new database named f1_analysis in your local SQL server.
  [] Open etl_telemetry.py and opp.py, and ensure the create_engine connection string matches your local database credentials (e.g., mysql+pymysql://root:password@localhost/f1_analysis).

5. Run the Application:
   [] Since the frontend utilizes Chart.js via CDN, no npm or Node.js installation is required.
   [] Simply start the Flask API server by running the following command in your terminal:

python opp.py

   [] Open index.html using the Live Server extension in VS Code, and your dashboard is ready to use!
