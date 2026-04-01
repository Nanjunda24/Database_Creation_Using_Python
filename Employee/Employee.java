package Employee;

public class Employee {

    String name;
    double baseSalary;

    Employee(String name , double baseSalary){
        this.name = name;
        this.baseSalary  = baseSalary ; 
    }

    // mthod to calculate the salry of employee

   double calculateSalary(){
    return this.baseSalary;  //we can  diraclty access basesalry without using this.

    }
    
}
