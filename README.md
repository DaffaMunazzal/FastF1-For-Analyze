**INDONESIA :**


🏎️ F1 Data Analytics Dashboard (Local API)
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


**ENGLISH :**


🏎️ F1 Data Analytics Dashboard (Local API)
A Full-Stack analytics dashboard designed to extract, process, and visualize Formula 1 telemetry and lap time data end-to-end. This project demonstrates a complete data pipeline implementation, from raw data extraction to interactive web visualization using Semantic HTML.

✨ Latest Update: Telemetry Integration
Added high-resolution telemetry data visualization. This feature extracts car sensor data (Speed, Throttle, Engine RPM, and Brake Pressure) on a driver's fastest lap and maps it against track distance. The visualization utilizes a multi-axis chart to proportionally separate different metric scales without overlapping.

🛠️ Tech Stack
Built with a strict Separation of Concerns approach, dividing data processing, API serving, and the user interface:

Data Source: FastF1 (Python Library)

Database: MariaDB / MySQL (Centralized relational storage)

Backend API: Python Flask (Serving JSON data with CORS enabled)

Frontend: Semantic HTML5, Vanilla CSS3 (Grid & Flexbox), Vanilla JavaScript (Fetch API)

Data Visualization: Chart.js

📊 Current Key Features
Driver Board: Displays a list of drivers along with their team identity colors dynamically pulled from the database.

Pace Comparison (Lap Times): An interactive chart comparing lap time fluctuations (e.g., Top 3 Finishers) from start to finish, highlighting pit-stop strategies and tire degradation.

Telemetry Analysis: In-depth analysis of a single full lap (fastest lap) showing synchronized curves of Speed (km/h), Throttle (%), Brake (%), and RPM against track position.

🚀 Development Roadmap (What's Next?)
The project is currently transitioning towards a Multi-Page Application (MPA) architecture with a more professional design overhaul:

[ ] Prototype UI/UX navigation systems and layout using Figma.

[ ] Separate views by category (Driver Profiles, Pace Comparison, Telemetry Analysis).

[ ] Enrich the driver profile database (Biography, Headshots, Nationality).

[ ] Split the telemetry visualization into multiple vertically stacked canvases (similar to actual F1 ATLAS/MoTeC software) for better readability.

Built as a practical exploration of Information Systems architecture and Data Analytics.
