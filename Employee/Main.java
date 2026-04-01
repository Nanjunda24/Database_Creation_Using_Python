package Employee;

public class Main {
    public static void main(String[] args) {
        
        Manager m = new Manager("Nanjunda K M",50000,7000,2456);

        double salary = m.calculateSalary();
        System.out.println("Salery of Manager :"+salary);
    }
    
}
