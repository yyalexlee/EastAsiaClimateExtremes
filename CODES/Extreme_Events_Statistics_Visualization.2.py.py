import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
from matplotlib.colors import BoundaryNorm
from collections import defaultdict
from scipy.stats import linregress


#########################################################################################################################################
## Creation Date: 12-Dec-2025                                                                                                          ##
## Please contact Yun-Young Lee (dolkong400@gmail.com), Team ART(AI-based prediction Research and Technology)/APCC(APEC Climate Center)##
#########################################################################################################################################


# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# This code performs the following tasks:
# - Calculates the long-term mean and trend of three event statistics 
#   (Frequency, Total Days, Mean Intensity) for:
#     • Anomalous High Temperature (AHT)
#     • Heavy Rainfall (HR)
#     • Marine Heatwaves (MHW)
#   across the East Asia domain.
# - Generates 2D maps displaying the long-term mean and the trend (per decade).
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------


# 0. define input/output directory and set extreme target
# ----------------------------------------------------------------------------------------------------------------
dir0 = 'YOUR WORKING DIRECTORY/'
dir_in = dir0 + 'DATA/0.ExtremeEvents_ERA5_OISST/'
dir_out1 = dir0 + 'OUTPUTS/'
dir_out2 = dir0 + 'IMAGES/'

hd = 'mhw'  # choose 'aht' or 'hr' or 'mhw'
mtr = 'event90_D5G2'
    # 'aht': mtr = 'event90_D5G2' 'event90_D3G5' 'event95_D5G2' 'event95_D3G5' 
    # 'hr':  mtr = 'event90_D1G3' 'event90_D3G3' 'event95_D1G3' 'event95_D3G3'
    # 'mhw': mtr = 'event90_D5G2' 'event90_D3G5' 'event95_D5G2' 'event95_D3G5'
rean = 'oisst' # chosse 'era5' or 'oisst', 'oisst' available only for mhw
rg = 'EA1.5'
syr,eyr = 1982, 2024
nyr = eyr - syr + 1
prd_out = str(syr)+'-'+str(eyr)
# ----------------------------------------------------------------------------------------------------------------



# 1. Define functions for displaying and basic calculation
# ----------------------------------------------------------------------------------------------------------------
# Function for 2d panel plot
def panel(irow,icol,lat,lon,x,cmap,levs,mn,mx,ttl,fs,fw,ha,opt_cbar,clb):

    proj = ccrs.PlateCarree()
    ax = fig.add_subplot(gs[irow,icol],projection=proj)
    ax.coastlines()
    # Calculate grid edges from cell centers
    intlon = (lon[1]-lon[0])
    intlat = (lat[1]-lat[0])
    lon_edges = np.linspace(lon[0], lon[-1]+intlon, len(lon)+1) - intlon/2.
    lat_edges = np.linspace(lat[0], lat[-1]+intlat, len(lat)+1) - intlat/2.

    cmap = plt.get_cmap(cmap)
    norm = BoundaryNorm(levs, ncolors=cmap.N, clip=True)

    im = ax.pcolormesh(lon_edges, lat_edges, x, vmin=mn, vmax=mx, cmap=cmap, norm=norm, shading='auto',transform=ccrs.PlateCarree(),  alpha=1, zorder=0)
    ax.set_extent([lon_edges[0], lon_edges[-1], lat_edges[0], lat_edges[-1]], crs=ccrs.PlateCarree())
    plt.title(ttl,fontsize=fs+5,fontweight='heavy')

    if opt_cbar == 1:
        ax = fig.add_subplot(gs[irow,icol+1])
        cbar = fig.colorbar(im,cax=ax,orientation='vertical')
    if opt_cbar == 2:
        ax = fig.add_subplot(gs[irow+1,icol])
        cbar = fig.colorbar(im,cax=ax,orientation='horizontal')
        cbar.set_label('['+clb+']', fontsize=fs-5, fontweight=fw, loc='right',labelpad=1)
    if opt_cbar == 3:
        plt.colorbar(im,orientation='vertical')

def compute_yearly_mean(dates, anomalies):
    yearly_data = defaultdict(list)
    for dt, val in zip(dates, anomalies):
        yearly_data[dt.year].append(val)
    return {year: sum(vals) / len(vals) for year, vals in yearly_data.items()}

