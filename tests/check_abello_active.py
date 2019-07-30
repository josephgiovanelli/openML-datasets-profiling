""" In this script I load both the original openML and the abello ones. Then I print the elements of abello which are not
 in the original openML. This is because in the original openML table there are only the active ones. """

import pandas as pd


# It checks if lst1 is contained in lst2
def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)


# Load the clean original openML csv
original_with_ids = pd.read_csv('csv/original/original_with_ids_all_metafeatures.csv')
original_with_ids_only_name = original_with_ids['Name'].values.tolist()

# Load the abello csv
abello = pd.read_csv('csv/abello/abello_simply_metafeatures.csv')
abello_only_name = abello['Name'].values.tolist()

# Check if the abello datasets are all contained in the original openML datasets
print('Are all the datasets active? ' + str(sublist(abello_only_name, original_with_ids_only_name)))

# Show the non active datasets
print('\nHere the non active datasets:')
for record in abello_only_name:
    if record not in original_with_ids_only_name:
        print(record)
