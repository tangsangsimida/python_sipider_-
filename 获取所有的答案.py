import json
import time
import selenium.webdriver
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("./answer_id.json", "r") as f:
        question_answer_id: dict = json.load(f)
    # 把所有的题目id拿到;
    google = selenium.webdriver.Chrome(r'D:\软件\google\ChromeCore\chromedriver.exe')
    url = 'https://www.jiakaobaodian.com/mnks/exercise/0-car-kemu1-beijing.html?id=800500'
    google.get(url)
    time.sleep(4)
    # 等待页面加载完成
    google.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div[1]/div[2]/label/input').click()
    # 取消正确直接下一题
    # for i, key in question_answer_id.items():
    for i in range(2250):  # 待优化----------------------------------------------------************************************************
        # 获取当前的题号
        time.sleep(0.2)
        html = google.page_source
        soup = BeautifulSoup(html, "html.parser")
        question_id = soup.find('div', class_="options-w left").get('data-questionid')
        # 先判断是否有为一个选择题
        try:
            # 是个选择题，点击a
            google.find_element_by_xpath('//*[@id="ComQuestionDetail_qundefined"]/div[2]/div/p[1]').click()
            # 寻找正确的答案
            time.sleep(0.2)
            html = google.page_source
            soup = BeautifulSoup(html, "html.parser")
            try:
                # 点击的答案是错的，获取正确的答案
                answer = soup.find('p', class_='success bug').text
                # 将正确的答案放进题号字典
                question_answer_id[f'{question_id}'] = answer
                print(question_id, end='-------->>')
                print(answer)
            except:
                # 点击的答案是正确的，直接提取正确的答案
                answer = soup.find('p', class_="success").text
                # 将正确的答案放进题号字典
                question_answer_id[f'{question_id}'] = answer
                print(question_id, end='-------->>')
                print(answer)
        except:
            # 是个判断题
            google.find_element_by_xpath('//*[@id="ComQuestionDetail_qundefined"]/div[2]/div/p[1]').click()
            # 点击a选项下面进行判断答案
            time.sleep(0.2)
            html = google.page_source
            soup = BeautifulSoup(html, "html.parser")
            try:
                # 点击的答案是错的，获取正确的答案
                answer = soup.find('p', class_='success bug').text
                # 将正确的答案放进题号字典
                question_answer_id[f'{question_id}'] = answer
                print(question_id, end='-------->>')
                print(answer)
            except:
                # 点击的答案是正确的，直接提取正确的答案
                answer = soup.find('p', class_="success").text
                # 将正确的答案放进题号字典
                question_answer_id[f'{question_id}'] = answer
                print(question_id, end='-------->>')
                print(answer)
        finally:
            google.find_element_by_xpath(
                '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div[1]/div[1]/button[2]').click()
    with open("./answer_id.json", 'w') as f:
        json.dumps(question_answer_id, sort_keys=False, indent=4, separators=(',', ': '))
    print(question_answer_id)

    '''
    还是会存在跳的情况，但是只有10道左右直接手动填上就行了，要是想不跳的话调整一下点击速度就行了
    '''
