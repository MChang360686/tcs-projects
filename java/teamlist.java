import java.util.ArrayList;
import java.util.Scanner;

class Person {
    String name = "";
    Integer number = 0;

    public Person(String name, Integer number) {
        this.name = name;
        this.number = number;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setNum(Integer number) {
        this.number = number;
    }
}

public class teamlist {

    private static void addPerson(String name, Integer number, ArrayList<Person> list) {
        Person newPerson = new Person(name, number);
        list.add(newPerson);
    }

    private static void printList(ArrayList<Person> list) {
        for (int i = 0; i < list.size(); i++) {
            Person p = list.get(i);
            System.out.println(p.name + ' ' + p.number);
        }
    }

    public static void main(String[] args) {
        ArrayList<Person> list = new ArrayList<Person>();
        addPerson("Robert", 32, list);
        printList(list);
    }
    
}
