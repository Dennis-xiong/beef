# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:57:49 2025

@author: bruger
"""

# The program finds swarming annotations within the dataset
# from the large EU project: Dooremalen et al 2024.

import pandas as pd

#  Load the excel file with the inspection data
file_path_T1_2020_inspection = 'bgood-data-dooremalen-et-al-2024/d7d782fd-81da-4c73-80f8-8817c48a2e9f/tier-1-2020-inspection-data-16032022.xlsx'
sheet_name = 'NL'

T1_2020_inspection = pd.read_excel(file_path_T1_2020_inspection, sheet_name = sheet_name)

# Search for rows containing 'swarm', 'swarming' or 'swarmed'
mask = T1_2020_inspection.apply(lambda row: row.astype(str).str.contains('swarm|swarming|swarmed',
                                                         case=False).any(), axis=1)

row_numbers = T1_2020_inspection[mask].index.tolist()

print("Row numbers containing 'swarm, swarming or swarmed':", row_numbers)

# Store the rows with indications of swarming in a data frame for inspection.
swarming_rows = T1_2020_inspection.loc[row_numbers]

