/**
 * SE 217: Object Oriented Programming Lab
 * Week 03 - Performance Task: Campus Bus Booking
 * 
 * Student Name: Faiaz ul Islam
 * Student ID:   252-35-597
 * Section:      45-H2
 */
public class BusTrip {
    private String tripCode;
    private String route;
    private int fare;
    private int capacity;
    private int seatsLeft;
    private static int tripCount = 0;

    /**
     * Constructs a BusTrip with custom capacity.
     * Increments static trip count and auto-generates trip code starting at BT-201.
     * 
     * @param route    the travel route (e.g., Mirpur-DSC)
     * @param fare     fare in Taka per seat
     * @param capacity total seating capacity of the bus
     */
    public BusTrip(String route, int fare, int capacity) {
        tripCount++;
        this.tripCode = "BT-" + (200 + tripCount);
        this.route = route;
        this.fare = fare;
        this.capacity = capacity;
        this.seatsLeft = capacity;
    }

    /**
     * Overloaded constructor with default capacity of 40 seats.
     * Uses constructor chaining via this(...).
     * 
     * @param route the travel route
     * @param fare  fare in Taka per seat
     */
    public BusTrip(String route, int fare) {
        this(route, fare, 40);
    }

    public static int getTripCount() {
        return tripCount;
    }

    public String getRoute() {
        return route;
    }

    public int getSeatsLeft() {
        return seatsLeft;
    }

    /**
     * Calculates total revenue collected from booked seats.
     * @return fare multiplied by seats already booked
     */
    public int getRevenue() {
        return fare * (capacity - seatsLeft);
    }

    /**
     * Attempts to book a specified number of seats.
     * 
     * @param count number of seats to book
     * @return true if booking succeeded; false if count is invalid or exceeds available seats
     */
    public boolean bookSeats(int count) {
        if (count <= 0 || count > seatsLeft) {
            return false;
        }
        seatsLeft -= count;
        return true;
    }

    /**
     * Prints formatted trip details.
     */
    public void printInfo() {
        System.out.printf("%s  %-12s Tk %3d  seats left: %2d%n", tripCode, route, fare, seatsLeft);
    }
}
