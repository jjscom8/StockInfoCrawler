from CFnguideModel import  CFnguideData
from CStockCustomModel import  CStockCustomData
import pandas as pd
import math


class CStockResultData:
    def __init__(self):
        self.__ResultDf = pd.DataFrame(
            columns=[
                self.__sTagStockCode,
                self.__sTagCompName,
                self.__sTagMarket,
                self.__sTagLastQ,
                self.__sBondBBB_5Rate,
                self.__sTagRoe_y1,
                self.__sTagRoe_y2,
                self.__sTagRoe_y3,
                self.__sTagRoeConsen,
                self.__sTagRoePredQ,
                self.__sTagRoePredY
            ])


    def AppendData(self, stockCode : str, fnData: CFnguideData , customData: CStockCustomData):
        dictData = {
            self.__sTagStockCode : stockCode,
            self.__sTagCompName : fnData.CompName(),
            self.__sTagMarket : fnData.Market(),
            self.__sTagLastQ : fnData.LastQ(),
            self.__sBondBBB_5Rate : customData.BondBBB_5Rate(),
            self.__sTagRoe_y1 : fnData.Roe_y1(),
            self.__sTagRoe_y2 : fnData.Roe_y2(),
            self.__sTagRoe_y3 : fnData.Roe_y3(),
            self.__sTagRoeConsen : fnData.RoeConsen(),
            self.__sTagRoePredQ : customData.RoePredQ(),
            self.__sTagRoePredY : customData.RoePredY()
        }

        self.__ResultDf = self.__ResultDf.append(dictData, ignore_index=True)

    def ResultDf(self):
        return  self.__ResultDf

    # Column Name
    __sTagStockCode = '종목코드'
    __sTagCompName = '회사명'
    __sTagMarket = '시장'
    __sTagLastQ = '회계분기'
    __sBondBBB_5Rate = '채권기대수익률'
    __sTagRoe_y1 = 'ROE[-Y1]'
    __sTagRoe_y2 = 'ROE[-Y2]'
    __sTagRoe_y3 = 'ROE[-Y3]'
    __sTagRoeConsen = 'ROE[C]'
    __sTagRoePredQ = 'ROE[Q+]'
    __sTagRoePredY = 'ROE[Y+]'



class CStockResultModel:
    def __init__(self):
        self.__Data = CStockResultData()

    def Data(self):
        return self.__Data

    def AppendData(self, stockCode : str, fnData: CFnguideData , customData: CStockCustomData):
        self.__Data.AppendData(stockCode, fnData, customData)

    def ExportExcel(self, outPath):
        self.__Data.ResultDf().to_excel(outPath)









