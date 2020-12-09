"""
Emular Cat


python cli/reader.py leer <path/to/file.txt>
"""


import fire


class LectorArchivos:
    def leer(self, filename):
        with open(filename, 'r') as file1:
            content = file1.read()
        return content


if __name__ == "__main__":
    fire.Fire(LectorArchivos)