def compute_yearly_sum(dates, anomalies):
    yearly_data = defaultdict(list)
    for dt, val in zip(dates, anomalies):
        yearly_data[dt.year].append(val)
    return {year: sum(vals) for year, vals in yearly_data.items()}

def compute_yearly_count(dates, anomalies):
    yearly_data = defaultdict(list)
    for dt, val in zip(dates, anomalies):
        yearly_data[dt.year].append(val)
    return {year: len(vals) for year, vals in yearly_data.items()}

def regress(yearly):
    years = np.array(list(yearly.keys()))
    values = np.array(list(yearly.values()))
    slope, intercept, r_value, p_value, std_err = linregress(years, values)
    return(slope)
# ----------------------------------------------------------------------------------------------------------------



# 2. Isolate event long-term statistics
# ----------------------------------------------------------------------------------------------------------------
prd =  '1982-2024' if rean == 'oisst' else '1940-2024'
fn = dir_in+'event.'+hd.upper()+'.'+rean+'.'+prd+'.'+rg+'.pkl'
with open(fn,'rb') as pickle_file:
    data = pickle.load(pickle_file)

lat,lon = data['lat'],data['lon']
ny,nx = len(lat),len(lon)

# Define arrays of long-term mean and trend of three extreme statistics
stt = np.full((3,ny,nx),np.nan)
stt_t = np.full((3,ny,nx),np.nan)

# Convert pts to NumPy array once before looping
pts = list(data[mtr]['n_events'].keys())
pts = np.array(pts)

for ix in range(nx):
    for iy in range(ny):

        latn, lonn = lat[iy], lon[ix]

        loc_key = (f"{latn}N", f"{lonn}E")

        # Check if location exists in pts
        if np.logical_and(pts[:, 0] == loc_key[0], pts[:, 1] == loc_key[1]).any():

            # Extract number of events and peak years
            nevents = data[mtr]['n_events'][loc_key]
            print(rg, rean, hd, lonn, latn, nevents)
            peak_dates = list(data[mtr]['date_peak'][loc_key])
            years = [date.year for date in peak_dates]

            # Filter years after start year
            years_array = np.array(years)
            valid_years = np.where((years_array - syr) >= 0, years_array, np.nan)
            idx = np.nanargmin(valid_years)

            # Aggregate metrics from idx onward
            durations = list(data[mtr]['duration'][loc_key])[idx:]
            intensities = list(data[mtr]['intensity_mean'][loc_key])[idx:]
            
            # Long-term Mean
            # frequency
            stt[0, iy, ix] = nevents - idx
            # total days(duration)
            stt[1, iy, ix] = np.sum(durations)
            # mean intensity
            stt[2, iy, ix] = np.mean(intensities)

            # Time series analysis
            dates = peak_dates[idx:]
            t1 = compute_yearly_count(dates, durations)
            t2 = compute_yearly_sum(dates, durations)
            t3 = compute_yearly_mean(dates, intensities)

            # Long-term Trend
            stt_t[0, iy, ix] = regress(t1)
            stt_t[1, iy, ix] = regress(t2)
            stt_t[2, iy, ix] = regress(t3)
    
# Normalize frequency and duration grids once after loop
stt[0] /= float(nyr)
stt[1] /= float(nyr)
# ----------------------------------------------------------------------------------------------------------------



# 3. Save long-term event statistics in pickle
# ----------------------------------------------------------------------------------------------------------------
ofn = dir_out1+hd.upper()+'.stats__'+rean.upper()+'.p'+mtr[5:]+'.'+prd_out+'.'+rg+'.npz'

np.savez(ofn,
         stt=stt, stt_t=stt_t,
         pts=pts,lat=lat,lon=lon)
# ----------------------------------------------------------------------------------------------------------------



# 4. Load long-term event statistics data
# ----------------------------------------------------------------------------------------------------------------
dd = np.load(ofn)
frq,dur,mint = dd['stt'][0],dd['stt'][1],dd['stt'][2]
frq_t,dur_t,mint_t = dd['stt_t'][0]*10,dd['stt_t'][1]*10,dd['stt_t'][2]*10 # trend per decade
lat,lon = dd['lat'],dd['lon']
# ----------------------------------------------------------------------------------------------------------------




