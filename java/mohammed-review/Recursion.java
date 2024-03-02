import java.util.ArrayList;

public class Recursion {

    public static Double randInt() {
        return Math.random();
    }

    public static ArrayList<Double> makeList() {
        ArrayList<Double> arr = new ArrayList<Double>();
        for (int i = 0; i < 10; i++) {
            arr.add(randInt());
        }

        return arr;
    }

    public static void push(ArrayList<Double> list, Double i) {
        list.add(i);
    }

    public static Double pop(ArrayList<Double> list) {
        return list.remove(list.size() - 1);
    }

    public static void printArrList(ArrayList<Double> list) {
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
    }

    public static ArrayList<Double> reverse(ArrayList<Double> list) {
        
    }

    public static void main(String[] args) {
        ArrayList<Double> l = makeList();

        push(l, 0.5);
        printArrList(l);
        Double num = pop(l);
        System.out.println(num);
    }
    
}
