import pandas as pd

races_csv = "../data/races.csv"
pit_stops_csv = "../data/pit_stops.csv"

races_df = pd.read_csv(
    filepath_or_buffer=races_csv,
    header=0,
    usecols=["raceId"]
)

pit_stops_df = pd.read_csv(
    filepath_or_buffer=pit_stops_csv,
    header=0,
    usecols=["raceId", "milliseconds"]
)

races_w_pit_stops_df = pd.merge(
    left=races_df,
    right=pit_stops_df,
    left_on="raceId",
    right_on="raceId",
    how="left"
)

avg_pit_stop_times_df = races_w_pit_stops_df.groupby("raceId").mean().reset_index()

races_info_df = pd.read_csv(
    filepath_or_buffer=races_csv,
    header=0,
    usecols=["raceId", "year", "name"]
)

final_avg_pit_stop_df = pd.merge(
    left=avg_pit_stop_times_df,
    right=races_info_df,
    left_on="raceId",
    right_on="raceId",
)

final_avg_pit_stop_df = final_avg_pit_stop_df[["raceId", "year", "name", "milliseconds"]]
final_avg_pit_stop_df.rename(columns={"raceId": "Race ID",
                                      "milliseconds": "Avg pit stop time (ms)",
                                      "year": "Year",
                                      "name": "Race Name"},
                             inplace=True)

final_avg_pit_stop_df.to_csv(
    path_or_buf="../output/avg_pit_stops_clean.csv",
    index=False,
    na_rep="\\N"
)