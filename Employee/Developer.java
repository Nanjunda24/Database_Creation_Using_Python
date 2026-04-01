package Employee;

public class Developer extends Employee{

    double bonous;

    Developer(String name, double baseSalary, double bonous){

        super(name,baseSalary);  //accessing properties from parent class means initialixing same properties for the delveloper class also

        this.bonous = bonous;    

    }

    //base salary overrinding method .
    @Override
    double calculateSalary(){
        return baseSalary+bonous;
    }
    
}
