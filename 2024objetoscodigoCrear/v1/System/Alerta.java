package System;


/**
 * @version 1.0
 * @created 14-nov.-2024 10:49:18 p. m.
 */
public class Alerta {

	private int id;
	private int lector_id;
	private char tipo;
	public Lector m_Lector;
	public Adminstrador m_Adminstrador;

	public Alerta(){

	}

	public void finalize() throws Throwable {

	}

	public boolean emitirAlerta(){
		return false;
	}

	public int registrarAccidente(){
		return 0;
	}

}