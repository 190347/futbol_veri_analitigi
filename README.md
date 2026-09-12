# Football Set-Piece Analytics & Data Pipeline

An end-to-end data engineering and analytics project extracting, transforming, and visualizing set-piece (corner kick) data using the StatsBomb Open Data repository.

## 📌 Project Architecture
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline tailored for sports analytics:
1. **Extract:** Parses complex JSON match events from StatsBomb.
2. **Transform:** Filters corner kicks, cleanses data, and splits standard coordinate arrays into relational formats.
3. **Load:** Ingests the transformed data into a structured **PostgreSQL** database via SQLAlchemy.
4. **Visualize:** Renders spatial data directly onto a pitch map using `mplsoccer` and `matplotlib`.

## 🛠️ Tech Stack
* **Database:** PostgreSQL, pgAdmin 4
* **Languages:** Python, SQL
* **Libraries:** Pandas, SQLAlchemy, psycopg2, mplsoccer, Matplotlib
* **Environment:** macOS (M1/ARM64)

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/futbol_veri_analitigi.git](https://github.com/KULLANICI_ADIN/futbol_veri_analitigi.git)
