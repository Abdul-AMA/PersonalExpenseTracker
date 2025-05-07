# 💸 ExpenseTracker

A simple yet powerful **personal expense tracking system** in Python that helps you **track income, categorize expenses, calculate savings**, and **visualize spending** using charts.

---

## 🚀 Features

- 🧾 **Track Income & Expenses**  
  Easily record how much you earn and spend.

- 🗂️ **Expense Categorization**  
  Organize expenses by categories

- 💰 **Real-time Savings Calculation**  
  Instantly see how much money you have left after spending.

- 📈 **Visual Reports**  
  Generate pie or bar charts to visualize your spending patterns.

- 💾 **Data Persistence**  
  All transactions are saved and loaded from a local JSON file (`transactions_data.json`).

---

## 🛠️ Requirements

Install all dependencies using:


```text
matplotlib==3.10.1
```

```bash
pip install matplotlib
```
---

## 🧪 How to Use

### 1. 🧠 Initialize Tracker

```python
from expense_tracker import ExpenseTracker

tracker = ExpenseTracker()
tracker.load_data()
```

### 2. 💵 Add Income

```python
tracker.add_income(1500)
```

### 3. 🧾 Add Expenses

```python
tracker.add_expense(200, 'Food', 'Groceries')
tracker.add_expense(100, 'Transport', 'Bus pass')
```

### 4. 📊 Generate Reports

```python
report = tracker.generate_expense_report_category()
print(report)
```

### 5. 📉 Visualize Expenses

```python
tracker.generate_expense_chart(chart_type='pie')  # or 'bar'
```

### 6. 💾 Save Your Data

```python
tracker.save_data()
```

---

## 📁 File Structure

```
expense_tracker.py     # Core class logic
main.py                # Example usage script
transactions_data.json # Auto-generated data file
requirements.txt       # Project dependencies
README.md              # You're reading it!
```

---


## 🧠 Future Ideas

- Add monthly budgeting goals
- Export reports to PDF/CSV
- Add a GUI with Tkinter or PyQt
- Secure sensitive data with encryption

---


## 🧑‍💻 Author

Made with ❤️ by **Mr.Abood** 


