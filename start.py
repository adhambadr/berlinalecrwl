from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://www.berlinale.de/en/programm/berlinale_programm/10_uhr.php")

a_selector = "//a[contains(@class,'tickets_N') and @href]"
f = open('interested_in.txt')
num_tickets = 1

windows = 0

for t in f:
    t = t.strip()
    try:
        elem = driver.find_element_by_xpath("//tr[td/a/strong[contains(text(),'%s')]]%s"%(t,a_selector))
        elem.click()
        windows+= 1
        if len(driver.window_handles) > windows:
            driver.switch_to_window(driver.window_handles[windows])
            driver.implicitly_wait(1)
            sel = Select(driver.find_element_by_xpath("//select"))
            print sel.options
            sel.select_by_index(num_tickets)
            btn = driver.find_element_by_xpath("//input[contains(@id,'ToShoppingCart')]")
        btn.click()
        driver.switch_to_window(driver.window_handles[0])
    except NoSuchElementException:
        print "%s is soldout"%t

driver.implicitly_wait(900) # 15 minutes 
driver.close()