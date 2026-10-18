# Week 04 - Performance Task: Result Manager

## Student Information
- **Name:** Faiaz ul Islam
- **Student ID:** 252-35-597
- **Section:** 45-H2
- **Course:** SE 217 - Object Oriented Programming Lab
- **Semester:** Fall 2026

---

## Scenario
A class instructor requires a console application to manage examination records for 5 students. The program accepts interactive input for student IDs, names, and marks, displays all records, identifies the highest-scoring student, computes the overall class average, and identifies students performing above average.

---

## File Overview

| File | Type | Description |
|:---|:---|:---|
| [`week4_597.java`](./week4_597.java) | Main Program File | Contains `Student` class and `week4_597` executable class, matching the required `Week4_YourID` naming standard. |

---

## Program Structure & Design

### `Student` Class
- **Fields:**
  - `int id`: Student identification number.
  - `String name`: Student name.
  - `double marks`: Examination marks scored.
- **Methods:**
  - `void display()`: Prints student details in the format:
    `ID: <id>, Name: <name>, Marks: <marks>`

### `week4_597` Execution Workflow
1. **Array Allocation:** `Student[] students = new Student[5];` allocates an array of 5 reference pointers (initialized to `null`).
2. **Object Creation Loop:** A `for` loop instantiates 5 concrete `Student` objects using `students[i] = new Student();`.
3. **Input Reading Loop:** Prompts the user sequentially for ID, Name, and Marks via `Scanner`.
   - *Buffer Clearing:* Calls `scanner.nextLine()` immediately following `scanner.nextInt()` to flush the residual newline (`\n`) character before reading the string name.
4. **Display Records:** Iterates through the array calling `s.display()` for each student.
5. **Top Scorer Algorithm:** Initializes `topStudent = students[0]` and iteratively updates whenever `s.marks > topStudent.marks`.
6. **Class Average:** Computes `totalMarks / students.length`.
7. **Optional Extension:**
   - Finds and displays the lowest-scoring student (`lowestStudent`).
   - Counts and prints how many students scored higher than the class average.

---

## How to Compile & Run

Open terminal in this directory:
```bash
# Compile
javac week4_597.java

# Run interactively
java week4_597
```

---

## Sample Run

### Input
```text
Enter information for Student 1
ID: 101
Name: Nila
Marks: 78.5

Enter information for Student 2
ID: 102
Name: Rafi
Marks: 85

Enter information for Student 3
ID: 103
Name: Mim
Marks: 92.5

Enter information for Student 4
ID: 104
Name: Tanvir
Marks: 64

Enter information for Student 5
ID: 105
Name: Sadia
Marks: 81
```

### Output
```text
===== Student Information =====
ID: 101, Name: Nila, Marks: 78.5
ID: 102, Name: Rafi, Marks: 85.0
ID: 103, Name: Mim, Marks: 92.5
ID: 104, Name: Tanvir, Marks: 64.0
ID: 105, Name: Sadia, Marks: 81.0

===== Top Student =====
ID: 103, Name: Mim, Marks: 92.5

Average Marks: 80.2

===== Lowest Student (Optional) =====
ID: 104, Name: Tanvir, Marks: 64.0
Students above average: 3
```

---

## Viva & Code Explanation Points
1. **Array of Objects vs Array of Primitives:**
   `new Student[5]` only allocates 5 memory references initialized to `null`. Without executing `students[i] = new Student()`, accessing any field causes a `NullPointerException`.
2. **Handling Scanner Newline (`\n`):**
   `nextInt()` and `nextDouble()` parse numeric tokens from standard input without consuming the trailing newline generated when pressing Enter. Calling `scanner.nextLine()` consumes that leftover newline so the subsequent name prompt doesn't capture an empty string.
3. **Linear Search for Extreme Values:**
   The algorithm sets `topStudent = students[0]` and inspects every element in $O(n)$ time.
