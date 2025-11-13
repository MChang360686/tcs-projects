import java.util.*;
import java.util.Scanner;
import java.util.Random;
import java.util.HashMap;
import java.util.Arrays;
import java.util.List;

class Player {
    Integer hp, stamina;
    Integer str, end, pre, inte, luc = 0;
    Integer food, rest = 100;
    public Player() {
        Scanner constrScanner = new Scanner(System.in);
        System.out.println("Choose a preset?(y/n) ");
        String choice = constrScanner.nextLine();
        if (choice.equals("y")) {
            HashMap<String, List<Integer>> presets = new HashMap<>();

            presets.put("Code Coach", Arrays.asList(5, 5, 5, 5, 5));
            presets.put("Construction Worker", Arrays.asList(7, 8, 3, 4, 3));
            presets.put("Librarian", Arrays.asList(4, 3, 5, 8, 5));
            presets.put("Lucky Dude", Arrays.asList(4, 4, 2, 3, 10));

            for (String key : presets.keySet()) {
                System.out.println(key);
            }
            System.out.println("Type a preset to choose: ");
            List<Integer> stats = presets.get(constrScanner.nextLine());
            str = stats.get(0);
            end = stats.get(1);
            luc = stats.get(4);
            pre = stats.get(2);
            inte = stats.get(3);

        } else {
            System.out.println("Allocate 25 points");

            for (int i = 0; i < 25; i++) {
                System.out.println("Type a stat name to allocate a point to: ");
                String statName = constrScanner.nextLine();
                switch (statName) {
                    case "str":
                        str++;
                        break;
                    case "end":
                        end++;
                        break;
                    case "pre":
                        pre++;
                        break;
                    case "inte":
                        inte++;
                        break;
                    case "luc":
                        luc++;
                        break;
                    default:
                        continue;
                }
            }
        }
    }
}

public class LastStand {
    public static void Main(String[] args) {

    }
}