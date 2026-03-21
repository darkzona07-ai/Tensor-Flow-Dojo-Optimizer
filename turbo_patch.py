import socket
import numpy as np

def apply_zero_copy_patch(sock, tensor_data):
    # Прямая передача тензорного буфера без копирования
    # Оптимизировано для Win7 / ASUS X550CC
    raw_buffer = memoryview(tensor_data.numpy())
    try:
        sent_bytes = sock.send(raw_buffer)
        return sent_bytes == len(raw_buffer)
    except Exception:
        return False
