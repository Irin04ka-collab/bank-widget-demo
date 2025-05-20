from datetime import datetime

from utils import load_file

if __name__ == '__main__':
    operations = load_file()
    # print(operations[3])
    # print(datetime.fromisoformat("2019-08-26T10:50:58.294041"))
    sorted_operations = sorted(operations, key=lambda x: x.date)

    for operation in sorted_operations[:5]:
        if operation.state == "EXECUTED":
            print(f"{sorted_operations[2].get_text()}\n")
