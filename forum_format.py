#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:01:32 2017

@author: matrixk
"""
import random

f = open('forum_format.md', 'w')

def fluctuation(hour_flu):
    standard = 35
    if int(hour_flu) == 0:
        standard = standard / 2.73
    elif int(hour_flu) == 1:
        standard = standard / 1.66
    elif int(hour_flu) == 2:
        standard = standard / 1.10
    elif int(hour_flu) == 3:
        standard = standard / 0.80
    elif int(hour_flu) == 4:
        standard = standard / 0.66
    elif int(hour_flu) == 5:
        standard = standard / 0.65
    elif int(hour_flu) == 6:
        standard = standard / 0.91
    elif int(hour_flu) == 7:
        standard = standard / 1.64
    elif int(hour_flu) == 8:
        standard = standard / 3.32
    elif int(hour_flu) == 9:
        standard = standard / 4.81
    elif int(hour_flu) == 10:
        standard = standard / 5.56
    elif int(hour_flu) == 11:
        standard = standard / 5.64
    elif int(hour_flu) == 12:
        standard = standard / 5.53
    elif int(hour_flu) == 13:
        standard = standard / 5.57
    elif int(hour_flu) == 14:
        standard = standard / 5.58
    elif int(hour_flu) == 15:
        standard = standard / 6.00
    elif int(hour_flu) == 16:
        standard = standard / 6.13
    elif int(hour_flu) == 17:
        standard = standard / 5.81
    elif int(hour_flu) == 18:
        standard = standard / 5.68
    elif int(hour_flu) == 19:
        standard = standard / 6.39
    elif int(hour_flu) == 20:
        standard = standard / 6.79
    elif int(hour_flu) == 21:
        standard = standard / 6.59
    elif int(hour_flu) == 22:
        standard = standard / 5.77
    elif int(hour_flu) == 23:
        standard = standard / 4.25
    else:
        standard = standard
    return standard

def forum_format(date, hour_start, min_start, sec_start, floor):
    #set initial
    floor_number = 0
    date_show = date
    time_hour = int(hour_start)
    time_min = int(min_start)
    time_sec = int(sec_start)
    standard = 35
    
    for i in range(int(floor)+1):
        standard = fluctuation(time_hour)
        f.write (u"\u2116".encode("utf-8")+str(floor_number)+u"\u0020\u2606\u2606\u2606=\u0020=于".encode("utf-8"))
        f.write (str(date_show) + u"\u0020".encode("utf-8"))
        f.write (str(time_hour).zfill(2) + ":" + str(time_min).zfill(2) + ":" + str(time_sec).zfill(2) +u"留言\u2606\u2606\u2606".encode("utf-8"))
        f.write ("\n\n- - - - -\n\n")
        floor_number = floor_number + 1
        time_sec = time_sec + random.randint(1,59)
        if time_sec >= 60:
            time_sec = time_sec - 60
            time_min = time_min + 1
            
        time_min = time_min + random.randint(1,int(standard))
        
        while time_min >= 60:
            time_hour = time_hour + 1
            time_min = time_min - 60
            
        while time_hour >= 24:
            time_hour = time_hour - 24
            date_day = int(date_show[8:10]) + 1
            date_show = date_show[0:8]+str(date_day).zfill(2)

    f.close()



date_input = raw_input("date: ")
time_start = raw_input("publish time of the first floor: ")
hour_input = time_start[0:2]
min_input = time_start[3:5]
sec_input = time_start[6:8]
floor_input = raw_input("floor: ")
forum_format(date_input, hour_input, min_input, sec_input, floor_input)
