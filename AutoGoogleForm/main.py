from selenium.common import WebDriverException
import random as rand
import package
from repeat_page import repeat_page, findElement, validateAge60

browser = package.browser

while True:

    try:
        if rand.randint(1, 2) == 2:
            repeat_page()
        elif rand.randint(1, 4) == 4:
            findElement("Male").click()
            repeat_page()
        else:
            findElement("Female").click()
            repeat_page()
            validateAge60()

    except:
        pass
    # try:
    #     if rand.randint(1, 5) == 5:
    #         findElement("No").click()
    #     else:
    #
    # except WebDriverException:
    #     pass
    # except AttributeError:
    #     pass
    try:
        findElement("Yes").click()
    except:
        try:
            findElement("Next").click()

        except:  # If could not find the next button of the form, find the submit button
            submit_btn = findElement("Submit")
            submit_btn.click()
    try:
        findElement("Next").click()

    except:  # If could not find the next button of the form, find the submit button
        submit_btn = findElement("Submit")
        submit_btn.click()

# ?phan row,col nay no chia ra nhu tung cau hoi nen phai xai for loop o trong nua
# list_of_question = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[{2,4,6,8}]/span/div[{2-6}]')

# lst_col = browser.find_elements(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div')
# lst_row = browser.find_elements(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div')
# even_row = len(lst_row)-len(lst_col)+1
# print(len(lst_col))
