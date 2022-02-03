import pandas as pd
import time
import tqdm
import datetime
import sys
import math

from CKisRatingModel import CKisRatingModel
from CFnguideModel import CFnguideModel
from CStockCustomModel import CStockCustomModel
from CStockResultModel import  CStockResultModel
from CKrxModel import CKrxModel


if __name__ == '__main__':

    # Init Main
    print(' <<< STOCK CRAWLER >>>')
    startDateTime = datetime.datetime.now()
    outDir = 'D:/DATA/STOCK_CRAWLING_DATA'
    print(' - START DATE TIME :: ', startDateTime.strftime('%Y-%m-%d %H:%M:%S'))

    inputComps = []
    if len(sys.argv) == 1:
        print(' - Crawling all companies')
    else:
        print(' - Crawling companies below :')
        for i in range(1, len(sys.argv)):
            print('     -> ', sys.argv[i])
            inputComps.append(sys.argv[i])

    ########## [ KRX 종목정보 크롤링 ] ##########
    krxModel = CKrxModel()

    if not krxModel.CrawlCompanies(inputComps) :
        print( " - Fail :: CrawlCompanies ")

    krxData = krxModel.Data()
    krxCompDf = krxData.CompDf()

    #Export Excel
    sTargetCompsFileName = 'DEVS_TARGET_' + startDateTime.strftime('%Y%m%d_%H%M%S') + '.xlsx'
    sTargetCompsPath = outDir + '/' + sTargetCompsFileName
    krxModel.ExportExcel(sTargetCompsPath)

    ########## [ KIS 채권정보 크롤링 ] ##########
    kisModel = CKisRatingModel()
    if not kisModel.CrawlBondBBBRate():
        print( " - Fail :: CrawlBondBBBRate ")
    kisData = kisModel.Data()

    # Define Result
    resModel = CStockResultModel()
    ########## [ Fnguide 크롤링 & Update Custom Data ] ##########
    stockCodes = krxCompDf.index.to_list()
    for curStockCode in tqdm.tqdm(stockCodes):
        ########## [ Fnguide 크롤링 ] ##########
        sCompName = krxCompDf.loc[curStockCode, krxModel.ColCompName()]
        print( '  => Crawling : ' , sCompName, curStockCode)
        fnModel = CFnguideModel(curStockCode, sCompName)
        if not fnModel.CrawlSnapshot() :
            print( " - Fail :: CrawlSnapshot ")

        if not fnModel.CrawlFinStat() :
            print(" - Fail :: CrawlFinStat ")

        if not fnModel.CrawlFinRate() :
            print(" - Fail :: CrawlFinRate ")

        fnData = fnModel.Data()

        ########## [ Update Custom Data ] ##########
        customModel = CStockCustomModel('005930')
        if not customModel.UpdateStockCustomData(fnData, kisData):
            print(" - Fail :: UpdateStockCustomData ")
        customData = customModel.Data()

        # Append To Result
        resModel.AppendData(curStockCode, fnData, customData)

        time.sleep(3)

    # Export Excel
    sResFileName = 'DEVS_RESULT_' + startDateTime.strftime('%Y%m%d_%H%M%S') + '.xlsx'
    sResPath = outDir + '/' + sResFileName
    resModel.ExportExcel(sResPath)


    endDateTime = datetime.datetime.now()

    print(' - FINISH CRAWLING :: ', sResPath)
    print(' => START DATE TIME :: ' , startDateTime.strftime('%Y-%m-%d %H:%M:%S'))
    print(' => END DATE TIME :: ', endDateTime.strftime('%Y-%m-%d %H:%M:%S'))
    print(' => RUNNING TIME :: ', endDateTime - startDateTime)







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