# Week 05 - Object Oriented Programming: Encapsulation & Data Validation

## Student Information
- **Name:** Faiaz ul Islam
- **Student ID:** 252-35-597
- **Section:** 45-H2
- **Course:** SE 217 - Object Oriented Programming Lab
- **Semester:** Fall 2026

---

## Scenario
This module demonstrates the OOP principle of **Encapsulation** and defensive programming via **Data Validation**. Restricting direct field access using private modifiers ensures that an object's internal state remains valid according to domain rules.

---

## File Overview

| File | Type | Description |
|:---|:---|:---|
| [`Student.java`](./Student.java) | Entity Class | Encapsulates student data (`studentId`, `name`, `marks`) with private visibility, explicit public getters/setters, and range validation (`0 <= marks <= 100`). |
| [`StudentDemo.java`](./StudentDemo.java) | Driver Class | Demonstrates object instantiation, valid attribute access, defensive invalid input handling, and object state printing. |

---

## Technical Specifications

### `Student` Class
- **Private Fields:**
  - `private int studentId`: Unique identification number.
  - `private String name`: Student full name.
  - `private double marks`: Academic score.
- **Constructor:**
  - `Student(int studentId, String name, double marks)`: Initializes attributes and routes initial marks through `setMarks(marks)` to ensure validation even at instantiation time.
- **Encapsulated Accessors & Mutators:**
  - `getStudentId()`, `setStudentId(int id)`
  - `getName()`, `setName(String name)`
  - `getMarks()`, `setMarks(double marks)`: Validates that `marks >= 0 && marks <= 100`. Prints an error message if marks are out of bounds.
- **Display Method:**
  - `displayInfo()`: Prints formatted student record.

---

## How to Compile & Run

Open terminal in this directory:
```bash
# Compile both Java source files
javac Student.java StudentDemo.java

# Run demo
java StudentDemo
```

---

## Expected Output
```text
Student ID: 597
Name: Faiaz ul Islam
Marks: 88.5

--- Testing Validation ---
Invalid marks! Marks must be between 0 and 100.
Updated Marks: 95.0
```

---

## Viva & Code Explanation Points
1. **Encapsulation Principle:**
   Fields are declared `private` to prevent external code from directly modifying data without validation (e.g., preventing `s.marks = -25` or `s.marks = 150`).
2. **Defensive Invariant Checking:**
   The mutator `setMarks()` acts as a gatekeeper, verifying that incoming values conform to business constraints before committing changes to internal state.
