import json

way = 'C:\\Users\\Админ\\Desktop\\json\\output.json'

x = {
"name": "Игорь",
"age": 99,
"city": "Курск"
}

with open(way, 'w', encoding='utf-8') as file:
    json.dump(x, file, ensure_ascii=False, indent='\t')

