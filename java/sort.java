import java.util.ArrayList;
import java.util.Random;

public class sort {

    // Create ArrayList
    public static ArrayList<Integer> getList() {
        Random rand = new Random();
        ArrayList<Integer> l = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++) {
            l.add(rand.nextInt(10));
        }

        return l;
    }

    // print ArrayList out
    public static void printList(ArrayList<Integer> list) {
        for (int i : list) {
            System.out.print(i + " ");
        }
    }

    public static ArrayList<Integer> sortArrList(ArrayList<Integer> list) {
        for (int i = 0; i < list.size(); i++) {
            Integer currentMin = list.get(i);
            for (int j = i; j < list.size(); j++) {
                Integer newItem = list.get(j);
                if (newItem < currentMin) {
                    currentMin = newItem;
                }
            }
            list.set(i, currentMin);
        }

        return list;
    }

    public static void main(String[] args) {
        ArrayList<Integer> newList = getList();
        newList = sortArrList(newList);
        printList(newList);

    }
}