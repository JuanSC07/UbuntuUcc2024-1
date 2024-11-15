package System;


/**
 * @version 1.0
 * @created 14-nov.-2024 11:22:03 p. m.
 */
public class Orden {

	private int cliente_id;
	private Date fecha;
	private int id;
	private int mesero_Id;
	public Mesero m_Mesero;
	public Cocina m_Cocina;
	public Cliente m_Cliente;
	public Pago m_Pago;

	public Orden(){

	}

	public void finalize() throws Throwable {

	}

}