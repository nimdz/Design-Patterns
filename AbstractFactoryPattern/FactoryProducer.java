package AbstractFactoryPattern;

public class FactoryProducer {
    public static RoundedShapeFactory getFactory(boolean rounded){   
        if(rounded){
           return new RoundedShapeFactory();         
        }else{
           return new ShapeFactory();
        }
     }
}
