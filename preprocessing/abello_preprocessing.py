""" In this script I clean the abello_simply_metafeatures.csv """

import pandas as pd

# Load the clean original openML csv
original_with_ids_all_metafeatures = pd.read_csv('csv/original/original_with_ids_all_metafeatures.csv')
# Select only the name of the datasets
original_with_ids_only_name = original_with_ids_all_metafeatures['Name'].values.tolist()


# Load the abello csv
abello_simply_metafeatures = pd.read_csv('csv/abello/abello_simply_metafeatures.csv')
# Select only the name of the dataset
abello_only_name = abello_simply_metafeatures['Name'].values.tolist()


# Get only the active dataset names
abello_active_simply_metafeatures = abello_simply_metafeatures.set_index('Name')
for record in abello_only_name:
    if record not in original_with_ids_only_name:
        abello_only_name.remove(record)


# Use the active dataset names to filter from the original openML dataframe
original_with_ids_all_metafeatures.set_index('Name', inplace=True)
abello_with_ids_all_metafeatures = original_with_ids_all_metafeatures.reindex(abello_only_name)
# Write the abello dataset with the all metafeatures
abello_with_ids_all_metafeatures.to_csv("csv/abello/abello_with_ids_all_metafeatures.csv")


