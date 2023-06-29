package persona;

public class Persona {
    private int id;
    private String nombre;
    private String tel;
    private String email;
    private static int numeroPersonas = 0;

    public Persona(){
        this.id= ++Persona.numeroPersonas;
    }

    public Persona(String nombre, String tel, String email){
        this(); // en esta parte no es necesario porque el ide se encarga, pero se especifica
        this.nombre = nombre;
        this.tel = tel;
        this.email = email;

    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getNumeroPersonas() {
        return Persona.numeroPersonas;
    }

    public void setNumeroPersonas(int numeroPersonas) {
        Persona.numeroPersonas = numeroPersonas;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", tel='" + tel + '\'' +
                ", email='" + email + '\'' +
                ", numeroPersonas=" + numeroPersonas +
                '}';
    }
}

