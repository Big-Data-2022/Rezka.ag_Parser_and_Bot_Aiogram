# import json
import json
# from bs4 import BeautifulSoup
# with open("core/all_kino.json", "r") as file:
#     all_kino = json.load(file)

# a = []
# for i in all_kino:
#     a.append(i.values())
# print(a)

# a =  {"fdjsf":{
#     "url":"dsf"
# }}
# b = {'fkdksf':11}

# a["fdjsf"].update(b)
# print(a)

with open("core/all_kino.json", "r") as file:
    read_file = json.load(file)

for item in read_file:
    for k in item.values():
        info = k

        b ={
            "url" : info["url"],
            "photo" : info["photo"],
            "description" : info["description"]
        }


    for j in item.keys():
        name = j
        
        a = {
            "title" : name,
        }
        
        a.update(b)
        print(a)
        


