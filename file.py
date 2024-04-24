import time
import os
import logging
import random

# Set up logging to write to standard output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_file():
    # Generate a random number to append to the filename
    random_number = random.randint(1000, 9999)
    file_path = f'/test/test-random{random_number}.csv'
    with open(file_path, 'w') as f:
        f.write('initial content\n')
    logging.info(f"File created: {file_path}")
    return file_path

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        logging.info("Read from file: %s", content.strip())
    except Exception as e:
        logging.error("Failed to read file: %s", str(e))

def write_to_file(file_path):
    try:
        with open(file_path, 'a') as f:
            f.write('new line\n')
        logging.info("Wrote to file: new line")
    except Exception as e:
        logging.error("Failed to write to file: %s", str(e))

def main():
    while True:
        # Ensure the /test directory exists
        if not os.path.exists('/test'):
            os.makedirs('/test')
        
        # Create a new file and set a timer
        file_path = create_file()
        start_time = time.time()

        while time.time() - start_time < 60:  # Run this loop for 1 minute
            time.sleep(5)
            read_file(file_path)
            time.sleep(5)
            write_to_file(file_path)
        
        # After 1 minute, remove the file and start over
        os.remove(file_path)
        logging.info(f"File removed: {file_path}")

if __name__ == "__main__":
    main()
