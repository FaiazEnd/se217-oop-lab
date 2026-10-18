# SE 217: Object Oriented Programming Lab

## Student Information
- **Name:** Faiaz ul Islam
- **Student ID:** 252-35-597
- **Section:** 45-H2
- **Course:** SE 217 - Object Oriented Programming Lab
- **Semester:** Fall 2026

---

## Repository Description
This repository contains lab performance tasks, practice solutions, and assignments for the **SE 217: Object Oriented Programming Lab** course at Daffodil International University.

---

## Repository Structure
```text
se217-oop-lab/
|-- README.md
|-- .gitignore
|-- Week01_597/
|   |-- FoodItem.java
|   \-- FoodItemDemo.java
|-- week02/
|   |-- Week02_252-35-597.pdf
|   \-- src/
|       |-- Java01.java ... Java19.java
|-- week3/
|   |-- BusTrip.java
|   \-- BusCounter.java
|-- week4/
|   \-- week4_597.java
\-- Week05/
    |-- Student.java
    \-- StudentDemo.java
```

---

## Lab Modules & Weekly Overview

### Week 01 - Performance Task: Canteen Stock Report
- **Directory:** [`Week01_597/`](./Week01_597/)
- **Topics:** Class modeling, instance variables, methods, object instantiation, stock valuation calculation.
- **Files:**
  - [`FoodItem.java`](./Week01_597/FoodItem.java): Models food items with `name`, `price`, and `quantity`, with methods `stockValue()`, `printLine()`, and optional `sell(amount)`.
  - [`FoodItemDemo.java`](./Week01_597/FoodItemDemo.java): Driver class instantiating three items (Khichuri, Tea, Samosa), printing individual line summaries, total stock value, and handling sale transactions.

### Week 02 - Syntax & Core Fundamentals
- **Directory:** [`week02/src/`](./week02/src/)
- **Topics:** Java basic syntax, control structures, loops, arrays, String methods, Scanner input, methods, and CLI applications.
- **Submission PDF:** [`Week02_252-35-597.pdf`](./Week02_252-35-597.pdf)
- **Reference Tutorial:** [Java Basic Syntax Bangla Playlist](https://www.youtube.com/playlist?list=PLdl6zXgLsy3xCae1uL6rJ8Ay9sIiyBy5I)
- **Program Index (19 programs):**
  - Output & Variables: `Java01.java` to `Java04.java`
  - Conditionals & Control Flow: `Java05.java` to `Java07.java`
  - Operators & Loops: `Java08.java` to `Java12.java`
  - Arrays & Strings: `Java13.java` to `Java16.java`
  - Scanner Input & Methods: `Java17.java` to `Java18.java`
  - Calculator Application: `Java19.java`

### Week 03 - Performance Task: Campus Bus Booking
- **Directory:** [`week3/`](./week3/)
- **Topics:** Encapsulation, static members/methods, constructor overloading and chaining (`this(...)`), reference assignment, formatted output (`printf`).
- **Files:**
  - [`BusTrip.java`](./week3/BusTrip.java): Models university bus routes with auto-generated trip codes (`BT-201`, etc.), seat booking logic, and revenue calculation.
  - [`BusCounter.java`](./week3/BusCounter.java): Demonstrates batch bookings, reference aliasing (`busy = trips[3]`), trip search (`findByRoute`), and tracking highest vacancy.

### Week 04 - Performance Task: Result Manager
- **Directory:** [`week4/`](./week4/)
- **Topics:** Object arrays, interactive `Scanner` input, input stream buffer clearing, min/max algorithms, and average calculation.
- **Files:**
  - [`week4_597.java`](./week4/week4_597.java): Implements `Student` class and interactive CLI managing results for 5 students, determining top performer, class average, lowest scorer, and count of above-average students.

### Week 05 - Encapsulation & Data Validation
- **Directory:** [`Week05/`](./Week05/)
- **Topics:** OOP encapsulation, private fields, public getters and setters, domain validation constraints.
- **Files:**
  - [`Student.java`](./Week05/Student.java): Encapsulated student model enforcing marks validation range `[0, 100]`.
  - [`StudentDemo.java`](./Week05/StudentDemo.java): Driver testing valid and invalid mark updates.

---

## How to Compile & Run

### Week 01 (Canteen Stock Report)
```bash
javac Week01_597/FoodItem.java Week01_597/FoodItemDemo.java
java -cp Week01_597 FoodItemDemo
```

### Week 02 (Syntax Exercises)
```bash
cd week02/src
javac Java01.java
java Java01
```

### Week 03 (Campus Bus Booking)
```bash
javac week3/BusTrip.java week3/BusCounter.java
java -cp week3 BusCounter
```

### Week 04 (Result Manager)
```bash
javac week4/week4_597.java
java -cp week4 week4_597
```

### Week 05 (Encapsulation Demo)
```bash
javac Week05/Student.java Week05/StudentDemo.java
java -cp Week05 StudentDemo
```