package Banking;

public class Saving extends BankAccount { // inheritance

    private static final double INTEREST_RATE = 0.06;

    public Saving(Customer customer){
        super(customer);
    }

    @Override
    public void withdraw(int amount){
        if(amount > 0 && amount <= customer.getBalance()){
            double balance = customer.getBalance() - amount;
            customer.setBalance(balance);
            System.out.println(amount + " rupees debited from your bank account successfully!!!!");
            System.out.println("Account balance after withdrawal : " + customer.getBalance() + " rupees");
        } else {
            System.out.println("Insufficient balance !!!");
        }
    }

    public double calculateInterest(){
        return customer.getBalance() * INTEREST_RATE;
    }

}
