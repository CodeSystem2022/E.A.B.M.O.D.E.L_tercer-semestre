
package paquete1;

public class Clase1 {
    public String atributoPublic = "valor atributo public"; 
    protected String atributoProtected = "valor atributo protected";
    
    public Clase1(){
        System.out.println("Constructo público");
    }
    
    protected Clase1(String atributoPublico){
        System.out.println("Constructor protected");
    }
    
    public void metodoPublico(){
        System.out.println("Metodo public");
    }
    
    protected void metodoProtected(){
        System.out.println("Metodo protected");
    }
}
