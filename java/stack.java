import java.util.ArrayList;

class stack {
    ArrayList<Integer> arr = new ArrayList<>();

    //public stack() {
    //    ArrayList<Integer> arr = new ArrayList<Integer>();
    //}

    public void push(Integer a) {
        arr.add(a);
    }

    public void pop() {
        arr.remove(arr.size() - 1);
    }

    public Integer peek() {
        return arr.get(arr.size() - 1);
    }

    public static void main(String[] args) {
        stack s = new stack();

        s.push(1);
        s.push(2);
        s.push(3);
        System.out.println(s.peek());
        s.pop();
        System.out.println(s.peek());
    }


}