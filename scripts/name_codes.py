import pandas as pd

def getDriverCode(surname: str):
    return surname.replace(" ", "")[:3].upper()

drivers_csv = "../data/drivers.csv"

drivers_df = pd.read_csv(
    filepath_or_buffer=drivers_csv,
    header=0
)

temp_df = drivers_df[drivers_df['code'] == "\\N"]

temp_df["code"] = temp_df.apply(
    lambda row: getDriverCode(row["surname"]),
    axis=1
)

final_name_codes_df = pd.merge(
    left=temp_df,
    right=drivers_df,
    left_on="driverId",
    right_on="driverId",
    how="left"
)

final_name_codes_df.to_csv(
    path_or_buf="../output/final_name_codes.csv",
    index=False,
    na_rep="\\N"
)


