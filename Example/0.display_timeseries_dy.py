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


# Function to plot time series in multiple rows
def plot_time_series(date, data, chunk_size,col,lb):

    nt = len(date)
    for i in range(num_chunks):
        st = i * chunk_size
        ed = (i + 1) * chunk_size 
        if ed > nt: ed = nt

        chunk_date = date[st : ed]
        chunk_data = data[st : ed]
        axs[i].fill_between(chunk_date, chunk_data, color=col, alpha=0.4, label=lb)
        axs[i].set_ylim(0,6)  # Set y-axis range)
            
t0 = 0
with open('./mhwD5G2.oisst.1982-2024.EA1.5.pkl','rb') as file:
     data = pickle.load(file)
lat,lon  = data['lat'],data['lon']
mhws = data['event']
dates = data['dates'][t0:]
t = np.array([d.toordinal() for d in dates])
t_ = np.arange(date(2022,5,1).toordinal(),date(2022,8,31).toordinal()+1)
dates_out = [date.fromordinal(tt.astype(int)) for tt in t_]


plt.close('all')
plt.figure(figsize=(10,15))

for ip,pnt in enumerate(pnts):

    ly, lx = ll[ip]
    ly_,lx_ = str(ly)+'N',str(lx)+'E'

    iy, ix = np.argwhere(lat==ly)[0][0], np.argwhere(lon==lx)[0][0]
 
    sst = data['sst'][t0:,iy,ix]
    thresh = data['clim']['thresh'][ly_,lx_][t0:]
    seas = data['clim']['seas'][ly_,lx_][t0:]

    ev = np.argmax(mhws['intensity_max'][ly_,lx_]) # Find largest event
    tev = len(mhws['intensity_max'][ly_,lx_]) # Find largest event

    plt.subplot(3,1,ip+1)
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
    plt.plot(dates, sst, 'k-', linewidth=1)
    plt.plot(dates, thresh, 'r-', linewidth=1)
    plt.plot(dates, seas, 'g-', linewidth=1)
    plt.title(pnt+' ['+ly_+', '+lx_+']: SST(black), MHW events(shading)', fontsize=15, fontweight='bold')
    plt.xlim(dates_out[0], dates_out[-1])
    plt.ylim(np.min(seas) - 1, np.max(seas) + mhws['intensity_max'][ly_,lx_][ev] + 0.5)
    plt.ylabel(r'SST [$^\circ$C]')

fn = './timeseries_3pnts.png'
plt.savefig(fn, dpi=300, bbox_inches='tight')





