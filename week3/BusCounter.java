/**
 * SE 217: Object Oriented Programming Lab
 * Week 03 - Performance Task: Campus Bus Booking Counter Demo
 * 
 * Student Name: Faiaz ul Islam
 * Student ID:   252-35-597
 * Section:      45-H2
 */
public class BusCounter {
    public static void main(String[] args) {
        // Instantiate array of 4 bus trips with sample routes
        BusTrip[] trips = new BusTrip[4];
        trips[0] = new BusTrip("Mirpur-DSC", 50, 30);
        trips[1] = new BusTrip("Uttara-DSC", 40, 25);
        trips[2] = new BusTrip("Gabtoli-DSC", 35);
        trips[3] = new BusTrip("Savar-DSC", 30, 20);

        // Display total number of trips created
        System.out.println("Trips created: " + BusTrip.getTripCount());

        // Process seat bookings
        if (!trips[0].bookSeats(12)) {
            System.out.println("Booking failed for " + trips[0].getRoute());
        }
        if (!trips[1].bookSeats(30)) {
            System.out.println("Booking failed for " + trips[1].getRoute());
        }
        if (!trips[2].bookSeats(8)) {
            System.out.println("Booking failed for " + trips[2].getRoute());
        }

        // Copy trips[3] reference into busy and book 20 seats
        BusTrip busy = trips[3];
        busy.bookSeats(20);

        // Iterate through all trips to display info, accumulate revenue, and locate the emptiest bus
        int totalRevenue = 0;
        BusTrip emptiest = trips[0];

        for (BusTrip trip : trips) {
            trip.printInfo();
            totalRevenue += trip.getRevenue();
            if (trip.getSeatsLeft() > emptiest.getSeatsLeft()) {
                emptiest = trip;
            }
        }

        // Print summary statistics
        System.out.println("Total revenue: Tk " + totalRevenue);
        System.out.println("Most seats left: " + emptiest.getRoute());
        System.out.println("trips[3] seats left: " + trips[3].getSeatsLeft());

        // Optional Extension: Search for trips by route name
        BusTrip foundTrip = findByRoute(trips, "Uttara-DSC");
        if (foundTrip != null) {
            foundTrip.printInfo();
        } else {
            System.out.println("No such route: Uttara-DSC");
        }

        BusTrip missingTrip = findByRoute(trips, "Banani-DSC");
        if (missingTrip != null) {
            missingTrip.printInfo();
        } else {
            System.out.println("No such route: Banani-DSC");
        }
    }

    /**
     * Optional extension: Finds a bus trip in an array matching the specified route name.
     * 
     * @param trips array of BusTrip objects
     * @param route target route name
     * @return matching BusTrip object if found, or null otherwise
     */
    public static BusTrip findByRoute(BusTrip[] trips, String route) {
        for (BusTrip trip : trips) {
            if (trip.getRoute().equalsIgnoreCase(route)) {
                return trip;
            }
        }
        return null;
    }
}
