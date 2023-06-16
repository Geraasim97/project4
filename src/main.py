from utils import load_file,make_operations,get_executed_five

file_url = "../json_file/operation.json"


def main():
    try:
        operations_list = load_file(file_url)
        operations = make_operations(operations_list)
        print(get_executed_five(operations))
    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    main()