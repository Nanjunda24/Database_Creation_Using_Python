package Banking;

public class Customer {

    // Encapsulate holding data
    private String name;
    private long accountNo;
    private double balance = 0.0;

    // Constructor
    public Customer(String name, long accountNo){
        this.name = name;
        this.accountNo = accountNo;
    }

    public String getName(){
        return name;
    }

    public long getAccountNo(){
        return accountNo;
    }

    public double getBalance(){
        return balance;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setAccountNo(long accountNo){
        this.accountNo = accountNo;
    }

    public void setBalance(double balance){
        this.balance = balance;
    }

}
