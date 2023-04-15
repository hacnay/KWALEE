Game App Churn Analysis
This project analyzes the churn rate for a game app by merging data from two CSV files, players.csv and level_progress.csv, and computing the proportion of players who stop playing the game without completing all levels.

Files
This project contains the following Python files:

Failed_level_code.py: analyzes the churn rate for players who failed a level
Level_progress.py: analyzes the churn rate for players who did not complete the game
plot churn rate by screen size.py: analyzes the churn rate by screen size
plot churn rate by Platform.py: analyzes the churn rate by platform
churn rate according to Country.py: analyzes the churn rate by country
Each Python file can be run separately using the command python <filename.py>.

The project also includes two CSV files:

players.csv: contains data on the characteristics of the players
level_progress.csv: contains data on player progress through the levels
Dependencies
The project requires the following Python libraries:

pandas
matplotlib
You can install these libraries using the command pip install <library>.

Running the code
To run the code, follow these steps:

Download or clone the project files to your local machine.
Install the required libraries using pip install pandas matplotlib.
Open a command prompt or terminal and navigate to the project directory.
Run one of the Python files using the command python <filename.py>. The output will be displayed in the console and a plot will be saved to the plots folder.
Note that some of the Python files may take longer to run depending on the size of the input data.

Output
The Python files will output the churn rate for the specified category (e.g. failed level, platform, country). They will also save a bar plot of the churn rate to the plots folder with a filename that reflects the category analyzed.

Conclusion
This project provides insights into the churn rate for a game app and identifies potential factors that may contribute to churn. The findings can be used to inform strategies to retain players and increase engagement.