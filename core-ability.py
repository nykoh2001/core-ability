from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from random import randrange

import os
from dotenv import load_dotenv

load_dotenv()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 새로 업데이트 된 내용에 따라 크롭 브라우저 작동 후 유지하도록 옵션 설정
browser = webdriver.Chrome(options=chrome_options)

# 사이트 접속
browser.get("https://ddp.dongguk.edu/login.jsp")

# 아이디 입력
useridInput = browser.find_element(By.ID, "userid")
useridInput.send_keys("2021111896")

# .env 파일의 비밀번호 가져오기
# 비밀번호 입력
password = os.environ.get("PASSWORD")
userpwInput = browser.find_element(By.ID, "userpw")
userpwInput.send_keys(password)

# 로그인 버튼 클릭
login_button = browser.find_element(By.XPATH, '//*[@id="login1"]/div[1]/a')
login_button.click()

# action 객체 생성
actions = ActionChains(browser)

# 인증/진단 버튼 위에 hover
certificate_diagnosis = browser.find_element(By.XPATH, '//*[@id="gnb"]/li[3]/a')
actions.move_to_element(certificate_diagnosis).perform()

# 핵심 역량 진단 검사 클릭
core_ability_test = browser.find_element(
    By.XPATH, '//*[@id="gnb"]/li[3]/div/div/ul/li[2]/a'
)
core_ability_test.click()

# 검사 시작 버튼
test_button = browser.find_element(By.XPATH, '//*[@id="DiagnosisrstForm"]/div[2]/a[1]')
test_button.click()

# 검사 문항 체크
radios = browser.find_elements(By.CLASS_NAME, "radio_group")
for r_num in range(len(radios)):
    num = randrange(3, 6)
    radio = browser.find_element(
        By.XPATH, f'//*[@id="DiagnosisrstForm"]/div[3]/table/tbody/tr[{r_num+1}]'
    )
    current = browser.find_element(
        By.XPATH, f'//*[@id="resultscore_{417 + r_num}_{num}"]'
    )
    current.click()

# 저장
save_button = browser.find_element(By.XPATH, '//*[@id="DiagnosisrstForm"]/div[4]/a[2]')
save_button.click()

try:
    # 확인 경고창 처리
    result = browser.switch_to.alert
    result.accept()
except:
    "There is no alert"
