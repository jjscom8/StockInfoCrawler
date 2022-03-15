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
from CStockInputModel import CStockInputModel


if __name__ == '__main__':

    # Init Main
    print(' <<< STOCK CRAWLER >>>')
    startDateTime = datetime.datetime.now()
    outDir = 'D:/DATA/STOCK_CRAWLING_DATA'
    print(' - START DATE TIME :: ', startDateTime.strftime('%Y-%m-%d %H:%M:%S'))


    bCustomOption = False
    inputModel = CStockInputModel()

    inputComps = []
    if len(sys.argv) == 1:
        print(' - Crawling all companies')
    else:
        sOption = sys.argv[1]
        # CUSTOM MODE : 최종 분기 정보를 CUSTOM으로 업데이트 하기 위한 모드
        if sOption.lower() == '--custom':
            if len(sys.argv) != 3:
                sys.exit(' Check Arguments : --custom path')

            print(' - Custom Crawling Mode ')
            print('   :: Input에 있는 항목만 UPDATE되며 나머지는 기존 Fnguide 정보 ')

            bCustomOption = True
            sInputPath = sys.argv[2]
            if not inputModel.LoadLastQInputCsv(sInputPath):
                sys.exit(' - Fail :: LoadLastQInputCsv' )

            #Update Target
            inputComps = inputModel.InputComps()
            # sys.exit(' Temp Quit')

        # Arguments
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
        sIndustry = krxCompDf.loc[curStockCode, krxModel.ColIndustry()]
        print( '  => Crawling : ' , sCompName, curStockCode)
        fnModel = CFnguideModel(curStockCode, sCompName, sIndustry)
        if not fnModel.CrawlSnapshot() :
            print( "            - Fail :: CrawlSnapshot ")

        if not fnModel.CrawlFinStat() :
            print("             - Fail :: CrawlFinStat ")

        if not fnModel.CrawlFinRate() :
            print("             - Fail :: CrawlFinRate ")

        fnData = fnModel.Data()

        ########## [ Check & Update Custom Input ] ##########
        # Python object - Call by Ref
        if bCustomOption:
            if not inputModel.UpdateFnData(fnData):# Call by Ref
                print("             - Fail :: UpdateFnData ")

        ########## [ Update Custom Data ] ##########
        customModel = CStockCustomModel('005930')
        if not customModel.UpdateStockCustomData(fnData, kisData):
            print(" - Fail :: UpdateStockCustomData ")
        customData = customModel.Data()

        # Append To Result
        resModel.AppendData(curStockCode, fnData, customData)

        time.sleep(3)

    # Export Excel
    sResFileName = 'DEVS_' + startDateTime.strftime('%Y%m%d_%H%M%S') + '.xlsx'
    sResFilePath = outDir + '/' + sResFileName

    krxModel.ExportExcel(sResFilePath, 'TARGET')
    resModel.ExportExcel(sResFilePath, 'RAW')
    resModel.ExportSummaryExcel(sResFilePath, 'SUMMARY')


    endDateTime = datetime.datetime.now()

    print(' - FINISH CRAWLING :: ', sResFilePath)
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