# dataset-download-scripts

contact: agnes.luhtaru@ut.ee or slwanna@utexas.edu

## Available Datasets

| Dataset           |      Status |
| :---------------- |   --------: |
| ALFRED            |    Complete |
| SCOUT             |    Complete |
| RT-1              |    Complete |
| Bridge            |    Complete |
| Tacoplay          |    Complete |

## Download Datasets

**WARNING: PLEASE PAY ATTENTION TO HOW LARGE THE DATASET YOU ARE DOWNLOADING IS. THIS IS COMMENTED IN THE SHELL SCRIPT**

Please follow these EXACT instructions:
- ```$ cd download_scripts``` 
- ```$ sh script_you_want.sh```

The data should be downloaded to the ```downloaded_datasets``` folder.

**WARNING: PLEASE PAY ATTENTION TO HOW LARGE THE DATASET YOU ARE DOWNLOADING IS. THIS IS COMMENTED IN THE SHELL SCRIPT**

## Parse out NL Commands in Datasets

These instructions tell you how to extract, from the downloaded robotics datasets, their natural language(NL)commands.
The resulting language-only *.csv should be saved to ```dataset-download-scripts/language_only_datasets```. 

However, I also use git-lfs to save out the NL commands *.csv files and then tar them using ```tar -cvf file_name.csv```. To use these datasets,
use ```tar -xvf file_name.tar``` to convert the file back into a *.csv file.

### General Setup Instructions

- ```$ conda env create -f environment.yml```
- ```$ conda activate conda activate hri-ds-download```

### RT-X Datasets

- ```$ cd extract_nl_commands```
- ```$ python rtx_datasets.py --ds_path PATH_TO/dataset-download-scripts/downloaded_datasets/dummy_ds_folder/0.1.0```

### Other Datasets

#### ALFRED

- ```$ cd extract_nl_commands```
- ```$ python alfred_dataset.py --ds_path PATH_TO/dataset-download-scripts/downloaded_datasets/alfred --level both```

#### ARL-SCOUT

- ```$ cd extract_nl_commands```
- ```$ python arl_scout_dataset.py --ds_path PATH_TO/dataset-download-scripts/downloaded_datasets/ARL-SCOUT```