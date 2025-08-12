import sys
import numpy as np
import xarray as xr
from datetime import date
from matplotlib import pyplot as plt
import pickle
from scipy.ndimage import convolve1d
import joblib

sys.path.append('/home/yyalee/ART_2025/Module')
import marineHeatWaves as mhw

with open('../Module/param.py','r') as file:
    code = file.read()
exec(code)


############################################################
wd = 7
############################################################

for rg in ['EA1.5']: # only for OISST
#for rg in ['EA1.5','EA0.25','EA']:
    if rg == 'EA':
        sy,ey = 110, 144 # 20.5 - 54.5N
        sx,ex = 110, 149 # 110.5 - 149.5E
    if rg == 'EA1.5':
        sy,ey = 74, 92 # 21 - 49N
        sx,ex = 76, 94 # 114 - 141E
    if rg == 'EA0.25':
        sy,ey = 0, 112 # EA, hres: 24 - 52N
        sx,ex = 0, 108 # EA, hres: 115.5 - 142.5E

    for var in ['sst','t2m','tp']:

        if var == 'sst': hd = 'mhw'; mD,mG = 5,2
        if var == 't2m': hd = 'aht'; mD,mG = 3,5
        if var == 'tp':  hd = 'hr'; mD,mG = 1,3
 
        hd = hd+'D'+str(mD)+'G'+str(mG) 

        if var == 'sst': reans = ['oisst','era5'] 
        else:            reans = ['era5'] 
    
        for rean in reans:
               
        
            if rean == 'oisst':
     
                syr,eyr = 1982,2024
        
                if rg == 'EA0.25':
                    path1 = '../Data/oisst/sst.day.mean.1981-2025.1440by721.ea.nc'
                elif rg == 'EA1.5':
                    path1 = '../Data/oisst/sst.day.mean.1981-2025.1.5by1.5.nc'
                else:
                    path1 = '../Data/oisst/sst.day.mean.1981-2025.1by1.nc'
        
                with xr.open_dataset(path1) as tmp:
                    lat,lon = tmp['lat'].values, tmp['lon'].values
                    tmp = tmp.sel(time=slice(f"1982-01-01",f"2024-12-31"))
                    ref = np.array(tmp['sst'])
        
            else:
         
                syr,eyr = 1940,2024
        
                if rg == 'EA0.25':
                    path2 = '../Data/era5/Daily/Processed/sst.day.mean.1940-2024.1440by721.ea.nc'
                elif rg == 'EA1.5':
                    path2 = '../Data/era5/Daily/Processed/sst.day.mean.1940-2024.1.5by1.5.nc'
                else:
                    path2 = '../Data/era5/Daily/Processed/sst.day.mean.1940-2024.1by1.nc'
        
                with xr.open_dataset(path2) as tmp:
                    tmp = tmp.sel(valid_time=slice(f"1940-01-01",f"2024-12-31"))
    
                ref = np.array(tmp['sst']) - 273.15
    
                if rg == 'EA0.25': lat,lon = tmp['latitude'].values, tmp['longitude'].values
                else:              lat,lon = tmp['lat'].values, tmp['lon'].values
    
            t = np.arange(date(syr,1,1).toordinal(),date(eyr,12,31).toordinal()+1)
    
            dates = [date.fromordinal(tt.astype(int)) for tt in t]
            pd_date = pd.to_datetime(dates)
    
            if lat[1]-lat[0] < 0: 
                lat = lat[::-1]
                ref = ref[:,::-1]
    
            ref = ref[:,sy:(ey+1),sx:(ex+1)]
    
            mhws_,clim_ = mhw.detect(t,ref[:,0,0],climatologyPeriod=[1991,2020])
            mhws = mhws_.copy()
            clim = clim_.copy()
        
           #ref_mhws = np.full(ref.shape,np.nan)               
           #ref_e = np.full(ref.shape,np.nan)               
            ImF = np.full(ref.shape,np.nan)               
            EDays = np.full(ref.shape,np.nan)               
            IntMx = np.full(ref.shape,np.nan)               
        
            icount = 0
            for ix in range(sx, ex+1):
                for iy in range(sy, ey+1): 
            
                    sst = ref[:,iy-sy,ix-sx]
            
                    if ~np.isnan(sst).any():
    
                        icount += 1
                        lonn,latn = lon[ix],lat[iy]
                        mhws_,clim_ = mhw.detect(t,sst,climatologyPeriod=[1991,2020],
                                                 minDuration=mD,
                                                 maxGap=mG
                                                 )
    
                        ext =  sst - clim_['thresh']
                        #ref_e[:,iy-sy,ix-sx] =  ext
                        #ref_e[:,iy-sy,ix-sx] =  np.where(ext>0, ext, np.nan)
                        d0,d1,d2 = transform_data(ext)
                        iix,iiy = ix-sx, iy-sy
                        ImF[:,iix,iiy],EDays[:,iix,iiy],IntMx[:,iix,iiy] = integrate_mhws_center(pd_date,d0,d1,d2,wd)
    
                       
                        print(rg,rean,lonn,latn,icount)
            
                        for key in mhws.keys():
            
                            if icount==1: mhws[key] = {}
            
                            siz = 1 if type(mhws_[key])==int else len(mhws_[key])
                            mhws[key][(str(latn)+'N',str(lonn)+'E')] = [0]*siz
            
                            if siz == 1: 
                                mhws[key][(str(latn)+'N',str(lonn)+'E')] = mhws_[key]
                            else: 
                                mhws[key][(str(latn)+'N',str(lonn)+'E')] = [i for i in mhws_[key]]
            
                        for key in clim.keys():
            
                            if icount==1: clim[key] = {}
            
                            siz = len(clim_[key])
                            clim[key][(str(latn)+'N',str(lonn)+'E')] = [0]*siz
                            clim[key][(str(latn)+'N',str(lonn)+'E')] = [i for i in clim_[key]]
        
        
                       #for ii in range(mhws_['n_events']):
                       #    id1,id2 = mhws_['index_start'][ii],mhws_['index_end'][ii]
                       #    ref_mhws[id1:id2+1,iy-sy,ix-sx] =  sst[id1:id2+1] - clim_['thresh'][id1:id2+1] 
    
    
            combined = {
                        'event':mhws, 'clim':clim, 'dates':dates, 
                        var:ref, 
                       #'sst_e':ref_e, 'sst_mhws':ref_mhws, 
                        'ImF_7dy':ImF,'EDays_7dy':EDays,'IntMx_7dy':IntMx, 
                        'lat':lat[sy:ey+1], 'lon': lon[sx:ex+1],
                       }
    
            with open('./'+hd+'.'+rean+'.'+str(syr)+'-'+str(eyr)+'.'+rg+'.pkl','wb') as pickle_file:
                pickle.dump(combined, pickle_file, protocol=5)
    

