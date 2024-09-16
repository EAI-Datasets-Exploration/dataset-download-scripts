#!/bin/bash


PYTHON_PKG_LOC=`dirname \`pwd\``
DS_DOWNLOAD_DIR=${PYTHON_PKG_LOC%%/}/downloaded_datasets

echo "This download assumes you are running the script from download_scripts. Please cancel if not."
echo "WARNING: This dataset is around 1.5GB"
echo "The download also assumes you have 7z installed and asks to install if not."
echo "This will download to $DS_DOWNLOAD_DIR"

sleep 30

echo "Now beginning download..."

# If repositoty needed as well
# git clone https://github.com/askforalfred/alfred.git $DS_DOWNLOAD_DIR/alfred

mkdir -p $DS_DOWNLOAD_DIR/alfred
cd $DS_DOWNLOAD_DIR/alfred

# Logic from the download script: https://github.com/askforalfred/alfred/blob/master/data/download_data.sh

wget https://ai2-vision-alfred.s3-us-west-2.amazonaws.com/json_2.1.0.7z
7z x json_2.1.0.7z -y && rm json_2.1.0.7z
mv json_2.1.0/* .
rmdir json_2.1.0
