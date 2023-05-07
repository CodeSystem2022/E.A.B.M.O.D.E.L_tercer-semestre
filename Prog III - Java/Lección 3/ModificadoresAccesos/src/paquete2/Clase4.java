package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributo Privado";
    
    private Clase4(){
        System.out.println("Constructor Privado");
    }
    
    //Creamos un constructor public para poder crear objetos
    
    public Clase4(String argumento){ // aquí se puede llamar al constructor vacio
        this();
        System.out.println("Constructor Público");
    }
    
    //Metodo private
    private void metodoPrivado(){
        System.out.println("Metodo Privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }         
}
