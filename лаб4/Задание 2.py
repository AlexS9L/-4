# TODO импортировать необходимые молули
import json
import  csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as a:
         l = [line for line in csv.DictReader(a)]

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as b:
        json.dump(l, b, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
