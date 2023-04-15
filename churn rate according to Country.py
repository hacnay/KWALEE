import pandas as pd
import matplotlib.pyplot as plt

# Read in the players and level progress data
players = pd.read_csv('players.csv')
level_progress = pd.read_csv('level_progress.csv')

# Merge the data on player_id
merged_data = pd.merge(players, level_progress, on='player_id')

# Calculate the churn rate by country
country_churn = merged_data.groupby('country').apply(lambda x: sum(x.status == 'fail') / len(x)).reset_index(name='churn_rate')

# Plot the churn rate by country as a bar graph
plt.figure(figsize=(12, 6))
plt.bar(country_churn['country'], country_churn['churn_rate'])
plt.xlabel('Country')
plt.ylabel('Churn Rate')
plt.title('Churn Rate by Country')
plt.show()
