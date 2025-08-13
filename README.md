# EastAsiaClimateExtremes

Initiative for Developing an East Asia Climate Extremes Dataset!

This repository provides historical data on climate extremes across the East Asia(EA) region, basically archiving the events of regular grid based climate extremes and weekly expectation of extreme events can be utilized as label dataset for developing AI-assisted models to predict anomalous temperature and rainfall events in East Asia. These efforts are part of the climate extreme prediction project led by the ART/APCC team (AI-based prediction Research and Technology at the APEC Climate Center). Currently, the repository focuses on extreme phenomena such as **anomalously high temperatures(AHT), heavy rainfall(HR), and marine heatwaves(MHW)**, with the potential for further expansion. Additionally, it addresses fundamental statistics and characteristics of atmospheric and oceanic extremes. We hope this page will serve as a meaningful and practical starting point for researchers diving into studies on the dynamics and prediction of extreme phenomena. 

<img width="886" height="243" alt="image" src="https://github.com/user-attachments/assets/0a89440f-f957-4998-b83a-cc4ee6a481ce" />



***Contents***

1. digial data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Event Profile**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start/end date, duration, peak intensity and so forth  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extreme thresholds: 90%tile, 95%tile  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event criteria: D5G2 (Minimum five-day Duration, permitting Gaps of up to two days), D3G5 for AHT/MHW  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D1G3, D3G3 for HR

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Period Extremeness Metrics:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SST_e/T2M_e/TP_e = SST/T2M/TP - thr_90/95  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extreme Days: Number of days in the period when SST, T2M, or TP exceeds the threshold (e.g., 90th or 95th percentile)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Max Intensity: Peak SST_e/T2M_e/TP_e observed during the period  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Impact Factor: Cumulative SST_e/T2M_e/TP_e over the period,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;representing an integrated measure that captures both the frequency and intensity of extreme events  

2. Codes for data processing and visualization 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Historical event statistics**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Frequeny per year, Total Days per year, Mean Intensity for AHT events (AHT_90)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Frequeny per year, Total Days per year, Mean Intensity for HR events (HR_90)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Frequeny per year, Total Days per year, Mean Intensity for MHW events (MHW_90)  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Seasonality and Long-term trend of climate extremes**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Seasonal evolution of Event Frequency/Duration/Mean Intensity  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes of Frequency per year, Duration per year, Mean Intensity per decade   


***Spatial coverage/temporal range***  
&nbsp;&nbsp;&nbsp;&nbsp;EA region: 21-48degN, 114-141degE (Resolution: 1.5, 0.25deg)  
&nbsp;&nbsp;&nbsp;&nbsp;Period: 1940-2024(ERA5), 1982-2024(OISST)


***Data format*** 



***Usage***  
&nbsp;&nbsp;&nbsp;&nbsp;if codes given: how to read the data and to isolate/plot timeseries of specific grid point?  
&nbsp;&nbsp;&nbsp;&nbsp;how about adding a table describing example codes given?  


**Reference**  
  https://github.com/ecjoliver/marineHeatWaves  
  Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238, doi: 10.1016/j.pocean.2015.12.014  
  Westby, Rebecca Marie et al. “Anomalous Temperature Regimes during the Cool Season: Long-Term Trends, Low-Frequency Mode Modulation, and Representation in CMIP5 Simulations.” Journal of Climate 26 (2013): 9061-9076  



####################################################################

**Why important?** Affecting human life (health and economics)

  suggesting climate disasters happened during recent few years in terms of heat and wet condition particularly over East Asia region? adding fatality and economic loss information.  And any issues in application sectors like further data request and so forth…

**What?** Type of atmospheric and oceanic climate extremes?
  - ***Definition*** of extreme phenomena 

  1. Extreme Hot Temperature?
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
    


