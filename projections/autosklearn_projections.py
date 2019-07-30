""" In this script I load the clean original csv, I select only the datasets used in auto-sklearn
 and I save the file with the projection described """


import pandas as pd

# Load the clean original openML csv
original_with_ids = pd.read_csv('csv/original/original_with_ids_all_metafeatures.csv', index_col='Id')

# Select only the dataset used in auto-sklearn
autosklearn_all_metafeatures = original_with_ids.reindex([3, 6, 12, 14, 16, 18, 22, 23, 24, 26, 28, 30, 31, 32, 36, 38, 44, 46, 57, 60, 179, 180, 181, 182, 184, 185, 273, 293, 300, 351, 354, 357, 389, 390, 391, 392, 393, 395, 396, 398, 399, 401, 554, 679, 715, 718, 720, 201, 723, 727, 728, 734, 735, 737, 740, 741, 743, 751, 752, 761, 772, 797, 799, 803, 806, 807, 813, 816, 819, 821, 823, 833, 837, 843, 845, 846, 847, 849, 866, 871, 881, 897, 901, 903, 904, 910, 912, 913, 914, 917, 923, 930, 934, 953, 958, 959, 962, 966, 971, 976, 977, 978, 979, 980, 991, 993, 995, 57, 32, 16, 30, 1040, 1041, 1049, 1050, 1053, 1056, 1067, 1068, 1069, 1111, 1112, 1114, 1116, 1119, 1120, 1128, 1130, 1134, 1138, 1139, 1142, 1146, 1161, 1166])
autosklearn_all_metafeatures.to_csv("csv/autosklearn/autosklearn_all_metafeatures.csv")

# Select only the metafeatures in http://www.essi.upc.edu/~bbilalli/datasets.html
autosklearn_simply_metafeatures = autosklearn_all_metafeatures[['Name','NumberOfInstances','NumberOfMissingValues','NumberOfNumericFeatures','NumberOfSymbolicFeatures','NumberOfClasses','MajorityClassPercentage']]
autosklearn_simply_metafeatures.to_csv("csv/autosklearn/autosklearn_simply_metafeatures.csv")

# Select only the metafeatures in the paper 'Intelligent assistance for data pre-processing'
autosklearn_abello_metafeatures = autosklearn_all_metafeatures[['Name','NumberOfNumericFeatures','PercentageOfNumericFeatures','MinMeansOfNumericAtts','MinStdDevOfNumericAtts','MinKurtosisOfNumericAtts','MinSkewnessOfNumericAtts','MeanMeansOfNumericAtts','MeanStdDevOfNumericAtts','MeanKurtosisOfNumericAtts','MeanSkewnessOfNumericAtts','MaxMeansOfNumericAtts','MaxStdDevOfNumericAtts','MaxKurtosisOfNumericAtts','MaxSkewnessOfNumericAtts', 'Quartile1MeansOfNumericAtts', 'Quartile2MeansOfNumericAtts', 'Quartile3MeansOfNumericAtts', 'Quartile1StdDevOfNumericAtts', 'Quartile2StdDevOfNumericAtts', 'Quartile3StdDevOfNumericAtts', 'Quartile1KurtosisOfNumericAtts', 'Quartile2KurtosisOfNumericAtts', 'Quartile3KurtosisOfNumericAtts', 'Quartile1SkewnessOfNumericAtts', 'Quartile2SkewnessOfNumericAtts', 'Quartile3SkewnessOfNumericAtts', 'NumberOfSymbolicFeatures', 'NumberOfBinaryFeatures', 'PercentageOfSymbolicFeatures', 'PercentageOfBinaryFeatures', 'MinAttributeEntropy', 'MeanAttributeEntropy', 'MaxAttributeEntropy', 'Quartile1AttributeEntropy', 'Quartile2AttributeEntropy', 'Quartile3AttributeEntropy', 'MinMutualInformation', 'MeanMutualInformation', 'MaxMutualInformation', 'Quartile1MutualInformation', 'Quartile2MutualInformation', 'Quartile3MutualInformation', 'EquivalentNumberOfAtts', 'MeanNoiseToSignalRatio', 'MinNominalAttDistinctValues', 'MeanNominalAttDistinctValues', 'MaxNominalAttDistinctValues', 'StdvNominalAttDistinctValues', 'NumberOfInstances', 'NumberOfFeatures', 'Dimensionality', 'NumberOfMissingValues', 'PercentageOfMissingValues', 'NumberOfInstancesWithMissingValues', 'PercentageOfInstancesWithMissingValues', 'NumberOfClasses', 'ClassEntropy', 'MinorityClassSize', 'MajorityClassSize', 'MinorityClassPercentage', 'MajorityClassPercentage']]
autosklearn_abello_metafeatures.to_csv("csv/autosklearn/autosklearn_abello_metafeatures.csv")

