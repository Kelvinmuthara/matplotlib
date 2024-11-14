import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for better-looking plots
plt.style.use('seaborn')

def load_and_explore_data():
    """
    Load and perform initial exploration of the dataset.
    Using the Titanic dataset as an example - you can replace with your dataset
    """
    # Load the dataset
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    
    # Display basic information about the dataset
    print("\nDataset Info:")
    print("-------------")
    print(df.info())
    
    print("\nFirst few rows:")
    print("--------------")
    print(df.head())
    
    print("\nBasic statistics:")
    print("----------------")
    print(df.describe())
    
    return df

def analyze_data(df):
    """
    Perform basic analysis on the dataset
    """
    # Calculate survival rate
    survival_rate = df['Survived'].mean() * 100
    print(f"\nOverall survival rate: {survival_rate:.2f}%")
    
    # Analyze survival by passenger class
    class_survival = df.groupby('Pclass')['Survived'].mean() * 100
    print("\nSurvival rate by passenger class:")
    print("--------------------------------")
    print(class_survival)
    
    # Analyze survival by gender
    gender_survival = df.groupby('Sex')['Survived'].mean() * 100
    print("\nSurvival rate by gender:")
    print("-----------------------")
    print(gender_survival)
    
    return class_survival, gender_survival

def create_visualizations(df, class_survival, gender_survival):
    """
    Create various visualizations to better understand the data
    """
    # Create a figure with multiple subplots
    plt.figure(figsize=(15, 10))
    
    # 1. Age distribution
    plt.subplot(2, 2, 1)
    sns.histplot(data=df, x='Age', bins=30)
    plt.title('Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Count')
    
    # 2. Survival by passenger class
    plt.subplot(2, 2, 2)
    class_survival.plot(kind='bar')
    plt.title('Survival Rate by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Survival Rate (%)')
    
    # 3. Survival by gender
    plt.subplot(2, 2, 3)
    gender_survival.plot(kind='bar')
    plt.title('Survival Rate by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Survival Rate (%)')
    
    # 4. Fare distribution by passenger class
    plt.subplot(2, 2, 4)
    sns.boxplot(data=df, x='Pclass', y='Fare')
    plt.title('Fare Distribution by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Fare')
    
    # Adjust layout and display plots
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the analysis
    """
    print("Starting Titanic Dataset Analysis")
    print("================================")
    
    # Load and explore data
    df = load_and_explore_data()
    
    # Perform analysis
    class_survival, gender_survival = analyze_data(df)
    
    # Create visualizations
    create_visualizations(df, class_survival, gender_survival)
    
    print("\nAnalysis Summary:")
    print("----------------")
    print("1. The dataset contains information about Titanic passengers including")
    print("   age, sex, passenger class, fare, and survival status.")
    print("2. Higher class passengers had better survival rates.")
    print("3. Women had significantly higher survival rates than men.")
    print("4. Ticket fares varied considerably by passenger class.")

if __name__ == "__main__":
    main()
