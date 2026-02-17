from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Amazon Price Finder

driver.get("https://www.amazon.in/Red-Tape-Designer-Comfortable-Adjustable/dp/B0CSWN4TCK/ref=zg_bs_c_shoes_d_sccl_1/259-5852959-1318806?pd_rd_w=OepAz&content-id=amzn1.sym.b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_p=b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_r=P70EBNJEHVHAP4EAJAJ2&pd_rd_wg=mIsQm&pd_rd_r=818dedf9-5979-47cb-99e5-584fe8642543&pd_rd_i=B0CSWN4TCK&th=1&psc=1")

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

driver.close()
driver.quit()


# Upcoming events in Python org
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://python.org")
events = driver.find_elements(By.XPATH,
                              '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
new_dict = {}
for event in events:
    lines = event.find_elements(By.TAG_NAME, "li")
    for li in lines:
        split_text = li.text.split("\n")
        new_dict[split_text[0]] = split_text[1]

print(new_dict)

driver.close()
driver.quit()