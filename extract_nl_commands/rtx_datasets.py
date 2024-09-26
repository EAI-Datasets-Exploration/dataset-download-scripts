import os
from argparse import ArgumentParser
import concurrent.futures
import pandas as pd
import tensorflow_datasets as tfds


def main(params):
    ds_path = params.ds_path

    b = tfds.builder_from_directory(ds_path)

    # Convert dataset into a list if it's not already iterable
    ds = b.as_dataset(split="train")  # full dataset

    # Function to extract natural language instruction from an episode step
    def process_step(step):
        return step["observation"]["natural_language_instruction"].numpy().decode("UTF-8")

    # Function to process an entire episode
    def process_episode(episode):
        instructions = []
        for step in episode["steps"]:
            instructions.append(process_step(step))
        return instructions

    # Using ThreadPoolExecutor or ProcessPoolExecutor for parallelism
    all_nl_instructions = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit each episode to be processed in parallel
        futures = [executor.submit(process_episode, episode) for episode in ds]
        
        # Collect the results
        for future in concurrent.futures.as_completed(futures):
            all_nl_instructions.extend(future.result())

    df = pd.DataFrame(all_nl_instructions, columns=["nl_instructions"])
    df = df[df["nl_instructions"].notnull()]

    results_dir_path = "/".join(os.getcwd().split("/")[:-1]) + "/language_only_datasets/"
    ds_name = ds_path.split("/")[ds_path.split("/").index("downloaded_datasets") + 1]

    df.to_csv(results_dir_path  + ds_name + "_nl_only.csv", index=False)

if __name__ == "__main__":
    parser = ArgumentParser()
    """ 
    ds_path should be the absolute path to the folder, e.g.,
    "/vast/home/slwanna/HRI_data_audit/downloaded_datasets/fractal20220817_data/0.1.0" 
    """
    parser.add_argument("--ds_path", default="None", type=str, required=True)

    args = parser.parse_args()

    main(args)