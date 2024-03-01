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

    public static void main(String []args) throws IOException {
        Scanner scan = new Scanner(System.in);

        File f = new File("data.csv");
        System.out.println(f.getCanonicalPath());

        try {
            BufferedReader br = new BufferedReader(new FileReader("data - Sheet1.csv"));
            String line = "";
            while((line = br.readLine()) != null) {
                System.out.println(line);
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
    