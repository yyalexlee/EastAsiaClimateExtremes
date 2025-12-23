## 💾 Data Download 
This directory should include historical data on East Asia Climate Extremes isolated from ERA5 and ECMWF. <br>

If you access the dataset below (***Dropbox***), you can download data separately from the following sub-folders:
```bash
DataFilesforEastAsiaClimateExtremes
├── 0.ExtremeEvents_ERA5_OISST
├── 1.Daily_ERA5_OISST
├── 2.Weekly_ERA5
└── 3.Daily_ECMWFhindcasts
```

To download the compressed dataset, use the following command:

0. ***ExtremeEvents_ERA5_OISST***: Extreme Event Profile and Weekly/Monthly Extremeness Metrics (ERA5/OISST)
```
wget -O 0.ExtremeEvents_ERA5_OISST.zip "https://www.dropbox.com/scl/fo/5hcy3r8jxd6o9qaa267bf/AMI0pTgTvZWf1MXq7SgAZwk?rlkey=z3x1kyrynjeg0wctprfk31aj1&st=ryo0cv1h&dl=0"    
```
1. ***Daily_ERA5_OISST***: Daily Data and Extreme Threshold (ERA5/OISST)
```
wget -O 1.Daily_ERA5_OISST.zip "https://www.dropbox.com/scl/fo/t8082lha97fi5ebqsq77x/ACZu-o6b-b4e05S81-7BkQs?rlkey=d5v7ztkp71nb4d7jx19pgv97u&st=9h8y9v6x&dl=0"    
```
2. ***Weekly_ERA5***: Weekly Data and Extreme Threshold (ERA5)
```
wget -O 2.Weekly_ERA5.zip "https://www.dropbox.com/scl/fo/w12fdxsv89tfhphrrot1l/AD7IuKrO3LrVvkCN1hEA2c0?rlkey=67vr21cu88jt9q625lzboocao&st=yo63qu2p&dl=0"
```
3. ***Daily_ECMWFhindcasts***: Daily Data and Extreme Threshold (ECMWF-hindcast ver.2016/ver.2024)
```
wget -O 3.Daily_ECMWFhindcasts.zip "https://www.dropbox.com/scl/fo/sv3lu1e3qzwwtt6dqnzkq/AEI6Vn0BLPvGmnynbGZ6_Gk?rlkey=8bdbyjjjg472mimxx1lpk9v3b&st=npjwog3p&dl=0"    
```

You can also use curl on Windows, which is available by default on most recent versions, with the following options -L -O -J.
```
curl -L -O -J "URL"
```
  
&nbsp;  
## 📝 Data Description

### ***0. Spatial/Temporal Coverage***  

|         |Domain    |Resolution|
|---------|----------|----------|
|**Space**|21°-48°N, 114°-141°E|1.5deg|
|**Time** |1940-2024(ERA5), 1982-2024(OISST), ECMWF-hindcast version 2016 & 2024|Daily / Weekly|  


### ***1. Original Climate Data***  

|        |Description|
|--------|-----------|
|Frequency         |Daily/Weekly|
|Variables         |2-m Air Temperature(T2M), Sea Surface Temperature(SST), Total Precipitation(TP)|
|Type              |Original Timeseries, Climatological Long-Term Mean, 90/95th Percentile Thresholds(p90/p95)|
|Resources         |ERA5, OISST(only for SST) and ECMWF-hindcast|
|Ref. Period       |1991-2020(ERA5/OISST, WMO recommendation), <br> 2004-2023(for ver.2024 of ECMWF-hindcast), 1996-2015(for ver.2016 of ECMWF-hindcast)|  
|Location          |EastAsiaClimateExtremes/DATA/1.Daily_ERA5/, 2.Weekly_ERA5/, 3.Daily_ECMWFhindcasts/|  


### ***2. Event Profile & Extremeness Metrics***
- List of Events: *AHT, HR, MHW*
- Location: EastAsiaClimateExtremes/DATA/0.ExtremeEvents_WeeklyMonthly/
  
|Event Profile  |Description|
|-------|-----------|
|**Extreme Thresholds**|p90, p95|**Extreme Days**      |           
|**Event Criteria**    |D3G5, D5G2 for *AHT/MHW* and D1G3, D3G3 for *HR*|
|**Event Meta**        |*Start/End Date, Frequency, Duration, Mean/Peak Intensity* and so forth|            
>*T2M_e = T2M - thr; TP_e = TP - thr; SST_e = SST - thr*  
>*e.g., D3G5 represents minimum three-day **D**uration, permitting **G**aps of up to five days*  

|Extremeness Metrics (Weekly/Monthly)|Description|
|--------|-----------|
|**Extreme Days**      |Number of days in the period when *T2M_e/TP_e/SST_e* exceed zero|
|**Max. Intensity**    |Peak *T2M_e/TP_e/SST_e* observed during the period|
|**Impact Factor**     |Cumulative *T2M_e/TP_e/SST_e* over the period|



### ***3. File Format & Details*** 

|        |Files in|Description|
|--------|------------|----------------|
|**Pickle**|0.ExtremeEvents_ERA5_OISST and 1.Daily_ERA5_OISST|Easy to use by **importing pickle** (e.g. import pickle)|
|**NetCDF**|2.Weekly_ERA5 and 3.Daily_ECMWFhindcasts|If you have **Python version 3.8 or higher**, you can easily read **nc files** with **xarray**|  


**3.0. ECMWF-hindcast datasets**    
**The ECMWF-hindcast NetCDF data1** was reconstructed from ECMWF Hindcast versions **2016** and **2024**.  
For each forecast initialization date, data corresponding to **lead week 3 (days 15–21 after initialization)** were extracted and reorganized into daily records.  
  
| data1 information (***e.g., nc file: v2024_ECMWF_hindcast_T2M_w3_2004-2023.nc***) |
| :---|
|Dimensions: (time: 7140, latitude: 72, longitude: 72) <br> Coordinates: <br> * time (time) datetime64[ns] 57kB 2004-01-19 2004-01-20 ... 2024-01-15 <br> * latitude (latitude) float64 576B 57.0 55.5 54.0 52.5 ... -46.5 -48.0 -49.5 <br> * longitude (longitude) float64 576B 52.5 54.0 55.5 ... 156.0 157.5 159.0 <br> Data variables: <br> t2m (time, latitude, longitude) float32 148MB|  

**The ECMWF-hindcast NetCDF data2** was generated based on **data 1**, 90th-percentile climatological thresholds nc file were computed for each ECMWF Hindcast version using the forecast issued dates.  
| data2 information (***e.g., nc file: v2024_ECMWF_hindcast_T2M_w3_clim90th.nc***) |
| :---|
|Dimensions: (latitude: 72, longitude: 72, doy: 356) <br> Coordinates: <br> * latitude (latitude) float64 576B 57.0 55.5 54.0 52.5 ... -46.5 -48.0 -49.5 <br> * longitude (longitude) float64 576B 52.5 54.0 55.5 ... 156.0 157.5 159.0 <br> quantile      float64 8B ... <br> doy (doy) int64 3kB 1 3 4 5 6 7 8 ... 360 361 362 363 364 365 366 <br> Data variables: <br> t2m_clim90th (doy, latitude, longitude) float64 15MB|  
