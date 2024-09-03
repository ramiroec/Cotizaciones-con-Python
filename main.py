import requests

url = 'https://dolar.melizeche.com/api/1.0/'

# Realizar la solicitud GET a la API
response = requests.get(url)
if response.status_code == 200:
    # Convertir la respuesta JSON a un diccionario de Python
    data = response.json()

    # Crear una lista para mostrar los datos
    cotizaciones = []

    # Extraer y agregar las cotizaciones a la lista
    for casa, valores in data['dolarpy'].items():
        compra = valores.get('compra', 'N/A')
        venta = valores.get('venta', 'N/A')
        cotizaciones.append(f"{casa.capitalize()}: Compra - {compra}, Venta - {venta}")

    # Formatear y devolver el resultado
    resultado = f"Cotizaciones del Dólar (Actualizado: {data['updated']}):\n" + "\n".join(cotizaciones)
    print(resultado)
else:
    print(f"Error en la solicitud: {response.status_code}")
