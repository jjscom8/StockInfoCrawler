import pandas as pd
import time
import datetime
import sys
import math

from CKisRatingModel import CKisRatingModel
from CFnguideModel import CFnguideModel
from CStockCustomModel import CStockCustomModel
from CStockResultModel import  CStockResultModel


if __name__ == '__main__':
    print(' <<< STOCK CRAWLER >>>')

    # KisRate Crawl
    kisModel = CKisRatingModel()
    if not kisModel.CrawlBondBBBRate():
        print( " - Fail :: CrawlBondBBBRate ")
    kisData = kisModel.Data()

    # Fnguide Crawling
    fnModel = CFnguideModel('005930') # 삼성전자
    if not fnModel.CrawlSnapshot() :
        print( " - Fail :: CrawlSnapshot ")
    if not fnModel.CrawlFinStat() :
        print(" - Fail :: CrawlFinStat ")
    if not fnModel.CrawlFinRate() :
        print(" - Fail :: CrawlFinRate ")
    fnData = fnModel.Data()

    # Update Custom Data
    customModel = CStockCustomModel('005930')
    if not customModel.UpdateStockCustomData(fnData,kisData):
        print(" - Fail :: UpdateStockCustomData ")
    customData = customModel.Data()





##### < Selenium Sample > #####
# 펼치기를 위한 Selenium
# options = webdriver.ChromeOptions()
# # options.add_argument("headless")
# chromedriver = self.__sTagChromeDriverPath
# # driver = webdriver.Chrome(chromedriver, options=options)
# driver = webdriver.Chrome(chromedriver)
# driver.implicitly_wait(3)
# driver.get(url)
#
# spreadBtns = driver.find_elements_by_class_name(self.__sTagSpreadDumBtnClass)
# # 펼치기 버튼
# for btn in spreadBtns:
#     print(btn.get_attribute('href'))
#     time.sleep(1)
#     btn.click()
# driver.quit()