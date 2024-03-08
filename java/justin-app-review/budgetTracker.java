import java.util.Scanner;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class budgetTracker {

    /*
     * Take input
     * 
     * Track how much money you spent
     * 
     * Track how much money you have saved
     * 
     * Use Person class to store the data for each person
     *  Write constructors and methods.
     * 
     * https://www.baeldung.com/java-csv
     * https://bootcamp.cvn.columbia.edu/blog/java-projects-for-beginners-to-gain-skills/
     * 
     */

    // Write a function to read a CSV

    // Write a function to write to a CSV

    // Print an array
    public static void printArr(String[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    // return hours worked
    public static Integer incrementHours(String[] arr, Integer i) {
        Integer increment = (Integer) arr[1];
        return i + increment;

    }

    // return amount paid
    public static Integer incrementSalary(String[] arr, Integer i) {
        Integer payIncrement = (Integer) arr[2];
        return i + payIncrement;
    }

    public static void main(String []args) throws IOException {
        Scanner scan = new Scanner(System.in);

        File f = new File("data.csv");
        System.out.println(f.getCanonicalPath());

        try {
            BufferedReader br = new BufferedReader(new FileReader("data - Sheet1.csv"));
            String line = "";
            Integer hoursWorked, salary = 0;
            while((line = br.readLine()) != null) {
                // Code goes here
                //System.out.println(line);
                String[] temp = line.split(",");

            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
    