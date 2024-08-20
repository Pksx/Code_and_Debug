"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#Intialize the driver
driver = webdriver.Chrome(executable_path = "D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe")

#Web driver basic methods
#get : it is lunch the new browser and to open the URL
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)

print(dir(driver))
#using ID locator
driver.find_element_by_id("txtUsername").send_keys("Admin")
time.sleep(3)
#using NAME locator
driver.find_element_by_name("txtPassword").send_keys("admin123")
time.sleep(3)
#using class locator
driver.find_element_by_class_name("button").click()

#using Link text locator
driver.find_element_by_link_text("Admin").click()
#using CSS selector ID locator (or) CSS selector class name
driver.find_element_by_css_selector("input#searchSystemUser_userName").send_keys("mounika")
#using partial link text locator
driver.find_element_by_partial_link_text("Admin").click()
"""



#all locators examples
"""
from selenium import webdriver
import time

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
#using name locator
driver.find_element_by_name("username").send_keys("Admin")
time.sleep(5)
driver.find_element_by_name("password").send_keys("admin123")
time.sleep(5)
#using relativexpath  locator
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
#using link_text locator
driver.find_element_by_link_text("Admin").click()
time.sleep(5)
#using partical link
driver.find_element_by_partial_link_text("Perfor").click()
time.sleep(5)
#using absloutexpath  locator
driver.find_element_by_xpath("/html/body/div/div/div/aside/nav/div/ul/li[2]/a/span").click()
#using tagname locator
time.sleep(5)
driver.find_element_by_tag_name("a").click()
time.sleep(10)
driver.close()

"""

"""
#Emplicity wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.amazon.in/")
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox"))).send_keys("pen")

"""




"""
#2.select class[for dropdownbox]

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://demo.guru99.com/test/newtours/register.php")
time.sleep(5)
dropdown_obj=driver.find_element_by_xpath("//select[@name='country']")
action_list_items=Select(dropdown_obj)
list_items=action_list_items.options
#select_by_index
action_list_items.select_by_index(index=6)
#select_by_text
action_list_items.select_by_visible_text("INDIA")
time.sleep(20)
driver.close()
"""

"""
#3.Action_chains[for mouse operations]

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(5)
#using name locator
driver.find_element_by_name("username").send_keys("Admin")
time.sleep(5)
driver.find_element_by_name("password").send_keys("admin123")
time.sleep(5)
#using relativexpath
locator
driver.find_element_by_xpath("//button[@type='submit']").click()
#time.sleep(5)
#act_admin=driver.find_element_by_link_text("Admin")
act_obj=ActionChains(driver)
time.sleep(9)
#perform move element
#act_obj.move_to_element(act_admin).perform()
#perform the click
#act_obj.context_click(act_admin).perform()
#click_and_hold
click_hold=driver.find_element_by_partial_link_text("Perfor")
time.sleep(3)
act_obj.click_and_hold(click_hold).perform()
time.sleep(5)
driver.close()

"""

"""
#4.actionchains(keyboardoperations)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(3)
wb=driver.find_element_by_name("username")
wb.send_keys("Admin")


act_obj=ActionChains(driver)

#time.sleep(5)
#act_obj.double_click(wb).perform()

#cntl-a
act_obj.key_down(Keys.LEFT_CONTROL).send_keys("a").key_up(Keys.LEFT_CONTROL).perform()
#act_obj.key_down(keys.LEFT_CONTROL).send_keys("a").key_up(keys.LEFT_CONTROL).perform()

#Ctrl-c
act_obj.key_down(Keys.LEFT_CONTROL).send_keys("c").key_up(Keys.LEFT_CONTROL).perform()
time.sleep(2)

#Press TAB
act_obj.send_keys(Keys.TAB).perform()
time.sleep(2)

#Ctrl-v
act_obj.key_down(Keys.LEFT_CONTROL).send_keys("v").key_up(Keys.LEFT_CONTROL).perform()

time.sleep(10)
driver.close()
"""
"""
#scroll &up_down
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.amazon.in/")
ele=driver.find_element_by_tag_name("html")
time.sleep(5)
ele.send_keys(Keys.END)
time.sleep(5)
driver.execute_script("window.scrollTo(0,600)")
time.sleep(5)
ele.send_keys(Keys.HOME)

"""




"""
#drag_drop by using action chains
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)
driver.get("http://demo.guru99.com/test/drag_drop.html")
source_path=driver.find_element_by_xpath("//a[text()=' BANK ']")
destination_path=driver.find_element_by_xpath("//li[@class='placeholder'][1]")
#obj_act
act_obj=ActionChains(driver)
act_obj.drag_and_drop(source_path,destination_path).perform()
"""


"""
#5.windows handling

from selenium import webdriver
import time

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")

driver.find_element_by_xpath("//span[@class='nav-line-2 ']").click()

driver.find_element_by_xpath("//input[@type='email']").send_keys("gopialone23@gmail.com")
driver.find_element_by_id("continue").click()
driver.find_element_by_xpath("//input[@type='password']").send_keys("Gopi@12345")
driver.find_element_by_xpath("//input[@id='signInSubmit']").click()
driver.find_element_by_xpath("//input[@type='text']").send_keys("pen")
driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()
driver.find_element_by_xpath("//span[@class='a-size-base-plus a-color-base a-text-normal'][1]").click()
#driver.find_element_by_xpath("//img[@alt='Parker Ambient Laque Black CT Roller Ball Pen']").click()

list_of_windows=driver.window_handles
print(driver.title)
print(list_of_windows)
for i in list_of_windows:
    i[1].close()
#driver.switch_to.window(list_of_windows[1])

"""

"""

from selenium import webdriver
import time

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://demo.guru99.com/test/delete_customer.php")

expmsg="Do you really want to delete this Customer?"
time.sleep(3)
driver.find_element_by_xpath("//input[@type='text']").send_keys("gopi")
time.sleep(3)
driver.find_element_by_name("submit").click()
time.sleep(2)
alt=driver.switch_to.alert

actmsg=alt.text
print(actmsg)

assert expmsg==actmsg

#alt.accept()
alt.dismiss()


"""
"""
#fileuploading
from selenium import webdriver
import time
path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://demo.guru99.com/test/upload/")
driver.find_element_by_name("uploadfile_0").send_keys("C:\\Users\\chand\\OneDrive\\Pictures\\beautiful-evening-landscape-minimal-8k-ag.jpg")
time.sleep(3)
driver.find_element_by_id("submitbutton").click()

"""

"""
#screenshot

from selenium import webdriver
from PIL import Image

path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://demo.guru99.com/test/upload/")
driver.save_screenshot("gopi.png")
# Loading the image
image = Image.open("gopi.png")
 
# Showing the image
image.show()

"""
















































































"""
from selenium import webdriver
import time

class pra_sel:

    def __init__(self):
        self.driver=None
        self.driver_path="D:\\Gopi_all_python\\chromedriver_win32\\chromedriver.exe"
    def intilize_driver(self):
        self.driver=webdriver.Chrome(self.driver_path)
    def lunch_browser(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
    def basic_locatores(self):
        #using name locator
        time.sleep(5)
        self.driver.find_element_by_name("username").send_keys("Admin")
        time.sleep(5)
        self.driver.find_element_by_name("password").send_keys("admin123")
        time.sleep(5)
        #using relativexpath  locator
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
    def close_window():
        time.sleep(10)
        self.driver.close()

obj=pra_sel()
obj.intilize_driver()
obj.lunch_browser()
obj.basic_locatores()
obj.close_window()

"""

        
        





