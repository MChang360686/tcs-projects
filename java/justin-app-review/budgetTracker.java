import java.util.Scanner;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.ArrayList;

public class budgetTracker {

    /*
     * Take input
     * 
     * 
     * Track how much money you have saved
     * 
     * 
     */

    // Write a function to write to a CSV

    // Print an array
    public static void printArr(String[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    // return hours worked
    public static Integer incrementHours(String[] arr, Integer i) {
        Integer increment = Integer.parseInt(arr[1]);
        return i + increment;

    }

    // return amount paid
    public static Integer incrementSalary(String[] arr, Integer i) {
        Integer payIncrement = Integer.parseInt(arr[2]);
        return i + payIncrement;
    }


    public static void main(String []args) throws IOException {
        Scanner scan = new Scanner(System.in);

        File f = new File("data.csv");
        System.out.println(f.getCanonicalPath());

        try {
            BufferedReader br = new BufferedReader(new FileReader("data - Sheet1.csv"));
            String line = "";
            Integer hoursWorked = 0, salary = 0;
            ArrayList l = new ArrayList<Integer>();
            br.readLine();
            while((line = br.readLine()) != null) {
                // Code goes here
                //System.out.println(line);
                String[] temp = line.split(",");
                hoursWorked = incrementHours(temp, hoursWorked);
                salary = incrementSalary(temp, salary);
            }

            Date today = java.time.LocalDate.now();
            l.add(new String[] {hoursWorked, salary, today});

            createCSV();

            

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
    