from CFnguideModel import CFnguideModel
import math
import re

class CStockCustomtData:
    def __init__(self, stockCode ):
        self.__sStockCode = stockCode

        self.__nDomNetProfPredQ = math.nan
        self.__nRoePredQ = math.nan
        self.__nRoePredY = math.nan # 가중평균


class CStockCustomModel:

    def __init__(self, stockCode ):
        self.__sStockCode = stockCode
        self.__Data = CStockCustomtData(stockCode)

    def Data(self):
        return self.__Data

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


    def RoePredY(self, dRoe_y1, dRoe_y2, dRoe_y3):
        if math.isnan(dRoe_y1) or math.isnan(dRoe_y2) or math.isnan(dRoe_y3):
            return math.nan

        dRoePredY = math.nan
        if self.HasRoeTrend(dRoe_y1, dRoe_y2, dRoe_y3):
            dRoePredY = dRoe_y3
        else:
            dTotalRoe = 0
            weight = 0
            for index, val in enumerate([dRoe_y3, dRoe_y2, dRoe_y1]):
                dTotalRoe = dTotalRoe + val * (index + 1)
                weight = weight + (index + 1)

            dRoePredY = dTotalRoe / weight

        return dRoePredY

    def SRim(self, nDomCapLastQ, dRoeRate, dBondRate, w):
        if math.isnan(nDomCapLastQ) or math.isnan(dRoeRate) or math.isnan(dBondRate):
            return math.nan

        dSrim = nDomCapLastQ \
                + (nDomCapLastQ * (dRoeRate - dBondRate)) \
                * w / (1 + dBondRate - w)

        return dSrim

    ### Util Function ###
    def HasRoeTrend(self, dRoe_y1, dRoe_y2, dRoe_y3):
        # 증가 추세이거나 감소추세일때 변화폭 확인
        if math.isnan(dRoe_y1) or math.isnan(dRoe_y2) or math.isnan(dRoe_y3):
            return False

        if (dRoe_y1 > dRoe_y2 and dRoe_y2 > dRoe_y3) \
                or (dRoe_y1 < dRoe_y2 and dRoe_y2 < dRoe_y3):
            return True

        return False

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





