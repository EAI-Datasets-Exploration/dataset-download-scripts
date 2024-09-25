"""
This file analyzes ARL-SCOUT dataset.

To download this dataset, follow the instructions in the download_scripts
folder at the top-level of this directory.
"""

import os
import json
from argparse import ArgumentParser
from pathlib import Path

import pandas as pd


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_instructions(data, level):
    instructions = []
    for annotation in data["turk_annotations"]["anns"]:
        if level in ["goal", "both"]:
            instructions.append({"nl_instructions": annotation["task_desc"]})
        if level in ["step-by-step", "both"]:
            instructions.extend(
                [{"nl_instructions": desc} for desc in annotation["high_descs"]]
            )
    return instructions


def read_json_to_df(ds_path: str, level: str) -> pd.DataFrame:
    dialogue_dir = Path(ds_path) / "train"
    data_rows = [
        instruction
        for task_dir in dialogue_dir.iterdir()
        for trial_dir in task_dir.iterdir()
        for json_file in trial_dir.glob("*.json")
        for instruction in extract_instructions(load_json(json_file), level)
    ]

    df = pd.DataFrame(data_rows)
    return df


def main(params):
    ds_path = params.ds_path
    level = params.level

    results_dir_path = "/".join(os.getcwd().split("/")[:-1]) + "/language_only_datasets/"
    ds_name = ds_path.split("/")[ds_path.split("/").index("downloaded_datasets") + 1]

    df = read_json_to_df(ds_path, level)
    df = df[df["nl_instructions"].notnull()]
    
    df.to_csv(results_dir_path + ds_name + "_" + level + "_results.csv")


if __name__ == "__main__":
    parser = ArgumentParser()
    """ 
    ds_path should be the absolute path to the folder, e.g.,
    "/home/slwanna/HRI_data_audit/downloaded_datasets/alfred" 
    """
    parser.add_argument("--ds_path", default="None", type=str, required=True)
    parser.add_argument(
        "--level",
        choices=["steps", "goal", "both"],
        default="both",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    main(args)