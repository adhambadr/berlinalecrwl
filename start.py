from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://www.berlinale.de/en/programm/berlinale_programm/10_uhr.php")

a_selector = "//a[contains(@class,'tickets_N') and @href]"
row_selectors = []
f = open('interested_in.txt')
num_tickets = 1

print len(driver.window_handles)
for t in f:
    t = t.strip()
    row_selectors.append("//tr[td/a/strong[contains(text(),'%s')]]"%t)
    #try:
    elem = driver.find_element_by_xpath(row_selectors[0]+a_selector)
    elem.click()
    if len(driver.window_handles) > 1:
        driver.switch_to_window(driver.window_handles[1])
        driver.implicitly_wait(1)
        print driver.title # assert eventim.de
        sel = Select(driver.find_element_by_xpath("//select"))
        print sel.options
        sel.select_by_index(num_tickets)
        btn = driver.find_element_by_xpath("//input[contains(@id,'ToShoppingCart')]")
    btn.click()

driver.close()