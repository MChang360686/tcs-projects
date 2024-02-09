import java.util.ArrayList;

public class traverse {

    public static ArrayList<Integer> traverse(ArrayList<Integer> list) {
        for (int i = 0; i < (list.size())/2; i++) {
            Integer temp = list.get(i);
            list.set(i, list.get((list.size() - (i + 1))));
            list.set((list.size() - (i + 1)), temp);
        }

        return list;
    }

    // for each loop
    public static void printArrayList(ArrayList<Integer> l) {
        for (Integer i : l) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(0);
        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        System.out.println(traverse(arr));
        printArrayList(arr);
    }
}
