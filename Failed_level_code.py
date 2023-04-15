import pandas as pd
import matplotlib.pyplot as plt

# Load the players.csv dataset into a pandas DataFrame
players_df = pd.read_csv('players.csv')

# Load the level_progress.csv dataset into another pandas DataFrame
level_progress_df = pd.read_csv('level_progress.csv')

# Merge the two datasets based on the player_id column
merged_df = pd.merge(players_df, level_progress_df, on='player_id')

# Add a new column indicating whether the player failed the level or not
merged_df['failed_level'] = (merged_df['status'] == 'fail')

# Group the data by whether the player failed the level or not, and calculate the proportion of players who churned in each group
grouped_df = merged_df.groupby('failed_level')['player_id'].nunique()
total_players = grouped_df.sum()
grouped_df = grouped_df / total_players * 100

# Visualize the results using a bar chart
grouped_df.plot(kind='bar')
plt.xlabel('Failed Level')
plt.ylabel('Churn Rate (%)')
plt.xticks([0, 1], ['No', 'Yes'], rotation=0)
plt.show()
