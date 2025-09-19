# EastAsiaClimateExtremes

Initiative for Developing an East Asia Climate Extremes Dataset!

This repository provides historical data on climate extremes across the East Asia(EA) region, basically archiving **the events of regular grid-based climate extremes**, and **weekly/monthly extremeness metrics** can be utilized as labels for AI-assisted models to predict anomalous climate events in East Asia. These efforts are part of the climate extreme prediction project led by the ART/APCC team (AI-based prediction Research and Technology at the APEC Climate Center). Currently, the repository focuses on extreme phenomena such as ***anomalously high temperatures(AHT)***, ***heavy rainfall(HR)***, and ***marine heatwaves(MHW)***, with the potential for further expansion. Additionally, it offers code for analyzing and visualizing key statistics and characteristics of atmospheric and oceanic extremes. We hope this page serves as a meaningful and practical starting point for researchers diving into studies on the dynamics and prediction of extreme phenomena. 

<img width="4400" height="847" alt="extremes" src="https://github.com/user-attachments/assets/192b100a-c327-41ab-90dc-f2adc006a53a" />

**Long-term Statistics of Climate Extremes**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2D Maps of Annual Mean Event Frequency/Duration/Mean Intensity  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2D Maps of Event Frequency/Duration/Mean Intensity Change per Decade

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*For **1982-2024** (ERA5 for AHT/HR, OISST for MHW),*  
<img width="2029" height="1239" alt="ext90 oisst 1982-2024 EA1 5 h_all" src="https://github.com/user-attachments/assets/ee67788e-2f4b-4991-9ccb-26ba517f658f" />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*For **1940-2024** (all ERA5 based),*  
<img width="2029" height="1239" alt="ext90 era5 1940-2024 EA1 5 h_all" src="https://github.com/user-attachments/assets/29d0da57-7a4f-4b91-8430-ce76c9886749" />  


## Data Download

  ```
  wget --content-disposition "https://www.dropbox.com/scl/fi/pqm64be2s46y8zpq0zn1e/EA1.5_P9095.zip?rlkey=rh8vnut3gzecn4472xycdr0da&st=63cbrbsl&dl=0"
  ```

***Spatial/Temporal Coverage***  

|         |Domain    |Resolution|
|---------|----------|----------|
|**Space**|21-48N, 114-141E|1.5deg|
|**Time** |1940-2024(ERA5), 1982-2024(OISST)|Daily / Weekly|
  
***Data format***   



## Contents  


***1. Climate Data*** 

|        |Description|
|--------|-----------|
|Frequency         |Daily/Weekly|
|Variables         |Mean Near Surface Temperature(T2M), Sea Surface Temperature(SST), Total Precipitation(TP)|
|Type              |Original Timeseries, Climatological Long-Term Mean, 90/95th Percentile Thresholds(p90/p95)|
|Resources         |ERA5, OISST(only for SST) and ECMWF-hindcast|
|Ref. Period       |1991-2020(ERA5/OISST, WMO recommendation), 2004-2023(ECMWF-hindcast)|



***2. Extreme Event Profile***

|        |Description|
|--------|-----------|
|Meta              |***Start/End Date, Duration, Mean/Peak Intensity*** and so forth|            
|Extreme Thresholds|p90, p95|            
|Event Criteria    |D3GG, D5G2 for *AHT/MHW* and D1G3, D3G3 for *HR*|

>*e.g., D3G5 represents minimum three-day **D**uration, permitting **G**aps of up to five days*  


***3. Period(Weekly/Monthly) Extremeness Metrics***  


|Metric         |Description|
|---------------|-----------|
|Extreme Days      |Number of days in the period when *T2M_e/TP_e/SST_e* exceed zero|
|Max. Intensity    |Peak *T2M_e/TP_e/SST_e* observed during the period|
|Impact Factor     |Cumulative *T2M_e/TP_e/SST_e* over the period|

>*T2M_e = T2M - thr; TP_e = TP - thr; SST_e = SST - thr*  


## Usage  

### Codes for Data Processing and Visualization
&nbsp;&nbsp;&nbsp;&nbsp;if codes given: how to read the data and to isolate/plot timeseries of specific grid point?  
&nbsp;&nbsp;&nbsp;&nbsp;how about adding a table describing example codes given?  

### Ouput Details
&nbsp;&nbsp;&nbsp;&nbsp;if codes given: how to read the data and to isolate/plot timeseries of specific grid point?  
 
*for individual grid points within EA domain,*  
  
***1. Historical Event Statistics***  
- List of Events: *AHT, HR, MHW*  
- Event Statistics: Frequeny, Duration, Mean Intensity  
- Daily/Weekly Timeseries and Extremeness  

***2. Seasonality and Trend of Climate Extremes***  
- Seasonal Evolution of Event Frequency/Duration/Mean Intensity  
- Annual Timeseries of Frequency/Duration/Mean Intensity per Year and its Least-Squared Fitted Line  

 




## Reference
  Westby, Rebecca Marie et al. “Anomalous Temperature Regimes during the Cool Season: Long-Term Trends, Low-Frequency Mode Modulation, and Representation in CMIP5 Simulations.” Journal of Climate 26 (2013): 9061-9076  
  Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238, doi: 10.1016/j.pocean.2015.12.014  
  https://github.com/ecjoliver/marineHeatWaves  

  
