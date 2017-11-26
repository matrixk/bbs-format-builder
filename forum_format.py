#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:01:32 2017

@author: matrixk
"""
import random

f = open('forum_format.md', 'w')

def fluctuation(hour_flu):
    standard = 60
    flufluc = [2.73, 1.66, 1.10, 0.80, 0.66, 0.65, 0.91, 1.64, 3.32, 4.81, 5.56, 5.64, 5.53, 5.57, 5.83, 6.00, 6.13, 5.81, 5.68, 6.39, 6.79, 6.59, 5.77, 4.25]
    standard = standard / flufluc[int(hour_flu)]
    return standard

def forum_format(date, hour_start, min_start, sec_start, floor):
    #set initial
    floor_number = 25
    date_show = date
    time_hour = int(hour_start)
    time_min = int(min_start)
    time_sec = int(sec_start)
    standard = 60
    
    for i in range(floor_number,int(floor)+1):
        standard = fluctuation(time_hour)
        f.write (u"\u2116".encode("utf-8")+str(floor_number)+u"\u0020\u2606\u2606\u2606=\u0020=于".encode("utf-8"))
        f.write (str(date_show) + u"\u0020".encode("utf-8"))
        f.write (str(time_hour).zfill(2) + ":" + str(time_min).zfill(2) + ":" + str(time_sec).zfill(2) +u"留言\u2606\u2606\u2606".encode("utf-8"))
        f.write ("\n\n- - - - -\n\n\n\n")
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



date_input = "20XX-08-11"#raw_input("date: ")
time_start = "22:40:03"#raw_input("publish time of the first floor: ")
hour_input = time_start[0:2]
min_input = time_start[3:5]
sec_input = time_start[6:8]
floor_input = 200#raw_input("floor: ")
forum_format(date_input, hour_input, min_input, sec_input, floor_input)
