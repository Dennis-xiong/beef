# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:09:45 2025

@author: ivot
"""

# Plot sound data from a hive
import pandas as pd
import matplotlib.pyplot as plt

# Load the excel file with the sensor data
# We load the Tier 1 data from 2021 for device_id 495, 425, 511, 435

file_path_T1_2021_d_id_495 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/DE beep-export-research-1-device-id-495-sensor-data-2021-01-01-2021-12-31-9Fw4endisE.csv'
file_path_T1_2021_d_id_425 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/GB beep-export-research-1-device-id-425-sensor-data-2021-01-01-2021-12-31-Ub5iUHrSQX.csv'
file_path_T1_2021_d_id_511 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/NL beep-export-research-1-device-id-511-sensor-data-2021-01-01-2021-12-31-ioKS99HRhe.csv'
file_path_T1_2021_d_id_435 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/PT beep-export-research-1-device-id-435-sensor-data-2021-01-01-2021-12-31-MiXyUAlgmv.csv'

d_id_495 = pd.read_csv(file_path_T1_2021_d_id_495)
d_id_425 = pd.read_csv(file_path_T1_2021_d_id_425)
d_id_511 = pd.read_csv(file_path_T1_2021_d_id_511)
d_id_435 = pd.read_csv(file_path_T1_2021_d_id_435)

# Convert the first column to datetime format
d_id_495.iloc[:, 0] = pd.to_datetime(d_id_495.iloc[:, 0], errors='coerce')
d_id_425.iloc[:, 0] = pd.to_datetime(d_id_425.iloc[:, 0], errors='coerce')
d_id_511.iloc[:, 0] = pd.to_datetime(d_id_511.iloc[:, 0], errors='coerce')
d_id_435.iloc[:, 0] = pd.to_datetime(d_id_435.iloc[:, 0], errors='coerce')

# Select a time interval around the swarming annotation
d_id_495_swarm = d_id_495.iloc[11329:14087]
d_id_425_swarm = d_id_425.iloc[8306:11019]
d_id_511_swarm = d_id_511.iloc[10356:10994]
d_id_435_swarm = d_id_435.iloc[9000:10000]

# Set the first column as the index
d_id_495_swarm.set_index(d_id_495_swarm.columns[0], inplace=True)
d_id_425_swarm.set_index(d_id_425_swarm.columns[0], inplace=True)
d_id_511_swarm.set_index(d_id_511_swarm.columns[0], inplace=True)
d_id_435_swarm.set_index(d_id_435_swarm.columns[0], inplace=True)

# Plot the data from column 8 to column 17 as a function of time
d_id_495_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 18033 Device_id = 495 Sensor Data')
plt.legend(loc='best')
plt.show()

d_id_511_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 20378 Device_id = 511 Sensor Data')
plt.legend(loc='best')
plt.show()

d_id_435_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 20378 Device_id = 435 Sensor Data')
plt.legend(loc='best')
plt.show()

d_id_425_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 14501 Device_id = 425 Sensor Data')
plt.legend(loc='best')
plt.show()

# Device_id 425 looks interesting.  
d_id_425_swarm.iloc[:,13:15].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 14501 Device_id = 425 Sensor Data Tooting?')
plt.legend(loc='best')
plt.show()

d_id_425_swarm.iloc[:,11:12].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 14501 Device_id = 425 Sensor Data Quacking?')
plt.legend(loc='best')
plt.show()

d_id_425_swarm.iloc[:,1:2].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 14501 Device_id = 425 Sensor Data')
plt.legend(loc='best')
plt.show()

