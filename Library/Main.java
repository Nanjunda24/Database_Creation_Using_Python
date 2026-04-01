package Library;

public class Main {
    public static void main(String[] args) {
        
        Library lib = new Library("Effective Java", "Joshua Bloch");

        Ebook eb = new Ebook("Java Programming", "John Doe", 350, "PDF");
        eb.displayInfo();
        lib.displayInfo();
    }
    
}
