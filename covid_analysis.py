# Library
import pandas as pd
import matplotlib.pyplot as plt
# Read the file
df = pd.read_csv("covid_19_clean_complete.csv") #EDIT YOURSELF

# date time
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# 1. TURKEY'S DATA ANALYSİS
# -----------------------------
turkey_df = df[df['Country/Region'] == 'Turkey']

# TOTAL DATE AND CASES
plt.figure(figsize=(10,6))
plt.plot(turkey_df['Date'], turkey_df['Confirmed'], label='Confirmed Cases', color='orange')
plt.plot(turkey_df['Date'], turkey_df['Deaths'], label='Deaths', color='red')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('COVID-19 in Turkey: Confirmed Cases & Deaths')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------
# 2. GLOBAL CASE
# -----------------------------
# LAST DATE
latest_date = df['Date'].max()
latest_df = df[df['Date'] == latest_date]

# THE 5 COUNTRIES WITH THE MOST CASES
top5_confirmed = latest_df.groupby("Country/Region")["Confirmed"].sum().sort_values(ascending=False).head(5)

# THE 5 COUNTRIES WITH THE MOST CASES
plt.figure(figsize=(8,5))
top5_confirmed.plot(kind='bar', color='skyblue')
plt.title("Top 5 Countries by Confirmed Cases (Latest Date)")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Daily Turkey Cases (difference)
# -----------------------------
turkey_df_sorted = turkey_df.sort_values('Date')
turkey_df_sorted['Daily Cases'] = turkey_df_sorted['Confirmed'].diff().fillna(0)

plt.figure(figsize=(10,5))
plt.plot(turkey_df_sorted['Date'], turkey_df_sorted['Daily Cases'], label='Daily New Cases', color='green')
plt.title('Daily New COVID-19 Cases in Turkey')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
