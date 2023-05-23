import json

way = 'C:\\Users\\Админ\\Desktop\\json\\fromIgor\\output.json'

x = {
"name": "Игорь",
"age": 99,
"city": "Курск"
}

with open(way, 'w', encoding='utf-8') as file:
    json.dump(x, file, ensure_ascii=False, indent='\t')



with open(way, 'r', encoding='utf-8') as f:
    templates = json.load(f)

print(templates)
# {'name': 'Игорь', 'age': 99, 'city': 'Курск'}
print(type(templates))
# <class 'dict'>