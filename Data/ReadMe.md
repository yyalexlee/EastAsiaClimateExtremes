### 📊 Data Download 
This directory should include historical data on East Asia Climate Extremes isolated from ERA5 and ECMWF.

To download the compressed dataset, use the following command:
> wget --content-disposition "https://www.dropbox.com/scl/fi/pqm64be2s46y8zpq0zn1e/EA1.5_P9095.zip?rlkey=rh8vnut3gzecn4472xycdr0da&st=63cbrbsl&dl=0"  
&nbsp;   
### 📦 Data Description
***1. Spatial/Temporal Coverage***  

|         |Domain    |Resolution|
|---------|----------|----------|
|**Space**|21-48N, 114-141E|1.5deg|
|**Time** |1940-2024(ERA5), 1982-2024(OISST), ECMWF-hindcast version 2016 & 2024|Daily / Weekly|  
  
***2. Climate Data***  

|        |Description|
|--------|-----------|
|Frequency         |Daily/Weekly|
|Variables         |Mean Near Surface Temperature(T2M), Sea Surface Temperature(SST), Total Precipitation(TP)|
|Type              |Original Timeseries, Climatological Long-Term Mean, 90/95th Percentile Thresholds(p90/p95)|
|Resources         |ERA5, OISST(only for SST) and ECMWF-hindcast|
|Ref. Period       |1991-2020(ERA5/OISST, WMO recommendation), <br> 2004-2023(for ver.2024 of ECMWF-hindcast), 1996-2015(for ver.2016 of ECMWF-hindcast)|  

***3. Extreme Event Profile***

|        |Description|
|--------|-----------|
|Meta              |***Start/End Date, Duration, Mean/Peak Intensity*** and so forth|            
|Extreme Thresholds|p90, p95|            
|Event Criteria    |D3G5, D5G2 for *AHT/MHW* and D1G3, D3G3 for *HR*|

>*e.g., D3G5 represents minimum three-day **D**uration, permitting **G**aps of up to five days*  

&nbsp;  
***4. Period(Weekly/Monthly) Extremeness Metrics***  

|Metric         |Description|
|---------------|-----------|
|Extreme Days      |Number of days in the period when *T2M_e/TP_e/SST_e* exceed zero|
|Max. Intensity    |Peak *T2M_e/TP_e/SST_e* observed during the period|
|Impact Factor     |Cumulative *T2M_e/TP_e/SST_e* over the period|

>*T2M_e = T2M - thr; TP_e = TP - thr; SST_e = SST - thr*  

&nbsp;  
***5. Data format*** 

|        |Desscription|
|--------|------------|
|Pickle|Easy to use by **importing pickle** (e.g. import pickle)|
|NetCDF|If you have **Python version 3.8 or higher**, you can easily read **nc files** with **xarray**|  

&nbsp;  
**5.1. ECMWF-hindcast datasets**    
**The ECMWF-hindcast NetCDF data1** was reconstructed from ECMWF Hindcast versions **2016** and **2024**.
For each forecast initialization date, data corresponding to **lead week 3 (days 15–21 after initialization)** were extracted and reorganized into daily records.  
  
| data1 information (***e.g., nc file: v2024_ECMWF_hindcast_T2M_w3_2004-2023.nc***) |
| :---|
|Dimensions: (time: 7140, latitude: 72, longitude: 72) <br> Coordinates: <br> * time (time) datetime64[ns] 57kB 2004-01-19 2004-01-20 ... 2024-01-15 <br> * latitude (latitude) float64 576B 57.0 55.5 54.0 52.5 ... -46.5 -48.0 -49.5 <br> * longitude (longitude) float64 576B 52.5 54.0 55.5 ... 156.0 157.5 159.0 <br> Data variables: <br> t2m (time, latitude, longitude) float32 148MB|  

**The ECMWF-hindcast NetCDF data2** was generated based on **data 1**, 90th-percentile climatological thresholds nc file were computed for each ECMWF Hindcast version using the forecast issued dates.  
| data2 information (***e.g., nc file: v2024_ECMWF_hindcast_T2M_w3_clim90th.nc***) |
| :---|
|Dimensions: (latitude: 72, longitude: 72, doy: 356) <br> Coordinates: <br> * latitude (latitude) float64 576B 57.0 55.5 54.0 52.5 ... -46.5 -48.0 -49.5 <br> * longitude (longitude) float64 576B 52.5 54.0 55.5 ... 156.0 157.5 159.0 <br> quantile      float64 8B ... <br> doy (doy) int64 3kB 1 3 4 5 6 7 8 ... 360 361 362 363 364 365 366 <br> Data variables: <br> t2m_clim90th (doy, latitude, longitude) float64 15MB|  
