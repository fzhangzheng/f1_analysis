import pandas as pd

"""
Which driver has the most wins and which driver has the most losses for each Grand Prix?
"""

drivers_csv = "../data/drivers.csv"
races_csv = "../data/races.csv"
results_csv = "../data/results.csv"

drivers_df = pd.read_csv(
    filepath_or_buffer=drivers_csv,
    header=0,
    usecols=["driverId", "forename", "surname"]
)

races_df = pd.read_csv(
    filepath_or_buffer=races_csv,
    header=0,
    usecols=["raceId", "year", "round"]
)

results_df = pd.read_csv(
    filepath_or_buffer=results_csv,
    header=0,
    usecols=["resultId", "raceId", "driverId", "position"]
)