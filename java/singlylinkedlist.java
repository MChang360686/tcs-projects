class node {
    int value;
    node next;

    public node(int value) {
        this.value = value;
        this.next = null;
    }
}

public class singlylinkedlist {

    public static void traverse(node head) {
        node current = head;

        while (current != null) {
            System.out.print(current.value + " ");
            current = current.next;
        }
    }

    public static void main(String[] args) {
        node head = new node(1);
        node second = new node(2);
        node third = new node(3);

        head.next = second;
        second.next = third;

        traverse(head);

    }
}
