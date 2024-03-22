
class Node{
    Integer value;
    Node left;
    Node right;

    Node(int value){
        this.value = value;
        left = null;
        right = null;
    }
}

public class binarytree{
    Node root;

    private Node add(Node current, Integer value){
        if (current == null){
            return new Node(value);
        }

        if (value < current.value) {
            current.left = add(current.left, value);
        } else if (value > current.value) {
            current.right = add(current.right, value);
        } else{
            return current;
        }

        return current;
    }

    public void addNode(Integer i){
        root = add(root, i);
    }

    private binarytree createBinaryTree() {
        binarytree bt = new binarytree();
        return binarytree;
    }

    private boolean containsNode(Node current, int value) {
        if (current == null) {
            return false;
        }

        if (value == current.value) {
            return true;
        } 

        return value < current.value ? containsNode(current.left, value) : containsNode(current.right, value);

    }

    public boolean containsNode(int value) {
        return containsNode(root, value);
    }

    private Node deleteRecursive(Node current, int value) {
        if (current == null) {
            return null;
        }

        if (value == current.value) {
            if (current.left == null && current.right == null) {
                return null;
            } 

            if (current.right == null) {
                return current.left;
            }

            if (current.left == null) {
                return current.right;
            }

            int smallest = findSmallest(current.right);
            current.value = smallest;
            current.right = deleteRecursive(current.right, smallest);
            return current;
        }

        if (value < current.value) {
            current.left = deleteRecursive(current.left, value);
            return current;
        } else { 
            current.right = deleteRecursive(current.right, value);
            return current;
        }
    }

    private int findSmallest(Node root) {
        return root.left == null ? root.value : findSmallest(root.left);
    }

    public void delete(int value) {
        root = deleteRecursive(root, value);
    }


}