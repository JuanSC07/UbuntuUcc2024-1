package System;


/**
 * @version 1.0
 * @created 14-nov.-2024 10:49:18 p. m.
 */
public class Registro {

	private int credencial_id;
	private char fecha;
	private int id;
	private int puerta_id;
	public Credencial m_Credencial;
	public Lector m_Lector;
	public Puerta m_Puerta;

	public Registro(){

	}

	public void finalize() throws Throwable {

	}

	public int generarReporte(){
		return 0;
	}

	public boolean registrarAcceso(){
		return false;
	}

}