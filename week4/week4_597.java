import java.util.Scanner;

/**
 * SE 217: Object Oriented Programming Lab
 * Week 04 - Performance Task: Result Manager
 * 
 * Student Name: Faiaz ul Islam
 * Student ID:   252-35-597
 * Section:      45-H2
 */
class Student {
    int id;
    String name;
    double marks;

    /**
     * Displays student details in the exact specified format:
     * ID: <id>, Name: <name>, Marks: <marks>
     */
    void display() {
        System.out.println("ID: " + id + ", Name: " + name + ", Marks: " + marks);
    }
}

public class week4_597 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Array capable of holding 5 Student objects
        Student[] students = new Student[5];

        // Loop 1: Instantiate 5 Student objects into the array
        for (int i = 0; i < students.length; i++) {
            students[i] = new Student();
        }

        // Loop 2: Read student details from user input
        for (int i = 0; i < students.length; i++) {
            System.out.println("Enter information for Student " + (i + 1));
            System.out.print("ID: ");
            students[i].id = scanner.nextInt();
            scanner.nextLine(); // Clear leftover newline buffer

            System.out.print("Name: ");
            students[i].name = scanner.nextLine();

            System.out.print("Marks: ");
            students[i].marks = scanner.nextDouble();
            System.out.println();
        }

        // Display summary of all students
        System.out.println("===== Student Information =====");
        for (Student s : students) {
            s.display();
        }

        // Find the top scorer and sum marks for average calculation
        Student topStudent = students[0];
        double totalMarks = 0;

        for (Student s : students) {
            totalMarks += s.marks;
            if (s.marks > topStudent.marks) {
                topStudent = s;
            }
        }

        // Display highest scoring student
        System.out.println();
        System.out.println("===== Top Student =====");
        topStudent.display();

        // Calculate and display class average
        double averageMarks = totalMarks / students.length;
        System.out.println();
        System.out.println("Average Marks: " + averageMarks);

        // Optional Extension: Lowest scorer and count of students above average
        Student lowestStudent = students[0];
        int aboveAverageCount = 0;

        for (Student s : students) {
            if (s.marks < lowestStudent.marks) {
                lowestStudent = s;
            }
            if (s.marks > averageMarks) {
                aboveAverageCount++;
            }
        }

        System.out.println();
        System.out.println("===== Lowest Student (Optional) =====");
        lowestStudent.display();
        System.out.println("Students above average: " + aboveAverageCount);

        scanner.close();
    }
}
