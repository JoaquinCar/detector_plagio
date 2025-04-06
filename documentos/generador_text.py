import random
import os

# Función para generar un documento de texto con palabras simples
def generar_documento(nombre_archivo, num_palabras=100):
    palabras_simples = ["hola", "mundo", "python", "programar", "codigo", "algoritmo", "texto", "documento", "aprendizaje", "inteligente"]
    texto = " ".join(random.choices(palabras_simples, k=num_palabras))

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)

num_documentos = 20  # Número de documentos a generar

# Crear una carpeta para almacenar los documentos generados
directorio_documentos = 'detector_plagio\documentos\documentos_generados'

if not os.path.exists(directorio_documentos):
    os.makedirs(directorio_documentos)

# Generar los documentos solicitados
for i in range(num_documentos):
    generar_documento(f'{directorio_documentos}/documento_{i+1}.txt')

# Verificar que los documentos han sido creados
print("Archivos generados:", os.listdir(directorio_documentos))