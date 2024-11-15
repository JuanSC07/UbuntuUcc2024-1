package System;


/**
 * @version 1.0
 * @created 14-nov.-2024 11:22:03 p. m.
 */
public class Pago {

	private int id;
	private int monto;
	private int orden_id;

	public Pago(){

	}

	public void finalize() throws Throwable {

	}

	public boolean generarRecibo(){
		return false;
	}

	public boolean procesarPago(){
		return false;
	}

}