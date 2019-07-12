name = "LS1_CA01:FTHS_N0001"
name_l = list(name)
name_l[3],name_l[8],name_l[13] = "-","-","-"
name_for_folder = "".join(name_l).lower()
print name_for_folder

sensor = "LS1:CA01:FTS:TX481A"
sensor_l = list(sensor)
sensor_l[3],sensor_l[12] = "_","_"
sensor_l.insert(10, "H")
sensor = "".join(sensor_l)
print sensor
