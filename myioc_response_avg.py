import epics
import time
import datetime
sleep_sec = input("Collect data for how many seconds: ")
fh = open('myioc.log','w')
epics.camonitor('LS1_CB04:CHA_RD',writer=fh.write)
time.sleep(int(sleep_sec))
epics.camonitor_clear('LS1_CB04:CHA_RD')
fh.close()
fh = open('myioc.log','r')

for i in fh.readlines():
    big_list = i.split(" ")
itr = 0
datetime_list = []
while itr < len(big_list):
    if big_list[itr][:4] == "2019":
        d = big_list[itr]
        t = big_list[itr+1]
        date_time_object = datetime.datetime(int(d[:4]),int(d[5:7]),int(d[8:10]),int(t[:2]),int(t[3:5]),int(t[6:8]),int(t[9:14])*10,None)
        datetime_list.append(date_time_object)
    itr += 1

difference_list = []
itr2 = 0
delta_list = []
while itr2 < len(datetime_list)-1:
    delta = datetime_list[itr2+1]-datetime_list[itr2]
    delta_list.append(delta.microseconds)
    itr2 += 1

tot_dif = 0.0
for num in delta_list:
    tot_dif += float("0." + str(num))
print("Avg hz, local ioc (" + sleep_sec + "sec): ", 1/(tot_dif/len(datetime_list)))
    
