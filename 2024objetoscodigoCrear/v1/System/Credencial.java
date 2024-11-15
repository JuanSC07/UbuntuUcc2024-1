package System;


/**
 * @version 1.0
 * @created 14-nov.-2024 10:49:18 p. m.
 */
public class Credencial {

	private double codigo;
	private boolean estado;
	private int id;
	private int usuario_id;
	public Usuario m_Usuario;
	public Adminstrador m_Adminstrador;

	public Credencial(){

	}

	public void finalize() throws Throwable {

	}

	public int ActualizarEstado(){
		return 0;
	}

	public int validarAcceso(){
		return 0;
	}

}