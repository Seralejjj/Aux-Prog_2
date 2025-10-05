import java.util.ArrayList;
import java.util.List;

public class Animal {
    
    protected String nombre;
    protected int edad;

    public Animal(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public void desplazarse() {
        System.out.println(this.nombre + " se desplaza de forma generica.");
    }
}

class Leon extends Animal {
    
    public Leon(String nombre, int edad) {
        super(nombre, edad);
    }
    
    public void desplazarse() {
        System.out.println("El " + this.nombre + " (Leon) esta caminando o corriendo.");
    }
}
class Pinguino extends Animal {
    
    public Pinguino(String nombre, int edad) {
        super(nombre, edad);
    }
    
    public void desplazarse() {
        System.out.println("El " + this.nombre + " (Pinguino) esta nadando o se desliza en el hielo.");
    }
}

class Canguro extends Animal {
    
    public Canguro(String nombre, int edad) {
        super(nombre, edad);
    }
    
    public void desplazarse() {
        System.out.println("El " + this.nombre + " (Canguro) esta saltando.");
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println("DEMOSTRACION DE POLIMORFISMO POR SOBREESCRITURA ");
        List<Animal> arregloAnimales = new ArrayList<>();
        arregloAnimales.add(new Leon("Simba", 5));
        arregloAnimales.add(new Pinguino("Pingu", 2));
        arregloAnimales.add(new Canguro("Skippy", 7));
        arregloAnimales.add(new Leon("Nala", 6));
        arregloAnimales.add(new Animal("Generico", 1));

        System.out.println();
        for (Animal animal : arregloAnimales) {
            animal.desplazarse();
        }
    }
}