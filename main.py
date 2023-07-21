import os
import pandas as pd

data_directory = "./input"

df = []
for file in os.listdir(data_directory):
    if file.endswith(".xlsx"):
        print("Loading Excel file {0}...".format(file))
        df.append(
            pd.read_excel(os.path.join(data_directory, file), sheet_name="RawData")
        )
    if file.endswith(".csv"):
        print("Loading CSV file {0}...".format(file))
        df.append(
            pd.read_csv(os.path.join(data_directory, file), sep=",")
        )
df_master = pd.concat(df, axis=0)
if os.path.isdir("./output"):
    output_directory = "./output"
else:
    os.mkdir("./output")
    output_directory = "./output"
df_master.to_excel(os.path.join(output_directory, "combined.xlsx"))
