import java.util.*;
import java.util.Scanner;

class person{
    String name = "";
    Integer hunger = 100;
    boolean sick, cold = false;
    boolean alive = true;

    public person(String name){
        this.name = name;
    }

    private Integer getHunger(){
        return hunger;
    }

    private void setHunger(int amt){
        hunger = hunger + amt;
        if (hunger > 100){
            hunger = 100;
        }
    }

    private void getCold(boolean hasClothes){
        if (hasClothes){
            cold = false;
        } else{
            cold = true;
        }
    }

    private void getSick(){
        if (hunger < 25 && cold == true){
            sick = true;
        }
    }

    private void kill(){
        alive = false;
    }
}

class party{
    Integer food, medicine, ammunition, tools, oxen = 0;
    Integer numPeople = 5;
    person person1, person2, person3, person4, person5;
    public party(String a, String b, String c, String  d, String e){
        person person1 = new person(a);
        person person2 = new person(b);
        person person3 = new person(c);
        person person4 = new person(d);
        person person5 = new person(e);
    }

    public Integer getFood(){
        return food;
    }

    public void setFood(Integer amt){
        food = food + amt;
    }

    public Integer getMedicine(){
        return medicine;
    }

    public void setMedicine(Integer amt){
        medicine = medicine + amt;
    }

    public Integer getAmmunition(){
        return ammunition;
    }

    public void setAmmunition(Integer amt){
        ammunition = ammunition + amt;
    }

    public Integer getTools(){
        return tools;
    }

    public void setTools(Integer amt){
        tools = tools + amt;
    }

    public Integer getNumPeopleAlive() {
        numPeople = 0;
        if (person1.alive) {
            numPeople++;
        }
        if (person2.alive) {
            numPeople++;
        }
        if (person3.alive) {
            numPeople++;
        }
        if (person4.alive) {
            numPeople++;
        }
        if (person5.alive) {
            numPeople++;
        }

        return numPeople;
    }

}

public class oregonTrail{
    Scanner scan = new Scanner(System.in);
    party p = new party("chungus", "!chungus", "small chungus", "dischungus", "bob");
    Random random = new Random();
    boolean setupParty = true;

    public oregonTrail() {
        System.out.println("You start at ");
        while (setupParty) {
            System.out.println("What would you like to do? (1-3)");
            System.out.println("1. Continue your journey");
            System.out.println("2. Buy Supplies");
            System.out.println("3. Get Advice");
            int choice = scan.nextInt();

            switch(choice) {
                case 1:
                    setupParty = false;
                    break;
                case 2:
                    System.out.println("What would you like to buy? ");
                    break;
                case 3:
                    System.out.println("Don't forget to buy supplies ");
                    break;
            }
        }
    }

    public int d10() {
        return random.nextInt(10) + 1;
    }

    public void game() {
        while (p.getNumPeopleAlive() > 0) {
            switch (d10()) {
                case 1:
                    System.out.println("You hunt food ");
                    p.setFood(d10());
                    p.setAmmunition(-1);
                    break;
                case 2:
                    System.out.println("You get ambushed and die");
                    p.numPeople = 0;
                    break;
                case 3:
                    System.out.println("You see a SHOP ");
                    break;
                case 4:
                    System.out.println("Nothing happens");
                    break;
                case 5:
                    System.out.println("You attempt to trade with some strangers");
                    break;
                case 6:
                    System.out.println("You find some supplies");
                    p.setAmmunition(2);
                    p.setFood(5);
                    p.setMedicine(3);
                    p.setTools(2);
                    break;
                case 7:
                    System.out.println("Someone gets sick");
                    p.setMedicine(-1);
                    break;
                case 8:
                    System.out.println("You get some water");
                    p.setFood(2);
                    break;
                case 9:
                    System.out.println("BEANS");
                    p.setFood(10);
                    break;
                case 10:
                    System.out.println("Wagon breaks down.  Use tools to fix");
                    if (p.getTools() > 0) {
                        p.setTools(-1);
                    } else {
                        System.out.println("You have no tools, so your whole party dies of exposure.");
                        p.numPeople = 0;
                    }
                    break;
                default:
                    System.out.println("d10 has problems lol");
                    break;
            }
        }
        System.out.println("Game Over");
    }
    public static void main(String[] args) {
        oregonTrail o = new oregonTrail();
        o.game();
    }
}