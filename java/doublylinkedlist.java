class node {
    int value;
    node next, prev;

    public node(int value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

public class doublylinkedlist {
    node head, tail;

    public doublylinkedlist() {
        this.head = null;
        this.tail = null;
    }

    void traverse(node head) {
        node current = head;
        while (current != null) {
            System.out.print(current.value + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        node head = new node(1);
        node second = new node(0);
        node third = new node(7);

        head.next = second;
        second.next = third;
        third.next = null;
        third.prev = second;
        second.prev = head;
        head.prev = null;

        doublylinkedlist d = new doublylinkedlist();
        d.traverse(head);
    }
  
}
