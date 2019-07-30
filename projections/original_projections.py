""" In this script I load the clean original openML csv and I save the file with the projection described """


import pandas as pd

# Load the clean original openML csv
original_with_ids = pd.read_csv('csv/original/original_with_ids_all_metafeatures.csv')

# Select only the metafeatures in http://www.essi.upc.edu/~bbilalli/datasets.html
original_with_ids_simply_metafeatures = original_with_ids[['Name','NumberOfInstances','NumberOfMissingValues','NumberOfNumericFeatures','NumberOfSymbolicFeatures','NumberOfClasses','MajorityClassPercentage']]
original_with_ids_simply_metafeatures.to_csv("csv/original/original_with_ids_simply_metafeatures.csv")

# Select only the metafeatures in the paper 'Intelligent assistance for data pre-processing'
original_with_ids_abello_metafeatures = original_with_ids[['Name','NumberOfNumericFeatures','PercentageOfNumericFeatures','MinMeansOfNumericAtts','MinStdDevOfNumericAtts','MinKurtosisOfNumericAtts','MinSkewnessOfNumericAtts','MeanMeansOfNumericAtts','MeanStdDevOfNumericAtts','MeanKurtosisOfNumericAtts','MeanSkewnessOfNumericAtts','MaxMeansOfNumericAtts','MaxStdDevOfNumericAtts','MaxKurtosisOfNumericAtts','MaxSkewnessOfNumericAtts', 'Quartile1MeansOfNumericAtts', 'Quartile2MeansOfNumericAtts', 'Quartile3MeansOfNumericAtts', 'Quartile1StdDevOfNumericAtts', 'Quartile2StdDevOfNumericAtts', 'Quartile3StdDevOfNumericAtts', 'Quartile1KurtosisOfNumericAtts', 'Quartile2KurtosisOfNumericAtts', 'Quartile3KurtosisOfNumericAtts', 'Quartile1SkewnessOfNumericAtts', 'Quartile2SkewnessOfNumericAtts', 'Quartile3SkewnessOfNumericAtts', 'NumberOfSymbolicFeatures', 'NumberOfBinaryFeatures', 'PercentageOfSymbolicFeatures', 'PercentageOfBinaryFeatures', 'MinAttributeEntropy', 'MeanAttributeEntropy', 'MaxAttributeEntropy', 'Quartile1AttributeEntropy', 'Quartile2AttributeEntropy', 'Quartile3AttributeEntropy', 'MinMutualInformation', 'MeanMutualInformation', 'MaxMutualInformation', 'Quartile1MutualInformation', 'Quartile2MutualInformation', 'Quartile3MutualInformation', 'EquivalentNumberOfAtts', 'MeanNoiseToSignalRatio', 'MinNominalAttDistinctValues', 'MeanNominalAttDistinctValues', 'MaxNominalAttDistinctValues', 'StdvNominalAttDistinctValues', 'NumberOfInstances', 'NumberOfFeatures', 'Dimensionality', 'NumberOfMissingValues', 'PercentageOfMissingValues', 'NumberOfInstancesWithMissingValues', 'PercentageOfInstancesWithMissingValues', 'NumberOfClasses', 'ClassEntropy', 'MinorityClassSize', 'MajorityClassSize', 'MinorityClassPercentage', 'MajorityClassPercentage']]
original_with_ids_abello_metafeatures.to_csv("csv/original/original_with_ids_abello_metafeatures.csv")


