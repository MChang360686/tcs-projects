package java.deanreview;
//import java.deanreview.Location;


public class GridPath {

    private int[][] grid = {{0, 1}, {3, 2}};


    public Location getNextLoc(int row, int col) {
        Location loc = new Location(0, 0);


        int width = grid.length;
        int height = grid[0].length;
        int rightValue = grid[row][col];
        int bottomValue = grid[row][col];

        if (col+1 < width) {
            rightValue = grid[row][col+1];
        } else {
            rightValue = -1000;
        }

        if (row+1 < height) {
            bottomValue = grid[row+1][col];
        } else {
            bottomValue = -1000;
        }

        if (rightValue > bottomValue) {
            loc = new Location(row, col+1);
        } else if (rightValue < bottomValue) {
            loc =  new Location(row+1, col);
        }

        return loc;
    }

    public int sumPath(int row, int col) {
        int sum = 0;

        while (row < grid[0].length && col < grid.length) {
            Location next = getNextLoc(row, col);

            sum = sum + grid[next.getRow()][next.getCol()];
            row = next.getRow();
            col = next.getCol();
        }

        return sum;
    }

    public static void main(String[] args) {
        Location l = new Location(0, 0);
    }
}
