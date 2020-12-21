import pandas as pd
import os.path
import glob


def find_available_csvs(data_root_folder, academic_year):
    path_to_csvs = os.path.join(data_root_folder, academic_year)
    csv_paths = glob.glob(f"{path_to_csvs}/*.csv")

    files = {}
    for csv_path in csv_paths:
        filename = csv_path.replace(f"{path_to_csvs}\\england_", "").replace(".csv", "").replace("-", "_")
        files[filename] = csv_path
    return files


#print(pd.read_csv("data//england_school_information.csv"))
if __name__ == "__main__":
    print(find_available_csvs("data", "2018-2019"))
    #print(pd.read_csv(os.path.join("data", "2018-2019", "england_school_information.csv")))