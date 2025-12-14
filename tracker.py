import json
import os
from datetime import datetime

DATA_FILE = "data.json"

# Initialize data file
def init_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "budget": 0,
            "income": [],
            "expenses": []
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def set_budget():
    data = load_data()
    budget = float(input("Enter monthly budget: ₹"))
    data["budget"] = budget
    save_data(data)
    print("✅ Budget set successfully!")

def add_income():
    data = load_data()
    amount = float(input("Enter income amount: ₹"))
    source = input("Enter income source: ")
    data["income"].append({
        "amount": amount,
        "source": source,
        "date": str(datetime.now().date())
    })
    save_data(data)
    print("✅ Income added!")

def add_expense():
    data = load_data()
    amount = float(input("Enter expense amount: ₹"))
    category = input("Enter category (Food, Rent, Travel, etc.): ")
    data["expenses"].append({
        "amount": amount,
        "category": category,
        "date": str(datetime.now().date())
    })
    save_data(data)
    print("✅ Expense added!")
    check_budget_alert()

def check_budget_alert():
    data = load_data()
    total_expenses = sum(e["amount"] for e in data["expenses"])
    budget = data["budget"]
    if budget > 0 and total_expenses > budget:
        print("⚠️ ALERT: Budget Exceeded!")
        print(f"Spent: ₹{total_expenses} / Budget: ₹{budget}")

def view_summary():
    data = load_data()
    total_income = sum(i["amount"] for i in data["income"])
    total_expenses = sum(e["amount"] for e in data["expenses"])
    savings = total_income - total_expenses

    print("\n📊 FINANCIAL SUMMARY")
    print(f"Total Income   : ₹{total_income}")
    print(f"Total Expenses : ₹{total_expenses}")
    print(f"Savings        : ₹{savings}")
    print(f"Budget Limit   : ₹{data['budget']}")

def menu():
    print("\n💰 Personal Financial Tracker")
    print("1. Set Monthly Budget")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. View Summary")
    print("5. Exit")

def main():
    init_data()
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            set_budget()
        elif choice == "2":
            add_income()
        elif choice == "3":
            add_expense()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
