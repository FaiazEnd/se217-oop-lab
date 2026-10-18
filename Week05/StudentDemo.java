/**
 * SE 217: Object Oriented Programming Lab
 * Week 05 - Encapsulation Demonstration: StudentDemo
 * 
 * Student Name: Faiaz ul Islam
 * Student ID:   252-35-597
 * Section:      45-H2
 */
public class StudentDemo {
    public static void main(String[] args) {
        // Create student with valid initial marks
        Student s1 = new Student(597, "Faiaz ul Islam", 88.5);
        s1.displayInfo();

        System.out.println("\n--- Testing Validation ---");
        // Test invalid mark update
        s1.setMarks(105.0); // Out of bounds

        // Test valid mark update
        s1.setMarks(95.0);
        System.out.println("Updated Marks: " + s1.getMarks());
    }
}
