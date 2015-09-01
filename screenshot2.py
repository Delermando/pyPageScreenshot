import os
import time
from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(600, 700))
display.start()
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("file:///home/dalves/Documentos/Repositorios/pyPageScreenshot/mandala.html")
time.sleep(5)
driver.save_screenshot("diogo.jpg");
driver.quit()