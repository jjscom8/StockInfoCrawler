import pandas as pd
import time
import datetime
import sys
import math
from CFnguideModel import CFnguideModel
from CStockResultModel import  CStockResultModel
from CStockCustomModel import CStockCustomModel

if __name__ == '__main__':
    print(' <<< STOCK CRAWLER >>>')

    # Fnguide Crawling
    fnModel = CFnguideModel('005930') # 삼성전자
    fnModel.CrawlSnapshot()
    fnModel.CrawlFinStat()
    fnModel.CrawlFinRate()
    fnData = fnModel.Data()

    # Update Custom Data
    customModel = CStockCustomModel('005930')
    nQuarterNum = customModel.QuarterNum(fnData.LastQ())
    nDomNetProfPredQ = customModel.DomNetProfPredQ(fnData.LastQ(),
                                                   fnData.DomNetProf_y1(),
                                                   fnData.DomNetProfLastQ(),
                                                   fnData.DomNetProfLastQ_y1())
    dRoePredQ = customModel.RoePredQ(nDomNetProfPredQ, fnData.DomCapLastQ())

    print(nQuarterNum, nDomNetProfPredQ, dRoePredQ)


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