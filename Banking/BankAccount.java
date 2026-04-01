package Banking;

abstract  class BankAccount {

    protected Customer customer ;  //protect accss within the package and sublk classes

    BankAccount(Customer customer){
        this.customer = customer ;
    }

    void deposite(int amount){
        if (amount > 0){

            double total;
            total = customer.getBalance() + amount ;
            customer.setBalance(total);
            System.out.println(amount +" rupess credited to your bank accountsuccessfully!!!");
            System.out.println("Accountbalance after deposition : "+customer.getBalance()+" rupees");

        }
        else{
            System.out.println("Amount should be positive !!!");
        }
    }

    void displayBalance(){
        System.out.println("Account holder name : " +customer.getName());
        System.out.println("Account number : " +customer.getAccountNo() );
        System.out.println("Account nalance: "+customer.getBalance()+" rupess");
    }

    abstract void withdraw(int amount);  //abstract method 


    }

    