# 5. Display 2D map of climate extreme long-term statistics
# ----------------------------------------------------------------------------------------------------------------
plt.close('all')
fig = plt.figure(figsize=(10,8))
gs = gridspec.GridSpec(6,4,
                   wspace=0.05, hspace=0.0,
                   height_ratios=[0.3,1,0.05,0.2,1,0.05],
                   width_ratios=[0.17,1,1,1])

proj = ccrs.PlateCarree()
plt.rcParams['font.family'] = 'Padauk'
plt.rcParams['axes.unicode_minus'] = False
plt.axis('off')

fs,fw = 20,'regular'
plt.rcParams['font.family'] = 'Padauk'
cb = 2

ax = fig.add_subplot(gs[0,2])
plt.text(0.5,0.8,hd.upper()+': '+mtr,rotation=0,fontsize=fs+10,fontweight='heavy',ha='center')
plt.axis('off')
ax = fig.add_subplot(gs[1,0])
plt.text(0.6,0.5,'Long-Term Mean',fontsize=fs+5,rotation=90, fontweight='heavy',ha='center',va='center')
plt.axis('off')
ax = fig.add_subplot(gs[4,0])
plt.text(0.6,0.5,'Long-Term Trend',fontsize=fs+5,rotation=90, fontweight='heavy',ha='center',va='center')
plt.axis('off')

if hd == 'hr': unit = 'mm/day'; mint *= 1000; mint_t *= 1000
else:          unit = 'degC'

if hd == 'aht': ihd = 0; cmap1 = 'afmhot_r'; cmap2 = 'RdBu_r'
if hd == 'hr' : ihd = 1; cmap1 = 'YlGnBu'  ; cmap2 = 'BrBG' 
if hd == 'mhw': ihd = 2; cmap1 = 'hot_r'   ; cmap2 = 'bwr'

# Define plotting configurations
plot_configs = [
    # Mean static metrics
    {
        'row': 1, 'col': 1, 'data': frq, 'title': 'Frequency', 'unit': 'times/yr',
        'cmap': cmap1, 'ranges': {0: (4.8, 2.4), 1: (28., 14.), 2: (2.8, 1.4)}, 'nlevs': 21
    },
    {
        'row': 1, 'col': 2, 'data': dur, 'title': 'Total Days', 'unit': 'days/yr',
        'cmap': cmap1, 'ranges': {0: (30, 10), 1: (55., 45.), 2: (40., 20.)}, 'nlevs': 21
    },
    {
        'row': 1, 'col': 3, 'data': mint, 'title': 'Mean Intencity', 'unit': unit,
        'cmap': cmap1, 'ranges': {0: (8, 0), 1: (35, 5.), 2: (2.4, 1.2)}, 'nlevs': 21
    },
    # Trend metrics
    {
        'row': 4, 'col': 1, 'data': frq_t, 'title': '', 'unit': 'times/yr/decade',
        'cmap': cmap2, 'ranges': {0: (2, -2.), 1: (1., -1), 2: (1.5, -1.5)}, 'nlevs': 21
    },
    {
        'row': 4, 'col': 2, 'data': dur_t, 'title': '', 'unit': 'days/yr/decade',
        'cmap': cmap2, 'ranges': {0: (2, -2.), 1: (1., -1), 2: (30, -30)}, 'nlevs': 21
    },
    {
        'row': 4, 'col': 3, 'data': mint_t, 'title': '', 'unit': unit+'/decade',
        'cmap': cmap2, 'ranges': {0: (.4, -.4), 1: (1, -1), 2: (.15, -.15)}, 'nlevs': 21
    }
]

# Loop through each config and plot
for config in plot_configs:
    mx, mn = config['ranges'][ihd]
    levs = np.linspace(mn, mx, config['nlevs'])
    panel(
        config['row'], config['col'], lat, lon, config['data'],
        config['cmap'], levs, mn, mx, config['title'],
        fs, fw, 'center', cb, config['unit']
    )
# ----------------------------------------------------------------------------------------------------------------



# 6. Save to exterenal figure file
# ----------------------------------------------------------------------------------------------------------------
fig.tight_layout(pad=0.0)
ofn2 = dir_out2+hd.upper()+'.stats.maps__'+rean.upper()+'.p'+mtr[5:]+'.'+prd_out+'.'+rg+'.png'
fig.savefig(ofn2,bbox_inches='tight')
# ----------------------------------------------------------------------------------------------------------------

