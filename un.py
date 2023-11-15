from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from saveExcel import createXL

gb_titles = []
gb_dates = []
gb_likes = []
gb_imgs = []

def getPage(PATH):
    
    driver = webdriver.Chrome()
    driver.get(PATH)
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h6 > a"))
        )
    except:
        driver.quit()
    finally:
        print("POSTS ON PATH ", PATH, ": \n")
        cards = driver.find_elements(By.CLASS_NAME, "blog-item")
        titles =[]
        dates =[]
        likes =[]
        imgs =[]
       
        for card in cards:
                title = card.find_element(By.CSS_SELECTOR, "h6 > a").text
                like = card.find_element(By.CSS_SELECTOR, ".zilla-likes > span").text
                try:
                    image_element = card.find_element(By.CSS_SELECTOR, ".img > a")
                    image = image_element.get_attribute("data-bg")
                except:
                    image = " " 
                date = card.find_element(By.CSS_SELECTOR, ".bd-item > span").text
                print(title)
                titles.append(title)
                likes.append(like)
                imgs.append(image)
                dates.append(date)
        # titles  = [i.text for i in driver.find_elements(By.CSS_SELECTOR, "h6 > a")]
        # bd_item = driver.find_elements(By.CSS_SELECTOR, ".bd-item > span")
        # dates = []
        # for i in range(0, len(bd_item)):
        #     if i%2==0:
        #         dates.append(bd_item[i].text)
        # likes = [i.text for i in driver.find_elements(By.CSS_SELECTOR, ".zilla-likes > span")]
        # imgs = [i.get_attribute('data-bg') for i in driver.find_elements(By.CSS_SELECTOR, ".wrap  > .img > a")]
        # print(titles, dates, likes)
        for i in titles:
            gb_titles.append(i)
        for i in dates:
            gb_dates.append(i)
        for i in likes:
            gb_likes.append(i)
        for i in imgs:
            gb_imgs.append(i)

    driver.quit()


BASE_PATH = "https://rategain.com/blog/"
st = int(input("Enter start page number "))
en = int(input("Ender end page number "))
for i in range(st, en+1):
    if i != 1:
        getPage(BASE_PATH + "page/" + str(i))
    else:
        getPage(BASE_PATH)
createXL(gb_titles, gb_dates, gb_imgs, gb_likes)