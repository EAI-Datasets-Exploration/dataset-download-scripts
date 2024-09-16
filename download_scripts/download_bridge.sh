#!/bin/bash


PYTHON_PKG_LOC=`dirname \`pwd\``
DS_DOWNLOAD_DIR=${PYTHON_PKG_LOC%%/}/downloaded_datasets/

echo "This download assumes you are running the script from download_scripts. Please cancel if not."
echo "WARNING: This dataset is 387 GB."
echo "This will download to $DS_DOWNLOAD_DIR "

sleep 30

echo "Now beginning download..."

gsutil -m cp -r gs://gresearch/robotics/bridge $DS_DOWNLOAD_DIR
