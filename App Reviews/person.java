
class Person {

    public class Person(String name, Integer age, double height, double weight) {
        this.name = name;
        this.age = age
        this.height = height;
        this.weight = weight;
    }

    private String getName() {
        return name;
    }

    private Integer getAge() {  
        return age;
    }

    private void setName(String newName) {
        name = newName;
    }

    private void setAge(Integer newAge) {
        age = newAge;
    }

    public static void main(String[] args) {
        Person p = new Person("Bob", 32, 6.0, 180.0);

        System.out.println(p.getName());
        System.out.println(p.getAge());
    }
}