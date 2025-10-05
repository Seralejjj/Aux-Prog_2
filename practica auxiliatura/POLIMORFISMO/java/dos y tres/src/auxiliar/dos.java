import java.util.Scanner;

public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantJugadores;

    public Videojuego(String nombre) {
        this(nombre, null, 0);
    }
    public Videojuego(String nombre, String plataforma, int cantJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantJugadores = cantJugadores;
        System.out.println("Videojuego '" + this.nombre + "' creado.");
    }
    public void agregarJugadores() {
        this.cantJugadores += 1;
        System.out.println("[" + this.nombre + "] Jugador agregado. Total: " + this.cantJugadores + " ahora.");
    }
    public void agregarJugadores(int cantidad) {
        if (cantidad > 0) {
            this.cantJugadores += cantidad;
            System.out.println("[" + this.nombre + "] Se agregaron " + cantidad + " jugadores. Total: " + this.cantJugadores + " ahora.");
        } else {
            System.out.println("ERROR: Cantidad de jugadores a agregar no valida.");
        }
    }
    public int reportarJugadores() {
        return this.cantJugadores;
    }
    public String getNombre() {
        return nombre;
    }
}

class Main {
    public static void main(String[] args) {
        Videojuego v1 = new Videojuego("Tierra de Calculo");

        Videojuego v2 = new Videojuego("Programacion Hero", "PC", 2);

        System.out.println("\n--- DEMOSTRACION DEL METODO SOBRECARGADO (POLIMORFISMO) ---");

        System.out.println("-> Llamada 1: Un jugador a la vez (Método sin parámetros)");
        v1.agregarJugadores(); 
        v2.agregarJugadores(); 

        System.out.println("\n-> Llamada 2: Varios jugadores (Método con parámetro INT)");
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese cuantos jugadores desea agregar a " + v1.getNombre() + ": ");
        
        int cantidadInput = scanner.nextInt(); 
        
        v1.agregarJugadores(cantidadInput);

        v2.agregarJugadores(5);
        
        scanner.close(); 

        System.out.println("\n--- ESTADO FINAL (Usando el metodo reportarJugadores) ---");
        System.out.println("Estado Final de " + v1.getNombre() + ": " + v1.reportarJugadores() + " jugadores.");
        System.out.println("Estado Final de " + v2.getNombre() + ": " + v2.reportarJugadores() + " jugadores.");
    }
}