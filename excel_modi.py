import os
import pandas as pd


def clean_data(filepath):
    df = pd.read_excel(filepath, usecols=[6, 8, 9, 10, 14], skiprows=12, engine="openpyxl")
    df.drop(0, inplace=True)
    df = df[df["TCode"] != "S000"]
    df = df[~df['TCode'].isnull()]
    df = df[~((df["TCode"] == "SESSION_MANAGER") & (df["Audit Log Msg. Text"].str.split(" ").str[0] != "Transaction"))]
    return df


def merge_data(result1, df):
    result1 = pd.concat([result1, df], axis=0, ignore_index=True)
    return result1


if __name__ == "__main__":
    folder_path = '/path/to/your/folder'  # Replace this with the actual path to your folder

    # Get the list of file names in the folder
    file_paths = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    result = pd.DataFrame()
    for file_path in file_paths:
        cleaned_data = clean_data(file_path)
        result = merge_data(result, cleaned_data)
    excel_file_path = 'your_file_path.xlsx'
    result.to_excel(excel_file_path, index=False)

