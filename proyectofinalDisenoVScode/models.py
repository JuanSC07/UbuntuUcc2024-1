


from datetime import datetime
from typing import Dict, List, Optional



import psycopg2
from psycopg2 import sql
from datetime import datetime


class Admin:
    def __init__(self, password: str):
        self.password = password

    def crearVuelo(self, vuelo) -> bool:
        return True

    def eliminarVuelo(self, id: int) -> bool:
        return True

class Vuelo:
    def __init__(self, id: int, numeroVuelo: str, origen: str, destino: str, 
                 capacidad: int, precio: float):
        self.id = id
        self.numeroVuelo = numeroVuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.precio = precio

 
    # 2. Modificar el método insertar_vuelo para crear asientos automáticamente:
    def insertar_vuelo(self, numeroVuelo, origen, destino, capacidad, precio):
        # Insertar vuelo
        query_vuelo = """
        INSERT INTO Vuelo (numeroVuelo, origen, destino, capacidad, precio)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        vuelo_id = self.db.fetch_query(query_vuelo, 
            (numeroVuelo, origen, destino, capacidad, precio))[0][0]

        # Crear asientos para el vuelo
        for i in range(capacidad):
            query_asiento = """
            INSERT INTO Asiento (vueloId, numeroAsiento, estado)
            VALUES (%s, %s, 'disponible');
            """
            self.db.execute_query(query_asiento, (vuelo_id, f"A{i+1}"))

        return vuelo_id
    
 
    # 4. Agregar método para listar asientos disponibles:
    def listar_asientos_disponibles(self, vuelo_id: int):
        query = """
        SELECT numeroAsiento 
        FROM Asiento 
        WHERE vueloId = %s AND estado = 'disponible'
        ORDER BY numeroAsiento
        """
        asientos = self.db.fetch_query(query, (vuelo_id,))
        return [asiento[0] for asiento in asientos]
    
class Asiento:
    def __init__(self, id: int, vuelo_id: int, numero_asiento: str, estado: str = "disponible"):
        self.id = id
        self.vuelo_id = vuelo_id
        self.numero_asiento = numero_asiento
        self.estado = estado

    # 3. Modificar el método verificar_disponibilidad:
    def verificar_disponibilidad(self, vuelo_id: int, numero_asiento: str) -> bool:
        query = """
        SELECT COUNT(*) 
        FROM Asiento 
        WHERE vueloId = %s 
        AND numeroAsiento = %s 
        AND estado = 'disponible'
        """
        result = self.db.fetch_query(query, (vuelo_id, numero_asiento))
        return result[0][0] > 0


 

    @staticmethod
    def actualizar_estado(db, vuelo_id: int, numero_asiento: str, nuevo_estado: str) -> bool:
        query = """
        UPDATE Asiento
        SET estado = %s
        WHERE vueloId = %s AND numeroAsiento = %s
        """
        db.execute_query(query, (nuevo_estado, vuelo_id, numero_asiento))
        return True


class Pasajero:
    def __init__(self, id: int, nombre: str, apellido: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def actualizarDatos(self) -> bool:
        return True

class Pago:
    def __init__(self, id: int, monto: float, metodoPago: str, reservaId: int):
        self.id = id
        self.monto = monto
        self.fechaPago = datetime.now()
        self.metodoPago = metodoPago
        self.referenciaPago = f"PAY-{id}"
        self.reservaId = reservaId

    def procesarPago(self) -> bool:
        return True

    def generarComprobante(self) -> str:
        return f"COMP-{self.id}"

    def reembolsar(self) -> bool:
        return True

    def validarPago(self) -> bool:
        return True

class Notificacion:
    def __init__(self, id: int, reservaId: int, mensaje: str, destinatario: str):
        self.id = id
        self.reservaId = reservaId
        self.mensaje = mensaje
        self.destinatario = destinatario

    def enviarNotificacion(self) -> bool:
        print(f"Notificación enviada a {self.destinatario}: {self.mensaje}")
        return True

class Reserva:
    def __init__(self):
        self.vuelos: Dict[int, Vuelo] = {}
        self.pasajeros: Dict[int, Pasajero] = {}
        self.pagos: Dict[int, Pago] = {}
        self.notificaciones: Dict[int, Notificacion] = {}
        self.asientos: Dict[int, Asiento] = {}
        self.admin = Admin("admin123")
        self.next_id = 1

    def confirmarReserva(self) -> bool:
        return True

    def cancelarReserva(self) -> bool:
        return True

    def asignarAsiento(self, asiento: str) -> bool:
        return True

    def generarCodigoReserva(self) -> str:
        return f"RES-{self.next_id}"

    def crear_vuelo(self, numeroVuelo: str, origen: str, destino: str, 
                   capacidad: int, precio: float) -> Optional[Vuelo]:
        vuelo = Vuelo(self.next_id, numeroVuelo, origen, destino, capacidad, precio)
        if self.admin.crearVuelo(vuelo):
            self.vuelos[self.next_id] = vuelo
            # Crear asientos para el vuelo
            for i in range(capacidad):
                asiento = Asiento(self.next_id + i, f"A{i+1}")
                self.asientos[self.next_id + i] = asiento
            self.next_id += capacidad + 1
            return vuelo
        return None

    def eliminar_vuelo(self, vuelo_id: int) -> bool:
        if vuelo_id in self.vuelos and self.admin.eliminarVuelo(vuelo_id):
            del self.vuelos[vuelo_id]
            return True
        return False

    def procesar_reserva(self, vuelo_id: int, pasajero_id: int, 
                        metodo_pago: str) -> bool:
        if not (vuelo_id in self.vuelos and 
                self.vuelos[vuelo_id].verificarDisponibilidad()):
            return False

        # Crear pago
        pago = Pago(self.next_id, self.vuelos[vuelo_id].precio, metodo_pago, 
                    self.next_id)
        if pago.procesarPago():
            self.pagos[self.next_id] = pago
            self.next_id += 1

            # Enviar notificación
            notificacion = Notificacion(
                self.next_id,
                self.next_id - 1,
                f"Reserva confirmada para el vuelo {self.vuelos[vuelo_id].numeroVuelo}",
                self.pasajeros[pasajero_id].email
            )
            self.notificaciones[self.next_id] = notificacion
            notificacion.enviarNotificacion()
            self.next_id += 1
            return True
        return False

