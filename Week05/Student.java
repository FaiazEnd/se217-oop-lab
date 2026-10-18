/**
 * SE 217: Object Oriented Programming Lab
 * Week 05 - Encapsulation and Data Validation: Student Class
 * 
 * Student Name: Faiaz ul Islam
 * Student ID:   252-35-597
 * Section:      45-H2
 */
public class Student {
    private int studentId;
    private String name;
    private double marks;

    /**
     * Parameterized constructor to initialize student attributes.
     * 
     * @param studentId unique student ID
     * @param name      student full name
     * @param marks     initial marks scored
     */
    public Student(int studentId, String name, double marks) {
        this.studentId = studentId;
        this.name = name;
        setMarks(marks);
    }

    public int getStudentId() {
        return studentId;
    }

    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getMarks() {
        return marks;
    }

    /**
     * Validates and updates student marks.
     * Marks must fall strictly between 0 and 100 inclusive.
     * 
     * @param marks new mark value
     */
    public void setMarks(double marks) {
        if (marks >= 0 && marks <= 100) {
            this.marks = marks;
        } else {
            System.out.println("Invalid marks! Marks must be between 0 and 100.");
        }
    }

    /**
     * Prints complete student record to console.
     */
    public void displayInfo() {
        System.out.println("Student ID: " + studentId);
        System.out.println("Name: " + name);
        System.out.println("Marks: " + marks);
    }
}
