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

class Zombie {
    double hp = 0;
    double dmg = 0;
    int speed = 0;
    int armor = 0;
    String type = "";
    Random r = new Random();

    public Zombie(String type) {
        if (type.equals("")) {
            hp = r.nextInt(25);
            dmg = 5.0;
            speed = 2;
        } else if (type.equals("fat")) {
            hp = r.nextInt(50);
            dmg = 5.0;
            speed = 1;
        } else if (type.equals("police")) {
            hp = r.nextInt(40);
            dmg = 6.0;
            speed = 2;
            armor = 15;
        } else if (type.equals("military")) {
            hp = r.nextInt(50);
            dmg = 8.0;
            speed = 3;
            armor = 25;
        } else if (type.equals("kid")) {
            hp = r.nextInt(15);
            dmg = 3.0;
            speed = 6;
        } else {
            hp = r.nextInt(25);
            dmg = 5.0;
            speed = 2;
        }
    }

    public double getHp() {
        return hp;
    }

    public void setHp(double amt) {
        hp = (amt > hp) ? 0 : hp - amt;
    }

    public double getDmg() {
        return dmg;
    }

    public void setDmg(double amt) {
        dmg = dmg + amt;
    }


}

public class LastStand {
    public static void main(String[] args) {

    }
}