# Final Project: Bar Tab & Order Tracker

Build a Command Line Interface (CLI) application to manage customer tabs and orders at a bar or restaurant.

---

## Requirements

### 1. Data Models
Create a `Tab` class to represent a single table or customer's bar tab:
- **Attributes**:
  - `table_name` (string)
  - `orders` (dictionary where keys are items and values are dictionary of quantity and price: `{item: {"quantity": int, "price": float}}`)
  - `tax_rate` (float, default to `0.10` or 10%)
  - `service_charge` (float, default to `0.05` or 5%)
- **Methods**:
  - `add_item(item, price, quantity=1)`: Adds items to the tab. If the item already exists, increment the quantity.
  - `calculate_subtotal()`: Returns sum of item prices * quantity.
  - `calculate_tax()`: Returns subtotal * tax_rate.
  - `calculate_service_charge()`: Returns subtotal * service_charge.
  - `calculate_total()`: Returns subtotal + tax + service_charge.
  - `print_bill()`: Returns a formatted string representing the bill receipt.

### 2. File Persistence
- When a bill is printed or when the user exits, save the tab information as a JSON file in a `tabs/` folder so it can be reloaded later.
- Create a function to load existing tabs from JSON files.

### 3. User Interface (CLI Menu)
Create an interactive CLI loop:
- Option 1: Create a new tab.
- Option 2: Add items to an existing tab.
- Option 3: View current status of a tab.
- Option 4: Print/Close a tab (calculates totals, prints bill, and saves to file).
- Option 5: Exit.

### 4. Code Modularity
- Split your code into modules:
  - `tab.py`: Contains the `Tab` class.
  - `menu.py`: Main CLI script.
  - `test_tab.py`: Unit tests for the `Tab` class.

---

## Starter Code Hints

### `tab.py`
```python
class Tab:
    def __init__(self, table_name, tax=0.10, service=0.05):
        self.table_name = table_name
        self.orders = {}
        self.tax_rate = tax
        self.service_charge = service

    def add_item(self, item, price, quantity=1):
        if item in self.orders:
            self.orders[item]['quantity'] += quantity
        else:
            self.orders[item] = {'price': price, 'quantity': quantity}

    # Implement calculations and print_bill methods...
```

### `test_tab.py`
Write unit tests using `unittest` to ensure that adding items and calculating subtotals/totals works correctly.

---

## 🚀 How to Complete
1. Build `tab.py` and write the test suite in `test_tab.py`.
2. Ensure all tests pass.
3. Build the interactive CLI loop in `menu.py`.
4. Validate user inputs (e.g. handle non-integer values when entering quantity).
