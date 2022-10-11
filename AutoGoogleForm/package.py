
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
# option.add_argument("--headless")
# option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='package/chromedriver.exe', options=option)
url = "https://docs.google.com/forms/d/e/1FAIpQLSd6jTi7_whIISHAPZ923gYqt0XEqz3f-fTPry81xOfdHhr8YQ/viewform?fbclid=IwAR1rzrl40wdCUX70LtQ3R6wm--3sC3oYZTlBChwbGYeb4xviQCUAgnJXwDI"
url_form1 = "https://docs.google.com/forms/d/e/1FAIpQLSffZrGfu20BtLGURv5wEPWZSA-QoGGF2L4Xu7O8N7mCylrs3Q/viewform?usp=sf_link"
url_form2= "https://docs.google.com/forms/d/e/1FAIpQLSfS7P_T0snrW780eICi1NWuznCO8iY7zqzhZVi__8pEB9T31w/viewform?usp=sf_link"
# url ="https://docs.google.com/forms/d/e/1FAIpQLSf9wiF6Riigs-sQZviXQ-MpBoVPalM0EYSQMn-P-Yp89pqcEA/viewform"
browser.get(url_form1)