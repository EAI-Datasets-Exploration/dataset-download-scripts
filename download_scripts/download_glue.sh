#!/bin/bash

PYTHON_PKG_LOC=`dirname \`pwd\``
DS_DOWNLOAD_DIR=${PYTHON_PKG_LOC%%/}/downloaded_datasets/

echo "This download assumes you are running the script from download_scripts. Please cancel if not."
echo "WARNING: This dataset is less than 1GB"
echo "This will download to $DS_DOWNLOAD_DIR "

sleep 30

echo "Now beginning download..."

mkdir -p $DS_DOWNLOAD_DIR/alfred
cd $DS_DOWNLOAD_DIR/alfred

git clone https://github.com/nyu-mll/GLUE-baselines.git
python3 GLUE-baselines/download_glue_data.py --data_dir ${PYTHON_PKG_LOC%%/}/downloaded_datasets/glue_data --tasks all
rm -rf GLUE-baselines