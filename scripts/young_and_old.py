import pandas as pd

drivers_csv = "../data/drivers.csv"
races_csv = "../data/races.csv"
results_csv = "../data/results.csv"

season_to_analyze = 2016

drivers_df = pd.read_csv(
    filepath_or_buffer=drivers_csv,
    header=0,
    usecols=["driverId", "forename", "surname", "dob"]
)

races_df = pd.read_csv(
    filepath_or_buffer=races_csv,
    header=0,
    usecols=["raceId", "year", "round"]
)

results_df = pd.read_csv(
    filepath_or_buffer=results_csv,
    header=0,
    usecols=["resultId", "raceId", "driverId"]
)


temp_df = races_df[races_df["year"] == season_to_analyze]
last_round = temp_df["round"].max()

first_and_last_race_df = temp_df[temp_df["round"].isin([1, last_round])]

race_season_results_df = pd.merge(
    left=first_and_last_race_df,
    right=results_df,
    left_on="raceId",
    right_on="raceId"
)

race_season_results_w_driver_df = pd.merge(
    left=race_season_results_df,
    right=drivers_df,
    left_on="driverId",
    right_on="driverId"
)

race_season_results_w_driver_df["dob"] = pd.to_datetime(race_season_results_w_driver_df["dob"])

oldest_driver_df = race_season_results_w_driver_df.loc[race_season_results_w_driver_df.groupby("round")["dob"].idxmin()]
youngest_driver_df = race_season_results_w_driver_df.loc[race_season_results_w_driver_df.groupby("round")["dob"].idxmax()]

oldest_youngest_df = oldest_driver_df.append(youngest_driver_df)

oldest_youngest_df.to_csv(
    path_or_buf="../output/oldest_youngest.csv",
    index=False,
    na_rep="\\N"
)


