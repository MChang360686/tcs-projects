
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

class BankAccount {
    String accountNumber;
    double balance;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public double get_balance() {
        return balance;
    }

    public void deposit(double depositAmount) {
        balance = balance + depositAmount;
    }

    private void withdraw(double withdrawAmount) {
        if (balance >= withdrawAmount) {
            balance = balance - withdrawAmount;
        } else {
            System.out.println("Insufficient Funds");
        }
    }

}

public static void main(String[] args) {
    BankAccount b = new BankAccount("J45", 500.0);
    System.out.println(b.get_balance());
}