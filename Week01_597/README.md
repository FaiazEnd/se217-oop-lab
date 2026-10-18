# Week 01 - Performance Task: Canteen Stock Report

## Student Information
- **Name:** Faiaz ul Islam
- **Student ID:** 252-35-597
- **Section:** 45-H2
- **Course:** SE 217 - Object Oriented Programming Lab
- **Semester:** Fall 2026

---

## Scenario
The campus canteen wants a small Java program to track inventory left on the shelf. Every food item has a name, a price in Taka, and a quantity of pieces in stock. This project models a food item as a class, creates three food item objects, computes their stock values, and generates a formatted stock report.

---

## File Overview

| File | Type | Description |
|:---|:---|:---|
| [`FoodItem.java`](./FoodItem.java) | Entity Class | Models food items with attributes `name`, `price`, `quantity`, and methods `stockValue()`, `printLine()`, and `sell()`. |
| [`FoodItemDemo.java`](./FoodItemDemo.java) | Driver Class | Instantiates 3 items (Khichuri, Tea, Samosa), displays stock status, computes total inventory value, and runs test sales transactions. |

---

## Class Design

### `FoodItem`
- **Fields:**
  - `String name`: The name of the food item.
  - `int price`: Price per piece in Taka.
  - `int quantity`: Number of pieces in stock.
- **Methods:**
  - `int stockValue()`: Returns `price * quantity`.
  - `void printLine()`: Prints item details formatted as:
    `name | Tk <price> | Qty <quantity> | Value <stockValue>`
  - `void sell(int amount)` *(Optional Extension)*:
    - If `amount > quantity`: Prints `"Not enough " + name + " in stock"`
    - Otherwise: Reduces `quantity` by `amount` and prints `"Sold " + amount + " " + name"`

---

## How to Compile & Run

Open terminal in this directory:
```bash
# Compile both Java source files
javac FoodItem.java FoodItemDemo.java

# Execute the demo program
java FoodItemDemo
```

---

## Expected Output
```text
Khichuri | Tk 90 | Qty 12 | Value 1080
Tea | Tk 15 | Qty 40 | Value 600
Samosa | Tk 10 | Qty 25 | Value 250
Total stock value: Tk 1930
Sold 5 Tea
Not enough Samosa in stock
Tea | Tk 15 | Qty 35 | Value 525
```

---

## Viva & Code Explanation Points
1. **Object Instantiation:**
   `FoodItem khichuri = new FoodItem();`
   - `new FoodItem()` allocates memory on the heap for a new `FoodItem` object.
   - `khichuri` is a reference variable on the stack pointing to that heap location.
2. **Independent Object State:**
   Each object maintains its own distinct copy of instance variables (`name`, `price`, `quantity`). Modifying `tea.quantity` does not affect `samosa.quantity`.
3. **Method Delegation:**
   `printLine()` calls `stockValue()` internally to print dynamic total value without duplicating arithmetic.
