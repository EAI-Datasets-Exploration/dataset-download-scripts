#!/bin/bash


PYTHON_PKG_LOC=`dirname \`pwd\``
DS_DOWNLOAD_DIR=${PYTHON_PKG_LOC%%/}/downloaded_datasets/

echo "This download assumes you are running the script from download_scripts. Please cancel if not."
echo "WARNING: This dataset is less than 1GB"
echo "This will download to $DS_DOWNLOAD_DIR "

sleep 30

echo "Now beginning download..."

git clone https://github.com/USArmyResearchLab/ARL-SCOUT.git $DS_DOWNLOAD_DIR/ARL-SCOUT