package persona;

import javax.xml.namespace.QName;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class ListadoPersonas{
    private static Scanner input;
    public static void main(String[] args) {
        input = new Scanner(System.in);
        List<Persona> personas = new ArrayList<>();
        boolean salir = false;
        mostrarMenu(personas);
    }
    private static void clearScreen(){
        System.out.print("\033[H\033[2J");
        System.out.flush();

    }

    private static void mostrarMenu(List<Persona> personas) {
        Scanner input = new Scanner(System.in);
        boolean salir = false;
        while(!salir){
            System.out.print("""
                    Opcion 1 agregar persona
                    Opcion 2 listar personas
                    Opcion 3 eliminar personas
                    Opcion 4 salir
""");
            System.out.println("Ingrese su opcion: ");
            var option = Integer.parseInt(input.nextLine());

            if (option == 4){
                salir = true;
            } else if (option == 3) {
                eliminarPersonas(personas);
                System.out.println("presione enter para continuar");
                input.nextLine();
                clearScreen();
            }
            else if (option == 2){
                listarPersonas(personas);
                System.out.println("presione enter para continuar");
                input.nextLine();
                clearScreen();

            }
            else if(option == 1){
                agregar_persona(personas);
                System.out.println("presione enter para continuar");
                input.nextLine();
                clearScreen();
            }
            else{
                System.out.println("La opcion ingresada no es valida");
                input.nextLine();
                clearScreen();
            }
        }


    }

    private static void agregar_persona(List<Persona> personas) {
        System.out.println("ingrese el nombre de la persona");
        String name = input.nextLine();
        System.out.println("ingrese el telefono de: "+name);
        String tel = input.nextLine();
        System.out.println("ingrese el email de: "+name);
        String email = input.nextLine();
        Persona nuevaPersona = new Persona(name, tel, email);
        personas.add(nuevaPersona);
    }

    private static void listarPersonas(List<Persona> personas) {
        if (personas.isEmpty()){
            System.out.println("no hay personas que mostrar en la lista");
        }
        else {
            System.out.println("lista de personas: ");
            for(Persona persona: personas){
                System.out.println(persona);
            }
        }
    }

    private static void eliminarPersonas(List<Persona> personas) {
        System.out.println("ingrese el nombre de la persona a eliminar: ");
        var nombre = input.nextLine();
        boolean personaEncontrada = false;
        for (Persona persona: personas){
            if(persona.getNombre().equalsIgnoreCase(nombre)){
                personas.remove(persona);
                personaEncontrada = true;
                break;
            }
        }
        if(personaEncontrada){
            System.out.println("Persona encontrada y eliminada");
        }
        else {
            System.out.println("Persona no encontrada, lo escribiste bien?");
        }
        
    }

}
