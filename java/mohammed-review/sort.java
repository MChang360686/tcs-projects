class selectionSort{

    public static Integer[] sort(Integer[] arr) {
        for(int i = 0; i < arr.length - 1; i++) {
            Integer minimum = arr[i];

            for(int j = i+1; j < arr.length; j++) {
                if (arr[j] < minimum) {
                    Integer temp = minimum;
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }

        }
        return arr;

    }

    public static void printArr(Integer[] arr) {
        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    
}

public class sort {

    public static void main(String[] args) {
        Integer[] arr = {1, 2, 4, 2, 3, 6, 4, 8, 2, 4};
        selectionSort s = new selectionSort();
        s.printArr(s.sort(arr));;
    }
    
}
