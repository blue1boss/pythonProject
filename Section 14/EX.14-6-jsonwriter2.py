import json

dict_list = [
    {
        'name':'james',
        'age': 20,
        'spec': [
            175.5,
            70.5
        ]
    },
    {
        'name':'홍길동',
        'age': 21,
        'spec': [
            182.5,
            79.5
        ]
    }
]

#indent들여쓰기,한글읽기가 가능한 ascii
json_string=json.dumps(dict_list, indent=4, ensure_ascii=False)
with open('dictList.json','w',encoding='UTF-8')as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다.')