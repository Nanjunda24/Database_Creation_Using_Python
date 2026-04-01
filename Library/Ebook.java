package Library;

public class Ebook extends Book{

    String format;

    Ebook(String title,String author,int pageCount,String format)
    {
        super(title,author, pageCount);
        this.format = format;
    }

    @Override
    void displayInfo() {
        // TODO Auto-generated method stub
        super.displayInfo();
        System.out.println("Foramt: "+format);
    }

    
    
}
