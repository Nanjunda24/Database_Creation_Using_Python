package Banking;

public class OnlineBankServices  extends BankService
    {

        @Override
        public void openAccount(){
            System.out.println("Congratulation!! Account opened successfully using online banking services");
        }

        @Override
        public void closeAccount(){
            System.out.println("Account closed successfully !!!");
        }

    
    
}
