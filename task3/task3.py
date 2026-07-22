import sys
import json
values_json=sys.argv[1]
tests_json=sys.argv[2]
report_json=sys.argv[3]
with open(values_json, 'r', encoding='utf-8') as f:
    values_data = json.load(f)
    value_dict = {item["id"]: item["value"] for item in values_data["values"]}

with open(tests_json,'r',encoding ='utf-8') as f:
    tests_data=json.load(f)


def fillvalues(file):
    for item in tests_data["tests"]:
        print(item)
        print(f"{item["id"]} hihih")
    if isinstance(file, dict):
        if "id" in file and "value" in file:
            file["value"] = value_dict.get(file["id"], file["value"])

        for key, val in file.items():
            fillvalues(val)
    elif isinstance(file, list):
        for item in file:
            fillvalues(item)
fillvalues(tests_data)


with open(report_json,'w',encoding ='utf-8') as f:
    json.dump(tests_data, f, indent=2, ensure_ascii=False)
