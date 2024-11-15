# TODO решите задачу
import json
def task() -> float:
    filename='input.json'
    with open(filename) as a:
        json_data = json.load(a)
    sum_value = sum([item['score']*item['weight'] for item in json_data])
    return round(sum_value,3)
print(task())







