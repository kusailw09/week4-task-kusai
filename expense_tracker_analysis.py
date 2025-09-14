import pandas as pd
import matplotlib.pyplot as plt
import os

FILE = "expenses.csv"

# Load existing data
if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=["Type", "Category", "Amount", "Month"])

def save_data():
    df.to_csv(FILE, index=False)

def add_record(record_type):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    month = input("Enter month (e.g., Jan, Feb): ")
    global df
    df = pd.concat([df, pd.DataFrame([[record_type, category, amount, month]],
                columns=["Type", "Category", "Amount", "Month"])], ignore_index=True)

def show_summary():
    income = df[df["Type"]=="Income"]["Amount"].sum()
    expense = df[df["Type"]=="Expense"]["Amount"].sum()
    print(f"Total Income: {income}\nTotal Expense: {expense}\nBalance: {income-expense}")

def analyze_data():
    if df.empty:
        print("No data available.")
        return
    print("\nMonthly Totals:")
    print(df.groupby("Month")["Amount"].sum())
    print("\nHighest Spending Category:")
    print(df[df["Type"]=="Expense"].groupby("Category")["Amount"].sum().idxmax())

def visualize():
    if df.empty:
        print("No data available.")
        return
    # Bar chart: Category-wise expenses
    df[df["Type"]=="Expense"].groupby("Category")["Amount"].sum().plot(kind="bar", title="Category-wise Expenses")
    plt.show()
    # Line chart: Monthly trend
    df.groupby("Month")["Amount"].sum().plot(kind="line", marker="o", title="Monthly Expense Trend")
    plt.show()

def main():
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. Show Summary\n4. Analyze Data\n5. Visualize\n6. Exit")
        ch = input("Choose option: ")
        if ch=="1": add_record("Income")
        elif ch=="2": add_record("Expense")
        elif ch=="3": show_summary()
        elif ch=="4": analyze_data()
        elif ch=="5": visualize()
        elif ch=="6":
            save_data()
            break
        else: print("Invalid choice!")

if __name__=="__main__":
    main()