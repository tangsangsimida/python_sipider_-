import time
import selenium.webdriver
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    selector = 0
    with open("./answer_id.json", 'r', encoding="utf-8") as f:
        answers: dict = json.load(f)  # 把答案字典返回
    google = selenium.webdriver.Chrome(r'D:\软件\google\ChromeCore\chromedriver.exe')
    url = 'https://www.jiakaobaodian.com/mnks/exam/car-kemu1-beijing.html'
    google.get(url)
    time.sleep(4)
    google.find_element_by_xpath('/html/body/div/div[15]/div/div[2]/div/div/div/div/div[2]/button').click()
    '''点击开始开始考试'''
    html = google.page_source
    soup = BeautifulSoup(html, "html.parser")
    data_questionid_lis = soup.find("div", class_='datika').find_all('li')
    questions = []
    for a in data_questionid_lis:
        questions.append(a.find('a').get('data-questionid'))
    # questions -----> 所有的题目编号
    for i in questions:
        # i----->>>单个题目的id
        the_answer = answers.get(f"{i}")
        # 获取当前的N个选项的值：
        time.sleep(0.1)
        html = google.page_source
        soup = BeautifulSoup(html, "html.parser")
        buttons = soup.find('div', class_="options-w left").find_all("p")
        for j in range(len(buttons)):
            buttons[j] = buttons[j].string
        # 把所有的按钮对象转换成按钮所对应的答案文字
        for x in range(len(buttons)):
            if the_answer[2:] == buttons[x][2:]:
                selector = x
                break
            # 这个答案必须截取从第3位开始的字符串
            # selector----->>获取当前题目的答案------>>0,1,2,3;;;
            # print(buttons.index(f"{the_answer}"))
        if selector == 0:
            google.find_element_by_xpath(
                '/html/body/div[1]/div[5]/div/div/div/div[2]/fieldset/div[2]/div/button[1]').click()
        elif selector == 1:
            google.find_element_by_xpath(
                '/html/body/div[1]/div[5]/div/div/div/div[2]/fieldset/div[2]/div/button[2]').click()
        elif selector == 2:
            google.find_element_by_xpath(
                '/html/body/div[1]/div[5]/div/div/div/div[2]/fieldset/div[2]/div/button[3]').click()
        elif selector == 3:
            google.find_element_by_xpath(
                '/html/body/div[1]/div[5]/div/div/div/div[2]/fieldset/div[2]/div/button[4]').click()
        else:
            print(i)
            google.find_element_by_xpath(
                "/html/body/div[1]/div[5]/div/div/div/div[2]/fieldset/div[2]/div/button[1]").click()
            # 没有找到正确答案先输出题号,再选择A继续答题
        # time.sleep(0.2)
    print("考试已完成")
