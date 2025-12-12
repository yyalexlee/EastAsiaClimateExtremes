### 🧮 Codes for Data Processing and Visualization
| Code File | Description | Location |
| ------ | ----- | ----- |
| `0.display_EAextremes_event_statistics.py`| Code for calculating and displaying long-term mean and trend of event statistics | EastAsiaClimateExtremes/CODES/ |
| `TART_visualization1_output.ipynb` | Code for timeseries and heatmap visualization | EastAsiaClimateExtremes/CODES/|
| `TART_visualization2_output.ipynb` | Code for 2-D map visualization of long-term statistics of weekly climate extremes | EastAsiaClimateExtremes/CODES/|
  
&nbsp;  
  
### 📊 Output Details 
***0. Historical Extreme Statistics***  
- Daily/Weekly Timeseries and Extremeness
- List of Events: *AHT, HR, MHW*  
- Event Statistics: Frequeny, Duration, Mean Intensity 
- Weekly Extreme Statistics: Frequeny, Mean/Max Intensity per year  
 
***1. Seasonality and Trend of Climate Extremes***  
- Seasonal Evolution of Event Frequency/Duration/Mean Intensity  
- Annual Timeseries of Frequency/Duration/Mean Intensity per Year and its Least-Squared Fitted Line

***2. Example images after runing codes***   

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.0. Line plot of daily timeseries: climatology, extreme threshold, events**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***(from `TART_visualization1_output.ipynb`)***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ *T2m timeseries & Anomalous High Temerature event (D5G2, 90%tile)*  

<img width="800" alt="2dmaps" src="../IMAGES/aht90_timeseries.png" />  


&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.1. Heatmap of Monthly Extreme Event Statistics: frequency and trend**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***(from `TART_visualization1_output.ipynb`)***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ *Monthly count of heavy rainfall events(D1G3, 90%tile) with trend (+/-)*  

<img width="800" alt="hr90_D1G3sum_heatmap" src="https://github.com/user-attachments/assets/bbe22dff-5327-4627-b3a3-fb8d94ffbffa" /> 


&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.2. 2D Maps of Extreme "Event" Statistics: long-term mean/trend of frq./duration/mean intensity**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***(from `0.display_EAextremes_event_statistics.py`)***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ *Marin Heatwave event (D5G2, 90%tile) statistics (1982-2024)*  

<img width="800" alt="stats mhw event90_D5G2 1982-2024 EA1 5" src="https://github.com/user-attachments/assets/ed1b7fc3-bf63-4927-be77-b6388c13f758" />

  
&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.3. 2D Maps of "Weekly" Extremes Statistics**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***(from `TART_visualization2_output.ipynb`)***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ *Counts of extreme weeks and their mean/max intensity per year based on weekly accumulated precipitation (1940-2024)*  

<img width="800" alt="2dmaps" src="../IMAGES/HR_extreme_statistics_maps.png" />  






  




