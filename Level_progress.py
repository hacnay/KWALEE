import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
players = pd.read_csv('players.csv')
level_progress = pd.read_csv('level_progress.csv')

# Merge the data on player_id
merged_data = pd.merge(players, level_progress, on='player_id')

# Convert screen size to inches
merged_data['screen_size_inches'] = merged_data['screen_size'] / 2.54

# Remove unnecessary columns
merged_data = merged_data.drop(columns=['install_datetime', 'system_memory'])

# Calculate churn rate based on level completion
churn_rate = merged_data.groupby(['level_number', 'status'])['player_id'].nunique().reset_index()
churn_rate = churn_rate.pivot(index='level_number', columns='status', values='player_id')
churn_rate['total_players'] = churn_rate.sum(axis=1)
churn_rate['churn_rate'] = churn_rate['complete'] / churn_rate['total_players']

# Plot churn rate by level
plt.figure(figsize=(10, 6))
sns.barplot(x=churn_rate.index, y=churn_rate['churn_rate'])
plt.title('Churn Rate by Level')
plt.xlabel('Level')
plt.ylabel('Churn Rate')
plt.show()

# Calculate churn rate based on level and stage completion
churn_rate = merged_data.groupby(['level_number', 'stage_number', 'status'])['player_id'].nunique().reset_index()
churn_rate = churn_rate.pivot_table(index=['level_number', 'stage_number'], columns='status', values='player_id')
churn_rate['total_players'] = churn_rate.sum(axis=1)
churn_rate['churn_rate'] = churn_rate['complete'] / churn_rate['total_players']

# Plot churn rate by level and stage
plt.figure(figsize=(15, 10))
sns.heatmap(churn_rate['churn_rate'].unstack(), annot=True, cmap='RdYlGn_r')
plt.title('Churn Rate by Level and Stage')
plt.xlabel('Status')
plt.ylabel('Level and Stage')
plt.show()

# Calculate churn rate for players who failed a level
failed_players = merged_data[merged_data['status'] == 'fail'].groupby('player_id').tail(1)
churn_rate = failed_players.groupby(['level_number'])['player_id'].nunique().reset_index()
churn_rate = pd.merge(churn_rate, merged_data.groupby(['level_number'])['player_id'].nunique().reset_index(),
                      on='level_number', suffixes=('_failed', '_total'))
churn_rate['churn_rate'] = churn_rate['player_id_failed'] / churn_rate['player_id_total']

# Plot churn rate for players who failed a level
plt.figure(figsize=(10, 6))
sns.barplot(x=churn_rate['level_number'], y=churn_rate['churn_rate'])
plt.title('Churn Rate for Players Who Failed a Level')
plt.xlabel('Level')
plt.ylabel('Churn Rate')
plt.show()

# Calculate churn rate based on platform, screen size, and country
churn_rate = merged_data.groupby(['platform', 'screen_size_inches', 'country', 'status'])['player_id'].nunique().reset_index()
churn_rate = churn_rate.pivot_table(index=['platform', 'screen_size_inches', 'country'], columns='status', values='player_id')
churn_rate['total_players'] = churn_rate.sum(axis=1)
churn_rate['churn_rate'] = churn_rate['complete'] / churn_rate['total_players']

# Plot churn rate by platform, screen size, and country
