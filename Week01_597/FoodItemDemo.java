/**
 * SE 217: Object Oriented Programming Lab
 * Week 01 - Performance Task: Canteen Stock Report Demo
 * 
 * Student Name: Faiaz ul Islam
 * Student ID:   252-35-597
 * Section:      45-H2
 */
public class FoodItemDemo {
    public static void main(String[] args) {
        // Instantiate and set properties for Khichuri: Tk 90, 12 pieces
        FoodItem khichuri = new FoodItem();
        khichuri.name = "Khichuri";
        khichuri.price = 90;
        khichuri.quantity = 12;

        // Instantiate and set properties for Tea: Tk 15, 40 pieces
        FoodItem tea = new FoodItem();
        tea.name = "Tea";
        tea.price = 15;
        tea.quantity = 40;

        // Instantiate and set properties for Samosa: Tk 10, 25 pieces
        FoodItem samosa = new FoodItem();
        samosa.name = "Samosa";
        samosa.price = 10;
        samosa.quantity = 25;

        // Display individual stock status
        khichuri.printLine();
        tea.printLine();
        samosa.printLine();

        // Calculate and display total stock value across all three items
        int totalStockValue = khichuri.stockValue() + tea.stockValue() + samosa.stockValue();
        System.out.println("Total stock value: Tk " + totalStockValue);

        // Optional Extension:
        tea.sell(5);
        samosa.sell(30);
        tea.printLine();
    }
}
