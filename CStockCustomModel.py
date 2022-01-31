from CFnguideModel import CFnguideModel
import math
import re

class CStockCustomtData:
    def __init__(self, stockCode ):
        self.__sStockCode = stockCode

        # 지배주주순이익
        self.__nDomNetProfPredQ = math.nan

        # 영업이익
        self.__nBsProfPredQ = math.nan

        # 비영업이익
        self.__nNonBsProf_y1 = math.nan
        self.__nNonBsProfLastQ = math.nan

        # 비영업이익 비율
        self.__dNonBsRate_y1 = math.nan
        self.__dNonBsRateLastQ = math.nan

        # ROE
        self.__dRoePredQ = math.nan
        self.__dRoePredY = math.nan # 가중평균

        # SRIM
        self.__nSRimConsen80 = math.nan
        self.__nSRimPredQ80 = math.nan
        self.__nSRimPredY80 = math.nan
        self.__nSRim_y180 = math.nan

        self.__nSRimConsen90 = math.nan
        self.__nSRimPredQ90 = math.nan
        self.__nSRimPredY90 = math.nan
        self.__nSRim_y190 = math.nan

        self.__nSRimConsen100 = math.nan
        self.__nSRimPredQ100 = math.nan
        self.__nSRimPredY100 = math.nan
        self.__nSRim_y1100 = math.nan

        # SRIM 적정주가
        self.__nSRimConsenPrice80 = math.nan
        self.__nSRimPredQPrice80 = math.nan
        self.__nSRimPredYPrice80 = math.nan
        self.__nSRim_y1Price80 = math.nan

        self.__nSRimConsenPrice90 = math.nan
        self.__nSRimPredQPrice90 = math.nan
        self.__nSRimPredYPrice90 = math.nan
        self.__nSRim_y1Price90 = math.nan

        self.__nSRimConsenPrice100 = math.nan
        self.__nSRimPredQPrice100 = math.nan
        self.__nSRimPredYPrice100 = math.nan
        self.__nSRim_y1Price100 = math.nan

        # SRIM 기대수익률
        self.__dSRimConsenExpRate80 = math.nan
        self.__dSRimPredQExpRate80 = math.nan
        self.__dSRimPredYExpRate80 = math.nan
        self.__dSRim_y1ExpRate80 = math.nan

        self.__dSRimConsenExpRate90 = math.nan
        self.__dSRimPredQExpRate90 = math.nan
        self.__dSRimPredYExpRate90 = math.nan
        self.__dSRim_y1ExpRate90 = math.nan

        self.__dSRimConsenExpRate100 = math.nan
        self.__dSRimPredQExpRate100 = math.nan
        self.__dSRimPredYExpRate100 = math.nan
        self.__dSRim_y1ExpRate100 = math.nan

    # 지배주주순이익
    def SetDomNetProfPredQ(self, nDomNetProfPredQ):
        self.__nDomNetProfPredQ = nDomNetProfPredQ

    def DomNetProfPredQ(self):
        return self.__nDomNetProfPredQ

    # ROE
    def SetRoePredQ(self, dRoePredQ):
        self.__dRoePredQ = dRoePredQ

    def RoePredQ(self):
        return self.__dRoePredQ

    def SetRoePredY(self, dRoePredY):
        self.__dRoePredY = dRoePredY

    def RoePredY(self):
        return self.__dRoePredY

    # SRIM
    def SetSRimConsen80(self, nSRimConsen80):
        self.__nSRimConsen80 = nSRimConsen80

    def SRimConsen80(self):
        return self.__nSRimConsen80

    def SetSRimPredQ80(self, nSRimPredQ80):
        self.__nSRimPredQ80 = nSRimPredQ80

    def SRimPredQ80(self):
        return self.__nSRimPredQ80

    def SetSRimPredY80(self, nSRimPredY80):
        self.__nSRimPredY80= nSRimPredY80

    def SRimPredY80(self):
        return self.__nSRimPredY80

    def SetSRim_y180(self, nSRim_y180):
        self.__nSRim_y180 = nSRim_y180

    def SRim_y180(self):
        return self.__nSRim_y180

    def SetSRimConsen90(self, nSRimConsen90):
        self.__nSRimConsen90 = nSRimConsen90

    def SRimConsen90(self):
        return self.__nSRimConsen90

    def SetSRimPredQ90(self, nSRimPredQ90):
        self.__nSRimPredQ90 = nSRimPredQ90

    def SRimPredQ90(self):
        return self.__nSRimPredQ90

    def SetSRimPredY90(self, nSRimPredY90):
        self.__nSRimPredY90= nSRimPredY90

    def SRimPredY90(self):
        return self.__nSRimPredY90

    def SetSRim_y190(self, nSRim_y190):
        self.__nSRim_y190 = nSRim_y190

    def SRim_y190(self):
        return self.__nSRim_y190


    def SetSRimConsen100(self, nSRimConsen100):
        self.__nSRimConsen100 = nSRimConsen100

    def SRimConsen100(self):
        return self.__nSRimConsen100

    def SetSRimPredQ100(self, nSRimPredQ100):
        self.__nSRimPredQ100 = nSRimPredQ100

    def SRimPredQ100(self):
        return self.__nSRimPredQ100

    def SetSRimPredY100(self, nSRimPredY100):
        self.__nSRimPredY100= nSRimPredY100

    def SRimPredY100(self):
        return self.__nSRimPredY100

    def SetSRim_y1100(self, nSRim_y1100):
        self.__nSRim_y1100 = nSRim_y1100

    def SRim_y1100(self):
        return self.__nSRim_y1100

    # SRIM 적정주가
    def SetSRimConsenPrice80(self, nSRimConsenPrice80):
        self.__nSRimConsenPrice80 = nSRimConsenPrice80

    def SRimConsenPrice80(self):
        return self.__nSRimConsenPrice80

    def SetSRimPredQPrice80(self, nSRimPredQPrice80):
        self.__nSRimPredQPrice80 = nSRimPredQPrice80

    def SRimPredQPrice80(self):
        return self.__nSRimPredQPrice80

    def SetSRimPredYPrice80(self, nSRimPredYPrice80):
        self.__nSRimPredYPrice80 = nSRimPredYPrice80

    def SRimPredYPrice80(self):
        return self.__nSRimPredYPrice80

    def SetSRim_y1Price80(self, nSRim_y1Price80):
        self.__nSRim_y1Price80 = nSRim_y1Price80

    def SRim_y1Price80(self):
        return self.__nSRim_y1Price80


    def SetSRimConsenPrice90(self, nSRimConsenPrice90):
        self.__nSRimConsenPrice90 = nSRimConsenPrice90

    def SRimConsenPrice90(self):
        return self.__nSRimConsenPrice90

    def SetSRimPredQPrice90(self, nSRimPredQPrice90):
        self.__nSRimPredQPrice90 = nSRimPredQPrice90

    def SRimPredQPrice90(self):
        return self.__nSRimPredQPrice90

    def SetSRimPredYPrice90(self, nSRimPredYPrice90):
        self.__nSRimPredYPrice90 = nSRimPredYPrice90

    def SRimPredYPrice90(self):
        return self.__nSRimPredYPrice90

    def SetSRim_y1Price90(self, nSRim_y1Price90):
        self.__nSRim_y1Price90 = nSRim_y1Price90

    def SRim_y1Price90(self):
        return self.__nSRim_y1Price90


    def SetSRimConsenPrice100(self, nSRimConsenPrice100):
        self.__nSRimConsenPrice100 = nSRimConsenPrice100

    def SRimConsenPrice100(self):
        return self.__nSRimConsenPrice100

    def SetSRimPredQPrice100(self, nSRimPredQPrice100):
        self.__nSRimPredQPrice100 = nSRimPredQPrice100

    def SRimPredQPrice100(self):
        return self.__nSRimPredQPrice100

    def SetSRimPredYPrice100(self, nSRimPredYPrice100):
        self.__nSRimPredYPrice100 = nSRimPredYPrice100

    def SRimPredYPrice100(self):
        return self.__nSRimPredYPrice100

    def SetSRim_y1Price100(self, nSRim_y1Price100):
        self.__nSRim_y1Price100 = nSRim_y1Price100

    def SRim_y1Price100(self):
        return self.__nSRim_y1Price100


    # SRIM 기대수익률
    def SetSRimConsenExpRate80(self, dSRimConsenExpRate80):
        self.__dSRimConsenExpRate80 = dSRimConsenExpRate80

    def SRimConsenExpRate80(self):
        return self.__dSRimConsenExpRate80

    def SetSRimPredQExpRate80(self, dSRimPredQExpRate80):
        self.__dSRimPredQExpRate80 = dSRimPredQExpRate80

    def SRimPredQExpRate80(self):
        return self.__dSRimPredQExpRate80

    def SetSRimPredYExpRate80(self, dSRimPredYExpRate80):
        self.__dSRimPredYExpRate80= dSRimPredYExpRate80

    def SRimPredYExpRate80(self):
        return self.__dSRimPredYExpRate80

    def SetSRim_y1ExpRate80(self, dSRim_y1ExpRate80):
        self.__dSRim_y1ExpRate80 = dSRim_y1ExpRate80

    def SRim_y1ExpRate80(self):
        return self.__dSRim_y1ExpRate80

    def SetSRimConsenExpRate90(self, dSRimConsenExpRate90):
        self.__dSRimConsenExpRate90 = dSRimConsenExpRate90

    def SRimConsenExpRate90(self):
        return self.__dSRimConsenExpRate90

    def SetSRimPredQExpRate90(self, dSRimPredQExpRate90):
        self.__dSRimPredQExpRate90 = dSRimPredQExpRate90

    def SRimPredQExpRate90(self):
        return self.__dSRimPredQExpRate90

    def SetSRimPredYExpRate90(self, dSRimPredYExpRate90):
        self.__dSRimPredYExpRate90= dSRimPredYExpRate90

    def SRimPredYExpRate90(self):
        return self.__dSRimPredYExpRate90

    def SetSRim_y1ExpRate90(self, dSRim_y1ExpRate90):
        self.__dSRim_y1ExpRate90 = dSRim_y1ExpRate90

    def SRim_y1ExpRate90(self):
        return self.__dSRim_y1ExpRate90


    def SetSRimConsenExpRate100(self, dSRimConsenExpRate100):
        self.__dSRimConsenExpRate100 = dSRimConsenExpRate100

    def SRimConsenExpRate100(self):
        return self.__dSRimConsenExpRate100

    def SetSRimPredQExpRate100(self, dSRimPredQExpRate100):
        self.__dSRimPredQExpRate100 = dSRimPredQExpRate100

    def SRimPredQExpRate100(self):
        return self.__dSRimPredQExpRate100

    def SetSRimPredYExpRate100(self, dSRimPredYExpRate100):
        self.__dSRimPredYExpRate100= dSRimPredYExpRate100

    def SRimPredYExpRate100(self):
        return self.__dSRimPredYExpRate100

    def SetSRim_y1ExpRate100(self, dSRim_y1ExpRate100):
        self.__dSRim_y1ExpRate100 = dSRim_y1ExpRate100

    def SRim_y1ExpRate100(self):
        return self.__dSRim_y1ExpRate100

    # 영업이익
    def SetBsProfPredQ(self, nBsProfPredQ):
        self.__nBsProfPredQ = nBsProfPredQ

    def BsProfPredQ(self):
        return self.__nBsProfPredQ

    # 비영업이익
    def SetNonBsProf_y1(self, nNonBsProf_y1):
       self.__nNonBsProf_y1 = nNonBsProf_y1

    def NonBsProf_y1(self):
        return self.__nNonBsProf_y1

    def SetNonBsProfLastQ(self, nNonBsProfLastQ):
        self.__nNonBsProfLastQ = nNonBsProfLastQ

    def NonBsProfLastQ(self):
        return self.__nNonBsProfLastQ

    # 비영업이익 비율
    def SetNonBsRate_y1(self, dNonBsRate_y1):
        self.__dNonBsRate_y1 = dNonBsRate_y1

    def NonBsRate_y1(self):
        return self.__dNonBsRate_y1

    def SetNonBsRateLastQ(self, dNonBsRateLastQ):
        self.__dNonBsRateLastQ = dNonBsRateLastQ

    def NonBsRateLastQ(self):
        return self.__dNonBsRateLastQ


