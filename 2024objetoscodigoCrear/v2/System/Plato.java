package System;


/**
 * @version 1.0
 * @created 14-nov.-2024 11:22:03 p. m.
 */
public class Plato {

	private int id;
	private char nombre;
	private int precio;
	public Orden m_Orden;
	public Inventario m_Inventario;

	public Plato(){

	}

	public void finalize() throws Throwable {

	}

	public boolean calcularPrecio(){
		return false;
	}

	public boolean verificarDisponible(){
		return false;
	}

}