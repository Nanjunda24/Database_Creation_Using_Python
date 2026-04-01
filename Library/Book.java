package Library;

public class Book extends Library{

    int pageCount ; 

    Book(String title, String author, int pageCount){
        super(title,author);
        this.pageCount = pageCount;

    }
    
    void displayInfo(){
        super.displayInfo();
        System.out.println(("Page count : "+pageCount));
    }
    
}
