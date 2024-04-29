import time
import os
import logging
import traceback

# Configuración del logging para escribir en la salida estándar
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ensure_file_exists(file_path):
    """
    Asegura que el archivo exista en el sistema de archivos. Si no existe, lo crea con contenido inicial.
    """
    try:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write('initial content\n')
            logging.info(f"File created: {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")
    except Exception as e:
        logging.error(f"Error creating file {file_path}: {str(e)}")
        traceback.print_exc()

def read_file(file_path):
    """
    Intenta leer el contenido del archivo y loguea el contenido o el error en caso de fallo.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        logging.info("Read from file: %s", content.strip())
    except Exception as e:
        logging.error(f"Failed to read file {file_path}: {str(e)}")
        traceback.print_exc()

def write_to_file(file_path, pod_name):
    """
    Intenta escribir un nuevo registro con timestamp en el archivo y loguea la acción o el error en caso de fallo.
    """
    try:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = f"{current_time} - New entry added from pod {pod_name}\n"
        with open(file_path, 'a') as f:
            f.write(message)
        logging.info("Wrote to file: %s", message.strip())
    except Exception as e:
        logging.error(f"Failed to write to file {file_path}: {str(e)}")
        traceback.print_exc()

def main():
    file_name = 'test1.csv'
    base_path = '/test/'
    pod_name = os.getenv('HOSTNAME', 'Unknown Pod')

    # Asegura que el directorio /test existe
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    file_path = os.path.join(base_path, file_name)
    ensure_file_exists(file_path)

    while True:
        read_file(file_path)
        time.sleep(5)
        write_to_file(file_path, pod_name)
        time.sleep(5)

if __name__ == "__main__":
    main()
