package Employee;

public class Manager extends Developer {

    double allowance ;

    Manager(String name, double baseSalary, double bonous, double allowance){
        super(name,baseSalary,bonous);
        this.allowance = allowance;
    }

    @Override
    double calculateSalary(){
        return super.calculateSalary()+allowance;
    }
    
}
