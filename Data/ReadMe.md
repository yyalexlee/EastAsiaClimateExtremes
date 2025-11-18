### 📦 Data Description

***1. Spatial/Temporal Coverage***  

|         |Domain    |Resolution|
|---------|----------|----------|
|**Space**|21-48N, 114-141E|1.5deg|
|**Time** |1940-2024(ERA5), 1982-2024(OISST), ECMWF-hindcast version 2016 & 2024|Daily / Weekly|  
  
&nbsp;  
***2. Data format*** 

|        |Desscription|
|--------|------------|
|Pickle|Easy to use by **importing pickle** (e.g. import pickle)|
|NetCDF|If you have **Python version 3.8 or higher**, you can easily read **nc files** with **xarray**|  

&nbsp;  
***3. Climate Data***  

|        |Description|
|--------|-----------|
|Frequency         |Daily/Weekly|
|Variables         |Mean Near Surface Temperature(T2M), Sea Surface Temperature(SST), Total Precipitation(TP)|
|Type              |Original Timeseries, Climatological Long-Term Mean, 90/95th Percentile Thresholds(p90/p95)|
|Resources         |ERA5, OISST(only for SST) and ECMWF-hindcast|
|Ref. Period       |1991-2020(ERA5/OISST, WMO recommendation), 2004-2023(ECMWF-hindcast)|  

**3.1. ERA5**  
(그냥 제안)  &nbsp;  
  
**3.2. OISST**  
(그냥 제안)  &nbsp;  
  
&nbsp;  
**3.3. ECMWF-hindcast datasets**  or 3.1. ECMWF-hindcast datasets  
**The ECMWF-hindcast NetCDF data1** was reconstructed from ECMWF Hindcast versions **2016** and **2024**.
For each forecast initialization date, data corresponding to **lead week 3 (days 15–21 after initialization)** were extracted and reorganized into daily records.  

**The ECMWF-hindcast NetCDF data2** was generated based on **data 1**, 90th-percentile climatological thresholds nc file (e.g., `t2m_clim90th`) were computed for each ECMWF Hindcast version using the forecast issued dates.  

