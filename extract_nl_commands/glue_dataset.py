import os
from argparse import ArgumentParser
import concurrent.futures
import pandas as pd
import tensorflow_datasets as tfds
import pandas as pd


def build_glue_dataframe(folder_path: str) -> pd.DataFrame:
    # Define the path to the GLUE datasets
    data_dir = folder_path

    # Initialize an empty list to store all data
    all_data = []

    # Mapping dataset names to the column(s) containing text
    column_mappings = {
        "CoLA": ["sentence"],
        "SST-2": ["sentence"],
        "MRPC": ["#1 String", "#2 String"],
        "QQP": ["question1", "question2"],
        "STS-B": ["sentence1", "sentence2"],
        "MNLI": ["premise", "hypothesis"],
        "QNLI": ["question", "sentence"],
        "RTE": ["sentence1", "sentence2"],
        "WNLI": ["sentence1", "sentence2"]
    }

    # Loop through each dataset folder
    for dataset, columns in column_mappings.items():
        dataset_path = os.path.join(data_dir, dataset)

        # Find the correct dataset file (usually "train.tsv")
        file_path = os.path.join(dataset_path, "train.tsv")

        if "MRPC" in dataset:
            print(dataset)
            file_path = os.path.join(dataset_path, "msr_paraphrase_train.txt")
            print(f"Because MRPC, we hot-fix to: {file_path}")

        if not os.path.exists(file_path):
            print(f"file path doesn't exist: {file_path}")
            continue

        try:
            # Read dataset with flexible parsing
            df = pd.read_csv(file_path, delimiter='\t', engine="python", on_bad_lines="skip")
            # Extract text columns and flatten into one column "nl_description"
            for col in columns:
                if col in df.columns:
                    temp_df = df[[col]].rename(columns={col: "nl_instructions"})
                    temp_df["dataset"] = dataset  # Add a dataset name column
                    all_data.append(temp_df)

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Combine all datasets into one DataFrame
    final_df = pd.concat(all_data, ignore_index=True)
    return final_df


def main(params):
    ds_path = params.ds_path

    df = build_glue_dataframe(ds_path)
    df = df[df["nl_instructions"].notnull()]

    results_dir_path = "/".join(os.getcwd().split("/")[:-1]) + "/language_only_datasets/"
    ds_name = ds_path.split("/")[ds_path.split("/").index("downloaded_datasets") + 1]

    df.to_csv(results_dir_path  + ds_name + "_nl_only.csv", index=False)

if __name__ == "__main__":
    parser = ArgumentParser()
    """ 
    ds_path should be the absolute path to the folder, e.g.,
    "/home/slwanna/code_projects/dataset-download-scripts/downloaded_datasets/glue_data" 
    """
    parser.add_argument("--ds_path", default="None", type=str, required=True)

    args = parser.parse_args()

    main(args)