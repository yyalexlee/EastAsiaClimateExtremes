# EastAsiaClimateExtremes

Initiative for Developing an East Asia Climate Extremes Dataset!

This repository provides historical data on climate extremes across the East Asia(EA) region, basically archiving **the events of regular grid-based climate extremes**, and **weekly/monthly extremeness metrics** can be utilized as labels for AI-based(or -assisted) models to predict anomalous climate events in East Asia. These efforts are part of the climate extreme prediction project led by the ART/APCC team (AI-based prediction Research and Technology at the APEC Climate Center). Currently, the repository focuses on extreme phenomena such as ***anomalously high temperatures(AHT)***, ***heavy rainfall(HR)***, and ***marine heatwaves(MHW)***, with the potential for further expansion. Additionally, it offers codes for analyzing and visualizing key statistics and characteristics of atmospheric and oceanic extremes. We hope this serves as a meaningful and practical starting point for researchers diving into studies on the dynamics and prediction of extreme phenomena. 

<img width="7750" height="3712" alt="inventory_intro" src="https://github.com/user-attachments/assets/75ad89f4-cc86-4b4c-a7d2-de80ec9ced01" />


## Data Download

  ```
  wget --content-disposition "https://www.dropbox.com/scl/fo/d3x654sonyblxni7ha3gm/ABzxk80RwyxIx6Hi_4A400g?rlkey=arvb3pmacdtrvkav367ld92kx&st=ryf7m45o&dl=0"
  ```
  
## Data Description

***0. Spatial/Temporal Coverage***  

|         |Domain    |Resolution|
|---------|----------|----------|
|**Space**|21-48N, 114-141E|1.5deg|
|**Time** |1940-2024(ERA5), 1982-2024(OISST), ECMWF-hindcast version 2016 & 2024|Daily / Weekly|  

  
***1. Climate Data***  

|        |Description|
|--------|-----------|
|Frequency         |Daily/Weekly|
|Variables         |2-m Air Temperature(T2M), Sea Surface Temperature(SST), Total Precipitation(TP)|
|Type              |Original Timeseries, Climatological Long-Term Mean, 90/95th Percentile Thresholds(p90/p95)|
|Resources         |ERA5, OISST(only for SST) and ECMWF-hindcast|
|Ref. Period       |1991-2020(ERA5/OISST, WMO recommendation), <br> 2004-2023(for ver.2024 of ECMWF-hindcast), 1996-2015(for ver.2016 of ECMWF-hindcast)|  
|Location          |EastAsiaClimateExtremes/DATA/1.Daily_ERA5/, 2.Weekly_ERA5/, 3.Daily_ECMWFhindcasts/|


***2. Event Profile & Extremeness Metrics***
- List of Events: *AHT, HR, MHW*
- Location: EastAsiaClimateExtremes/DATA/0.ExtremeEvents_WeeklyMonthly/
  
|Event Profile  |Description|Extremeness Metrics (Weekly/Monthly)|Description|
|-------|-----------|--------|-----------|
|**Extreme Thresholds**|p90, p95|**Extreme Days**      |Number of days in the period when *T2M_e/TP_e/SST_e* exceed zero|            
|**Event Criteria**    |D3G5, D5G2 for *AHT/MHW* and D1G3, D3G3 for *HR*|**Max. Intensity**    |Peak *T2M_e/TP_e/SST_e* observed during the period|
|**Event Meta**        |*Start/End Date, Frequency, Duration, Mean/Peak Intensity* and so forth|**Impact Factor**     |Cumulative *T2M_e/TP_e/SST_e* over the period|            
>*T2M_e = T2M - thr; TP_e = TP - thr; SST_e = SST - thr*  
>*e.g., D3G5 represents minimum three-day **D**uration, permitting **G**aps of up to five days*  


## Usage  

### Codes for Data Processing and Visualization
| Code File | Description | Location |
| --- | --- | --- |
| `TART_visualization1.ipynb` | Code for timeseries and heatmap visualization and saving statistics | EastAsiaClimateExtremes/CODES/
| `TART_visualization2.ipynb` | Code for 2-D map visualization for climatological extreme event statistics and saving statistics | EastAsiaClimateExtremes/CODES/


## Ouput Details
| Outputs  |Visualization | Data Format|
|----------|--------|--------|
|Daily extreme events, Yearly event counts|Timeseries| NetCDF|
|Frequency, Mean Intensity, Max Intensity|2D maps   | NetCDF|
|Monthly Event Counts+Trend(+/-)|Heatmaps  | NetCDF|


## Reference
  Westby, Rebecca Marie et al. “Anomalous Temperature Regimes during the Cool Season: Long-Term Trends, Low-Frequency Mode Modulation, and Representation in CMIP5 Simulations.” Journal of Climate 26 (2013): 9061-9076  
  Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238, doi: 10.1016/j.pocean.2015.12.014  
  https://github.com/ecjoliver/marineHeatWaves  



## Citation
  Lee, Y., M. Kim, U. Chung (2025). EastAsiaClimateExtremes. GitHub. https://github.com/yyalexlee/EastAsiaClimateExtremes

## Acknowledgments
  This research is supported by APEC Climate Center. 
