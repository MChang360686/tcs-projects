public class dynprog {
    public static void main(String[] args) {
        // Create array of weights
        int[] weights = new int[]{8, 2, 6, 1};
        int[] value = new int[]{50, 150, 210, 30};

        // Create 2D array w/ items = 5, capacity = 10
        int[][] knapsack = new int[5][10];

        // Memoization time
        for (int i = 0; i < weights.length; i++) {
            System.out.println(value[i]);
        }

    }
}
