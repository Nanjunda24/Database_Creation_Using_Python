package Library;

public class Library {

    protected String title;   //protected visible to only within the package and subclass

    protected String author ; 

    Library(String title,String author){
        this.title = title ;
        this.author = author ;
    }

    void displayInfo(){
        System.out.println("Title: "+title);
        System.out.println("Author: "+author);
    }



    
}
