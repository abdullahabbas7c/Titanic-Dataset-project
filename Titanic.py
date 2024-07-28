import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.read_csv('C:/Users/ASUS/Desktop/Python Course 2024/Assignments/titanic/train.csv')

print("Options:")
print("1-Show Data set")
print("2-Heat Map")
print("3-Casualties Graph")
print("4-Class Distribution Chart")
print("5-Age Distribution Graph")
print("6-Wealth Distribution Graph")
print("7-Boarding Station Distribution Graph")
print("8-Comparisons",end="\n\n")

co=input("Enter Choice:")

pd.set_option('future.no_silent_downcasting', True)

def show_data():
    i=int(input("Enter no. of rows:"))
    print(data.head(i))
    
def heatmap():
    df=pd.DataFrame(data)
    df.drop(['PassengerId','Cabin'], axis=1, inplace=True)
    df.dropna(inplace=True)
    df["Sex"] = df['Sex'].replace({'male': 0, 'female': 1}).astype(int)
    df["Embarked"] = df['Embarked'].replace({'C': 1, 'S': 2, 'Q': 3}).astype(int)
    plt.figure(figsize=(16,8))
    numerical_df = df.select_dtypes(include=['number'])
    sns.heatmap(numerical_df.corr().abs(), annot=True)
    plt.show()

def casualties():
    survived_counts = data['Survived'].value_counts().reset_index()
    survived_counts.columns = ['Survived', 'Count']
    sns.barplot(x='Survived', y='Count', data=survived_counts)
    plt.title("Number of Survivors and Casualties")
    plt.xlabel("Survived (1) or Not Survived (0)")
    plt.ylabel("Count")
    plt.show()
    
def class_distribution():
    first_class_count=(data['Pclass']==1).sum()
    second_class_count=(data['Pclass']==2).sum()
    third_class_count=(data['Pclass']==3).sum()
    labels=["First Class","Second Class","Third Class"]
    counts=[first_class_count, second_class_count, third_class_count]
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Class Distribution")
    plt.show()

def age_distribution():
    data.hist(column='Age', bins=80)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()

def wealth_distribution():
    data.hist(column='Fare', bins=200)
    plt.title("Wealth Distribution")
    plt.xlabel("Fair paid")
    plt.ylabel("Count")
    plt.show()

def boarding_station_distribution():
    sns.countplot(x=data["Embarked"], palette="viridis", hue=data["Embarked"], legend=True)
    plt.title("Boarding Station Distribution")
    plt.xlabel("Ports")
    plt.ylabel("Count")
    plt.show()

def comparisons():
    
    print("Comparisons between:")
    print("1-Survival & Class")
    print("2-Survival & Age")
    print("3-Fare & Age")
    print("4-Survival & Gender")
    print("5-Survival & Boarding Station Count",end="\n\n")
    
    co2=input("Enter Choice:")
    
    def survial_count():
        sns.countplot(x=data["Pclass"], hue=data["Survived"])
        plt.title("Survival wrt Class")
        plt.xlabel("Classes")
        plt.ylabel("Count")
        plt.show()
    
    def survival_age():
        axs=sns.kdeplot(data.Age[data.Survived==1], fill=True, label="Survived")
        axs=sns.kdeplot(data.Age[data.Survived==0], fill=True, label="Died")
        plt.title("Survival wrt Age")
        plt.xlabel("Age")
        plt.ylabel("Normalized Count")
        plt.legend()
        plt.show()

    def fare_age():
        plt.scatter(data["Age"], data["Fare"])
        plt.title("Fare wrt Age")
        plt.xlabel("Age")
        plt.ylabel("Fare")
        plt.show()

    def survival_gender():
        m_dead=((data["Sex"]=="male") & (data["Survived"]==0)).sum()
        m_live=((data["Sex"]=="male") & (data["Survived"]==1)).sum()
        f_dead=((data["Sex"]=="female") & (data["Survived"]==0)).sum()
        f_live=((data["Sex"]=="female") & (data["Survived"]==1)).sum()
        m_data=(m_dead, m_live)
        f_data=(f_dead, f_live)
        p1=plt.bar(np.arange(2), (m_data), width=0.4)
        p2=plt.bar(np.arange(2), (f_data), bottom=(m_data), width=0.4) 
        plt.title("Men & Woman Survival rates")
        plt.xticks(np.arange(2), ["Men", "Women"])
        plt.xlabel("Gender")
        plt.ylabel("Count")
        plt.legend((p1[0], p2[0]), ("Died", "Survived"))
        plt.show()

    def survival_boarding_station_count(): 
        sns.countplot(x=data["Embarked"],hue=data["Survived"], palette="viridis")
        plt.title("Boarding Station Count Survival")
        plt.xlabel("Ports")
        plt.ylabel("Count")
        plt.show()

    if co2=="1":
        survial_count()
    elif co2=="2":
        survival_age()
    elif co2=="3":
        fare_age()
    elif co2=="4":
        survival_gender()
    elif co2=="5":
        survival_boarding_station_count()
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
    
if True:
    if co=="1":
        show_data()
    elif co=="2":
        heatmap()
    elif co=="3":
        casualties()
    elif co=="4":
        class_distribution()
    elif co=="5":
        age_distribution()
    elif co=="6":
        wealth_distribution()
    elif co=="7":
        boarding_station_distribution()
    elif co=="8":
        comparisons()
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")