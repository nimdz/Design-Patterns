package SingeltonPattern;

public class SingeltonPatternDemo {

    public static void main(String[] args){
        
        SingleObject object=SingleObject.getInstance();

        object.showMessage();
    }

    
}
