
import pandas as pd
from typing import List


##function to add the columns to a specified row.
# def add_columns(heart_data: pd.DataFrame, street_data: pd.DataFrame, street_columns: List[str], index):
#     for column in street_columns:
#         heart_data.at[index, column] = street_data[column].values[0]
import numpy as np

def remove_irrelevant_rows(
    heart_data: pd.DataFrame,
    latitude_min: float = 41.677476,
    latitude_max: float = 41.679436,
    longitude_min: float = -86.253347,
    longitude_max: float = -86.243803
) -> pd.DataFrame:
    filtered_data = heart_data[
        (heart_data['Latitude'].between(latitude_min, latitude_max)) &
        (heart_data['Longitude'].between(longitude_min, longitude_max))
    ]
    return filtered_data



##initalizes the data sets into pd dataframes
heart_data = './dataset/heartrate_data.csv'
street_data = './dataset/prelim_data.csv'


dirty_heart_file = pd.read_csv(heart_data)
street_file = pd.read_csv(street_data)





dirty_heart_file['Latitude'] = pd.to_numeric(dirty_heart_file['Latitude'], errors='coerce')
dirty_heart_file['Longitude'] = pd.to_numeric(dirty_heart_file['Longitude'], errors='coerce')
##cleans file of irrelevant data


heart_file = remove_irrelevant_rows(
    dirty_heart_file, 
    latitude_min= 41.677476,
    latitude_max = 41.679436,
    longitude_min= -86.243803,
    longitude_max = -86.253347)

print(heart_file)


heart_file.to_csv('filtered_heart_data.csv', index=False)
street_columns = [
    'streetname', 'num_of_uplifts', 'maintenance_suggestion', 'repair_priority', 'surface_type',
    'length_ft', 'area_sy', 'sci_2023', 'sw_id', 'avg_width', 'num_of_distresses', 'bufferwidth_avg',
    'num_crack_minor', 'num_crack_moderate', 'num_crack_severe', 'num_grass_present', 
    'num_surface_distortion_minor', 'num_surface_distortion_mod', 'num_surface_distortion_severe',
    'num_uplift_general_minor', 'num_uplift_general_moderate', 'num_uplift_general_severe',
    'num_uplift_tree_minor', 'num_uplift_tree_moderate', 'num_uplift_tree_severe',
    'num_utility_hazard_present', 'avg_stress_lvl_Dummy'
]


##initalizes new columns within the heart data
# for column in street_columns:
#     heart_file[column] = None

# print(street_file['streetname'].values)
## goes through every row of the heart data 
# for index, row in heart_data.iterrows():
#     longitude = row['longitude']
#     latitue = row['latitude']

#     if longitude and latitude matches a :
#         pass
        
       


        


# heart_data.to_csv('updated_file.csv', index=False)


#3
## if latitude between lattitude_min and Latitude_max
    ##if between longtidue_min and longtiude_max
        ##

