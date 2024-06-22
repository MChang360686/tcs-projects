class node {
    public Integer value = null;
    public node left, right = null;
}

public class tree {
    
    public void insert(Integer a, node head) {
        if (head.value != null) {
            if (a >= head.value) {
                insert(a, head.right);
            } else {
                insert(a, head.left);
            }
        } else {
            head.value = a;
        }
    }

    public void print(node n) {
        System.out.print(n.value + " ");
        print(n.left);
        print(n.right);
    }

    public static void main(String[] args) {
        tree t = new tree();
        node head = new node();
        node l = new node();
        node r = new node();
        head.left = l;
        head.right = r;
        t.insert(5, head);
        t.insert(1, head);
        t.insert(10, head);
        t.print(head);


    }
}
