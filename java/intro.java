import java.util.Scanner;

public class intro{


    public static double splitBill(int numPeople, double money){
        return money / numPeople;
    }

    public static void main(String[] args) {
        System.out.println(splitBill(50, 100));

        Scanner scan = new Scanner(System.in);

        String name = scan.nextLine();
        System.out.println(name);

        scan.close();
    }
}