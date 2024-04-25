import pandas as pd

# Original Dataset
df = pd.read_csv('cohort_statistics-virginia-schools.csv')

df.loc[df["Graduation Rate"] == "<", "Graduation Rate"] = 0
df.loc[df["Students in Cohort"] == "<", "Students in Cohort"] = 0
df.loc[df["Total Graduates"] == "<", "Total Graduates"] = 0
df.loc[df["Advanced Studies"] == "<", "Advanced Studies"] = 0
df.loc[df["IB"] == "<", "IB"] = 0
df.loc[df["Standard"] == "<", "Standard"] = 0
df.loc[df["Other Diplomas"] == "<", "Other Diplomas"] = 0
df.loc[df["Applied Studies"] == "<", "Applied Studies"] = 0
df.loc[df["GED"] == "<", "GED"] = 0
df.loc[df["ISAEP"] == "<", "ISAEP"] = 0
df.loc[df["Certificate of Completion"] == "<", "Certificate of Completion"] = 0
df.loc[df["Completion Rate"] == "<", "Completion Rate"] = 0
df.loc[df["Dropout Rate"] == "<", "Dropout Rate"] = 0
df.loc[df["Dropouts"] == "<", "Dropouts"] = 0
df.loc[df["Still Enrolled"] == "<", "Still Enrolled"] = 0
df.loc[df["Long-Term Absence"] == "<", "Long-Term Absence"] = 0

df.to_csv('cohort_statistics_virginia_schools.csv')
