# openML-datasets-profiling
OpenML stores for each dataset a set of 226 meta-features.
In this project, for computing power reasons, I analyze these meta-features only on the 2872 active datasets.

## CSV Folder Description
The csv folder contains the tables that link for each dataset (in the rows) the relative value of each meta-feature (in the column).
Specifically:
- the **abello** folder contains only tables that analyze the datasets used in the paper `T.Aluja-Banet andR.Wrembel B.Bilalli, A.Abello. Intelligentassistance for data pre-processing. Computer Standards Interfaces 57 (2018), 101 – 109, 2018.` (which are listed in this [link](http://www.essi.upc.edu/~bbilalli/datasets.html));
- the **autosklearn** folder contains only tables that analyze the datasets used in the paper `K. Eggensperger J. Springenberg M. Blum M. Feurer, A. Klein and F. Hut- ter. Efficient and Robust Automated Machine Learning. Advances in Neural Information Processing Systems 28 (NIPS 2015), 2015.`;
- the **original** folder contains the tables that analyze the all 2872 openML active datasets.

### original folder
- **original_all_metafeatures.csv** is the raw file downloaded;
- **original_with_ids_all_metafeatures.csv** adds the column ID to the previous one (it was done because then it is easier to filter the datasets);
- **original_with_ids_abello_metafeatures.csv** contains only the meta-features used in the paper `T.Aluja-Banet andR.Wrembel B.Bilalli, A.Abello. Intelligentassistance for data pre-processing. Computer Standards Interfaces 57 (2018), 101 – 109, 2018.` (plus the ID column);
- **original_with_ids_simply_metafeatures.csv** contains only the meta-features listed in this [link](http://www.essi.upc.edu/~bbilalli/datasets.html) (plus the ID column).

### abello folder
- **abello_simply_metafeatures.csv** is the raw table download by this [link](http://www.essi.upc.edu/~bbilalli/datasets.html);
- **abello_with_ids_simply_metafeatures.csv** contains only the datasets that are both in [link](http://www.essi.upc.edu/~bbilalli/datasets.html) and that are active. It also adds the column ID to the previous one;
- **abello_with_ids_all_metafeatures.csv** adds the all openML meta-features (plus the ID column).
- **abello_with_ids_abello_metafeatures.csv** contains only the meta-features used in the paper `T.Aluja-Banet andR.Wrembel B.Bilalli, A.Abello. Intelligentassistance for data pre-processing. Computer Standards Interfaces 57 (2018), 101 – 109, 2018.` (plus the ID column).

### autosklearn folder
- **autosklearn_with_ids_all_metafeatures.csv** contains only the datasets that are both in the paper `K. Eggensperger J. Springenberg M. Blum M. Feurer, A. Klein and F. Hut- ter. Efficient and Robust Automated Machine Learning. Advances in Neural Information Processing Systems 28 (NIPS 2015), 2015.` and that are active. It also contains all the openML meta-features (plus the ID column);.
- **autosklearn_with_ids_abello_metafeatures.csv** contains only the meta-features used in the paper `T.Aluja-Banet andR.Wrembel B.Bilalli, A.Abello. Intelligentassistance for data pre-processing. Computer Standards Interfaces 57 (2018), 101 – 109, 2018.` (plus the ID column);
- **autosklearn_with_ids_simply_metafeatures.csv** contains only the meta-features listed in this [link](http://www.essi.upc.edu/~bbilalli/datasets.html) (plus the ID column).

## Script Description
There are three packages:
- **preprocessing** contains the scripts that have the raw files as input and clean them;
- **projections** contains the scripts that apply projections on the columns;
- **tests** contains a simply util test.

### preprocessing package
There is a script for each csv folder:
- **original_preprocessing** cleans ``original_all_metafeatures.csv`` and generates ``original_with_ids_all_metafeatures.csv``;
- **autosklearn_preprocessing** generates ``autosklearn_with_ids_all_metafeatures.csv`` from ``original_with_ids_all_metafeatures.csv``;
- **abello_preprocessing** cleans the ``abello_simply_metafeatures.csv`` and generates ``abello_with_ids_all_metafeatures.csv``.

### projections package
There is a script for each csv folder:
- **original_projections** loads ``original_all_metafeatures.csv`` and generates ``original_with_ids_abello_metafeatures.csv`` and ``original_with_ids_simply_metafeatures.csv``;
- **autosklearn_projections** loads ``autosklearn_with_ids_all_metafeatures.csv`` and generates ``autosklearn_with_ids_abello_metafeatures.csv`` and ``autosklearn_with_ids_simply_metafeatures.csv``;
- **abello_projections** loads ``abello_with_ids_all_metafeatures.csv``and generates ``abello_with_ids_abello_metafeatures.csv`` and ``autosklearn_with_ids_simply_metafeatures.csv``.

### tests package
The only script contained, **check_abello_active**, checks if the abello datasets are all contained in the original openML datasets; therefore it checks if the abello datasets are all active on openML.
