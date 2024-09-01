import requests
from prettytable import PrettyTable
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def obtener_cotizaciones():
    url = 'https://dolar.melizeche.com/api/1.0/'
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa

        # Convertir la respuesta JSON a un diccionario de Python
        data = response.json()

        # Crear una tabla para mostrar los datos
        tabla = PrettyTable()
        tabla.field_names = ["Casa de Cambio", "Compra", "Venta"]

        # Extraer y agregar las cotizaciones a la tabla
        for casa, valores in data['dolarpy'].items():
            compra = valores.get('compra', 'N/A')
            venta = valores.get('venta', 'N/A')
            tabla.add_row([Fore.YELLOW + casa.capitalize() + Style.RESET_ALL, 
                           Fore.GREEN + str(compra) + Style.RESET_ALL, 
                           Fore.RED + str(venta) + Style.RESET_ALL])

        # Formatear y devolver el resultado
        return f"Cotizaciones del Dólar (Actualizado: {data['updated']}):\n{tabla}"
    except requests.exceptions.RequestException as e:
        # Manejar errores de la solicitud
        return f"Error en la solicitud: {str(e)}"
    except ValueError:
        # Manejar errores de conversión JSON
        return "Error al procesar la respuesta JSON"
    except KeyError:
        # Manejar errores de clave no encontrada en el diccionario
        return "Error: Clave no encontrada en la respuesta"

if __name__ == '__main__':
    # Imprimir las cotizaciones obtenidas
    print(obtener_cotizaciones())
