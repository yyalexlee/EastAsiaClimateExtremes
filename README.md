# EastAsiaClimateExtremes

Initiative for Developing an East Asia Climate Extremes Dataset!

This repository provides historical data on climate extremes across the East Asia(EA) region, basically archiving **the events of regular grid-based climate extremes**, and **weekly/monthly extremeness metrics** can be utilized as labels for AI-based(or -assisted) models to predict anomalous climate events in East Asia. These efforts are part of the climate extreme prediction project led by the ART/APCC team (AI-based prediction Research and Technology at the APEC Climate Center). Currently, the repository focuses on extreme phenomena such as ***anomalously high temperatures(AHT)***, ***heavy rainfall(HR)***, and ***marine heatwaves(MHW)***, with the potential for further expansion. Additionally, it offers codes for analyzing and visualizing key statistics and characteristics of atmospheric and oceanic extremes. We hope this serves as a meaningful and practical starting point for researchers diving into studies on the dynamics and prediction of extreme phenomena.  


<img width="860" alt="githubmain" src="https://github.com/user-attachments/assets/87b64045-471f-4d1c-8069-19d878d16ddb" />


## Data Download

&nbsp;&nbsp;&nbsp;&nbsp;**0. Extreme Event Profile and Weekly/Monthly Extremeness Metrics (ERA5/OISST)**
  ```
  wget -O 0.ExtremeEvents_ERA5_OISST.zip "https://www.dropbox.com/scl/fo/5hcy3r8jxd6o9qaa267bf/AMI0pTgTvZWf1MXq7SgAZwk?rlkey=z3x1kyrynjeg0wctprfk31aj1&st=ryo0cv1h&dl=0"  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;**1. Daily Data and Extreme Threshold (ERA5/OISST)**
  ```
  wget -O 1.Daily_ERA5_OISST.zip "https://www.dropbox.com/scl/fo/t8082lha97fi5ebqsq77x/ACZu-o6b-b4e05S81-7BkQs?rlkey=d5v7ztkp71nb4d7jx19pgv97u&st=9h8y9v6x&dl=0"  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;**2. Weekly Data and Extreme Threshold (ERA5)**
  ```
  wget -O 2.Weekly_ERA5.zip "https://www.dropbox.com/scl/fo/w12fdxsv89tfhphrrot1l/AD7IuKrO3LrVvkCN1hEA2c0?rlkey=67vr21cu88jt9q625lzboocao&st=yo63qu2p&dl=0"
  ```
&nbsp;&nbsp;&nbsp;&nbsp;**3. Daily Data and Extreme Threshold (ECMWF-hindcast ver.2016/ver.2024)**
  ```
  wget -O 3.Daily_ECMWFhindcasts.zip "https://www.dropbox.com/scl/fo/sv3lu1e3qzwwtt6dqnzkq/AEI6Vn0BLPvGmnynbGZ6_Gk?rlkey=8bdbyjjjg472mimxx1lpk9v3b&st=npjwog3p&dl=0"  
  ```
  
## Data Description

***0. Spatial/Temporal Coverage***  

|         |Domain    |Resolution|
|---------|----------|----------|
|**Space**|21°-48°N, 114°-141°E|1.5deg|
|**Time** |1940-2024(ERA5), 1982-2024(OISST), ECMWF-hindcast version 2016 & 2024|Daily / Weekly|  

  
***1. Original Climate Data***  

|        |Description|
|--------|-----------|
|Frequency         |Daily/Weekly|
|Variables         |2m Air Temperature(T2M), Sea Surface Temperature(SST), Total Precipitation(TP)|
|Type              |Original Timeseries, Climatological Long-Term Mean, 90/95th Percentile Thresholds(p90/p95)|
|Resources         |ERA5, OISST(only for SST) and ECMWF-hindcast|
|Ref. Period       |1991-2020(ERA5/OISST, WMO recommendation), <br> 2004-2023(for ver.2024 of ECMWF-hindcast), 1996-2015(for ver.2016 of ECMWF-hindcast)|  
|Location          |[EastAsiaClimateExtremes/DATA/1.Daily_ERA5_OISST/](./DATA/1.Daily_ERA5_OISST/), [2.Weekly_ERA5/](./DATA/2.Weekly_ERA5/), [3.Daily_ECMWFhindcasts/](./DATA/3.Daily_ECMWFhindcasts/)|


***2. Event Profile & Extremeness Metrics***
- List of Events: *AHT, HR, MHW*
- Location: [EastAsiaClimateExtremes/DATA/0.ExtremeEvents_ERA5_OISST/](./DATA/0.ExtremeEvents_ERA5_OISST/)
  
|Event Profile  |Description|Extremeness Metrics (Weekly/Monthly)|Description|
|-------|-----------|--------|-----------|
|**Extreme Thresholds**|p90, p95|**Extreme Days**      |Number of days in the period when *T2M_e/TP_e/SST_e* exceed zero|            
|**Event Criteria**    |D3G5, D5G2 for *AHT/MHW* and D1G3, D3G3 for *HR*|**Max. Intensity**    |Peak *T2M_e/TP_e/SST_e* observed during the period|
|**Event Meta**        |*Start/End Date, Frequency, Duration, Mean/Peak Intensity* and so forth|**Impact Factor**     |Cumulative *T2M_e/TP_e/SST_e* over the period|            
>*T2M_e = T2M - thr; TP_e = TP - thr; SST_e = SST - thr*  
>*e.g., D3G5 represents minimum three-day **D**uration, permitting **G**aps of up to five days*  


## Usage  

**Codes for Data Processing and Visualization**
- Location: [ EastAsiaClimateExtremes/CODES/](./CODES/)

| Code File | Description |
| ------ | ----- | 
| [`0.display_EAextremes_event_statistics.py`](./CODES/0.display_EAextremes_event_statistics.py)| Code for calculating and displaying long-term mean and trend of event statistics |
| [`TART_visualization1_output.ipynb`](./CODES/TART_visualization1_output.ipynb) | Code for timeseries and heatmap visualization |
| [`TART_visualization2_output.ipynb`](./CODES/TART_visualization2_output.ipynb) | Code for 2-D map visualization of long-term statistics of weekly climate extremes |

## Ouput Details
| Outputs  |Visualization | Data Format|
|----------|--------|--------|
|Daily based extreme events, Yearly event counts|Timeseries| NetCDF|
|Monthly Event Counts+Trend(+/-)|Heatmaps  | NetCDF|
|Long-term Mean/Trend of Event Statistics|2D maps   | Numpy|
|Count of Extreme Weeks, Mean/Max Intensity|2D maps   | NetCDF|



## Reference
  Westby, Rebecca Marie et al. “Anomalous Temperature Regimes during the Cool Season: Long-Term Trends, Low-Frequency Mode Modulation, and Representation in CMIP5 Simulations.” Journal of Climate 26 (2013): 9061-9076  
  Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238, doi: 10.1016/j.pocean.2015.12.014  
  https://github.com/ecjoliver/marineHeatWaves  



## Citation
  Lee, Y., M. Kim, U. Chung (2025). EastAsiaClimateExtremes. GitHub. https://github.com/yyalexlee/EastAsiaClimateExtremes

## Acknowledgments
  This research is supported by APEC Climate Center. 
