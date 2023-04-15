import pandas as pd
import matplotlib.pyplot as plt

# load player data
players = pd.read_csv('players.csv')

# load level progress data
level_progress = pd.read_csv('level_progress.csv')

# merge data on player_id
merged_data = pd.merge(players, level_progress, on='player_id')

# extract screen size in inches
merged_data['screen_size_inches'] = merged_data['screen_size'].apply(lambda x: round(x / 25.4, 1))

# calculate churn rate by screen size
churn_data = merged_data.groupby('screen_size_inches') \
    .apply(lambda x: ((x['status'] == 'fail').sum() + (x['status'] == 'not_completed').sum()) / x['player_id'].nunique()) \
    .reset_index(name='churn_rate')

# plot churn rate by screen size
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(churn_data['screen_size_inches'], churn_data['churn_rate'], width=0.2)
ax.set_xlabel('Screen Size (inches)')
ax.set_ylabel('Churn Rate')
ax.set_title('Churn Rate by Screen Size')
plt.show()
