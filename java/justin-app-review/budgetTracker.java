import java.util.Scanner;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

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

        File f = new File("data.csv");
        System.out.println(f.getCanonicalPath());

        try {
            BufferedReader br = new BufferedReader(new FileReader("data - Sheet1.csv"));
            String line = "";
            Integer hoursWorked = 0, salary = 0;
            
            br.readLine();
            while((line = br.readLine()) != null) {
                // Code goes here
                //System.out.println(line);
                String[] temp = line.split(",");
                hoursWorked = incrementHours(temp, hoursWorked);
                salary = incrementSalary(temp, salary);
            }

            String h = Integer.toString(hoursWorked);
            String s = Integer.toString(salary);

            Date date = new Date();
            SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yy");
            String today = sdf.format(date);


            try {
                File output = new File("output.csv");

                if(output.createNewFile()) {
                    System.out.println("Created output.csv");
                } else {
                    System.out.println("output.csv already exists");
                }

                FileWriter fw = new FileWriter("output.csv");
                fw.write(h + ',' + s + ',' + today);
                fw.close();
            } catch (IOException ioException) {
                System.out.println("ioexception caught ");
                ioException.printStackTrace();
            }


            

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
    