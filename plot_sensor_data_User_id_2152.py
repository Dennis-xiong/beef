# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:09:45 2025

@author: ivot
"""

# Plot sound data from a hive
import pandas as pd
import matplotlib.pyplot as plt

# Load the excel file with the sensor data
# We load the Tier 1 data from 2021 for user_id 2152 GB device_id 424, 425, 426, 427

file_path_T1_2021_d_id_424 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/GB beep-export-research-1-device-id-424-sensor-data-2021-01-01-2021-12-31-Wxjjz4pzQd.csv'
file_path_T1_2021_d_id_425 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/GB beep-export-research-1-device-id-425-sensor-data-2021-01-01-2021-12-31-Ub5iUHrSQX.csv'
file_path_T1_2021_d_id_426 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/GB beep-export-research-1-device-id-426-sensor-data-2021-01-01-2021-12-31-Jo0HDx3n3S.csv'
file_path_T1_2021_d_id_427 = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-sensor-data/3_sensor data files/GB beep-export-research-1-device-id-427-sensor-data-2021-01-01-2021-12-31-wGpkHc0Zm1.csv'

d_id_424 = pd.read_csv(file_path_T1_2021_d_id_424)
d_id_425 = pd.read_csv(file_path_T1_2021_d_id_425)
d_id_426 = pd.read_csv(file_path_T1_2021_d_id_426)
d_id_427 = pd.read_csv(file_path_T1_2021_d_id_427)


# Convert the first column to datetime format
d_id_424.iloc[:, 0] = pd.to_datetime(d_id_424.iloc[:, 0], errors='coerce')
d_id_425.iloc[:, 0] = pd.to_datetime(d_id_425.iloc[:, 0], errors='coerce')
d_id_426.iloc[:, 0] = pd.to_datetime(d_id_426.iloc[:, 0], errors='coerce')
d_id_427.iloc[:, 0] = pd.to_datetime(d_id_427.iloc[:, 0], errors='coerce')

# Select a time window around the swarming event of d_id_424
# Define the start and end time
start_time = pd.Timestamp('2021-04-10 00:00:00+00:00')
end_time = pd.Timestamp('2021-05-10 00:00:00+00:00')

# Find index of start and end time
start_index_424 = d_id_424[d_id_424['time'] > start_time].index[0]
start_index_425 = d_id_425[d_id_425['time'] > start_time].index[0]
start_index_426 = d_id_426[d_id_426['time'] > start_time].index[0]
start_index_427 = d_id_427[d_id_427['time'] > start_time].index[0]
end_index_424 = d_id_424[d_id_424['time'] > end_time].index[0]
end_index_425 = d_id_425[d_id_425['time'] > end_time].index[0]
end_index_426 = d_id_426[d_id_426['time'] > end_time].index[0]
end_index_427 = d_id_427[d_id_427['time'] > end_time].index[0]


d_id_424_swarm = d_id_424.iloc[start_index_424:end_index_424]
d_id_425_swarm = d_id_425.iloc[start_index_425:end_index_425]
d_id_426_swarm = d_id_426.iloc[start_index_426:end_index_426]
d_id_427_swarm = d_id_427.iloc[start_index_427:end_index_427]

# Set the first column as the index
d_id_424_swarm.set_index(d_id_424_swarm.columns[0], inplace=True)
d_id_425_swarm.set_index(d_id_425_swarm.columns[0], inplace=True)
d_id_426_swarm.set_index(d_id_426_swarm.columns[0], inplace=True)
d_id_427_swarm.set_index(d_id_427_swarm.columns[0], inplace=True)

# Plot the data from column 8 to column 17 as a function of time
d_id_424_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 29546 Device_id = 424 Sensor Data')
plt.legend(loc='best')
plt.show()

d_id_425_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 14501 Device_id = 425 Sensor Data')
plt.legend(loc='best')
plt.show()

d_id_426_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 23922 Device_id = 426 Sensor Data')
plt.legend(loc='best')
plt.show()

d_id_427_swarm.iloc[:, 6:16].plot(figsize=(12, 6))
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Hive_id = 32038 Device_id = 427 Sensor Data')
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

