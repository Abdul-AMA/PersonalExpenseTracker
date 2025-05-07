import json
from datetime import datetime
import matplotlib.pyplot as plt


class ExpenseTracker:

    def __init__(self):
        self.income = 0.0
        self.expenses = []
        self.savings = 0.0

    def load_data(self):
        try:
            with open('transactions_data.json', 'r') as file:
                data = json.load(file)
                self.income = data.get('income', 0.0)
                self.expenses = data.get('expenses', [])
                self.savings = data.get('savings', 0.0)
        except FileNotFoundError:
            print("No existing data found. Starting fresh.")

    def save_data(self):
        data = {
            'income': self.income,
            'expenses': self.expenses,
            'savings': self.savings
        }
        with open('transactions_data.json', 'w') as file:
            json.dump(data, file, indent=4)

    def add_income(self, income):
        if income <= 0:
            raise ValueError("Income must be positive.")
        self.income += income
        self.calculate_savings()
        return self.income

    def add_expense(self, amount, category, description):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        expense = {
            'description': description,
            'amount': amount,
            'category': category,
            'date': datetime.now().strftime("%Y-%m-%d")
        }
        self.expenses.append(expense)
        self.calculate_savings()

    def calculate_savings(self):
        self.savings = self.income - sum(expense['amount'] for expense in self.expenses)
        print(f'You have {self.savings} savings.')
        return self.savings


    def get_expense_category(self):
        return  sorted(set(expense['category'] for expense in self.expenses))


    def generate_expense_report_category(self, category=None):
        if category and category not in self.get_expense_category():
            print(f"Warning: Category '{category}' not found!")
            return {
                'category': category,
                'total_amount': 0.0,
                'expenses': []
            }
        if category:
            expenses = [exp for exp in self.expenses if exp['category'] == category]
        else:
            expenses = self.expenses

        total = sum(exp['amount'] for exp in expenses)
        return {
            'category': category or 'All',
            'total_amount': total,
            'expenses': expenses  #
        }

    def generate_expense_chart(self, chart_type='pie'):
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            category_totals[category] = category_totals.get(category, 0) + expense['amount']

        # Prepare data for plotting
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        # Create the chart
        plt.figure(figsize=(8, 6))

        if chart_type == 'pie':
            plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
            plt.title('Expense Distribution by Category (Pie Chart)')
        elif chart_type == 'bar':
            plt.bar(categories, amounts)
            plt.title('Expense Distribution by Category (Bar Chart)')
            plt.ylabel('Amount ($)')
            plt.xticks(rotation=45)
        else:
            raise ValueError("Invalid chart type. Use 'pie' or 'bar'.")

        plt.tight_layout()
        plt.show()



tracker =  ExpenseTracker()

# Load any previous data (optional)
tracker.load_data()

# Add income
# tracker.add_income(1500)

# Add expenses
tracker.add_expense(200, 'Food', 'Groceries')
tracker.add_expense(100, 'Transport', 'Bus pass')
tracker.add_expense(50, 'Entertainment', 'Movies')
tracker.add_expense(35, 'Food', 'veges')
tracker.add_expense(500, 'Entertainment', 'new gaming console')
tracker.add_expense(1200, 'education', 'uni fees')
tracker.add_expense(1500, 'house', 'home rent')


# Generate report
report = tracker.generate_expense_report_category()
print(f"\nExpense Report:"
      f"\nCategory: {report['category']}"
      f"\nTotal Spent: ${report['total_amount']:.2f}"
      f"\nBalance: {tracker.savings}"
      )

# Draw a chart (change to 'bar' if you want)
tracker.generate_expense_chart(chart_type='pie')

# Save data
tracker.save_data()
