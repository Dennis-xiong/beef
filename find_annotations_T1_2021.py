# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:57:49 2025

@author: bruger
"""

# The program finds swarming annotations within the dataset
# from the large EU project: Dooremalen et al 2024.

import pandas as pd

#  Load the excel file with the inspection data
file_path_T1_2021_inspection = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2021-inspection-data-20230107.xlsx'

T1_2021_inspection = pd.read_excel(file_path_T1_2021_inspection)

# Search for rows containing 'swarm','swarming' or 'swarmed'
mask_swarm = T1_2021_inspection.apply(lambda row: row.astype(str).str.contains('swarm|swarming|swarmed',
                                                         case=False).any(), axis=1)
# Search for rows containing a 'Yes' under Beecolony>Activity>Swarming>Swarmed'
mask_yes = T1_2021_inspection['Bee colony > Activity > Swarming > Swarmed'] == 'Yes'

# Combine the maske
mask = mask_swarm|mask_yes

# Find the corresponding row numbers

row_numbers = T1_2021_inspection[mask].index.tolist()

# print the row numbers indicating swarming
print("Row numbers containing 'swarm, swarming or swarmed':", row_numbers)

# make a data frame consisting of rows with swarming indications for inspection.
swarming_rows = T1_2021_inspection.loc[row_numbers]

# make a data frame consisting of annotations for selected hives 
# with swarming indicated

inspections_h_id_14501 = T1_2021_inspection[T1_2021_inspection['Hive_id'] == 14501]
inspections_h_id_19414 = T1_2021_inspection[T1_2021_inspection['Hive_id'] == 19414]