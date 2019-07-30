""" In this script I load the clean abello csv and I save the file with the projection described """

import pandas as pd

# Load the clean abello csv
abello_with_ids_all_metafeatures = pd.read_csv('csv/abello/abello_with_ids_all_metafeatures.csv')

# Select only the metafeatures in http://www.essi.upc.edu/~bbilalli/datasets.html
abello_with_ids_simply_metafeatures = abello_with_ids_all_metafeatures[['Name','NumberOfInstances','NumberOfMissingValues','NumberOfNumericFeatures','NumberOfSymbolicFeatures','NumberOfClasses','MajorityClassPercentage']]
abello_with_ids_simply_metafeatures.to_csv("csv/abello/abello_with_ids_simply_metafeatures.csv")

# Select only the metafeatures in the paper 'Intelligent assistance for data pre-processing'
abello_with_ids_abello_metafeatures = abello_with_ids_all_metafeatures[['Name','NumberOfNumericFeatures','PercentageOfNumericFeatures','MinMeansOfNumericAtts','MinStdDevOfNumericAtts','MinKurtosisOfNumericAtts','MinSkewnessOfNumericAtts','MeanMeansOfNumericAtts','MeanStdDevOfNumericAtts','MeanKurtosisOfNumericAtts','MeanSkewnessOfNumericAtts','MaxMeansOfNumericAtts','MaxStdDevOfNumericAtts','MaxKurtosisOfNumericAtts','MaxSkewnessOfNumericAtts', 'Quartile1MeansOfNumericAtts', 'Quartile2MeansOfNumericAtts', 'Quartile3MeansOfNumericAtts', 'Quartile1StdDevOfNumericAtts', 'Quartile2StdDevOfNumericAtts', 'Quartile3StdDevOfNumericAtts', 'Quartile1KurtosisOfNumericAtts', 'Quartile2KurtosisOfNumericAtts', 'Quartile3KurtosisOfNumericAtts', 'Quartile1SkewnessOfNumericAtts', 'Quartile2SkewnessOfNumericAtts', 'Quartile3SkewnessOfNumericAtts', 'NumberOfSymbolicFeatures', 'NumberOfBinaryFeatures', 'PercentageOfSymbolicFeatures', 'PercentageOfBinaryFeatures', 'MinAttributeEntropy', 'MeanAttributeEntropy', 'MaxAttributeEntropy', 'Quartile1AttributeEntropy', 'Quartile2AttributeEntropy', 'Quartile3AttributeEntropy', 'MinMutualInformation', 'MeanMutualInformation', 'MaxMutualInformation', 'Quartile1MutualInformation', 'Quartile2MutualInformation', 'Quartile3MutualInformation', 'EquivalentNumberOfAtts', 'MeanNoiseToSignalRatio', 'MinNominalAttDistinctValues', 'MeanNominalAttDistinctValues', 'MaxNominalAttDistinctValues', 'StdvNominalAttDistinctValues', 'NumberOfInstances', 'NumberOfFeatures', 'Dimensionality', 'NumberOfMissingValues', 'PercentageOfMissingValues', 'NumberOfInstancesWithMissingValues', 'PercentageOfInstancesWithMissingValues', 'NumberOfClasses', 'ClassEntropy', 'MinorityClassSize', 'MajorityClassSize', 'MinorityClassPercentage', 'MajorityClassPercentage']]
abello_with_ids_abello_metafeatures.to_csv("csv/abello/abello_with_ids_abello_metafeatures.csv")