import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from matplotlib.gridspec import GridSpec


## grid points interested ##
pnts = ['Dokdo','YS','EJS']
cols = ['k','o','g']
ll = [[37.5,130.5],[34.5,124.5],[40.5,135.0]]


t0 = 0
hd = 'hr90'
crt1 = '90'
crt2 = '_D3G3'
with open(hd+'.era5.1940-2024.EA1.5.pkl','rb') as file:
     data = pickle.load(file)
lat,lon  = data['lat'],data['lon']
mhws = data['event'+crt1+crt2]
dates = data['dates'][t0:]
t = np.array([d.toordinal() for d in dates])

plt.close('all')
plt.figure(figsize=(10,12))

for ip,pnt in enumerate(pnts[:2]):

    ly, lx = ll[ip]
    ly_,lx_ = str(ly)+'N',str(lx)+'E'

    iy, ix = np.argwhere(lat==ly)[0][0], np.argwhere(lon==lx)[0][0]
 
    sst = data['tp'][t0:,iy,ix] 
    thresh = data['clim'+crt1]['thresh'][ly_,lx_][t0:]
    seas = data['clim'+crt1]['seas'][ly_,lx_][t0:]

    if hd == 'hr':
        sst *= 1000.
        thresh = np.array(thresh)*1000.
        seas = np.array(seas)*1000.
    
    ev = np.argmax(mhws['intensity_max'][ly_,lx_]) # Find largest event
    tev = len(mhws['intensity_max'][ly_,lx_]) # Find largest event

    plt.subplot(2,1,ip+1)
    # Find indices for all ten MHWs before and after event of interest and shade accordingly
    for ev0 in np.arange(ev-50, tev-1, 1):
        t1 = np.where(t==mhws['time_end'][ly_,lx_][ev0])[0][0]
        t2 = np.where(t==mhws['time_start'][ly_,lx_][ev0+1])[0][0]
        plt.fill_between(dates[t1:t2+1], sst[t1:t2+1], thresh[t1:t2+1], \
                         color=(0.68, 0.85, 0.9))
    for ev0 in np.arange(ev-50, tev, 1):
        t1 = np.where(t==mhws['time_start'][ly_,lx_][ev0])[0][0]
        t2 = np.where(t==mhws['time_end'][ly_,lx_][ev0])[0][0]
        plt.fill_between(dates[t1:t2+1], sst[t1:t2+1], thresh[t1:t2+1], \
                         color=(1,0.6,0.5))
    # Find indices for MHW of interest and shade accordingly
    t1 = np.where(t==mhws['time_start'][ly_,lx_][ev])[0][0]
    t2 = np.where(t==mhws['time_end'][ly_,lx_][ev])[0][0]
    print(ly_,lx_, dates[t1], dates[t2])

 
    plt.fill_between(dates[t1:t2+1], sst[t1:t2+1], thresh[t1:t2+1], \
                     color='r')
    # Plot SST, seasonal cycle, threshold, shade MHWs with main event in red
    plt.plot(dates, sst, 'k-', linewidth=1 )
    plt.plot(dates, thresh, 'r-', linewidth=1)
    plt.plot(dates, seas, 'g-', linewidth=1)
    plt.xlim(dates[t1-300],dates[t2+300])
    #plt.xlim(date.fromordinal(t1.astype(int)),date.fromordinal(t2.astype(int)))
    #plt.ylim(np.min(seas) - 0.1, np.max(seas) + mhws['intensity_max'][ly_,lx_][ev] + 0.05)
    if hd == 'hr': plt.ylabel(r'TP [mm/day]'); var = 'tp'
    if hd == 'mhw': plt.ylabel(r'SST [degC]'); var = 'sst'
    if hd == 'aht': plt.ylabel(r'T2m [degC]'); var = 't2m'
    #plt.ylabel(r'TP [$^\circ$C]')
    plt.title(pnt+' ['+ly_+', '+lx_+']: '+var.upper()+'(black), '+hd.upper()+' events(shading)', fontsize=15, fontweight='bold')

fn = './timeseries_3pnts.png'
plt.savefig(fn, dpi=300, bbox_inches='tight')
 




