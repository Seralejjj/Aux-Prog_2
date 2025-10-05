import java.util.Arrays;

public class Matriz {

    private int tamano;
    private double[][] datos;

    public Matriz(int tamano) {
        this.tamano = tamano;
        this.datos = new double[tamano][tamano];
        
        for (int i = 0; i < tamano; i++) {
            for (int j = 0; j < tamano; j++) {
                if (i == j) {
                    this.datos[i][j] = 1.0;
                } else {
                    this.datos[i][j] = 0.0;
                }
            }
        }
        System.out.println("Matriz de identidad de " + tamano + "x" + tamano + " creada.");
    }
    public Matriz(int tamano, double[][] valoresIniciales) {

        if (valoresIniciales.length != tamano || 
            (tamano > 0 && valoresIniciales[0].length != tamano)) 
        {
            throw new IllegalArgumentException("Los valores iniciales no coinciden con el tamano de la matriz.");
        }
        
        this.tamano = tamano;
        this.datos = new double[tamano][tamano];
        for (int i = 0; i < tamano; i++) {
            System.arraycopy(valoresIniciales[i], 0, this.datos[i], 0, tamano);
        }
        
        System.out.println("Matriz de " + tamano + "x" + tamano + " creada con valores dados.");
    }
    public Matriz sumar(Matriz otraMatriz) {
        if (this.tamano != otraMatriz.tamano) {
            System.out.println("ERROR: Las matrices deben ser del mismo tamano para sumar.");
            return null;
        }
        
        double[][] nuevaMatrizDatos = new double[this.tamano][this.tamano];
        
        for (int i = 0; i < this.tamano; i++) {
            for (int j = 0; j < this.tamano; j++) {
                nuevaMatrizDatos[i][j] = this.datos[i][j] + otraMatriz.datos[i][j];
            }
        }
        return new Matriz(this.tamano, nuevaMatrizDatos);
    }
    public Matriz restar(Matriz otraMatriz) {
        if (this.tamano != otraMatriz.tamano) {
            System.out.println("ERROR: Las matrices deben ser del mismo tamano para restar.");
            return null;
        }
        
        double[][] nuevaMatrizDatos = new double[this.tamano][this.tamano];
        
        for (int i = 0; i < this.tamano; i++) {
            for (int j = 0; j < this.tamano; j++) {
                nuevaMatrizDatos[i][j] = this.datos[i][j] - otraMatriz.datos[i][j];
            }
        }
        return new Matriz(this.tamano, nuevaMatrizDatos);
    }
    public boolean igual(Matriz otraMatriz) {
        if (this.tamano != otraMatriz.tamano) {
            return false;
        }
        return Arrays.deepEquals(this.datos, otraMatriz.datos);
        
    }

    public void mostrar() {
        for (double[] fila : this.datos) {
            System.out.println(Arrays.toString(fila));
        }
    }
}

class Main {
    private static final double[][] VALORES_A = {{5.0, 2.0}, {1.0, 3.0}};
    private static final double[][] VALORES_B = {{1.0, 1.0}, {0.0, 2.0}};
    
    public static void main(String[] args) {
        System.out.println("1. SOBRECARGA DE CONSTRUCTOR");
        
        Matriz mIdentidad = new Matriz(3);
        mIdentidad.mostrar();

        System.out.println("\n");

        Matriz mA = new Matriz(2, VALORES_A);
        mA.mostrar();

        Matriz mB = new Matriz(2, VALORES_B);
        mB.mostrar();

        System.out.println("\n2. POLIMORFISMO EN METODOS (Sumar y Restar)");
        
        Matriz mSuma = mA.sumar(mB);
        if (mSuma != null) {
            System.out.println("Resultado Suma:");
            mSuma.mostrar();
        }

        Matriz mResta = mA.restar(mB);
        if (mResta != null) {
            System.out.println("Resultado Resta:");
            mResta.mostrar();
        }
        
        System.out.println("\nEjemplo de ERROR:");
        mIdentidad.sumar(mA); // Intentar sumar 3x3 y 2x2
        
        System.out.println("\n3. METODO IGUAL");
        Matriz mC = new Matriz(2, VALORES_A); 

        System.out.println("M_a es igual a M_b: " + mA.igual(mB));
        System.out.println("M_a es igual a M_c: " + mA.igual(mC));
    }
}