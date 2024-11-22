 

from datetime import datetime
from typing import Dict, List, Optional
from models import *;
from database import *;

 







 



# [Previous code remains the same until main() function]

def main():
    try:
        db = Database()
        db.connect()
        sistema_reservas = Reserva(db)
        
        # Create tables at startup
        print("Inicializando base de datos...")
        sistema_reservas.crear_tablas()
        print("Base de datos inicializada correctamente.")

        while True:
            print("\n=== Sistema de Reservas de Vuelos ===")
            print("1. Cliente: Realizar Reserva")
            print("2. Administrador: Gestionar Vuelos")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    vuelo_id = int(input("Ingrese el ID del vuelo: "))
                    
                    # Mostrar asientos disponibles
                    asientos_disponibles = sistema_reservas.listar_asientos_disponibles(vuelo_id)
                    if not asientos_disponibles:
                        print("No hay asientos disponibles en este vuelo.")
                        continue
                        
                    print("\nAsientos disponibles:", ", ".join(asientos_disponibles))
                    
                    pasajero_id = int(input("Ingrese su ID de pasajero: "))
                    numero_asiento = input("Ingrese el número de asiento: ")
                    
                    if numero_asiento not in asientos_disponibles:
                        print("Asiento no válido o no disponible")
                        continue
                        
                    metodo_pago = input("Ingrese el método de pago: ")

                    if sistema_reservas.confirmar_reserva(vuelo_id, pasajero_id, numero_asiento, metodo_pago):
                        print("Reserva realizada exitosamente.")
                    else:
                        print("Error al realizar la reserva.")
                except ValueError:
                    print("Error: Por favor ingrese valores válidos.")
                except Exception as e:
                    print(f"Error al procesar la reserva: {str(e)}")

            elif opcion == "2":
                try:
                    print("\n=== Modo Administrador ===")
                    print("1. Crear Vuelo")
                    print("2. Eliminar Vuelo")
                    print("3. Listar Vuelos")
                    admin_opcion = input("Seleccione una opción: ")

                    if admin_opcion == "1":
                        numeroVuelo = input("Número de vuelo: ")
                        origen = input("Origen: ")
                        destino = input("Destino: ")
                        capacidad = int(input("Capacidad: "))
                        precio = float(input("Precio: "))

                        sistema_reservas.insertar_vuelo(numeroVuelo, origen, destino, capacidad, precio)
                        print("Vuelo creado exitosamente.")

                    elif admin_opcion == "2":
                        vuelo_id = int(input("Ingrese el ID del vuelo a eliminar: "))
                        query = "DELETE FROM Vuelo WHERE id = %s"
                        db.execute_query(query, (vuelo_id,))
                        print("Vuelo eliminado.")

                    elif admin_opcion == "3":
                        query = "SELECT * FROM Vuelo"
                        vuelos = db.fetch_query(query)
                        if vuelos:
                            print("\nListado de Vuelos:")
                            print("ID | Número | Origen | Destino | Capacidad | Precio")
                            print("-" * 60)
                            for vuelo in vuelos:
                                print(f"{vuelo[0]} | {vuelo[1]} | {vuelo[2]} | {vuelo[3]} | {vuelo[4]} | ${vuelo[5]}")
                        else:
                            print("No hay vuelos registrados.")
                except ValueError:
                    print("Error: Por favor ingrese valores válidos.")
                except Exception as e:
                    print(f"Error en la gestión de vuelos: {str(e)}")

            elif opcion == "3":
                print("Gracias por usar el sistema.")
                break

    except Exception as e:
        print(f"Error en la aplicación: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
