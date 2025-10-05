package auxiliar;

public class Bus {
    private static final double COSTO_PASAJE = 1.50;
    
    private int capacidad;
    private int pasajeros;
    private double recaudacion;

    public Bus(int capacidad) {
        this.capacidad = capacidad;
        this.pasajeros = 0;    
        this.recaudacion = 0.0; 
    }

    public int subir(int cantidad) {
        int espacio = this.capacidad - this.pasajeros;

        if (cantidad <= espacio) {
            this.pasajeros += cantidad;
            System.out.printf("Suben %d pasajeros. Bus: %d/%d%n", cantidad, this.pasajeros, this.capacidad);
            return cantidad;
        } else {
            int paxSuben = espacio;
            this.pasajeros += paxSuben;
            System.out.println("Suben " + paxSuben + " pasajeros. El Bus esta lleno");
            return paxSuben;
        }
    }

    public void cobrar(int cantidadPax) {
        double monto = cantidadPax * COSTO_PASAJE;
        this.recaudacion += monto;
        System.out.printf("Se cobro Bs. %.2f a %d personas. Recaudacion total: Bs. %.2f%n", monto, cantidadPax, this.recaudacion);
    }

    public int asientosLibres() {
        return this.capacidad - this.pasajeros;
    }
    
    public int getPasajeros() {
        return pasajeros;
    }

    public double getRecaudacion() {
        return recaudacion;
    }
}

class Main {
    public static void main(String[] args) {
        Bus mibus = new Bus(20);

        System.out.println("Simulacion Bus UMSA");
        
        System.out.println("\nParada 1");
        int paxP1 = 12;
        int subieron = mibus.subir(paxP1);
        mibus.cobrar(subieron);

        System.out.println("Asientos libres restantes: " + mibus.asientosLibres());

        System.out.println("\nParada 2");
        int paxP2 = 10;
        subieron = mibus.subir(paxP2);
        mibus.cobrar(subieron);

        System.out.println("Asientos libres restantes: " + mibus.asientosLibres());
        System.out.printf("\nREPORTE FINAL: Pasajeros: %d | Recaudacion: Bs. %.2f%n", 
            mibus.getPasajeros(), mibus.getRecaudacion());
    }
}
