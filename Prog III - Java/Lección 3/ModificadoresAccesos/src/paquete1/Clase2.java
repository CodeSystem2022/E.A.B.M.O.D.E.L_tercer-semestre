package paquete1;

class Clase2 extends Clase1{
    String atributoDefault = "valor del atributo default";
    
    //Clase2(){
    //    System.out.println("Constructor Default");
    //}
    
    public Clase2(){
        super();
        this.atributoDefault = "Modificación del atributo default";
        System.out.println("Atributo Default = " + this.atributoDefault );
        this.metodoDefault();
    }       
    
    void metodoDefault(){
        System.out.println("Método Default");
    }
}
