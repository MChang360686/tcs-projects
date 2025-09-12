
abstract class hardware {
    public String componentName;
    public abstract String returnManufacturer();
    public String function() {
        return "This is a hardware component.";
    }

}

class CPU extends hardware {
    public String componentName = "Intel Core i7";
    private String returnManufacturer() {
        return "Intel";
    }
    public String function() {
        return "This CPU processes data.";
    }
}