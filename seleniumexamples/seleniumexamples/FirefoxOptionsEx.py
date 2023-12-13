from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from webdrivermanager import GeckoDriverManager

# from webdriver_manager.firefox import GeckoDriverManager

#firefox_options = Options()


#chrome_options = webdriver.ChromeOptions()
fx_op = webdriver.FirefoxOptions()
fx_op.add_argument("--headless=new")
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=fx_op)
driver=webdriver.Chrome()
driver.get("https://www.google.in")
driver.maximize_window()
print(driver.title)