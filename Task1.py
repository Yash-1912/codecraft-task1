import pandas as pd
import matplotlib.pyplot as plt

# Correct file path (point to CSV file)
file_path = r"G:/Task1/API_SP.POP.TOTL_DS2_en_csv_v2_34.csv"

# Load dataset (skip metadata rows)
df = pd.read_csv(file_path, skiprows=4)

# Select year 2022
df_2022 = df[["Country Name", "2022"]].dropna()

# Convert population to numeric
df_2022["2022"] = pd.to_numeric(df_2022["2022"], errors="coerce")

# Select top 10 countries by population
top10 = df_2022.sort_values(by="2022", ascending=False).head(10)

# Create bar chart
plt.figure()
plt.bar(top10["Country Name"], top10["2022"])
plt.title("Top 10 Most Populated Countries (2022)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
