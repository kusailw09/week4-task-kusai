import pandas as pd
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, roll, scores):
        self.name = name
        self.roll = roll
        self.scores = scores

    def to_dict(self):
        return {"Name": self.name, "Roll": self.roll, **self.scores}

FILE = "students.csv"

def load_data():
    try: return pd.read_csv(FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name","Roll","Math","Science","English"])

def save_data(df): df.to_csv(FILE, index=False)

def analyze(df):
    if df.empty: 
        print("No data available!"); return
    df["Average"] = df[["Math","Science","English"]].mean(axis=1)
    df["Pass/Fail"] = df["Average"].apply(lambda x: "Pass" if x>=40 else "Fail")
    print("\nOverall:\n", df[["Name","Roll","Average","Pass/Fail"]])
    print("\nTop Performers:\n", df.nlargest(3,"Average")[["Name","Average"]])
    df[["Math","Science","English"]].mean().plot(kind="bar",title="Avg by Subject"); plt.show()
    df["Average"].plot(kind="hist",bins=5,title="Histogram of Averages"); plt.show()

df = load_data()

while True:
    print("\n1.Add Student  2.Analyze  3.Exit")
    ch = input("Choice: ")
    if ch=="1":
        name=input("Name: "); roll=input("Roll: ")
        scores={"Math":int(input("Math: ")), "Science":int(input("Science: ")), "English":int(input("English: "))}
        df = df.append(Student(name,roll,scores).to_dict(), ignore_index=True)
        save_data(df); print("Student Added!")
    elif ch=="2": analyze(df)
    elif ch=="3": break
    else: print("Invalid!")