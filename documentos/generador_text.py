import random
import os

# Función para generar un documento de texto con palabras simples
def generar_documento(nombre_archivo, num_palabras=100):
    palabras_simples = ["hola", "mundo", "python", "programar", "codigo", "algoritmo", "texto", "documento", "aprendizaje", "inteligente", "Machine Learning", "redes", "neuronales", "datos", "análisis", "ciencia", "informática", "tecnología", "computadora", "software", "hardware", "programación", "desarrollo", "sistema", "aplicación", "función", "variable", "bucle", "condicional", "lista", "diccionario", "conjunto", "tupla"]
    texto = " ".join(random.choices(palabras_simples, k=num_palabras))

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)

num_documentos = 40  # Número de documentos a generar

# Ruta de la carpeta donde se guardarán los documentos
directorio_documentos = 'documentos/documentos_generados'

# Crear la carpeta si no existe
if not os.path.exists(directorio_documentos):
    os.makedirs(directorio_documentos)
    print(f"Carpeta creada: {directorio_documentos}")

# Generar los documentos solicitados
for i in range(num_documentos):
    generar_documento(f'{directorio_documentos}/documento_{i+1}.txt')

# Verificar que los documentos han sido creados
print("Archivos generados:", os.listdir(directorio_documentos))