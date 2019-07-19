import epics
import time
import numpy as np

data = []

def cb(pvname, timestamp, *args, **kwargs):
    data.append(timestamp)

if __name__ == '__main__':
    pvname = 'LS1_CB04:CHA_RD'
    epics.camonitor(pvname, callback=cb)
    time.sleep(5)
    print(np.mean(1.0/np.diff(data)))

