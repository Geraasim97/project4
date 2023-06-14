from utils import load_file,make_operations,get_executed_five

FILE_URL = "../../../coursework3/json_file/operations.json"


def main():
    try:
        operations_list = load_file(FILE_URL)
        operations = make_operations(operations_list)
        print(get_executed_five(operations))
    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    main()