import pandas as pd
import matplotlib.pyplot as plt

# load player data
players = pd.read_csv('players.csv')

# load level progress data
level_progress = pd.read_csv('level_progress.csv')

# merge data on player_id
merged_data = pd.merge(players, level_progress, on='player_id')

# calculate churn rate by platform
churn_data = merged_data.groupby('platform') \
    .apply(lambda x: ((x['status'] == 'fail').sum() + (x['status'] == 'not_completed').sum()) / x['player_id'].nunique()) \
    .reset_index(name='churn_rate')

# plot churn rate by platform
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(churn_data['platform'], churn_data['churn_rate'])
ax.set_xlabel('Platform')
ax.set_ylabel('Churn Rate')
ax.set_title('Churn Rate by Platform')
plt.show()
