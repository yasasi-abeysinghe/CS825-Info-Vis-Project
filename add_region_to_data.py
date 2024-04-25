import os
import pandas as pd
from datetime import datetime


def search_city_in_files(row):
    directory_path = "data/region_data/"
    city_name = row["Division Name"].rsplit(' ', 1)[0]
    city_name = city_name.lower()  # Convert input to lowercase for case-insensitive search
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                if city_name in file.read().lower():
                    return filename
    return None


def update_date(row):
    s = row["Date"]
    d = datetime.strptime(s, '%b %Y')
    return str(d.strftime('%Y-%m'))


df = pd.read_csv("cohort_statistics_virginia_schools.csv")
df["Demographic Region"] = df.apply(search_city_in_files, axis=1)
df.to_csv("cohort_stats_virginia_schools.csv", index=False)
