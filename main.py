import requests
import json
from bs4 import BeautifulSoup as bs

url = "https://github.com/trending"
page = requests.get(url)
soup = bs(page.text, "html.parser")

json_text = []
stars = list()#список всех звёзд
i = 0 #переменная для поиска нужных звёзд

all_rep_n = soup.findAll('span', class_="text-normal")
all_stars = soup.findAll('svg', class_="octicon octicon-star")

for star in all_stars:
    stars.append((star.parent.text).split()[0])

for repositories in all_rep_n:
    info = {'id':'%.0f' % (i/2+1), 'name':(repositories.parent).text.split()[0], 'author':(repositories.parent).text.split()[2], 'Stars': stars[i]}
    i+=2
    print(f"{info['id']}. Repository: {info['name']} / {info['author']}; Stars: {info['Stars']};")
    json_text.append(info)

with open("data.json", "w", encoding='utf-8') as file:
    json.dump(json_text, file, indent=4, ensure_ascii=True)

with open("index.html", "w", encoding='utf-8') as file:
    file.write("<html><head><title>Repositories</title>\n<style>div{text-align: center;width: 70%;margin: auto;min-height: 500px;background: #22262b; }\na{text-decoration: none;color:aliceblue;}\na:visited{text-decoration: none;color:aliceblue;}\na:hover{text-decoration: none;color: antiquewhite;}\nbody{background: linear-gradient(#262e36, #020014);color:aliceblue;}\nh2{color:aliceblue}\ntable {width: 100%;border-collapse: collapse;}\ntd, th{border: 1px solid #020014;padding: 8px;text-align: center;}\n</style>\n</head>\n<body>\n<div>\n")
    file.write("<h2>\nRepositories\n<table>\n<tr>\n<th>№</th>\n<th>Name</th>\n<th>Author</th>\n<th>Stars</th>\n</tr>\n")
    for i in range(len(json_text)):
        file.write(f"<tr>\n<td>{json_text[i]['id']}</td>\n<td>{json_text[i]['name']}</td>\n<td>{json_text[i]['author']}</td>\n<td>{json_text[i]['Stars']}</td>\n</tr>")
    file.write("</table>\n<a href='https://github.com/trending'>To GitHub.com/trending</a>\n")
    file.write("</div>\n</body></html>")