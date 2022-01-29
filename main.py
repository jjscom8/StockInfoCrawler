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

    # KisRate

    kisModel = CKisRatingModel()
    kisModel.CrawlBondBBBRate()
    kisData = kisModel.Data()
    print( kisData.BondBBB_5Rate() )

    # Fnguide Crawling
    fnModel = CFnguideModel('005930') # 삼성전자
    fnModel.CrawlSnapshot()
    fnModel.CrawlFinStat()
    fnModel.CrawlFinRate()
    fnData = fnModel.Data()

    # Update Custom Data
    customModel = CStockCustomModel('005930')
    customData = customModel.Data()

    nQuarterNum = customModel.QuarterNum(fnData.LastQ())
    nDomNetProfPredQ = customModel.DomNetProfPredQ(fnData.LastQ(),
                                                   fnData.DomNetProf_y1(),
                                                   fnData.DomNetProfLastQ(),
                                                   fnData.DomNetProfLastQ_y1())
    dRoePredQ = customModel.RoePredQ(nDomNetProfPredQ, fnData.DomCapLastQ())

    print(dRoePredQ)

    dRoePredY = customModel.RoePredY(fnData.Roe_y1(),
                                     fnData.Roe_y2(),
                                     fnData.Roe_y3())
    print(dRoePredY)

    nSRimConsen80 = customModel.SRim(fnData.DomCapLastQ(),
                                     fnData.RoeConsen(),
                                     kisData.BondBBB_5Rate(),
                                     0.9)
    nSRimPredQ80 = customModel.SRim(fnData.DomCapLastQ(),
                                     dRoePredQ,
                                    kisData.BondBBB_5Rate(),
                                     0.9)
    nSRimPredY80 = customModel.SRim(fnData.DomCapLastQ(),
                                    dRoePredY,
                                    kisData.BondBBB_5Rate(),
                                    0.9)

    print( nSRimConsen80, nSRimPredQ80, nSRimPredY80)



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