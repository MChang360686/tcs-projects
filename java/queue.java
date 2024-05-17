import java.util.ArrayList;

public class queue {
    ArrayList<Integer> arr = new ArrayList<>();

    public void enqueue(Integer a) {
        arr.add(a);
    }

    public Integer dequeue() {
        return arr.remove(0);
    }

    public Integer peek() {
        return arr.get(0);
    }

    public boolean empty() {
        if (arr.size() == 0) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        queue q = new queue();

        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);

        System.out.println(q.dequeue());
    }

}
