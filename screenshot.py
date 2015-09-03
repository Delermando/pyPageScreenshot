import os
import time
from selenium import webdriver
from pyvirtualdisplay import Display
import sys


display = Display(visible=1, size=(600, 700))
display.start()
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(sys.argv[2])
time.sleep(2)
driver.save_screenshot("app/static/mandalas/"+sys.argv[1]+".png");
driver.close()
driver.quit()
display.stop()