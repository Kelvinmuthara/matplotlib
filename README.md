# Data Analysis Project

## Overview
This project performs exploratory data analysis on the Titanic dataset using Python. It includes data loading, basic analysis, and visualization of key patterns and relationships within the data.

## Prerequisites
Before running this project, ensure you have Python installed on your system along with the following libraries:
- pandas
- matplotlib
- seaborn

You can install the required packages using pip:
```bash
pip install pandas matplotlib seaborn
```

## Project Structure
```
data-analysis-project/
├── data_analysis.py    # Main analysis script
└── README.md          # This file
```

## Features
The script performs the following operations:

1. **Data Loading and Exploration**
   - Loads the Titanic dataset
   - Displays basic dataset information
   - Shows summary statistics

2. **Data Analysis**
   - Calculates overall survival rates
   - Analyzes survival patterns by passenger class
   - Examines survival rates by gender

3. **Data Visualization**
   - Age distribution of passengers
   - Survival rates by passenger class
   - Survival rates by gender
   - Fare distribution across passenger classes

## Usage
1. Clone or download this repository to your local machine
2. Navigate to the project directory
3. Run the script:
```bash
python data_analysis.py
```

## Output
The script will generate:
- Console output with dataset information and statistics
- Four visualizations in a single figure
- Summary of key findings

## Sample Output
```
Starting Titanic Dataset Analysis
================================

Dataset Info:
-------------
[Dataset information will be displayed here]

First few rows:
--------------
[First 5 rows of the dataset will be displayed]

Basic statistics:
----------------
[Summary statistics will be displayed]

Analysis Summary:
----------------
1. The dataset contains information about Titanic passengers including
   age, sex, passenger class, fare, and survival status.
2. Higher class passengers had better survival rates.
3. Women had significantly higher survival rates than men.
4. Ticket fares varied considerably by passenger class.
```

## Customization
To use your own dataset:
1. Open `data_analysis.py`
2. Modify the `load_and_explore_data()` function to load your dataset
3. Adjust the analysis and visualization functions as needed for your data

## Contributing
Feel free to fork this project and submit pull requests with improvements. You can also open issues for any bugs or feature requests.

## License
This project is open source and available under the MIT License.

## Author
[Your Name]

## Acknowledgments
- Dataset source: Titanic dataset from Data Science Dojo
- Thanks to the pandas, matplotlib, and seaborn development teams

## Version History
- v1.0.0 (2024-11-14): Initial release

---
*Note: This project was created as part of a data analysis assignment.*
