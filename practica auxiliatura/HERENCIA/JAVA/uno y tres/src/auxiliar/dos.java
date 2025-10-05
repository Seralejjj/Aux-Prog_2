
public class Persona {

    protected String nombre;
    protected String apellido;
    protected String ci;

    public Persona(String nombre, String apellido, String ci) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.ci = ci;
    }

    public void mostrarDatos() {
        System.out.println("CI: " + this.ci + " | Nombre Completo: " + this.nombre + " " + this.apellido);
    }
}

class Cliente extends Persona {
    
    private String nroCompra;
    private String idCliente;

    public Cliente(String nombre, String apellido, String ci, String nroCompra, String idCliente) {

        super(nombre, apellido, ci);
        this.nroCompra = nroCompra;
        this.idCliente = idCliente;
    }
    
    public void mostrarDatos() {
        System.out.println(" DATOS CLIENTE");
        
        super.mostrarDatos();
        
        System.out.println("ID Cliente: " + this.idCliente + " | Ultima Compra: " + this.nroCompra);
    }
}

class Jefe extends Persona {
    
    private String sucursal;
    private String tipo;

    public Jefe(String nombre, String apellido, String ci, String sucursal, String tipo) {

        super(nombre, apellido, ci);
        this.sucursal = sucursal;
        this.tipo = tipo;
    }
    
    public void mostrarDatos() {
        System.out.println(" DATOS JEFE ");

        super.mostrarDatos();
        
        System.out.println("Sucursal: " + this.sucursal + " | Tipo de Jefe: " + this.tipo);
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println(" DEMOSTRACION DE HERENCIA CORREGIDA ");

        Jefe j1 = new Jefe("Maria", "Perez", "12345", "Zona Central", "Supervisor");
        j1.mostrarDatos();

        Cliente c1 = new Cliente("Juan", "Vargas", "67890", "F00123", "C-005");
        c1.mostrarDatos();
    }
}