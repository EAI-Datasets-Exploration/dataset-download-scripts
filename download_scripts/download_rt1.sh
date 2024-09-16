#!/bin/bash


PYTHON_PKG_LOC=`dirname \`pwd\``
DS_DOWNLOAD_DIR=${PYTHON_PKG_LOC%%/}/downloaded_datasets/

echo "This download assumes you are running the script from download_scripts. Please cancel if not."
echo "WARNING: This dataset is 111.1 GB."
echo "This will download to $DS_DOWNLOAD_DIR "

sleep 30

echo "Now beginning download..."

gsutil -m cp -r gs://gresearch/robotics/fractal20220817_data $DS_DOWNLOAD_DIR
