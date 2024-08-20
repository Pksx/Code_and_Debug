"""
#SELENIUM Architecture:
+-----------------------------+          +-------------------------+          +-----------------+
| Selenium Client Libraries    |          |    JSON Wire Protocol    |          | Web Browser      |
| (Python, Java, C#, etc.)     | <------> | (HTTP over JSON)         | <------> | (Chrome, Firefox)|
+-----------------------------+          +-------------------------+          +-----------------+
         |                                       |                                |
         v                                       v                                |
+--------------------+             +------------------------+                   |
|     Test Script    | <---------> |    WebDriver           |                   |
+--------------------+             +------------------------+                   |
                                                    |                            |
                                                    v                            v
                                        +---------------------------+
                                        |  Browser-Specific Driver  |
                                        |  (ChromeDriver, etc.)     |
                                        +---------------------------+

"""
"""
ADVANATGES AND DISADAVANATEGS IN SELENIUM
ADVANAGTES:
OPER SOURCE
SUPPORTED MULTIPLE BROWSER
SUPPORTED MULTIPLE OPERATING SYSTEM
SUPPOET for multiple langues
parallel test execution
intergartion with other tool
rich community

DISADAVANATEGS 

LIMITED To web application :it is supports only web application .It does nto support desktop or window ,mobile
No built reporting: selenium does not have in built reportinng capabilties. we need to intergra other tools such as junit or testng
or other libraries.
Handling the dynamic  content or pop-up:
selenium can struggle with dynamic web content,such as elements that change frequently, 
as well as handling pop-ups, alerts, and file uploads/downloads.
No Support for Captcha, OTPs, or Two-Factor Authentication:
Selenium cannot handle Captchas, OTPs, or other two-factor authentication methods out of the box
Browser and WebDriver Version Compatibility:
Keeping the WebDriver up to date with the latest browser versions can be challenging,
 and mismatches can lead to issues in script execution.
SPEED:selenium can be slower compared to other tool expecilly when execute the complix scripts.
Requires Programming Knowledge:

"""
"""
NoSuchWindowException: Occurs when the current list of windows isn’t updated, and you can’t switch to a non-existent window.
NoSuchFrameException: Raised when an element tries to interact with a frame that no longer exists in the DOM.
NoSuchElementException: Thrown when an element you’re trying to interact with is not found on the page.
NoAlertPresentException: Happens when you try to handle an alert that doesn’t exist.
InvalidSelectorException: Indicates an issue with the selector syntax.
TimeoutException: Occurs when a command takes more time than the specified or default wait time.
ElementNotVisibleException: Raised when an element is not visible on the page.

what is the use of "findelements" and which scenario we are going to use?
Using findElements is crucial when you need to work with multiple elements that share common attributes or need to validate the presence and count of such elements on a web page

#DISADAVANATAGES OF SELENIUM:
Selenium, while powerful, has some limitations:

Browser Support: It primarily supports web applications and may not handle mobile or desktop apps.
Performance: Can be slower compared to other testing tools due to its reliance on browser interaction.
Complexity: Requires good programming skills to write test scripts.
Maintenance: Test scripts can be brittle and require maintenance with changes in the web application.
No Built-in Reporting: Lacks a comprehensive reporting feature; third-party tools are often needed.

"""

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.XPATH,value="//input[@name='username']").send_keys("admin")
driver.find_element(By.NAME,value="password").send_keys("admin123")

time.sleep(5)
driver.quit()
# driver.close()
"""
import time

"""
#select method
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,value="//input[@name='username']").send_keys("admin")
driver.find_element(By.NAME,value="password").send_keys("admin123")
driver.find_element(By.XPATH,value="//*[@type='submit']").click()
time.sleep(10)
driver.find_element(By.XPATH,value="//*[@class='oxd-main-menu-item active']").click()
time.sleep(5)

drop_down=driver.find_element(By.XPATH,value="//*[contains(text(),'User Role')]/../..//div[@class='oxd-select-text oxd-select-text--active']")
selct_dropdown=Select(drop_down)
selct_dropdown.select_by_value("Admin")
selct_dropdown.select_by_index(2)
res= select_dropdown.options

for i in selct_dropdown:
    i.text()

time.sleep(5)
driver.close()

"""
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(10)

menu=driver.find_element(By.XPATH,value="//input[@name='username']")
act=ActionChains(driver)
act.context_click(menu).perform()

time.sleep(3)
driver.close()

"""
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
menu=driver.find_element(By.XPATH,value="//input[@name='username']")
menu.send_keys("admin")
act=ActionChains(driver)
act.double_click(menu).perform()

#control-A
act.key_down(Keys.LEFT_CONTROL).send_keys("a").key_up(Keys.LEFT_CONTROL).perform()

#control-C
act.key_down(Keys.LEFT_CONTROL).send_keys("c").key_up(Keys.LEFT_CONTROL).perform()

#control-tab
act.send_keys(Keys.TAB).perform()

#contorl-V
act.key_down(Keys.LEFT_CONTROL).send_keys("v").key_up(Keys.LEFT_CONTROL).perform()

time.sleep(3)
driver.quit()

"""
"""
#window handle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.execute_script("window.open('www.gmail.com'),window.open('www.facebook.com'),window.open('www.flipkart.com')")
multiple=driver.window_handles
for i in multiple:
    driver.switch_to.window(i)
    driver.title
    if driver=="flipkart":
        driver.close()
        
"""
"""
#alert popup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("http://demo.guru99.com/test/delete_customer.php")

exp_msg="Do you really want to delete this Customer?"

#send the data
driver.find_element(By.NAME,value="cusid").send_keys("wromgg customerid")
driver.find_element(By.NAME,value="submit").click()

alt=driver.switch_to.alert

act_msg=alt.text
assert act_msg==exp_msg
alt.accept()
alt.dismiss()
driver.close()

"""
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("http://demo.guru99.com/test/upload/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,value="//input[@id='uploadfile_0']").send_keys("C:\\Users\\chand\\OneDrive\\Pictures\\download.jpg")
time.sleep(5)


driver.find_element(By.XPATH,value="//button[@id='submitbutton']").click()

time.sleep(5)
driver.close()

"""

#"""

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# options=Options()
# options.add_experimental_option("deatch",True)
#
# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=Options)
# driver.get("http://demo.guru99.com/test/upload")
# driver.save_screenshot("pathurl")
# #"""


"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Start the WebDriver and load the page
driver = webdriver.Chrome()
driver.get('YOUR_TABLE_URL')

# Find the table by its unique identifier
table_id = driver.find_element(By.ID, 'YOUR_TABLE_ID')

# Iterate over each row in the table
for row in table_id.find_elements(By.TAG_NAME, 'tr'):
    # Each 'row' is a WebElement for a row in the table
    # Now iterate over the cells (columns) in the row
    for cell in row.find_elements(By.TAG_NAME, 'td'):
        # 'cell' is a WebElement for a cell in the row
        print(cell.text)  # or any other interaction you need

# Don't forget to quit the driver
driver.quit()

"""
"""
# how do you handle the otp by uinsg selenium
uasually otp is send by via sms and gmail so 
if we wnat to validate the otp by using some gmail apis or "imap" 
if you want to validate the otp by using sms we can use "twillo or "nexmo"
"""


































