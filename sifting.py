
import pandas as pd
import numpy as np
from typing import List

def find_matching_street(lat, lon, street_data):
    for _, street in street_data.iterrows():
        if (street_data['left_bound_long'] <= lon <= street_data['right_bound_long'] and
            street_data['down_bound_lat'] <= lat <= street_data['up_bound_lat']):
            return street
    return None


#function to add the columns to a specified row.
def add_columns(heart_data: pd.DataFrame, street_data: pd.DataFrame, street_columns: List[str], index):
    for column in street_columns:
        heart_data.at[index, column] = street_data[column].values[0]


##initalizes the data sets into pd dataframes
heart_data = './dataset/filtered_heart_data.csv'
street_data = './dataset/second_data.csv'


heart_file = pd.read_csv(heart_data)
street_file = pd.read_csv(street_data)

street_columns = [
    'streetname', 'fromstreetname', 'tostreetname', 'sci', 'num_of_uplifts',
    'maintenance_suggestion', 'estimated_cost', 'repair_priority', 'functional_class',
    'functional_class_id', 'surface_type', 'survey_date', 'width_ft', 'length_ft',
    'area_sy', 'sci_2023', 'sw_id', 'begin_width', 'end_width', 'avg_width',
    'nu_of_distresses', 'num_crack_minor', 'num_crack_moderate', 'num_crack_severe',
    'num_grass_present', 'num_surface_distortion_minor', 'num_surface_distortion_mod',
    'num_surface_distortion_severe', 'num_uplift_general_minor', 'num_uplift_general_moderate',
    'num_uplift_general_severe', 'num_uplift_tree_minor', 'num_uplift_tree_moderate',
    'num_uplift_tree_severe', 'num_utility_hazard_present', 'left_bound_long',
    'right_bound_long', 'down_bound_lat', 'up_bound_lat'
]


#initalizes new columns within the heart data
# Initialize new columns within the heart data with appropriate dtypes
for column in street_columns:
    if column in street_file.select_dtypes(include=['object']).columns:
        heart_file[column] = pd.Series(dtype='object')
    else:
        heart_file[column] = pd.Series(dtype='float64')

# goes through every row of the heart data 
for index, row in heart_file.iterrows():
    longitude = row['Longitude']
    latitude = row['Latitude']
    matching_street = find_matching_street(latitude, longitude, street_file)
    
    if matching_street is not None:
        for column in street_columns:
            heart_file.at[index, column] = matching_street[column]
        
       


        
# Calculate average stress level for each street
heart_file['avg_stress_lvl_Dummy'] = heart_file.groupby('streetname')['Stress score'].transform('mean')

# Save the updated data to a new CSV file
heart_file.to_csv('updated_file.csv', index=False)



# if latitude between lattitude_min and Latitude_max
    #if between longtidue_min and longtiude_max
        #

