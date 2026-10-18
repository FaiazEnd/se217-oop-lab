/**
 * SE 217: Object Oriented Programming Lab
 * Week 01 - Performance Task: Canteen Stock Report
 * 
 * Student Name: Faiaz ul Islam
 * Student ID:   252-35-597
 * Section:      45-H2
 */
public class FoodItem {
    String name;
    int price;      // Taka per piece
    int quantity;   // Number of pieces in stock

    /**
     * Calculates and returns total stock value for this item.
     * @return price multiplied by quantity
     */
    int stockValue() {
        return price * quantity;
    }

    /**
     * Prints one line formatted exactly as required:
     * Name | Tk <price> | Qty <quantity> | Value <stockValue>
     */
    void printLine() {
        System.out.println(name + " | Tk " + price + " | Qty " + quantity + " | Value " + stockValue());
    }

    /**
     * Optional extension: Sells specified amount of this item.
     * If amount exceeds stock, displays insufficient stock message.
     * Otherwise deducts from stock and displays sold confirmation.
     * 
     * @param amount number of pieces to sell
     */
    void sell(int amount) {
        if (amount > quantity) {
            System.out.println("Not enough " + name + " in stock");
        } else {
            quantity -= amount;
            System.out.println("Sold " + amount + " " + name);
        }
    }
}
