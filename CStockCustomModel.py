from CFnguideModel import CFnguideModel
import math
import re

class CStockCustomtData:
    def __init__(self, stockCode ):
        self.__sStockCode = stockCode

        self.__nDomNetProfPredQ = math.nan
        self.__nRoePredQ = math.nan



class CStockCustomModel:
    def __init__(self, stockCode ):
        self.__sStockCode = stockCode
        self.__Data = CStockCustomtData(stockCode)

    def UpdateStockCustomData(self, fnguideData):
        return True

    def DomNetProfPredQ(self, sLastQ, nDomNetProf_y1, nDomNetProfLastQ, nDomNetProfLastQ_y1):
        # todo
        if math.isnan(nDomNetProf_y1) or math.isnan(nDomNetProfLastQ) or math.isnan(nDomNetProfLastQ_y1):
            return math.nan

        if self.QuarterNum(sLastQ) == 4:
            return nDomNetProfLastQ

        dIncRate = (nDomNetProfLastQ - nDomNetProfLastQ_y1) / nDomNetProfLastQ_y1
        nDomNetProfPredQ = nDomNetProf_y1 * (1+dIncRate)

        return nDomNetProfPredQ

    def RoePredQ(self, nDomNetProfFromQ, nDomCapLastQ):
        if math.isnan(nDomNetProfFromQ) or math.isnan(nDomCapLastQ):
            return math.nan

        dRoePredQ = nDomNetProfFromQ / nDomCapLastQ * 100
        return dRoePredQ

    def QuarterNum(self, sLastQ):
        re1q = re.compile(self.__sTagRegQurter1)
        re2q = re.compile(self.__sTagRegQurter2)
        re3q = re.compile(self.__sTagRegQurter3)
        re4q = re.compile(self.__sTagRegQurter4)

        if re1q.match(sLastQ):
            return 1
        if re2q.match(sLastQ):
            return 2
        if re3q.match(sLastQ):
            return 3
        if re4q.match(sLastQ):
            return 4

        return math.nan


    ### 분기 ###
    # - 실적 발표시즌에는 마지막 분기 뒤에 (P)와 같은 문자가 붙는다.
    __sTagRegQurter1 = '.*/03.*'
    __sTagRegQurter2 = '.*/06.*'
    __sTagRegQurter3 = '.*/09.*'
    __sTagRegQurter4 = '.*/12.*'





