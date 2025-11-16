## 📦 Data Description
***1. Climate Data*** 

|        |Description|
|--------|-----------|
|Frequency         |Daily/Weekly|
|Variables         |Mean Near Surface Temperature(T2M), Sea Surface Temperature(SST), Total Precipitation(TP)|
|Type              |Original Timeseries, Climatological Long-Term Mean, 90/95th Percentile Thresholds(p90/p95)|
|Resources         |ERA5, OISST(only for SST) and ECMWF-hindcast|
|Ref. Period       |1991-2020(ERA5/OISST, WMO recommendation), 2004-2023(ECMWF-hindcast)|  

**1.1. ERA5**  

**1.2. OISST**


**1.3. ECMWF-hindcast datasets**  
The ECMWF-hindcast NetCDF data1 was reconstructed from ECMWF Hindcast versions **2016** and **2024**, containing:
- Mean temperature (T2M)
- Sea surface temperature (SST)
- Precipitation (PREC)  

For each forecast initialization date, data corresponding to **lead week 3 (days 15–21 after initialization)**  
were extracted and reorganized into daily records.

The ECMWF-hindcast NetCDF data2 was generated based on **data 1**, 90th-percentile climatological thresholds (eg., `t2m_clim90th`) were computed for each ECMWF Hindcast version using the forecast issued dates.  

