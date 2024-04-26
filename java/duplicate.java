import java.util.Hashtable;

class duplicate{

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 8, 4, 5, 7, 9, 10, 4};

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    System.out.println(nums[i]);
                } else {

                }
            }
        }

        Hashtable<Integer, Integer> h = new Hashtable<>();

        for (int i = 0; i < nums.length; i++) {
            //Hashtable<String, Integer> keys = h.keys();
            if (h.containsKey(nums[i])) {
                System.out.println(nums[i]);
            } else {
                h.put(nums[i], 0);
            }
        }
    }


}