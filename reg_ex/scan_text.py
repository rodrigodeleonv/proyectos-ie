import os
import re


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    with open(os.path.join(BASE_DIR, 'file1.txt'), 'r') as f1:
        content = f1.read()
    print(content)
    nombres = re.findall(r'^\w+\s\w+\s', content, re.M)
    print(nombres)
    edades = re.findall(r'\s\d{2}\s', content, re.M)
    print(edades)
    dpis = re.findall(r'\d{13}', content, re.M)
    print(dpis)
    fechas = re.findall(r'\d{2}/\d{2}/\d{4}', content, re.M)
    print(fechas)
