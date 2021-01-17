from selenium import webdriver
import time


chrome_driver_path = "C:/Users/Nitin/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
items = driver.find_elements_by_css_selector("#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")

        price_list = [price.text.split("-")[1].strip().replace(",", "") for price in all_prices]

        cookies_upgrade = {}
        for n in range(len(price_list)):
            cookies_upgrade[price_list[n]] = items_ids[n]

        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookies_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookies_upgrade.items():
            if cost < cookies_count:
                affordable_upgrades[cost] = id
        highest_price_affordable = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable]
        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break



