import java.util.ArrayList;

class Book {
    private String title;
    private String author;
    private boolean isAvailable;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.isAvailable = true;
    }

    public String getTitle() {
        return title;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean status) {
        this.isAvailable = status;
    }

    public void showBookInfo() {
        System.out.println("Title: " + title + ", Author: " + author + ", Available: " + isAvailable);
    }
}

class Library {
    private ArrayList<Book> books = new ArrayList<>();

    public void addBook(Book b) {
        books.add(b);
    }

    public void borrowBook(String title) {
        for (Book b : books) {
            if (b.getTitle().equalsIgnoreCase(title) && b.isAvailable()) {
                b.setAvailable(false);
                System.out.println(title + " borrowed successfully!");
                return;
            }
        }
        System.out.println(title + " is not available!");
    }

    public void returnBook(String title) {
        for (Book b : books) {
            if (b.getTitle().equalsIgnoreCase(title)) {
                b.setAvailable(true);
                System.out.println(title + " returned successfully!");
                return;
            }
        }
        System.out.println(title + " not found in library!");
    }

    public void showAllBooks() {
        for (Book b : books)
            b.showBookInfo();
    }
}

public class Main {
    public static void main(String[] args) {
        Library lib = new Library();

        Book b1 = new Book("Java Basics", "James Gosling");
        Book b2 = new Book("Python ML", "Guido van Rossum");

        lib.addBook(b1);
        lib.addBook(b2);

        lib.showAllBooks();
        lib.borrowBook("Java Basics");
        lib.showAllBooks();
    }
}
