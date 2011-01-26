import numpy as np

def get_coast_line(Bgrd):
    '''
    coast = get_coast_line(grd)

    return the coastline from the grid object grid 
    '''

    #get data
    lon = Bgrd.lon_t_vert
    lat = Bgrd.lat_t_vert
    mask = Bgrd.mask_t[0,:]

    #get land point
    jidx, iidx = np.where(mask == 0)

    coast = []

    for i in range(iidx.shape[0]):
        if jidx[i] != mask.shape[0]-1:
            if mask[jidx[i], iidx[i]] != mask[jidx[i]+1, iidx[i]]:
                lonc = ([lon[jidx[i]+1,iidx[i]], lon[jidx[i]+1,iidx[i]+1]])
                latc = ([lat[jidx[i]+1,iidx[i]], lat[jidx[i]+1,iidx[i]+1]])
                seg = zip(lonc,latc)
                coast.append(seg)

        if jidx[i] != 0:
            if mask[jidx[i], iidx[i]] != mask[jidx[i]-1, iidx[i]]:
                lonc = ([lon[jidx[i],iidx[i]], lon[jidx[i],iidx[i]+1]])
                latc = ([lat[jidx[i],iidx[i]], lat[jidx[i],iidx[i]+1]])
                seg = zip(lonc,latc)
                coast.append(seg)

        if iidx[i] != mask.shape[1]-1:
            if mask[jidx[i], iidx[i]] != mask[jidx[i], iidx[i]+1]:
                lonc = ([lon[jidx[i],iidx[i]+1], lon[jidx[i]+1,iidx[i]+1]])
                latc = ([lat[jidx[i],iidx[i]+1], lat[jidx[i]+1,iidx[i]+1]])
                seg = zip(lonc,latc)
                coast.append(seg)

        if iidx[i] != 0:
            if mask[jidx[i], iidx[i]] != mask[jidx[i], iidx[i]-1]:
                lonc = ([lon[jidx[i],iidx[i]], lon[jidx[i]+1,iidx[i]]])
                latc = ([lat[jidx[i],iidx[i]], lat[jidx[i]+1,iidx[i]]])
                seg = zip(lonc,latc)
                coast.append(seg)

    return coast
