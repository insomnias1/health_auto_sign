from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import yagmail
import schedule

username = 'xxx'# 学号
passwd  = 'xxx'# 密码
tw = '36.5'
zwtw = '36.5'
sender = 'xxx'# 发件邮箱
password = 'xxx'# QQsmtp服务的授权码，自行百度获得
server = 'smtp.qq.com'
receivers = ['xxx']# 收件邮箱
subject = '健康信息'
contents = ['打卡成功！！！']

def is_element_present(browser, id):
    from selenium.common.exceptions import NoSuchElementException

    try:
        element = browser.find_element_by_id(id)
    except NoSuchElementException as e:
        # print(e)
        return False
    else:
        return True



def SATRT():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    browser = webdriver.Chrome(options=chrome_options)
    browser.get("http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp;jsessionid=5E6D7D70A7B28EFE72EFDE35D2F49E08?_p=YXM9MiZ0PTImZD0xMDEmcD0xJmY9MzAmbT1OJg__&_l=&_t=")
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(passwd)
    browser.find_element_by_id("passbutton").click()
    print("登陆成功,Checking whether User {0} has signed in".format(username))
    time.sleep(2)

    browser.find_element_by_id("input_tw").send_keys(tw)
    browser.find_element_by_id("input_zwtw").send_keys(zwtw)
    time.sleep(2)
    FLAG = True
    while(FLAG):
        try:
            button =  browser.find_element_by_id("post").click()
            browser.execute_script(button)
            time.sleep(2)
            FLAG = False
        except:
            FLAG = False
    browser.quit()


# SMTP用于发邮件
def send_mail():
    mail = yagmail.SMTP(user=sender, password=password, host=server)
    mail.send(to=receivers, subject=subject, contents=contents)
    print("successfully")
    while True:
        schedule.run_pending()


if __name__ == "__main__":
    SATRT()
    send_mail()