class CStockCustomModel:

    def __init__(self, stockCode ):
        self.__sStockCode = stockCode
        self.__Data = CStockCustomtData(stockCode)

    def Data(self):
        return self.__Data

    def UpdateStockCustomData(self, fnData, kisData):

        if not fnData or not kisData :
            print(" - Fail :: Invalid Data ")
            return False

        # 지배주주순이익
        nDomNetProfPredQ = self.DomNetProfPredQ(fnData.LastQ(),
                                                fnData.DomNetProf_y1(),
                                                fnData.DomNetProfLastQ(),
                                                fnData.DomNetProfLastQ_y1())

        # ROE
        dRoePredQ = self.RoePredQ(nDomNetProfPredQ, fnData.DomCapLastQ())

        dRoePredY = self.RoePredY(fnData.Roe_y1(), fnData.Roe_y2(), fnData.Roe_y3())

        # SRIM
        nSRimConsen80 = self.SRim(fnData.DomCapLastQ(), fnData.RoeConsen(),
                                  kisData.BondBBB_5Rate(), 0.8)
        nSRimPredQ80 = self.SRim(fnData.DomCapLastQ(), dRoePredQ,
                                 kisData.BondBBB_5Rate(), 0.8)
        nSRimPredY80 = self.SRim(fnData.DomCapLastQ(), dRoePredY,
                                 kisData.BondBBB_5Rate(), 0.8)
        nSRim_y180 = self.SRim(fnData.DomCapLastQ(), fnData.Roe_y1(),
                               kisData.BondBBB_5Rate(), 0.8)

        nSRimConsen90 = self.SRim(fnData.DomCapLastQ(), fnData.RoeConsen(),
                                  kisData.BondBBB_5Rate(), 0.9)
        nSRimPredQ90 = self.SRim(fnData.DomCapLastQ(), dRoePredQ,
                                 kisData.BondBBB_5Rate(), 0.9)
        nSRimPredY90 = self.SRim(fnData.DomCapLastQ(), dRoePredY,
                                 kisData.BondBBB_5Rate(), 0.9)
        nSRim_y190 = self.SRim(fnData.DomCapLastQ(), fnData.Roe_y1(),
                               kisData.BondBBB_5Rate(), 0.9)

        nSRimConsen100 = self.SRim(fnData.DomCapLastQ(), fnData.RoeConsen(),
                                   kisData.BondBBB_5Rate(), 0.9)
        nSRimPredQ100 = self.SRim(fnData.DomCapLastQ(), dRoePredQ,
                                  kisData.BondBBB_5Rate(), 0.9)
        nSRimPredY100 = self.SRim(fnData.DomCapLastQ(), dRoePredY,
                                  kisData.BondBBB_5Rate(), 0.9)
        nSRim_y1100 = self.SRim(fnData.DomCapLastQ(), fnData.Roe_y1(),
                                kisData.BondBBB_5Rate(), 0.9)

        # SRIM 적정주가
        nSRimConsenPrice80 = self.SRimPrice(nSRimConsen80,fnData.StockCntTot())
        nSRimPredQPrice80 = self.SRimPrice(nSRimPredQ80,fnData.StockCntTot())
        nSRimPredYPrice80 = self.SRimPrice(nSRimPredY80,fnData.StockCntTot())
        nSRim_y1Price80 = self.SRimPrice(nSRim_y180,fnData.StockCntTot())

        nSRimConsenPrice90 = self.SRimPrice(nSRimConsen90, fnData.StockCntTot())
        nSRimPredQPrice90 = self.SRimPrice(nSRimPredQ90, fnData.StockCntTot())
        nSRimPredYPrice90 = self.SRimPrice(nSRimPredY90, fnData.StockCntTot())
        nSRim_y1Price90 = self.SRimPrice(nSRim_y190, fnData.StockCntTot())

        nSRimConsenPrice100 = self.SRimPrice(nSRimConsen100, fnData.StockCntTot())
        nSRimPredQPrice100 = self.SRimPrice(nSRimPredQ100, fnData.StockCntTot())
        nSRimPredYPrice100 = self.SRimPrice(nSRimPredY100, fnData.StockCntTot())
        nSRim_y1Price100 = self.SRimPrice(nSRim_y1100, fnData.StockCntTot())

        # SRIM 기대수익률
        dSRimConseneExpRate80 = self.ExpReturnRate(nSRimConsenPrice80, fnData.LastPrice())
        dSRimPredQExpRate80 = self.ExpReturnRate(nSRimPredQPrice80, fnData.LastPrice())
        dSRimPredYExpRate80 = self.ExpReturnRate(nSRimPredYPrice80, fnData.LastPrice())
        dSRim_y1ExpRate80 = self.ExpReturnRate(nSRim_y1Price80, fnData.LastPrice())

        dSRimConseneExpRate90 = self.ExpReturnRate(nSRimConsenPrice90, fnData.LastPrice())
        dSRimPredQExpRate90 = self.ExpReturnRate(nSRimPredQPrice90, fnData.LastPrice())
        dSRimPredYExpRate90 = self.ExpReturnRate(nSRimPredYPrice90, fnData.LastPrice())
        dSRim_y1ExpRate90 = self.ExpReturnRate(nSRim_y1Price90, fnData.LastPrice())

        dSRimConseneExpRate100 = self.ExpReturnRate(nSRimConsenPrice100, fnData.LastPrice())
        dSRimPredQExpRate100 = self.ExpReturnRate(nSRimPredQPrice100, fnData.LastPrice())
        dSRimPredYExpRate100 = self.ExpReturnRate(nSRimPredYPrice100, fnData.LastPrice())
        dSRim_y1ExpRate100 = self.ExpReturnRate(nSRim_y1Price100, fnData.LastPrice())

        # 영업이익
        nBsProfPredQ = self.BsProfPredQ(fnData.LastQ(), fnData.BsProf_y1(),
                                        fnData.BsProfLastQ(), fnData.BsProfLastQ_y1())
        # 비영업이익
        nNonBsProf_y1 = self.NonBsProf_y1(fnData.BsProfBefTax_y1(), fnData.BsProf_y1())

        nNonBsProfLastQ = self.NonBsProfLastQ(fnData.BsProfBefTaxLastQ(), fnData.BsProfLastQ())

        # 비영업이익 비율
        dNonBsRate_y = self.NonBsRate_y1(fnData.BsProf_y1(), nNonBsProf_y1)

        dNonBsRateLastQ = self.NonBsRateLastQ(fnData.BsProfLastQ(), nNonBsProfLastQ)

        print( nBsProfPredQ, nNonBsProf_y1, nNonBsProfLastQ, dNonBsRate_y, dNonBsRateLastQ)

        return True

    def DomNetProfPredQ(self, sLastQ, nDomNetProf_y1, nDomNetProfLastQ, nDomNetProfLastQ_y1):
        if math.isnan(nDomNetProf_y1) or math.isnan(nDomNetProfLastQ) or math.isnan(nDomNetProfLastQ_y1):
            return math.nan

        if self.QuarterNum(sLastQ) == 4:
            return nDomNetProfLastQ

        dIncRate = (nDomNetProfLastQ - nDomNetProfLastQ_y1) / nDomNetProfLastQ_y1
        nDomNetProfPredQ = nDomNetProf_y1 * (1+dIncRate)

        return nDomNetProfPredQ

    # 영업이익
    def BsProfPredQ(self, sLastQ, nBsProf_y1, nBsProfLastQ, nBsProfLastQ_y1):
        if math.isnan(nBsProf_y1) or math.isnan(nBsProfLastQ) or math.isnan(nBsProfLastQ_y1):
            return math.nan

        if self.QuarterNum(sLastQ) == 4:
            return nBsProfLastQ

        dIncRate = (nBsProfLastQ - nBsProfLastQ_y1) / nBsProfLastQ_y1
        nBsProfPredQ = nBsProf_y1 * (1+dIncRate)

        return nBsProfPredQ

    # 비영업이익
    def NonBsProf_y1(self, nBsProfBefTax_y1, nBsProf_y1):
        if math.isnan(nBsProfBefTax_y1) or math.isnan(nBsProf_y1):
            return math.nan
        nNonBsProf_y1 = nBsProfBefTax_y1 - nBsProf_y1
        return nNonBsProf_y1

    def NonBsProfLastQ(self, nBsProfBefTaxLastQ, nBsProfLastQ):
        if math.isnan(nBsProfBefTaxLastQ) or math.isnan(nBsProfLastQ):
            return math.nan
        nNonBsProfPredQ = nBsProfBefTaxLastQ - nBsProfLastQ
        return nNonBsProfPredQ

    # 비영업이익 비율
    def NonBsRate_y1(self, nBsProf_y1, nNonBsProf_y1):
        if math.isnan(nBsProf_y1) or math.isnan(nNonBsProf_y1):
            return math.nan
        dNonBsRate_y1 = nNonBsProf_y1 / nBsProf_y1 * 100
        return dNonBsRate_y1

    def NonBsRateLastQ(self, nBsProfLastQ, nNonBsProfLastQ ):
        if math.isnan(nBsProfLastQ) or math.isnan(nNonBsProfLastQ):
            return math.nan
        dNonBsRateLastQ = nNonBsProfLastQ / nBsProfLastQ * 100
        return dNonBsRateLastQ

    # ROE
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

    def SRimPrice(self, nSRim, nStockCnt, unit = 100000000 ):
        if math.isnan(nSRim) or math.isnan(nStockCnt):
            return math.nan

        nSRimPrice = nSRim / nStockCnt * unit

        return nSRimPrice


    ### Util Function ###
    def HasRoeTrend(self, dRoe_y1, dRoe_y2, dRoe_y3):
        # 증가 추세이거나 감소추세일때 변화폭 확인
        if math.isnan(dRoe_y1) or math.isnan(dRoe_y2) or math.isnan(dRoe_y3):
            return False

        if (dRoe_y1 > dRoe_y2 and dRoe_y2 > dRoe_y3) \
                or (dRoe_y1 < dRoe_y2 and dRoe_y2 < dRoe_y3):
            return True

        return False

    def ExpReturnRate(self, nExpPrice, nLastPrice):
        if math.isnan(nExpPrice) or math.isnan(nLastPrice):
            return math.nan

        dExpReturnRate = (nExpPrice - nLastPrice) / nLastPrice * 100

        return dExpReturnRate

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





