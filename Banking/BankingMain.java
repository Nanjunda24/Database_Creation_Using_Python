package Banking;

public class BankingMain {

    public static void main(String[] args) {
        System.out.println("===========Welcome to Banking system============= "); 
        OnlineBankServices o = new OnlineBankServices();
        o.openAccount();

    BankAccount bank ; 
    // create a customer and pass it to the account (don't pass null)
    Customer cust = new Customer("Nanjunda K M", 73090100045714L);
    // set an initial balance
    cust.setBalance(20000);

    bank = new Saving(cust);
    bank.deposite(10000);
    bank.withdraw(5000);
    bank.displayBalance();
    System.out.println("---------------------------------------------------");
    Saving s = new Saving(cust);

    System.out.println("Interest amount: "+s.calculateInterest());

    System.out.println("---------------------------------------------------");
    

    bank = new Current(cust);

    System.out.println("----------------------------------------------------");
    bank.displayBalance(); 
    System.out.println("================================================================---------------------------------------------------");

    bank.withdraw(1000);
    o.closeAccount();
    }
    
}
