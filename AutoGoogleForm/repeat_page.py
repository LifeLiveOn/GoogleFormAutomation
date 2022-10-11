import package
from selenium.webdriver.common.by import By
import random as rand
import time
from selenium.common.exceptions import WebDriverException

browser = package.browser


def findElement(value):
    try:
        return browser.find_element(By.XPATH, f"//*[contains(text(),'{value}')]")
    except WebDriverException:
        return "cant find the element"


def randomNumber(a, b):
    return rand.randint(a, b)


def validateAge60():
    try:
        findElement("18-25").click()
        findElement("Student").click()
    except:
        pass


def repeat_page():

    # time.sleep(randomNumber(1, 2))
    list_of_question = browser.find_elements(By.CLASS_NAME, 'Qr7Oae')
    random_choice = ""
    for question in range(1, len(list_of_question) + 1):
        # this is for radio button choice that align by row
        if bool(browser.find_elements(By.XPATH,
                                      f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div/div['
                                      f'2]/div/div/span/div/div')):
            choices = browser.find_elements(By.XPATH,
                                            f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div/div['
                                            f'2]/div/div/span/div/div')
            if rand.randint(1, 4) == 4:
                random_choice = browser.find_element(By.XPATH,
                                                     f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div'
                                                     f'/div[2]/div/div/span/div/div[{randomNumber(1, 4)}]')
            elif rand.randint(1, 10) == 5:
                random_choice = browser.find_element(By.XPATH,
                                                     f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div'
                                                     f'/div[2]/div/div/span/div/div[{randomNumber(1, len(choices))}]')

            random_choice.click()
        # radio button that align by column
        elif bool(browser.find_elements(By.XPATH,
                                        f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div/div[2]/div['
                                        '1]/span/div/label')):

            try:
                choices = browser.find_elements(By.XPATH,
                                                f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div/div['
                                                f'2]/div[ '
                                                '1]/span/div/label')
                if rand.randint(1, 8) == 8:
                    random_choice = browser.find_element(By.XPATH,
                                                         f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div'
                                                         f'/div[2]/div[1]/span/div/label[{randomNumber(1, 3)}]')
                else:
                    random_choice = browser.find_element(By.XPATH,
                                                         f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div'
                                                         f'/div[2]/div[1]/span/div/label[{randomNumber(3, len(choices))}]')
                random_choice.click()
            except ValueError:
                question += 1
        # radio button that align by column and row, has to use an for loop inside and screw down to bottom
        elif bool(browser.find_elements(By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div/div['
                                                  f'2]/div/div[1]/div/div[2]/span/div')):

            lst_col = browser.find_elements(By.XPATH,
                                            f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div/div['
                                            f'2]/div/div[1]/div/div[2]/span/div')
            lst_row = browser.find_elements(By.XPATH,
                                            f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div/div/div['
                                            f'2]/div/div[1]/div/div')

            for row in range(2, len(lst_row), 2):
                if rand.randint(1, 5) == 5:
                    # random_choice = browser.find_element(By.XPATH,
                    #                                      f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div'
                    #                                      f'/div/div[2]/div/div[1]/div/div[{row}]/span/div['
                    #                                      f'{randomNumber(2, len(lst_col))}]')
                    random_choice = browser.find_element(By.XPATH,
                                                         f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div'
                                                         f'/div/div[2]/div/div[1]/div/div[{row}]/span/div['
                                                         f'{randomNumber(2, len(lst_col))}]')
                else:
                    random_choice = browser.find_element(By.XPATH,
                                                         f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{question}]/div'
                                                         f'/div/div[2]/div/div[1]/div/div[{row}]/span/div['
                                                         f'{randomNumber(4, 6)}]')

                random_choice.click()

                time.sleep(0.5)
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)//span[contains(., '{option1}')]")
