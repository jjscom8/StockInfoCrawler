from CFnguideModel import  CFnguideModel
import math



class CStockResultData:
    def __init__(self, stockCode, fnguideData ):
        self.__sStockCode = stockCode
        self.__fnguideData = fnguideData

class CStockResultModel:
    def __init__(self, stockCode, fnguideData ):
        self.m_sStockCode = stockCode
        self.m_Data = CStockResultData(fnguideData)









