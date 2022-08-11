import selenium.webdriver
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    dict_question = {}
    url = "https://www.jiakaobaodian.com/mnks/exercise/0-car-kemu1-beijing.html?id=800500"
    google = selenium.webdriver.Chrome(r'D:\软件\google\ChromeCore\chromedriver.exe')
    google.get(url)
    html = google.page_source
    google.quit()
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    ul = soup.find('ul', class_="list-w clearfix hide")
    li_all = ul.find_all("li")
    '''
    数据库更新了之后只需要将对应更新的题数加上即可-----------------------------------------------**************************************
    '''
    li_all = li_all[0:2204]
    for li in li_all:
        i = li.find('a')
        dict_question[f'{i.get("data-id")}'] = f"{eval(i.get('data-index')) + 1}"
    dict_json = json.dumps(dict_question, sort_keys=False, indent=4, separators=(',', ':'))
    with open("./question.json",'w') as f:
        f.write(dict_json)
