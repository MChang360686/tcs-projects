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

    private void getHunger(){
        return hunger;
    }

    private void setHunger(int amt){
        hunger = hunger + amt
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

}

public class oregonTrail{
    Scanner scan = new Scanner(System.in);
    party p = new party()
}