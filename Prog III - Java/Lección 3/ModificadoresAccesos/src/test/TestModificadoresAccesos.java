
package test;

import paquete1.Clase1;
import paquete2.Clase3;
import paquete2.Clase4;

public class TestModificadoresAccesos {
    public static void main(String[] args) {
        Clase1 clase1 = new Clase1();
        System.out.println("clase1 = " + clase1.atributoPublic);
        clase1.metodoPublico();
        Clase3 claseHija = new Clase3();
        System.out.println("claseHija = " + claseHija);
        
        Clase4 clase4 = new Clase4("Publico");
        System.out.println(clase4.getAtributoPrivate());
        clase4.setAtributoPrivate("Cambio");
        System.out.println("clase4 = " + clase4.getAtributoPrivate());
    }
}
