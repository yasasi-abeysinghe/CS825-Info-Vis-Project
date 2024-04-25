# CS825-Info-Vis-Project

Original Data Source: [Cohort Graduation and Dropout Reports](https://www.doe.virginia.gov/data-policy-funding/data-reports/statistics-reports/graduation-completion-dropout-postsecondary-data/virginia-cohort-reports-713) dataset. 

## Data
* **Region Data:** Each file in data/region_data folder represents a demographic region in the state of Virginia. Each file contains the cities and counties in the particular region.
* **Original Dataset:** data/cohort_statistics-virginia-schools.csv
* **Cleaned Dataset:** data/cohort_statistics_virginia_schools.csv
* **Data with Demographic Region:** data/cohort_stats_virginia_schools.csv

## Scripts
* data_preparation.py was used to clean the data
* add_region_to_data.py was used to add the demographic region column to the dataset.