#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:02:11 2020

@author: zihan
"""

import os
import pandas as pd
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
sns.set(color_codes=True)

os.chdir('/Users/zihan/Desktop/spider_wd')

connect = pd.read_csv('Dunkin-FtMyers_Front-RTU1_1242020.csv', header=None, sep='\n')
connect = connect[0].str.split(',', expand=True)
connect = connect.iloc[1:,0:7]
connect.columns = ['Date', 'Time', 'ColdTemp', 'RoomTemp', 'Mode', 'Relay', 'State']

connect.dtypes
#check and drop the missing values 
print(connect.isnull().sum())
connect = connect.dropna() 

#convert numeric features to float type
connect['ColdTemp'] = pd.to_numeric(connect['ColdTemp'])
connect['RoomTemp'] = pd.to_numeric(connect['RoomTemp'])
connect['Datetime'] = connect['Date'].map(str) + ' ' + connect['Time']
connect['Datetime'] = pd.to_datetime(connect['Datetime'])
connect.index = connect['Datetime']
connect.drop(columns = ['Date'],inplace = True)
connect.drop(columns = ['Time'],inplace = True)
connect.dtypes

connect = connect.iloc[1866: ]
connect_agg = connect.resample('H').mean()


'''fig, axes = plt.subplots(figsize=(8,6))
axes1=axes.twinx()
connect[['Datetime', 'ColdTemp']].set_index('Datetime').resample('D').mean()['ColdTemp'].plot(ax=axes1,alpha=0.9, label='ColdTemp', color='green')
connect[['Datetime', 'RoomTemp']].set_index('Datetime').resample('D').mean()['RoomTemp'].plot(ax=axes1,alpha=0.9, label='RoomTemp', color='red')
plt.legend()'''

temp1 = pd.read_csv('Back Door-3.csv',delimiter = ',')
temp2 = pd.read_csv('Back Door-4.csv',delimiter = ',')
temp3 = pd.read_csv('Back Door-5.csv',delimiter = ',')
temp4 = pd.read_csv('Back Door-6.csv',delimiter = ',')

week3_cook = pd.read_csv('COOK Station MONITOR-2.csv',delimiter = ',')
week3_cook['Timestamp'] = pd.to_datetime(week3_cook['Timestamp'], format = '%Y-%m-%d %H:%M')
week3_cook.index = week3_cook['Timestamp']
week3_cook_agg = week3_cook.resample('H').mean()

week3_lob = pd.read_csv('Lobby Sign.csv',delimiter = ',')
week3_lob['Timestamp'] = pd.to_datetime(week3_lob['Timestamp'], format = '%Y-%m-%d %H:%M')
week3_lob.index = week3_lob['Timestamp']
week3_lob_agg = week3_lob.resample('H').mean()

week3_off = pd.read_csv('Office Next To TSTAT.csv',delimiter = ',')
week3_off['Timestamp'] = pd.to_datetime(week3_off['Timestamp'], format = '%Y-%m-%d %H:%M')
week3_off.index = week3_off['Timestamp']
week3_off_agg = week3_off.resample('H').mean()

weather = pd.read_csv('weather.csv',delimiter = ',')
week3_weather = weather.iloc[2445:3452]
week3_weather['time'] = pd.to_datetime(week3_weather['time'], format = '%Y-%m-%d %H:%M')
week3_weather.index = week3_weather['time']
week3_weather_agg = week3_weather.resample('H').mean()

wea = weather.iloc[431:]
wea['time'] = pd.to_datetime(wea['time'], format = '%Y-%m-%d %H:%M')
wea.index = wea['time']
wea_agg = wea.resample('D').mean()



temp4 = temp4.iloc[33120: ]

temp = pd.concat([temp4, temp3, temp2, temp1], axis = 0, ignore_index=True)
temp['Timestamp'] = pd.to_datetime(temp['Timestamp'], format = '%Y-%m-%d %H:%M')
temp.index = temp['Timestamp']
temp.dtypes


week1, week2, week3, week4 = np.array_split(temp,4)
week3_agg = week3.resample('H').mean()


fig, axes = plt.subplots(figsize=(12,6))
#plt.plot(connect_agg['ColdTemp'], color='black', linewidth=1.0, linestyle='-', label='ColdTemp')
#plt.plot(connect_agg['RoomTemp'], color='red', linewidth=1.0, linestyle='-', label='RoomTemp')
plt.plot(week3_agg['Temperature_Fahrenheit'], color='orange', linewidth=1.0, linestyle='-', label='Back Door')
plt.plot(week3_weather_agg['tem'], color='green', linewidth=1.0, linestyle='-', label='Outside')
plt.plot(week3_cook_agg['Temperature_Fahrenheit'], color='blue', linewidth=1.0, linestyle='-', label='Cook Station')
plt.plot(week3_lob_agg['Temperature_Fahrenheit'], color='red', linewidth=1.0, linestyle='-', label='Lobby')
plt.plot(week3_off_agg['Temperature_Fahrenheit'], color='purple', linewidth=1.0, linestyle='-', label='Office')
plt.title('Week3 Temperature _ Hour')
plt.legend()

fig, axes = plt.subplots(figsize=(12,6))
plt.plot(week3_agg['Relative_Humidity'], color='orange', linewidth=1.0, linestyle='-', label='Back Door')
plt.plot(week3_weather_agg['humidity'], color='green', linewidth=1.0, linestyle='-', label='Outside')
plt.plot(week3_cook_agg['Relative_Humidity'], color='blue', linewidth=1.0, linestyle='-', label='Cook Station')
plt.plot(week3_lob_agg['Relative_Humidity'], color='red', linewidth=1.0, linestyle='-', label='Lobby')
plt.plot(week3_off_agg['Relative_Humidity'], color='purple', linewidth=1.0, linestyle='-', label='Office')
plt.title('Week3 Humidity _ Hour')
plt.legend()

#all data
#back door

temp_agg = temp.resample('D').mean()

#cook station
cook1 = pd.read_csv('1.4-1.10.csv',delimiter = ',')
cook2 = pd.read_csv('1.11-1.17.csv',delimiter = ',')
cook3 = pd.read_csv('1.18-1.24.csv',delimiter = ',')
cook4 = pd.read_csv('1.25-1.31.csv',delimiter = ',')
cook = pd.concat([cook1, cook2, cook3, cook4], axis = 0, ignore_index=True)
cook['Timestamp'] = pd.to_datetime(cook['Timestamp'], format = '%Y-%m-%d %H:%M')
cook.index = cook['Timestamp']
cook_agg = cook.resample('D').mean()

# office
off1 = pd.read_csv('1-1.csv',delimiter = ',')
off2 = pd.read_csv('1-10.csv',delimiter = ',')
off3 = pd.read_csv('1-18.csv',delimiter = ',')
off4 = pd.read_csv('1-25.csv',delimiter = ',')
off = pd.concat([off1, off2, off3, off4], axis = 0, ignore_index=True)
off = off.iloc[31680: ]
off['Timestamp'] = pd.to_datetime(off['Timestamp'], format = '%Y-%m-%d %H:%M')
off.index = off['Timestamp']
off['min'] = 68.42 
off['max'] = 76.13
off['hmin'] = 20
off['hmax'] = 80
off_agg = off.resample('D').mean()

# lobby
lob1 = pd.read_csv('lobby_1.4-1.10 1.csv',delimiter = ',')
lob2 = pd.read_csv('lobby_1.11-1.17.csv',delimiter = ',')
lob3 = pd.read_csv('lobby_1.18-1.24.csv',delimiter = ',')
lob4 = pd.read_csv('lobby_1.25-1.31.csv',delimiter = ',')
lob = pd.concat([lob1, lob2, lob3, lob4], axis = 0, ignore_index=True)
lob['Timestamp'] = pd.to_datetime(lob['Timestamp'], format = '%Y-%m-%d %H:%M')
lob.index = lob['Timestamp']
lob_agg = lob.resample('D').mean()

lob1['Timestamp'] = pd.to_datetime(lob1['Timestamp'], format = '%Y-%m-%d %H:%M')
lob1.index = lob1['Timestamp']
lob1_agg = lob1.resample('H').mean()
#lob1_agg.index  = lob1_agg.index.time


lob2['Timestamp'] = pd.to_datetime(lob2['Timestamp'], format = '%Y-%m-%d %H:%M')
lob2.index = lob2['Timestamp']
lob2_agg = lob2.resample('H').mean()
#lob2_agg.index  = lob2_agg.index.time

lob3['Timestamp'] = pd.to_datetime(lob3['Timestamp'], format = '%Y-%m-%d %H:%M')
lob3.index = lob3['Timestamp']
lob3_agg = lob3.resample('H').mean()
#lob3_agg.index  = lob3_agg.index.time


lob4['Timestamp'] = pd.to_datetime(lob4['Timestamp'], format = '%Y-%m-%d %H:%M')
lob4.index = lob4['Timestamp']
lob4_agg = lob4.resample('H').mean()
#lob4_agg.index  = lob4_agg.index.time


#temperature
fig, axes = plt.subplots(figsize=(12,6))
plt.plot(lob_agg['Temperature_Fahrenheit'], color='orange', linewidth=1.0, linestyle='-', label='Lobby')
plt.plot(wea_agg['tem'], color='green', linewidth=1.0, linestyle='-', label='Outside')
plt.plot(cook_agg['Temperature_Fahrenheit'], color='blue', linewidth=1.0, linestyle='-', label='Cook Station')
plt.plot(temp_agg['Temperature_Fahrenheit'], color='red', linewidth=1.0, linestyle='-', label='Back Door')
plt.plot(off_agg['Temperature_Fahrenheit'], color='purple', linewidth=1.0, linestyle='-', label='Office')
plt.plot(off_agg['min'], color='black', linewidth=1.0, linestyle='--', label='Min')
plt.plot(off_agg['max'], color='black', linewidth=1.0, linestyle='--', label='Max')
plt.title("Temperature_Day")
plt.legend()
plt.savefig('T.png')

fig, axes = plt.subplots(figsize=(12,6))
plt.plot(temp_agg['Relative_Humidity'], color='orange', linewidth=1.0, linestyle='-', label='Back Door')
plt.plot(wea_agg['humidity'], color='green', linewidth=1.0, linestyle='-', label='Outside')
plt.plot(cook_agg['Relative_Humidity'], color='blue', linewidth=1.0, linestyle='-', label='Cook Station')
plt.plot(lob_agg['Relative_Humidity'], color='red', linewidth=1.0, linestyle='-', label='Lobby')
plt.plot(off_agg['Relative_Humidity'], color='purple', linewidth=1.0, linestyle='-', label='Office')
plt.plot(off_agg['hmin'], color='black', linewidth=1.0, linestyle='--', label='Min')
plt.plot(off_agg['hmax'], color='black', linewidth=1.0, linestyle='--', label='Max')
plt.title("Humidity_Day")
plt.legend()
plt.savefig('T.png')

#boxplot

temp.describe()

fig = plt.figure()
ax = plt.subplot()
ax.boxplot([temp['Temperature_Fahrenheit'],cook['Temperature_Fahrenheit'],off['Temperature_Fahrenheit'],lob['Temperature_Fahrenheit'],wea['tem']])
ax.set_xticklabels(['Back Door', 'Cook Station', 'Office', 'Lobby', 'Weather'])
ax.set_title('Boxplots')
plt.show()

#lobby 
lob_new = lob.copy()
lob_new_agg = lob_new.resample('H').mean()
lob_new_agg.describe()
#IQR: 76.13 - 68.42

#visualize the weekly comparison on temperature and humidity of different locations
fig, axes = plt.subplots(figsize=(12,6))
plt.plot(lob1_agg['Temperature_Fahrenheit'], color='red', linewidth=1.0, linestyle='-', label='WEEK1')
plt.plot(lob2_agg['Temperature_Fahrenheit'], color='purple', linewidth=1.0, linestyle='-', label='WEEK2')
plt.plot(lob3_agg['Temperature_Fahrenheit'], color='green', linewidth=1.0, linestyle='-', label='WEEK3')
plt.plot(lob4_agg['Temperature_Fahrenheit'], color='orange', linewidth=1.0, linestyle='-', label='WEEK4')
plt.plot(off_agg['min'], color='blue', linewidth=1.0, linestyle='--', label='Upper: 76.13')
plt.plot(off_agg['max'], color='blue', linewidth=1.0, linestyle='--', label='Lower: 68.42')
plt.title("Weekly lobby Temperature")
plt.legend()

fig, axes = plt.subplots(figsize=(12,6))
plt.plot(lob1['Temperature_Fahrenheit'], color='red', linewidth=1.0, linestyle='-', label='WEEK1')
plt.plot(lob2['Temperature_Fahrenheit'], color='purple', linewidth=1.0, linestyle='-', label='WEEK2')
plt.plot(lob3['Temperature_Fahrenheit'], color='green', linewidth=1.0, linestyle='-', label='WEEK3')
plt.plot(lob4['Temperature_Fahrenheit'], color='orange', linewidth=1.0, linestyle='-', label='WEEK4')
plt.plot(off_agg['min'], color='blue', linewidth=1.0, linestyle='--', label='Upper: 76.13')
plt.plot(off_agg['max'], color='blue', linewidth=1.0, linestyle='--', label='Lower: 68.42')
plt.title("Lobby Temperature")
plt.legend()
