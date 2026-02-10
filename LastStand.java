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
        constrScanner.close();

        hp = (2 * end) + str;
        stamina = end + str + 5;
    }

    public Integer getHp() {
        return hp;
    }

    public Integer getSta() {
        return stamina;
    }

    public void setHp(Integer amt) {
        if ((hp - amt) < 1) {
            hp = 0;
        } else {
            hp = hp - amt;
        }
    }

    public void setSta(Integer amt) {
        if ((stamina - amt) < 1) {
            stamina = 0;
        } else {
            stamina = stamina - amt;
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

    public int getSpd() {
        return speed;
    }

    public void setSpd(int amt) {
        speed = speed + amt;
    }

    public int getArm() {
        return armor;
    }

    public void setArm(int amt) {
        armor = armor + amt;
    }

}

class Weapon {
    String name;
    double dmg;
    int weight;
    int range;
    int capacity;
    int ammo;

    public Weapon(String name, double dmg, int wt, int rng, int cap, int amm) {
        this.name = name;
        this.dmg = dmg;
        weight = wt;
        range = rng;
        capacity = cap;
        ammo = amm;
    }

    public String getName() {
        return name;
    }

    public double getDmg() {
        return dmg;
    }

    public int getWeight() {
        return weight;
    }

    public int getRange() {
        return range;
    }

    public int getCapacity() {
        return capacity;
    }

    public int getAmmo() {
        return ammo;
    }

    public void reload(Integer newAmmo) {
        ammo = newAmmo;
    }

}

public class LastStand {
    public static void main(String[] args) {
        Player p = new Player();
        Integer distance = 500, supplies = 30, money = 250;
        Scanner scan = new Scanner(System.in);
        Random r = new Random();
        Weapon w1 = new Weapon("tire iron", 5.0, 5, 1, 0, 0);
        Weapon w2 = new Weapon("taurus revolver", 15.0, 3, 10, 5, 15);
        Weapon selectedWeapon = w1;

        for (int i = 0; i < distance; i += Math.floor((p.str + p.end) / 2)) {
            String cmd = scan.nextLine();
            System.out.println("What do you want to do? ");
            System.out.println("0. travel \n1. search \n2. fight zombies \n3. shop");

            switch (cmd) {
                case "0":
                    break;
                case "1":
                    Integer encounter = r.nextInt(101);
                    if (encounter < 75) {
                        Integer supp = r.nextInt(6) + 1;
                        System.out.println("You find" + supp.toString() + " supplies ");

                    } else {
                        String[] types = {"", "fat", "police", "military", "kid"};
                        Zombie z = new Zombie(types[r.nextInt(types.length)]);
                        Integer fightDistance = r.nextInt(10) + 1;
                        while (z.getHp() > 0) {
                            // fight until zombie is dead
                            System.out.println("Choose an action (0-4): ");
                            Integer act = scan.nextInt();
                            switch (act) {
                                case 0:
                                    //attack
                                    z.setHp(selectedWeapon.getDmg() - z.getArm());
                                    if ((p.getHp() - z.getDmg()) < 1) {
                                        System.out.print("You Died");
                                        break;
                                    } else {
                                        p.setHp((int) Math.ceil(z.getDmg()));
                                    }
                                    break;
                                case 1:
                                    //reload
                                    if (selectedWeapon.getAmmo() < 1 && selectedWeapon.range > 1) {
                                        selectedWeapon.reload(selectedWeapon.getCapacity());
                                    }
                                    break;
                                case 2:
                                    //switch weapons
                                    if (selectedWeapon == w1) {
                                        selectedWeapon = w2;
                                    } else {
                                        selectedWeapon = w1;
                                    }
                                    break;
                                case 3:
                                    //move forward
                                    fightDistance -= 10;
                                    break;
                                case 4:
                                    //move backwards
                                    fightDistance += 10;
                                    break;
                                default:
                                    //bad input, make player suffer
                                    System.out.println("Bad input, skipping turn. ");
                                    break;
                            }
                        }
                    }
                    break;
                case "2":
                    String[] types = {"", "fat", "police", "military", "kid"};
                    Zombie z = new Zombie(types[r.nextInt(types.length)]);
                    Integer fightDistance = r.nextInt(10) + 1;
                    while (z.getHp() > 0) {
                        // fight until zombie is dead
                        System.out.println("Choose an action (0-4): ");
                        Integer act = scan.nextInt();
                        switch (act) {
                            case 0:
                                //attack
                                z.setHp(selectedWeapon.getDmg() - z.getArm());
                                if ((p.getHp() - z.getDmg()) < 1) {
                                    System.out.print("You Died");
                                    break;
                                } else {
                                    p.setHp((int) Math.ceil(z.getDmg()));
                                }
                                break;
                            case 1:
                                //reload
                                if (selectedWeapon.getAmmo() < 1 && selectedWeapon.range > 1) {
                                    selectedWeapon.reload(selectedWeapon.getCapacity());
                                }
                                break;
                            case 2:
                                //switch weapons
                                if (selectedWeapon == w1) {
                                    selectedWeapon = w2;
                                } else {
                                    selectedWeapon = w1;
                                }
                                break;
                            case 3:
                                //move forward
                                fightDistance -= 10;
                                break;
                            case 4:
                                //move backwards
                                fightDistance += 10;
                                break;
                            default:
                                //bad input, make player suffer
                                System.out.println("Bad input, skipping turn. ");
                                break;
                        }
                    }
                    break;
                case "3":
                    HashMap<Integer, Weapon> weapons = new HashMap<Integer, Weapon>();
                    weapons.put(500, new Weapon("ar15", 50.0, 10, 400, 30, 30));
                    weapons.forEach((key, value) -> System.out.println("Price: " + key + ", Weapon: " + value.getName()));
                    break;
            }

            supplies--;
        }
    }
}