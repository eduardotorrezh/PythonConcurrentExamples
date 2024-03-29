import os
import logging
import time
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)



if __name__ == '__main__':
    current_process = multiprocessing.current_process()
    pid = current_process.pid
    name = current_process.name

    logging.info(f'El proceso actual es {current_process}')
    logging.info(f'El ID del proceso actual es {pid}')
    logging.info(f'El nombre del proceso actual es {name}')
