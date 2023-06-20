from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import telebot
import settings

bot = telebot.TeleBot(settings.BOT_TOKEN)
driver= webdriver.Chrome()

url="https://oykufashion.com/sort/haki-dugmeli-sort-tulum/"

driver.get(url)

time.sleep(2)
while True:
    button_size_s = driver.find_element(By.XPATH,'//*[@id="product-79264"]/div[1]/div[2]/div/div/div[2]/div/form/table/tbody/tr/td/div[1]/div[2]')

    button_size_s.click()
    time.sleep(2)
    stok_span = driver.find_element(By.XPATH, '//*[@id="product-79264"]/div[1]/div[2]/div/div/div[2]/div/form/div/div[1]/div[3]/p')
    stok_text = stok_span.text
    print(stok_text)
    if stok_text == "Stokta yok":
        
        print("Ürün bulunamadı")
        bot.send_message(settings.CHAT_ID,"Ürün bulunamadı")
        time.sleep(60)
        driver.refresh()
        time.sleep(5)
    elif stok_text == "Stokta":
        print("Ürün bulundu.")
        bot.send_message(settings.CHAT_ID,"Ürün bulundu")
        break
    else:
        print("Beklenmedik hata")
        time.sleep(60)
        driver.refresh()
