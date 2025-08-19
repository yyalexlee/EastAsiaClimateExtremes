# EastAsiaClimateExtremes

Initiative for Developing an East Asia Climate Extremes Dataset!

This repository provides historical data on climate extremes across the East Asia(EA) region, basically archiving the events of regular grid-based climate extremes, and weekly expectations of extreme events can be utilized as labels for AI-assisted models to predict anomalous climate events in East Asia. These efforts are part of the climate extreme prediction project led by the ART/APCC team (AI-based prediction Research and Technology at the APEC Climate Center). Currently, the repository focuses on extreme phenomena such as **anomalously high temperatures(AHT), heavy rainfall(HR), and marine heatwaves(MHW)**, with the potential for further expansion. Additionally, it addresses fundamental statistics and characteristics of the atmospheric and oceanic extremes. We hope this page serves as a meaningful and practical starting point for researchers diving into studies on the dynamics and prediction of extreme phenomena. 

<img width="886" height="243" alt="image" src="https://github.com/user-attachments/assets/0a89440f-f957-4998-b83a-cc4ee6a481ce" />

**Long-term Statistics of Climate Extremes**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2D Maps of Annual Mean Event Frequency/Duration/Mean Intensity  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2D Maps of Event Frequency/Duration/Mean Intensity Change per Decade

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*For AHT,*  
<img width="2020" height="419" alt="aht90_D3G5 era5 1940-2024 EA1 5 h" src="https://github.com/user-attachments/assets/71f9f102-785d-4e1b-8c63-b4462e51268a" />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*For HR,*  
<img width="2023" height="419" alt="hr90_D1G3 era5 1940-2024 EA1 5 h" src="https://github.com/user-attachments/assets/989347a2-502f-435a-a140-24244cdc6272" />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*For MHW,*  
<img width="2020" height="419" alt="mhw90_D5G2 era5 1940-2024 EA1 5 h" src="https://github.com/user-attachments/assets/d336b984-7f65-4e81-a229-71ceb568a34b" />


## Contents

***1. Digital Data***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Climate Data**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Daily/Weekly Mean Near Surface Temperature(T2M)/Sea Surface Temperature(SST)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Daily/Weekly Sum Total Precipitation(TP)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Climatological Long-Term Mean and 90/95th percentile thresholds for ERA5, OISST(SST only) and ECMWF  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference period: 1991-2020(ERA5, WMO recommendation) / 2004-2023(ECMWF hindcast period)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Extreme Event Profile**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Start/End date, Duration, Peak Intensity and so forth  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for Extreme thresholds: 90%ile, 95%ile  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for Event Criteria: D3GG, D5G2 for *AHT/MHW* and D1G3, D3G3 for *HR*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*e.g., D3G5 represents minimum three-day **D**uration, permitting **G**aps of up to five days*  
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Period(Weekly/Monthly) Extremeness Metrics**    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extreme Days: Number of days in the period when SST/T2M/TP exceeds the threshold (e.g., 90/95th percentile)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*SST_e/T2M_e/TP_e = SST/T2M/TP - thr_90/95*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Max Intensity: Peak *SST_e/T2M_e/TP_e* observed during the period  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Impact Factor: Cumulative *SST_e/T2M_e/TP_e* over the period  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*SST_e/T2M_e/TP_e = SST/T2M/TP - thr_90/95*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---------------------|-----------|
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Extreme Days         |Number of days in the period when *SST_e/T2M_e/TP_e* exceed zero|
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Max. Intensity       |Peak *SST_e/T2M_e/TP_e* observed during the period|
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Impact Factor        |Cumulative *SST_e/T2M_e/TP_e* over the period|


***2. Codes for Data Processing and Visualization***  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*for individual grid points within EA domain,*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Historical Event Statistics**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List of Events (*AHT, HR, MHW*)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Event Statistics: Frequeny, Duration, Mean Intensity  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Daily/Weekly Timeseries and Extremeness  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Seasonality and Trend of Climate Extremes**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Seasonal Evolution of Event Frequency/Duration/Mean Intensity  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Annual Timeseries of Frequency/Duration/Mean Intensity per Year and its Least-Squared Fitted Line 


## Spatial/Temporal Coverage  
&nbsp;&nbsp;&nbsp;&nbsp;**S**: 21-48degN, 114-141degE with 1.5, 0.25deg resolution  
&nbsp;&nbsp;&nbsp;&nbsp;**T**: 1940-2024(ERA5), 1982-2024(OISST)


***Data format*** 


## Usage  
&nbsp;&nbsp;&nbsp;&nbsp;if codes given: how to read the data and to isolate/plot timeseries of specific grid point?  
&nbsp;&nbsp;&nbsp;&nbsp;how about adding a table describing example codes given?  


## Reference
  Westby, Rebecca Marie et al. “Anomalous Temperature Regimes during the Cool Season: Long-Term Trends, Low-Frequency Mode Modulation, and Representation in CMIP5 Simulations.” Journal of Climate 26 (2013): 9061-9076  
  Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238, doi: 10.1016/j.pocean.2015.12.014  
  https://github.com/ecjoliver/marineHeatWaves  



####################################################################

**Why important?** Affecting human life (health and economics)

  suggesting climate disasters happened during recent few years in terms of heat and wet condition particularly over East Asia region? adding fatality and economic loss information.  And any issues in application sectors like further data request and so forth…

**What?** Type of atmospheric and oceanic climate extremes?
  - ***Definition*** of extreme phenomena 

  1. Extreme Hot Temperature
  2. Heavy Rainfall
  3. Marine Heat Waves over East Asia Marginal Seas

  - ***Event Characteristics***
    1. Frequency: How often they occur
    2. Intensity: How severe they are
    3. Duration: How long they last
    4. Geographic location: Where they happen
    5. Seasonality: When they tend to occur

  - ***Impacts*** may not possible
    1. Human casualties and health effects
    2. Economic losses (infrastructure, agriculture, etc.)
    3. Environmental damage (ecosystems, biodiversity)
    4. Social disruption (migration, displacement)

  - ***Trends and Projections***
    1. Historical trends over decades
    2. Future projections under different climate scenarios (e.g., IPCC pathways) may not possible ???


***Strengths/Limitations***

  Example applications and good use of data

  Recommendations and considerations
    


