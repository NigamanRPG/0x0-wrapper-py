import os
import requests
import argparse
def main():
    try:
        parser = argparse.ArgumentParser(description='0x0 Wrapper')
        parser.add_argument("--f", default=1, help="To download the file to 0x0.st")
        args = parser.parse_args()
        f = args.f
        path = os.path.join(f)
        if not os.path.exists(path):
            return print("Файл не найден")        
        
        testing_size = os.path.getsize(path)
        if testing_size >= 536870912:
            return print("Вес файла превышает 512 MiB")
        
        files = {'file': open(path, 'rb')}
        r = requests.post("https://0x0.st", files=files)
        print(r.text)
    except TypeError:
        parser.print_help()
    except:
        print("Неизвестная ошибка")
main()
