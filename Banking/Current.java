package Banking;

public class Current extends BankAccount {

    final double OVERDRAFTLIMIT  = 10000.0 ;
   
    Current(Customer customer){
        super(customer);
    }


     @Override
    void withdraw(int amount){
        if (amount > 0 && amount <= (customer.getBalance() + OVERDRAFTLIMIT)){

            double total = customer.getBalance() - amount ;
            customer.setBalance(total);
            System.out.println(amount +" rupees successfully debited from your current  bank account!!!");
            System.out.println("Bank balance after withdrawal : "+customer.getBalance());
        }
        else{
            System.out.println("Withdrawal amount exceeds overdraft limit!!!");
        }

    }
    
}