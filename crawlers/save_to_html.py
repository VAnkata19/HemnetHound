from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os 

def check_if_valid(html):
    for file in os.listdir("soups"):
        soup = BeautifulSoup(open(os.path.join("soups", file), encoding="utf-8"), 'html.parser')
        if soup == html:
            return True

def save_to_html(urls):
    for url in urls:
        driver = webdriver.Chrome()
        driver.get(url)
        wait = WebDriverWait(driver, 4)

        driver.execute_script("""
        var element = document.querySelector("aside#usercentrics-cmp-ui");
        if (element)
            element.parentNode.removeChild(element);
        """)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #Parses page with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        with open(os.path.join("soups", f"soup_page_{urls.index(url)+1}.html"), "w", encoding="utf-8") as f:
            f.write(str(soup))
            driver.quit()

            if not check_if_valid(soup):
                print(f"Html conversion failed {f"soup_page_{urls.index(url)+1}.html"}")
