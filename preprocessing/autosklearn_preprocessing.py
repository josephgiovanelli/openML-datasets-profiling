""" In this script I load the clean original csv and I select only the datasets used in auto-sklearn """

import pandas as pd

# Load the clean original openML csv
original_with_ids = pd.read_csv('csv/original/original_with_ids_all_metafeatures.csv', index_col='Id')

# Select only the dataset used in auto-sklearn
autosklearn_with_ids_all_metafeatures = original_with_ids.reindex([3, 6, 12, 14, 16, 18, 22, 23, 24, 26, 28, 30, 31, 32, 36, 38, 44, 46, 57, 60, 179, 180, 181, 182, 184, 185, 273, 293, 300, 351, 354, 357, 389, 390, 391, 392, 393, 395, 396, 398, 399, 401, 554, 679, 715, 718, 720, 201, 723, 727, 728, 734, 735, 737, 740, 741, 743, 751, 752, 761, 772, 797, 799, 803, 806, 807, 813, 816, 819, 821, 823, 833, 837, 843, 845, 846, 847, 849, 866, 871, 881, 897, 901, 903, 904, 910, 912, 913, 914, 917, 923, 930, 934, 953, 958, 959, 962, 966, 971, 976, 977, 978, 979, 980, 991, 993, 995, 57, 32, 16, 30, 1040, 1041, 1049, 1050, 1053, 1056, 1067, 1068, 1069, 1111, 1112, 1114, 1116, 1119, 1120, 1128, 1130, 1134, 1138, 1139, 1142, 1146, 1161, 1166])
autosklearn_with_ids_all_metafeatures.to_csv("csv/autosklearn/autosklearn_with_ids_all_metafeatures.csv")
