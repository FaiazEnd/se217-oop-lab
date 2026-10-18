# Week 03 - Performance Task: Campus Bus Booking

## Student Information
- **Name:** Faiaz ul Islam
- **Student ID:** 252-35-597
- **Section:** 45-H2
- **Course:** SE 217 - Object Oriented Programming Lab
- **Semester:** Fall 2026

---

## Scenario
The university transport office operates scheduled bus routes connecting various points across Dhaka to Daffodil Smart City (DSC). Administrative staff need a Java system to monitor trips, track seat occupancy, process booking requests, and report collected revenues.

---

## File Overview

| File | Type | Description |
|:---|:---|:---|
| [`BusTrip.java`](./BusTrip.java) | Entity Class | Encapsulates bus trip data (`tripCode`, `route`, `fare`, `capacity`, `seatsLeft`), static trip counter, overloaded constructors with chaining, booking validation, and formatted printing. |
| [`BusCounter.java`](./BusCounter.java) | Driver Class | Instantiates an array of 4 trips, executes booking operations, demonstrates object reference assignment, computes total revenue, identifies the most vacant trip, and searches routes via `findByRoute()`. |

---

## Technical Specifications

### `BusTrip` Class Design
- **Private Fields:**
  - `String tripCode`: Auto-generated identifier (`BT-201`, `BT-202`, ...).
  - `String route`: Travel route name (e.g., `Mirpur-DSC`).
  - `int fare`: Cost per passenger seat in Taka.
  - `int capacity`: Total seat capacity.
  - `int seatsLeft`: Currently unoccupied seats.
  - `static int tripCount`: Static tracker for trips created, initialized to 0.
- **Constructors:**
  - `BusTrip(String route, int fare, int capacity)`: Increments `tripCount`, sets `tripCode` to `"BT-" + (200 + tripCount)`, initializes attributes and sets `seatsLeft = capacity`.
  - `BusTrip(String route, int fare)`: Constructor chaining via `this(route, fare, 40)` to assign a default capacity of 40 seats.
- **Methods:**
  - `static int getTripCount()`: Returns static counter.
  - `String getRoute()`: Returns route name.
  - `int getSeatsLeft()`: Returns remaining seats.
  - `int getRevenue()`: Returns `fare * (capacity - seatsLeft)`.
  - `boolean bookSeats(int count)`: Deducts seats and returns `true` if valid (`1 <= count <= seatsLeft`); returns `false` otherwise without modifying state.
  - `void printInfo()`: Prints formatted record using `System.out.printf("%s  %-12s Tk %3d  seats left: %2d%n", tripCode, route, fare, seatsLeft)`.

### Driver Logic (`BusCounter`)
1. Instantiates 4 trips:
   - `trips[0] = new BusTrip("Mirpur-DSC", 50, 30)`
   - `trips[1] = new BusTrip("Uttara-DSC", 40, 25)`
   - `trips[2] = new BusTrip("Gabtoli-DSC", 35)` *(default 40 seats)*
   - `trips[3] = new BusTrip("Savar-DSC", 30, 20)`
2. Books seats: 12 on `trips[0]`, 30 on `trips[1]` *(fails - exceeds 25)*, 8 on `trips[2]`.
3. Reference Aliasing Demonstration:
   - `BusTrip busy = trips[3];`
   - `busy.bookSeats(20);` *(alters `trips[3]` directly)*
4. Traversal: Computes cumulative revenue and finds the emptiest route (`emptiest`).
5. Optional Extension: `findByRoute(BusTrip[] trips, String route)` tests searching for `"Uttara-DSC"` and non-existent `"Banani-DSC"`.

---

## How to Compile & Run

Open terminal in this directory:
```bash
# Compile source files
javac BusTrip.java BusCounter.java

# Run the booking counter demo
java BusCounter
```

---

## Expected Output
```text
Trips created: 4
Booking failed for Uttara-DSC
BT-201  Mirpur-DSC   Tk  50  seats left: 18
BT-202  Uttara-DSC   Tk  40  seats left: 25
BT-203  Gabtoli-DSC  Tk  35  seats left: 32
BT-204  Savar-DSC    Tk  30  seats left:  0
Total revenue: Tk 1480
Most seats left: Gabtoli-DSC
trips[3] seats left: 0
BT-202  Uttara-DSC   Tk  40  seats left: 25
No such route: Banani-DSC
```

---

## Viva & Code Explanation Points
1. **Static Variable vs Instance Variable:**
   `tripCount` belongs to the class itself, not any single object. Every time `new BusTrip(...)` is called, all instances share and increment the exact same counter.
2. **Constructor Chaining (`this`):**
   `this(route, fare, 40);` invokes the 3-argument constructor from the 2-argument constructor, ensuring single-source initialization and preventing repetitive code.
3. **Reference Aliasing:**
   `BusTrip busy = trips[3];` does not clone the object. Both `busy` and `trips[3]` store the same memory reference. Calling `busy.bookSeats(20)` directly updates `trips[3].getSeatsLeft()`.
