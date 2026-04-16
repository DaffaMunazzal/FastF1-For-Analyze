### 🏎️ F1 Data Analytics Dashboard (Local API)
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


### HOW TO INSTAL LIBRARY
 ```
⚙️ Local Setup & Installation

Ensure you have **Python 3.8+** and **MySQL/MariaDB** installed on your machine before running this project.
```
1. **Clone the repository:**  
   ```bash
   git clone [https://github.com/your-username/f1-dashboard.git](https://github.com/your-username/f1-dashboard.git)
   cd f1-dashboard

2. Create a Virtual Environment (Recommended):  
   This ensures project dependencies remain isolated from your global Python environment.
   python -m venv venv

# For Windows users:  
 ```bash
 venv\Scripts\activate
 ```
# For Mac/Linux users:  
 ```bash
 source venv/bin/activate
 ```
3. Install the required Python libraries:  
   Run the following command to install all necessary backend and ETL dependencies:
   ```bash
   pip install fastf1 pandas sqlalchemy pymysql flask flask-cors
   ```
4. MySQL/MariaDB Database Setup:  
 [] Create a new database named f1_analysis in your local SQL server.
 [] Open etl_telemetry.py and opp.py, and ensure the create_engine connection string matches your local database credentials (e.g., mysql+pymysql://root:password@localhost/f1_analysis).

5. Run the Application:  
 [] Since the frontend utilizes Chart.js via CDN, no npm or Node.js installation is required.
 [] Simply start the Flask API server by running the following command in your terminal:
 ```bash
 python opp.py
 ```
 [] Open index.html using the Live Server extension in VS Code, and your dashboard is ready to use!
