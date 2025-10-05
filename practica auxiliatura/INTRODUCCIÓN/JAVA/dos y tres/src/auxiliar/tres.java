package auxiliar;

public class Producto {
    private String nombre;
    private double precio;
    private int stock;

    public Producto(String nombre, double precio, int stockInicial) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stockInicial;
    }

    public void vender(int cantidad) {
        if (cantidad <= this.stock) {
            this.stock -= cantidad;
            double ingreso = cantidad * this.precio;
            System.out.printf("VENTA: Se vendieron %d de %s. Ingreso: Bs. %.2f%n", cantidad, this.nombre, ingreso);
        } else {
            System.out.printf("ERROR: No hay suficiente stock para vender %d de %s. Stock actual: %d%n", 
                cantidad, this.nombre, this.stock);
        }
    }
    public void reabastecer(int cantidad) {
        this.stock += cantidad;
        System.out.printf("REABASTECIMIENTO: Se agregaron %d unidades de %s.%n", cantidad, this.nombre);
    }

    public int obtenerStock() {
        return this.stock;
    }

    public String getNombre() {
        return nombre;
    }
}

class Main {
    public static void main(String[] args) {
        Producto cuaderno = new Producto("Cuaderno Universitario", 15.00, 80);

        System.out.println("ESTADO INICIAL");
        System.out.println("Stock de " + cuaderno.getNombre() + ": " + cuaderno.obtenerStock());

        System.out.println("\nOPERACION VENTA EXITOSA ");
        cuaderno.vender(30);
        System.out.println("Nuevo Stock: " + cuaderno.obtenerStock());

        System.out.println("\nOPERACION REABASTECER ");
        cuaderno.reabastecer(50);
        System.out.println("Nuevo Stock: " + cuaderno.obtenerStock());

        System.out.println("\nOPERACION VENTA FALLIDA ");
        cuaderno.vender(150);
        System.out.println("Stock Final: " + cuaderno.obtenerStock());
    }
}
