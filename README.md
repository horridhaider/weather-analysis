# U.S. Cities Weather Analysis 2025

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0.2-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-4C72B0)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.8-orange)
![API](https://img.shields.io/badge/API-Open--Meteo-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

End-to-end weather data analysis project. Pulls real 2025 daily weather data from the **Open-Meteo API** for 5 major U.S. cities, engineers features, and extracts quantitative insights — covering seasonal trends, city comparisons, extreme events, heatwaves, and precipitation patterns.

<p float="left">
  <img width="2209" height="1765" alt="heatmap_avg_monthly_temp" src="https://github.com/user-attachments/assets/7356065b-cb2c-4c5e-b494-06af5433914e" />
  <img width="2534" height="1407" alt="avg_temp_timeline" src="https://github.com/user-attachments/assets/18689bad-1f61-4514-a283-00687b1add74" />
</p>





---

## Cities Covered

| City | State | Climate |
|------|-------|---------|
| New York | NY | Humid continental |
| Los Angeles | CA | Mediterranean |
| Chicago | IL | Humid continental |
| Houston | TX | Humid subtropical |
| Phoenix | AZ | Hot desert |

---

## Project Structure

```
hr-analysis/
│
├── openweather.ipynb       # Main notebook (fetch -> clean -> EDA -> analysis)
├── fetcher.py              # Open-Meteo API module
├── requirements.txt
├── .gitignore
│
├── fetched data/           # Raw API output (.xlsx)
├── clean output/           # Cleaned dataset (.xlsx)
└── plots/                  # Auto-saved visualizations (.png)
```

---

## Pipeline

```
Open-Meteo API
      |
      v
  fetcher.py  -->  raw DataFrame
      |
      v
  Data Cleaning
  - Rename columns
  - Fix datetime dtype
      |
      v
  Feature Engineering
  - avg_temp = (temp_max + temp_min) / 2
  - temp_range = temp_max - temp_min
  - month (extracted from date)
  - season (mapped from month)
      |
      v
  EDA + Analysis
  - Distributions, trends, outliers
  - City comparisons, heatmaps
  - Extreme events, heatwaves
  - Seasonal pattern analysis
```

---

## Key Findings

- **Phoenix** peaks at ~38 degC in summer — hottest city by a wide margin
- **Chicago** has the highest temperature volatility (std ~10.5 degC) — most unpredictable weather
- **Los Angeles** is the most stable city year-round — lowest temperature standard deviation
- **July/August** are the harshest months when combining heat and precipitation
- **Houston** records the most high-precipitation days (>20mm) among all cities
- **Chicago** has the sharpest seasonal swing — nearly 30 degC between summer and winter averages

---

## Visualizations

| Chart | What it shows |
|-------|--------------|
| Min/Max Scatter | Correlation between daily lows and highs |
| City Boxplot | Full-year temperature spread per city |
| Monthly Catplot Grid | Month-by-month distributions per city |
| Temperature Timeline | Monthly avg temp trends for all cities |
| Precipitation Timeline | Monthly avg rainfall trends for all cities |
| Heatmap | All cities x all months at a glance |
| Volatility Barplot | Which city's weather changes the most |
| Precipitation Barplot | Average daily rainfall by city |

---

## Setup

```bash
# Clone the repo
git clone https://github.com/horridhaider/hr-analysis.git
cd hr-analysis

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook openweather.ipynb
```

---

## Data Source

[Open-Meteo](https://open-meteo.com/) — Free weather API, no API key required.
Data period: **January 1, 2025 – December 31, 2025**
Variables fetched: `temperature_2m_max`, `temperature_2m_min`, `precipitation_sum`

---

## Author

**Haider Mirza** — Data Analyst & Python Developer
- GitHub: [@horridhaider](https://github.com/horridhaider)
- Fiverr: [haidar_mirza](https://www.fiverr.com/haidar_mirza)
