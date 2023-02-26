from CFnguideModel import CFnguideData
from CKisRatingModel import  CKisRatingData
import math
import re

class CStockCustomData:
    def __init__(self, stockCode ):
        self.__sStockCode = stockCode

        #채권 기대수익률
        self.__dBondBBB_5Rate = math.nan

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

        # 지배주주자본
        self.__nDomCapPredQ = math.nan

        # ROE
        self.__dRoePredQ = math.nan
        self.__dRoePredY = math.nan # 가중평균
        self.__dRoeBsProfPredQ = math.nan # 영업이익으로 계산한 ROE
        self.__dRoeBsProf_y1 = math.nan # 영업이익으로 계산한 ROE

        # EPS
        self.__nEpsPredQ = math.nan
        self.__nEpsPredY = math.nan
        self.__nEpsBsProf_y1 = math.nan # 영업이익으로 계산한 ROE
        self.__nEpsBsProfPredQ = math.nan # 영업이익으로 계산한 EPS

        # SRIM
        self.__nSRim80Consen = math.nan
        self.__nSRim80PredQ = math.nan
        self.__nSRim80PredY = math.nan
        self.__nSRim80_y1 = math.nan

        self.__nSRim90Consen = math.nan
        self.__nSRim90PredQ = math.nan
        self.__nSRim90PredY = math.nan
        self.__nSRim90_y1 = math.nan

        self.__nSRim100Consen = math.nan
        self.__nSRim100PredQ = math.nan
        self.__nSRim100PredY = math.nan
        self.__nSRim100_y1 = math.nan

        # SRIM 적정주가
        self.__nSRimPrice80Consen = math.nan
        self.__nSRimPrice80PredQ = math.nan
        self.__nSRimPrice80PredY = math.nan
        self.__nSRimPrice80_y1 = math.nan

        self.__nSRimPrice90Consen = math.nan
        self.__nSRimPrice90PredQ = math.nan
        self.__nSRimPrice90PredY = math.nan
        self.__nSRimPrice90_y1 = math.nan

        self.__nSRimPrice100Consen = math.nan
        self.__nSRimPrice100PredQ = math.nan
        self.__nSRimPrice100PredY = math.nan
        self.__nSRimPrice100_y1 = math.nan

        # SRIM 기대수익률
        self.__dSRimExpRate80Consen = math.nan
        self.__dSRimExpRate80PredQ = math.nan
        self.__dSRimExpRate80PredY = math.nan
        self.__dSRimExpRateAvg80 = math.nan
        self.__dSRimExpRate80_y1 = math.nan

        self.__dSRimExpRate90Consen = math.nan
        self.__dSRimExpRate90PredQ = math.nan
        self.__dSRimExpRate90PredY = math.nan
        self.__dSRimExpRateAvg90 = math.nan
        self.__dSRimExpRate90_y1 = math.nan

        self.__dSRimExpRate100Consen = math.nan
        self.__dSRimExpRate100PredQ = math.nan
        self.__dSRimExpRate100PredY = math.nan
        self.__dSRimExpRateAvg100 = math.nan
        self.__dSRimExpRate100_y1 = math.nan

        # 영업현금흐름 - 영업이익
        self.__nCfBsProfDiff_y1 = math.nan
        self.__nCfBsProfDiffLastQ = math.nan

        # 현금흐름패턴
        self.__sCfPattern_y1 = ""
        self.__sCfPatternLastQ = ""

        # PEGR
        self.__dPegr = math.nan

        # 자본잠식
        self.__sCortaxCond = ""

        # KPRICE
        self.__nKPriceBsProf_y1 = math.nan
        self.__nKPriceBsProfPredQ = math.nan
        self.__nKPriceNetProf_y1 = math.nan
        self.__nKPriceNetProfPredQ = math.nan
        self.__nKPriceNetProfPredY = math.nan
        self.__nKPriceNetProfConsen = math.nan

        # KPRICE 기대수익률
        self.__nKPriceBsProfExpRate_y1= math.nan
        self.__nKPriceBsProfExpRatePredQ = math.nan
        self.__nKPriceNetProfExpRate_y1 = math.nan
        self.__nKPriceNetProfExpRatePredQ = math.nan
        self.__nKPriceNetProfExpRatePredY = math.nan
        self.__nKPriceNetProfExpRateConsen = math.nan

        # Pass/Fail
        self.__bPassFail = ''
        self.__sFailReason = ''

        # 매출 증가율
        self.__dSalesIncRate_y3_y2 = math.nan
        self.__dSalesIncRate_y2_y1 = math.nan
        self.__dSalesIncRate_lqy1_lq = math.nan
        self.__dSalesIncRateAvg = math.nan
        self.__sSalesIncRateTrend = ''

        # 영익 증가율
        self.__dBsProfIncRate_y3_y2 = math.nan
        self.__dBsProfIncRate_y2_y1 = math.nan
        self.__dBsProfIncRate_lqy1_lq = math.nan
        self.__dBsProfIncRateAvg = math.nan
        self.__sBsProfIncRateTrend = ''


    def SetBondBBB_5Rate(self, dBondBBB_5Rate):
        self.__dBondBBB_5Rate = dBondBBB_5Rate

    def BondBBB_5Rate(self):
        return self.__dBondBBB_5Rate

    # 지배주주순이익
    def SetDomNetProfPredQ(self, nDomNetProfPredQ):
        self.__nDomNetProfPredQ = nDomNetProfPredQ

    def DomNetProfPredQ(self):
        return self.__nDomNetProfPredQ

    # 지배주주지분
    def SetDomCapPredQ(self, nDomCapPredQ):
        self.__nDomCapPredQ = nDomCapPredQ

    def DomCapPredQ(self):
        return self.__nDomCapPredQ

    # ROE
    def SetRoePredQ(self, dRoePredQ):
        self.__dRoePredQ = dRoePredQ

    def RoePredQ(self):
        return self.__dRoePredQ

    def SetRoePredY(self, dRoePredY):
        self.__dRoePredY = dRoePredY

    def RoePredY(self):
        return self.__dRoePredY

    def SetRoeBsProfPredQ(self, dRoeBsProfPredQ):
        self.__dRoeBsProfPredQ = dRoeBsProfPredQ

    def RoeBsProfPredQ(self):
        return self.__dRoeBsProfPredQ

    def SetRoeBsProf_y1(self, dRoeBsProf_y1):
        self.__dRoeBsProf_y1 = dRoeBsProf_y1

    def RoeBsProf_y1(self):
        return self.__dRoeBsProf_y1

    # EPS
    def SetEpsPredQ(self, nEpsPredQ):
        self.__nEpsPredQ = nEpsPredQ

    def EpsPredQ(self):
        return self.__nEpsPredQ

    def SetEpsPredY(self, nEpsPredY):
        self.__nEpsPredY = nEpsPredY

    def EpsPredY(self):
        return self.__nEpsPredY

    def SetEpsBsProfPredQ(self, nEpsBsProfPredQ):
        self.__nEpsBsProfPredQ = nEpsBsProfPredQ

    def EpsBsProfPredQ(self):
        return self.__nEpsBsProfPredQ

    def SetEpsBsProf_y1(self, nEpsBsProf_y1):
        self.__nEpsBsProf_y1 = nEpsBsProf_y1

    def EpsBsProf_y1(self):
        return self.__nEpsBsProf_y1

    # SRIM
    def SetSRim80Consen(self, nSRim80Consen):
        self.__nSRim80Consen = nSRim80Consen

    def SRim80Consen(self):
        return self.__nSRim80Consen

    def SetSRim80PredQ(self, nSRim80PredQ):
        self.__nSRim80PredQ = nSRim80PredQ

    def SRim80PredQ(self):
        return self.__nSRim80PredQ

    def SetSRim80PredY(self, nSRim80PredY):
        self.__nSRim80PredY= nSRim80PredY

    def SRim80PredY(self):
        return self.__nSRim80PredY

    def SetSRim80_y1(self, nSRim80_y1):
        self.__nSRim80_y1 = nSRim80_y1

    def SRim80_y1(self):
        return self.__nSRim80_y1

    def SetSRim90Consen(self, nSRim90Consen):
        self.__nSRim90Consen = nSRim90Consen

    def SRim90Consen(self):
        return self.__nSRim90Consen

    def SetSRim90PredQ(self, nSRim90PredQ):
        self.__nSRim90PredQ = nSRim90PredQ

    def SRim90PredQ(self):
        return self.__nSRim90PredQ

    def SetSRim90PredY(self, nSRim90PredY):
        self.__nSRim90PredY= nSRim90PredY

    def SRim90PredY(self):
        return self.__nSRim90PredY

    def SetSRim90_y1(self, nSRim90_y1):
        self.__nSRim90_y1 = nSRim90_y1

    def SRim90_y1(self):
        return self.__nSRim90_y1


    def SetSRim100Consen(self, nSRim100Consen):
        self.__nSRim100Consen = nSRim100Consen

    def SRim100Consen(self):
        return self.__nSRim100Consen

    def SetSRim100PredQ(self, nSRim100PredQ):
        self.__nSRim100PredQ = nSRim100PredQ

    def SRim100PredQ(self):
        return self.__nSRim100PredQ

    def SetSRim100PredY(self, nSRim100PredY):
        self.__nSRim100PredY= nSRim100PredY

    def SRim100PredY(self):
        return self.__nSRim100PredY

    def SetSRim100_y1(self, nSRim100_y1):
        self.__nSRim100_y1 = nSRim100_y1

    def SRim100_y1(self):
        return self.__nSRim100_y1

    # SRIM 적정주가
    def SetSRimPrice80Consen(self, nSRimPrice80Consen):
        self.__nSRimPrice80Consen = nSRimPrice80Consen

    def SRimPrice80Consen(self):
        return self.__nSRimPrice80Consen

    def SetSRimPrice80PredQ(self, nSRimPrice80PredQ):
        self.__nSRimPrice80PredQ = nSRimPrice80PredQ

    def SRimPrice80PredQ(self):
        return self.__nSRimPrice80PredQ

    def SetSRimPrice80PredY(self, nSRimPrice80PredY):
        self.__nSRimPrice80PredY = nSRimPrice80PredY

    def SRimPrice80PredY(self):
        return self.__nSRimPrice80PredY

    def SetSRimPrice80_y1(self, nSRimPrice80_y1):
        self.__nSRimPrice80_y1 = nSRimPrice80_y1

    def SRimPrice80_y1(self):
        return self.__nSRimPrice80_y1


    def SetSRimPrice90Consen(self, nSRimPrice90Consen):
        self.__nSRimPrice90Consen = nSRimPrice90Consen

    def SRimPrice90Consen(self):
        return self.__nSRimPrice90Consen

    def SetSRimPrice90PredQ(self, nSRimPrice90PredQ):
        self.__nSRimPrice90PredQ = nSRimPrice90PredQ

    def SRimPrice90PredQ(self):
        return self.__nSRimPrice90PredQ

    def SetSRimPrice90PredY(self, nSRiPrice90mPredY):
        self.__nSRimPrice90PredY = nSRiPrice90mPredY

    def SRimPrice90PredY(self):
        return self.__nSRimPrice90PredY

    def SetSRimPrice90_y1(self, nSRimPrice90_y1):
        self.__nSRimPrice90_y1 = nSRimPrice90_y1

    def SRimPrice90_y1(self):
        return self.__nSRimPrice90_y1


    def SetSRimPrice100Consen(self, nSRimPrice100Consen):
        self.__nSRimPrice100Consen = nSRimPrice100Consen

    def SRimPrice100Consen(self):
        return self.__nSRimPrice100Consen

    def SetSRimPrice100PredQ(self, nSRimPrice100PredQ):
        self.__nSRimPrice100PredQ = nSRimPrice100PredQ

    def SRimPrice100PredQ(self):
        return self.__nSRimPrice100PredQ

    def SetSRimPrice100PredY(self, nSRimPrice100PredY):
        self.__nSRimPrice100PredY = nSRimPrice100PredY

    def SRimPrice100PredY(self):
        return self.__nSRimPrice100PredY

    def SetSRimPrice100_y1(self, nSRimPrice100_y1):
        self.__nSRimPrice100_y1 = nSRimPrice100_y1

    def SRimPrice100_y1(self):
        return self.__nSRimPrice100_y1


    # SRIM 기대수익률
    def SetSRimExpRate80Consen(self, dSRimExpRate80Consen):
        self.__dSRimExpRate80Consen = dSRimExpRate80Consen

    def SRimExpRate80Consen(self):
        return self.__dSRimExpRate80Consen

    def SetSRimExpRate80PredQ(self, dSRimExpRate80PredQ):
        self.__dSRimExpRate80PredQ = dSRimExpRate80PredQ

    def SRimExpRate80PredQ(self):
        return self.__dSRimExpRate80PredQ

    def SetSRimExpRate80PredY(self, dSRimExpRate80PredY):
        self.__dSRimExpRate80PredY= dSRimExpRate80PredY

    def SRimExpRate80PredY(self):
        return self.__dSRimExpRate80PredY

    def SetSRimExpRate80_y1(self, dSRimExpRate80_y1):
        self.__dSRimExpRate80_y1 = dSRimExpRate80_y1

    def SRimExpRate80_y1(self):
        return self.__dSRimExpRate80_y1

    def SetSRimExpRateAvg80(self, dSRimExpRateAvg80):
        self.__dSRimExpRateAvg80 = dSRimExpRateAvg80

    def SRimExpRateAvg80(self):
        return self.__dSRimExpRateAvg80

    def SetSRimExpRate90Consen(self, dSRimExpRate90Consen):
        self.__dSRimExpRate90Consen = dSRimExpRate90Consen

    def SRimExpRate90Consen(self):
        return self.__dSRimExpRate90Consen

    def SetSRimExpRate90PredQ(self, dSRimExpRate90PredQ):
        self.__dSRimExpRate90PredQ = dSRimExpRate90PredQ

    def SRimExpRate90PredQ(self):
        return self.__dSRimExpRate90PredQ

    def SetSRimExpRate90PredY(self, dSRimExpRate90PredY):
        self.__dSRimExpRate90PredY= dSRimExpRate90PredY

    def SRimExpRate90PredY(self):
        return self.__dSRimExpRate90PredY

    def SetSRimExpRate90_y1(self, dSRimExpRate90_y1):
        self.__dSRimExpRate90_y1 = dSRimExpRate90_y1

    def SRimExpRate90_y1(self):
        return self.__dSRimExpRate90_y1

    def SetSRimExpRateAvg90(self, dSRimExpRateAvg90):
        self.__dSRimExpRateAvg90 = dSRimExpRateAvg90

    def SRimExpRateAvg90(self):
        return self.__dSRimExpRateAvg90

    def SetSRimExpRate100Consen(self, dSRimExpRate100Consen):
        self.__dSRimExpRate100Consen = dSRimExpRate100Consen

    def SRimExpRate100Consen(self):
        return self.__dSRimExpRate100Consen

    def SetSRimExpRate100PredQ(self, dSRimExpRate100PredQ):
        self.__dSRimExpRate100PredQ = dSRimExpRate100PredQ

    def SRimExpRate100PredQ(self):
        return self.__dSRimExpRate100PredQ

    def SetSRimExpRate100PredY(self, dSRimExpRate100PredY):
        self.__dSRimExpRate100PredY= dSRimExpRate100PredY

    def SRimExpRate100PredY(self):
        return self.__dSRimExpRate100PredY

    def SetSRimExpRate100_y1(self, dSRimExpRate100_y1):
        self.__dSRimExpRate100_y1 = dSRimExpRate100_y1

    def SRimExpRate100_y1(self):
        return self.__dSRimExpRate100_y1

    def SetSRimExpRateAvg100(self, dSRimExpRateAvg100):
        self.__dSRimExpRateAvg100 = dSRimExpRateAvg100

    def SRimExpRateAvg100(self):
        return self.__dSRimExpRateAvg100

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

    # 영업현금흐름 - 영업이익
    def SetCfBsProfDiff_y1(self, nCfBsProfDiff_y1):
        self.__nCfBsProfDiff_y1 = nCfBsProfDiff_y1

    def CfBsProfDiff_y1(self):
        return self.__nCfBsProfDiff_y1

    def SetCfBsProfDiffLastQ(self, nCfBsProfDiffLastQ):
        self.__nCfBsProfDiffLastQ = nCfBsProfDiffLastQ

    def CfBsProfDiffLastQ(self):
        return self.__nCfBsProfDiffLastQ

    # 현금흐름패턴
    def SetCfPattern_y1(self, sCfPattern_y1):
        self.__sCfPattern_y1 = sCfPattern_y1

    def CfPattern_y1(self):
        return self.__sCfPattern_y1

    def SetCfPatternLastQ(self, sCfPatternLastQ):
        self.__sCfPatternLastQ = sCfPatternLastQ

    def CfPatternLastQ(self):
        return self.__sCfPatternLastQ

    # PEGR
    def SetPegr(self, dPegr):
        self.__dPegr = dPegr

    def Pegr(self):
        return self.__dPegr


    # 자본잠식
    def SetCortaxCond(self, sCortaxCond):
        self.__sCortaxCond = sCortaxCond

    def CortaxCond(self):
        return self.__sCortaxCond


    # KPRICE
    def SetKPriceBsProf_y1(self, nKPriceBsProf_y1):
        self.__nKPriceBsProf_y1 = nKPriceBsProf_y1

    def KPriceBsProf_y1(self):
        return self.__nKPriceBsProf_y1

    def SetKPriceBsProfPredQ(self, nKPriceBsProfPredQ):
        self.__nKPriceBsProfPredQ = nKPriceBsProfPredQ

    def KPriceBsProfPredQ(self):
        return self.__nKPriceBsProfPredQ

    def SetKPriceNetProf_y1(self, nKPriceNetProf_y1):
        self.__nKPriceNetProf_y1 = nKPriceNetProf_y1

    def KPriceNetProf_y1(self):
        return  self.__nKPriceNetProf_y1

    def SetKPriceNetProfPredQ(self, nKPriceNetProfPredQ):
        self.__nKPriceNetProfPredQ = nKPriceNetProfPredQ

    def KPriceNetProfPredQ(self):
        return self.__nKPriceNetProfPredQ

    def SetKPriceNetProfPredY(self, nKPriceNetProfPredY):
        self.__nKPriceNetProfPredY = nKPriceNetProfPredY

    def KPriceNetProfPredY(self):
        return self.__nKPriceNetProfPredY

    def SetKPriceNetProfConsen(self, nKPriceNetProfConsen):
        self.__nKPriceNetProfConsen = nKPriceNetProfConsen

    def KPriceNetProfConsen(self):
        return self.__nKPriceNetProfConsen

    # KPRICE 기대수익률
    def SetKPriceBsProfExpRate_y1(self, nKPriceBsProfExpRate_y1):
        self.__nKPriceBsProfExpRate_y1= nKPriceBsProfExpRate_y1

    def KPriceBsProfExpRate_y1(self):
        return self.__nKPriceBsProfExpRate_y1

    def SetKPriceBsProfExpRatePredQ(self, nKPriceBsProfExpRatePredQ):
        self.__nKPriceBsProfExpRatePredQ = nKPriceBsProfExpRatePredQ

    def KPriceBsProfExpRatePredQ(self):
        return self.__nKPriceBsProfExpRatePredQ


    def SetKPriceNetProfExpRate_y1(self, nKPriceNetProfExpRate_y1):
        self.__nKPriceNetProfExpRate_y1 = nKPriceNetProfExpRate_y1

    def KPriceNetProfExpRate_y1(self):
        return self.__nKPriceNetProfExpRate_y1

    def SetKPriceNetProfExpRatePredQ(self, nKPriceNetProfExpRatePredQ):
        self.__nKPriceNetProfExpRatePredQ = nKPriceNetProfExpRatePredQ

    def KPriceNetProfExpRatePredQ(self):
        return self.__nKPriceNetProfExpRatePredQ

    def SetKPriceNetProfExpRatePredY(self, nKPriceNetProfExpRatePredY):
        self.__nKPriceNetProfExpRatePredY = nKPriceNetProfExpRatePredY

    def KPriceNetProfExpRatePredY(self):
        return self.__nKPriceNetProfExpRatePredY

    def SetKPriceNetProfExpRateConsen(self, nKPriceNetProfExpRateConsen):
        self.__nKPriceNetProfExpRateConsen = nKPriceNetProfExpRateConsen

    def KPriceNetProfExpRateConsen(self):
        return self.__nKPriceNetProfExpRateConsen

    # Pass/Fail
    def SetPassFail(self, sPassFail):
        self.__sPassFail = sPassFail

    def PassFail(self):
        return self.__sPassFail

    def SetFailReason(self, sFailReason):
        self.__sFailReason = sFailReason

    def FailReason(self):
        return self.__sFailReason

    # 매출 증가율
    # Setter
    def SetSalesIncRate_y3_y2(self, dRate):
        self.__dSalesIncRate_y3_y2 = dRate

    def SetSalesIncRate_y2_y1(self, dRate):
        self.__dSalesIncRate_y2_y1 = dRate

    def SetSalesIncRate_lqy1_lq(self, dRate):
        self.__dSalesIncRate_lqy1_lq = dRate

    def SetSalesIncRateAvg(self, dRate):
        self.__dSalesIncRateAvg = dRate

    def SetSalesIncRateTrend(self, sTrend):
        self.__sSalesIncRateTrend = sTrend

    # Getter
    def SalesIncRate_y3_y2(self):
        return self.__dSalesIncRate_y3_y2

    def SalesIncRate_y2_y1(self):
        return self.__dSalesIncRate_y2_y1

    def SalesIncRate_lqy1_lq(self):
        return self.__dSalesIncRate_lqy1_lq

    def SalesIncRateAvg(self):
        return self.__dSalesIncRateAvg

    def SalesIncRateTrend(self):
        return self.__sSalesIncRateTrend

    # 영익 증가율
    # Setter
    def SetBsProfIncRate_y3_y2(self, dRate):
        self.__dBsProfIncRate_y3_y2 = dRate

    def SetBsProfIncRate_y2_y1(self, dRate):
        self.__dBsProfIncRate_y2_y1 = dRate

    def SetBsProfIncRate_lqy1_lq(self, dRate):
        self.__dBsProfIncRate_lqy1_lq = dRate

    def SetBsProfIncRateAvg(self, dRate):
        self.__dBsProfIncRateAvg = dRate

    def SetBsProfIncRateTrend(self, sTrend):
        self.__sBsProfIncRateTrend = sTrend

    # Getter
    def BsProfIncRate_y3_y2(self):
        return self.__dBsProfIncRate_y3_y2

    def BsProfIncRate_y2_y1(self):
        return self.__dBsProfIncRate_y2_y1

    def BsProfIncRate_lqy1_lq(self):
        return self.__dBsProfIncRate_lqy1_lq

    def BsProfIncRateAvg(self):
        return self.__dBsProfIncRateAvg

    def BsProfIncRateTrend(self):
        return self.__sBsProfIncRateTrend


class CStockCustomModel:

    def __init__(self, stockCode ):
        self.__sStockCode = stockCode
        self.__Data = CStockCustomData(stockCode)

    def Data(self):
        return self.__Data

    def UpdateStockCustomData(self, fnData : CFnguideData, kisData : CKisRatingData):

        if not fnData or not kisData :
            print(" - Fail :: Invalid Data ")
            return False

        # 채권기대수익률
        self.__Data.SetBondBBB_5Rate(kisData.BondBBB_5Rate())

        # 지배주주순이익
        nDomNetProfPredQ = self.DomNetProfPredQ(fnData.LastQ(),
                                                fnData.DomNetProf_y1(),
                                                fnData.DomNetProfLastQ(),
                                                fnData.DomNetProfLastQ_y1())
        self.__Data.SetDomNetProfPredQ(nDomNetProfPredQ)
        # 영업이익
        nBsProfPredQ = self.BsProfPredQ(fnData.LastQ(),
                                        fnData.BsProf_y1(),
                                        fnData.BsProfLastQ(),
                                        fnData.BsProfLastQ_y1())
        self.__Data.SetBsProfPredQ(nBsProfPredQ)

        # 지배주주지분
        nDomCapPredQ = self.DomCapPredQ(fnData.LastQ(),
                                        fnData.DomCap_y1(),
                                        fnData.DomCapLastQ(),
                                        nDomNetProfPredQ)
        self.__Data.SetDomCapPredQ(nDomCapPredQ)

        # ROE
        dRoePredQ = self.RoePredQ(nDomNetProfPredQ, fnData.DomCapLastQ())
        dRoePredY = self.RoePredY(fnData.Roe_y1(), fnData.Roe_y2(), fnData.Roe_y3())
        dRoeBsProf_y1 = self.RoeBsProf(fnData.BsProf_y1(),fnData.DomCap_y1())
        dRoeBsProfPredQ = self.RoeBsProfPredQ(nBsProfPredQ,fnData.DomCapLastQ())
        self.__Data.SetRoePredQ(dRoePredQ)
        self.__Data.SetRoePredY(dRoePredY)
        self.__Data.SetRoeBsProf_y1(dRoeBsProf_y1)
        self.__Data.SetRoeBsProfPredQ(dRoeBsProfPredQ)

        # EPS
        nEpsPredQ = self.EpsPredQ(nDomNetProfPredQ, fnData.StockCntTot())
        nEpsPredY = self.EpsPredY(fnData.Eps_y1(), fnData.Eps_y2(), fnData.Eps_y3())
        nEpsBsProfPredQ = self.EpsBsProfPredQ(nBsProfPredQ, fnData.StockCntTot())
        nEpsBsProf_y1 = self.EpsBsProf(fnData.BsProf_y1(), fnData.StockCntTot())
        self.__Data.SetEpsPredQ(nEpsPredQ)
        self.__Data.SetEpsPredY(nEpsPredY)
        self.__Data.SetEpsBsProfPredQ(nEpsBsProfPredQ)
        self.__Data.SetEpsBsProf_y1(nEpsBsProf_y1)

        # SRIM
        nSRim80Consen = self.SRim(nDomCapPredQ, fnData.RoeConsen(),
                                  kisData.BondBBB_5Rate(), 0.8)
        nSRim80PredQ = self.SRim(nDomCapPredQ, dRoePredQ,
                                 kisData.BondBBB_5Rate(), 0.8)
        nSRim80PredY = self.SRim(nDomCapPredQ, dRoePredY,
                                 kisData.BondBBB_5Rate(), 0.8)
        nSRim80_y1 = self.SRim(nDomCapPredQ, fnData.Roe_y1(),
                               kisData.BondBBB_5Rate(), 0.8)
        self.__Data.SetSRim80Consen(nSRim80Consen)
        self.__Data.SetSRim80PredQ(nSRim80PredQ)
        self.__Data.SetSRim80PredY(nSRim80PredY)
        self.__Data.SetSRim80_y1(nSRim80_y1)

        nSRim90Consen = self.SRim(nDomCapPredQ, fnData.RoeConsen(),
                                  kisData.BondBBB_5Rate(), 0.9)
        nSRim90PredQ = self.SRim(nDomCapPredQ, dRoePredQ,
                                 kisData.BondBBB_5Rate(), 0.9)
        nSRim90PredY = self.SRim(nDomCapPredQ, dRoePredY,
                                 kisData.BondBBB_5Rate(), 0.9)
        nSRim90_y1 = self.SRim(nDomCapPredQ, fnData.Roe_y1(),
                               kisData.BondBBB_5Rate(), 0.9)
        self.__Data.SetSRim90Consen(nSRim90Consen)
        self.__Data.SetSRim90PredQ(nSRim90PredQ)
        self.__Data.SetSRim90PredY(nSRim90PredY)
        self.__Data.SetSRim90_y1(nSRim90_y1)

        nSRim100Consen = self.SRim(nDomCapPredQ, fnData.RoeConsen(),
                                   kisData.BondBBB_5Rate(), 1.0)
        nSRim100PredQ = self.SRim(nDomCapPredQ, dRoePredQ,
                                  kisData.BondBBB_5Rate(), 1.0)
        nSRim100PredY = self.SRim(nDomCapPredQ, dRoePredY,
                                  kisData.BondBBB_5Rate(), 1.0)
        nSRim100_y1 = self.SRim(nDomCapPredQ, fnData.Roe_y1(),
                                kisData.BondBBB_5Rate(), 1.0)
        self.__Data.SetSRim100Consen(nSRim100Consen)
        self.__Data.SetSRim100PredQ(nSRim100PredQ)
        self.__Data.SetSRim100PredY(nSRim100PredY)
        self.__Data.SetSRim100_y1(nSRim100_y1)

        # SRIM 적정주가
        nSRimPrice80Consen = self.SRimPrice(nSRim80Consen,fnData.StockCntTot())
        nSRimPrice80PredQ = self.SRimPrice(nSRim80PredQ,fnData.StockCntTot())
        nSRimPrice80PredY = self.SRimPrice(nSRim80PredY,fnData.StockCntTot())
        nSRimPrice80_y1 = self.SRimPrice(nSRim80_y1,fnData.StockCntTot())
        self.__Data.SetSRimPrice80Consen(nSRimPrice80Consen)
        self.__Data.SetSRimPrice80PredQ(nSRimPrice80PredQ)
        self.__Data.SetSRimPrice80PredY(nSRimPrice80PredY)
        self.__Data.SetSRimPrice80_y1(nSRimPrice80_y1)

        nSRimPrice90Consen = self.SRimPrice(nSRim90Consen, fnData.StockCntTot())
        nSRimPrice90PredQ = self.SRimPrice(nSRim90PredQ, fnData.StockCntTot())
        nSRimPrice90PredY = self.SRimPrice(nSRim90PredY, fnData.StockCntTot())
        nSRimPrice90_y1 = self.SRimPrice(nSRim90_y1, fnData.StockCntTot())
        self.__Data.SetSRimPrice90Consen(nSRimPrice90Consen)
        self.__Data.SetSRimPrice90PredQ(nSRimPrice90PredQ)
        self.__Data.SetSRimPrice90PredY(nSRimPrice90PredY)
        self.__Data.SetSRimPrice90_y1(nSRimPrice90_y1)

        nSRimPrice100Consen = self.SRimPrice(nSRim100Consen, fnData.StockCntTot())
        nSRimPrice100PredQ = self.SRimPrice(nSRim100PredQ, fnData.StockCntTot())
        nSRimPrice100PredY = self.SRimPrice(nSRim100PredY, fnData.StockCntTot())
        nSRimPrice100_y1 = self.SRimPrice(nSRim100_y1, fnData.StockCntTot())
        self.__Data.SetSRimPrice100Consen(nSRimPrice100Consen)
        self.__Data.SetSRimPrice100PredQ(nSRimPrice100PredQ)
        self.__Data.SetSRimPrice100PredY(nSRimPrice100PredY)
        self.__Data.SetSRimPrice100_y1(nSRimPrice100_y1)

        # SRIM 기대수익률
        dSRimExpRate80Consen = self.ExpReturnRate(nSRimPrice80Consen, fnData.LastPrice())
        dSRimExpRate80PredQ = self.ExpReturnRate(nSRimPrice80PredQ, fnData.LastPrice())
        dSRimExpRate80PredY = self.ExpReturnRate(nSRimPrice80PredY, fnData.LastPrice())
        dSRimExpRate80_y1 = self.ExpReturnRate(nSRimPrice80_y1, fnData.LastPrice())
        self.__Data.SetSRimExpRate80Consen(dSRimExpRate80Consen)
        self.__Data.SetSRimExpRate80PredQ(dSRimExpRate80PredQ)
        self.__Data.SetSRimExpRate80PredY(dSRimExpRate80PredY)
        self.__Data.SetSRimExpRate80_y1(dSRimExpRate80_y1)

        dSRimExpRate90Consen = self.ExpReturnRate(nSRimPrice90Consen, fnData.LastPrice())
        dSRimExpRate90PredQ = self.ExpReturnRate(nSRimPrice90PredQ, fnData.LastPrice())
        dSRimExpRate90PredY = self.ExpReturnRate(nSRimPrice90PredY, fnData.LastPrice())
        dSRimExpRate90_y1 = self.ExpReturnRate(nSRimPrice90_y1, fnData.LastPrice())
        self.__Data.SetSRimExpRate90Consen(dSRimExpRate90Consen)
        self.__Data.SetSRimExpRate90PredQ(dSRimExpRate90PredQ)
        self.__Data.SetSRimExpRate90PredY(dSRimExpRate90PredY)
        self.__Data.SetSRimExpRate90_y1(dSRimExpRate90_y1)

        dSRimExpRate100Consen = self.ExpReturnRate(nSRimPrice100Consen, fnData.LastPrice())
        dSRimExpRate100PredQ = self.ExpReturnRate(nSRimPrice100PredQ, fnData.LastPrice())
        dSRimExpRate100PredY = self.ExpReturnRate(nSRimPrice100PredY, fnData.LastPrice())
        dSRimExpRate100_y1 = self.ExpReturnRate(nSRimPrice100_y1, fnData.LastPrice())
        self.__Data.SetSRimExpRate100Consen(dSRimExpRate100Consen)
        self.__Data.SetSRimExpRate100PredQ(dSRimExpRate100PredQ)
        self.__Data.SetSRimExpRate100PredY(dSRimExpRate100PredY)
        self.__Data.SetSRimExpRate100_y1(dSRimExpRate100_y1)

        exp100List = [dSRimExpRate100Consen, dSRimExpRate100PredQ, dSRimExpRate100PredY, dSRimExpRate100_y1]
        dSRimExpRateAvg100 = self.Average(exp100List)
        self.__Data.SetSRimExpRateAvg100(dSRimExpRateAvg100)

        exp90List = [dSRimExpRate90Consen, dSRimExpRate90PredQ, dSRimExpRate90PredY, dSRimExpRate100_y1]
        dSRimExpRateAvg90 = self.Average(exp90List)
        self.__Data.SetSRimExpRateAvg90(dSRimExpRateAvg90)

        exp80List = [dSRimExpRate80Consen, dSRimExpRate80PredQ, dSRimExpRate80PredY, dSRimExpRate100_y1]
        dSRimExpRateAvg80 = self.Average(exp80List)
        self.__Data.SetSRimExpRateAvg80(dSRimExpRateAvg80)

        # 비영업이익
        nNonBsProf_y1 = self.NonBsProf_y1(fnData.BsProfBefTax_y1(), fnData.BsProf_y1())
        nNonBsProfLastQ = self.NonBsProfLastQ(fnData.BsProfBefTaxLastQ(), fnData.BsProfLastQ())
        self.__Data.SetNonBsProf_y1(nNonBsProf_y1)
        self.__Data.SetNonBsProfLastQ(nNonBsProfLastQ)

        # 비영업이익 비율
        dNonBsRate_y1 = self.NonBsRate_y1(fnData.BsProf_y1(), nNonBsProf_y1)
        dNonBsRateLastQ = self.NonBsRateLastQ(fnData.BsProfLastQ(), nNonBsProfLastQ)
        self.__Data.SetNonBsRate_y1(dNonBsRate_y1)
        self.__Data.SetNonBsRateLastQ(dNonBsRateLastQ)

        # 영업현금흐름 - 영업이익
        nCfBsProfDiff_y1 = self.DiffVal(fnData.CfBs_y1(), fnData.BsProf_y1())
        nCfBsProfDiffLastQ = self.DiffVal(fnData.CfBsLastQ(), fnData.BsProfLastQ())
        self.__Data.SetCfBsProfDiff_y1(nCfBsProfDiff_y1)
        self.__Data.SetCfBsProfDiffLastQ(nCfBsProfDiffLastQ)

        # 현금흐름패턴
        sCfPattern_y1 = self.CfPattern(fnData.CfBs_y1(), fnData.CfInv_y1(), fnData.CfFin_y1())
        sCfPatternLastQ = self.CfPattern(fnData.CfBsLastQ(), fnData.CfInvLastQ(), fnData.CfFinLastQ())
        self.__Data.SetCfPattern_y1(sCfPattern_y1)
        self.__Data.SetCfPatternLastQ(sCfPatternLastQ)

        # PEGR
        dPegr = self.Pegr(fnData.EpsIncrRate(), fnData.Per())
        self.__Data.SetPegr(dPegr)

        # 자본잠식
        sCortaxCond = self.CortaxCond(fnData.CapTotalLastQ(), fnData.CapOrgLastQ())
        self.__Data.SetCortaxCond(sCortaxCond)

        # KPRICE
        nKPriceBsProf_y1 = self.KPrice(nEpsBsProf_y1, dRoeBsProf_y1)
        nKPriceBsProfPredQ = self.KPrice(nEpsBsProfPredQ, dRoeBsProfPredQ)
        self.__Data.SetKPriceBsProf_y1(nKPriceBsProf_y1)
        self.__Data.SetKPriceBsProfPredQ(nKPriceBsProfPredQ)

        nKPriceNetProf_y1 = self.KPrice(fnData.Eps_y1(),fnData.Roe_y1())
        nKPriceNetProfPredQ = self.KPrice(nEpsPredQ, dRoePredQ)
        nKPriceNetProfPredY = self.KPrice(nEpsPredY, dRoePredY)
        nKPriceNetProfConsen = self.KPrice(fnData.EpsConsen(), fnData.RoeConsen())
        self.__Data.SetKPriceNetProf_y1(nKPriceNetProf_y1)
        self.__Data.SetKPriceNetProfPredQ(nKPriceNetProfPredQ)
        self.__Data.SetKPriceNetProfPredY(nKPriceNetProfPredY)
        self.__Data.SetKPriceNetProfConsen(nKPriceNetProfConsen)

        # KPRICE 기대수익률
        nKPriceBsProfExpRate_y1 = self.ExpReturnRate(nKPriceBsProf_y1, fnData.LastPrice())
        nKPriceBsProfExpRatePredQ = self.ExpReturnRate(nKPriceBsProfPredQ, fnData.LastPrice())
        self.__Data.SetKPriceBsProfExpRate_y1(nKPriceBsProfExpRate_y1)
        self.__Data.SetKPriceBsProfExpRatePredQ(nKPriceBsProfExpRatePredQ)

        nKPriceNetProfExpRate_y1 = self.ExpReturnRate(nKPriceNetProf_y1, fnData.LastPrice())
        nKPriceNetProfExpRatePredQ = self.ExpReturnRate(nKPriceNetProfPredQ, fnData.LastPrice())
        nKPriceNetProfExpRatePredY = self.ExpReturnRate(nKPriceNetProfPredY, fnData.LastPrice())
        nKPriceNetProfExpRateConsen = self.ExpReturnRate(nKPriceNetProfConsen, fnData.LastPrice())
        self.__Data.SetKPriceNetProfExpRate_y1(nKPriceNetProfExpRate_y1)
        self.__Data.SetKPriceNetProfExpRatePredQ(nKPriceNetProfExpRatePredQ)
        self.__Data.SetKPriceNetProfExpRatePredY(nKPriceNetProfExpRatePredY)
        self.__Data.SetKPriceNetProfExpRateConsen(nKPriceNetProfExpRateConsen)

        # Pass/Fail
        bCortax = self.IsCortax(fnData.CapTotalLastQ(), fnData.CapOrgLastQ())
        bBsProfLoss = self.IsBsProfLoss(fnData.BsProfLastQ())
        bCfBsLoss = self.IsCfBsLoss(fnData.CfBsLastQ())
        sFailReason = self.FailReason(bBsProfLoss,bCortax,bCfBsLoss)

        self.__Data.SetFailReason(sFailReason)
        if sFailReason:
            self.__Data.SetPassFail('FAIL')
        else:
            self.__Data.SetPassFail('PASS')

        # 매출증가율
        dSalesIncRate_y3_y2 = self.ExpReturnRate(fnData.Sales_y2(), fnData.Sales_y3())
        dSalesIncRate_y2_y1 = self.ExpReturnRate(fnData.Sales_y1(), fnData.Sales_y2())
        dSalesIncRate_lqy1_lq = self.ExpReturnRate(fnData.SalesLastQ(), fnData.SalesLastQ_y1())

        self.__Data.SetSalesIncRate_y3_y2(dSalesIncRate_y3_y2)
        self.__Data.SetSalesIncRate_y2_y1(dSalesIncRate_y2_y1)
        self.__Data.SetSalesIncRate_lqy1_lq(dSalesIncRate_lqy1_lq)

        dSalesIncRateList = [dSalesIncRate_y3_y2, dSalesIncRate_y2_y1, dSalesIncRate_lqy1_lq]
        dSalesIncRateAvg = self.Average(dSalesIncRateList)
        self.__Data.SetSalesIncRateAvg(dSalesIncRateAvg)

        dSalesList = [fnData.Sales_y3(), fnData.Sales_y2(), fnData.Sales_y1()]
        sSalesIncRateTrend = self.TrendInfo(dSalesList)
        self.__Data.SetSalesIncRateTrend(sSalesIncRateTrend)

        # 영업이익 증가율
        dBsProfIncRate_y3_y2 = self.ExpReturnRate(fnData.BsProf_y2(), fnData.BsProf_y3())
        dBsProfIncRate_y2_y1 = self.ExpReturnRate(fnData.BsProf_y1(), fnData.BsProf_y2())
        dBsProfIncRate_lqy1_lq = self.ExpReturnRate(fnData.BsProfLastQ(), fnData.BsProfLastQ_y1())

        self.__Data.SetBsProfIncRate_y3_y2(dBsProfIncRate_y3_y2)
        self.__Data.SetBsProfIncRate_y2_y1(dBsProfIncRate_y2_y1)
        self.__Data.SetBsProfIncRate_lqy1_lq(dBsProfIncRate_lqy1_lq)

        dBsProfIncRateList = [dBsProfIncRate_y3_y2, dBsProfIncRate_y2_y1, dBsProfIncRate_lqy1_lq]
        dBsProfIncRateAvg = self.Average(dBsProfIncRateList)
        self.__Data.SetBsProfIncRateAvg(dBsProfIncRateAvg)

        dBsProfList = [fnData.BsProf_y3(), fnData.BsProf_y2(), fnData.BsProf_y1()]
        sBsProfIncRateTrend = self.TrendInfo(dBsProfList)
        self.__Data.SetBsProfIncRateTrend(sBsProfIncRateTrend)


        return True


    def DomNetProfPredQ(self, sLastQ, nDomNetProf_y1, nDomNetProfLastQ, nDomNetProfLastQ_y1):
        if math.isnan(nDomNetProf_y1) or math.isnan(nDomNetProfLastQ) or math.isnan(nDomNetProfLastQ_y1):
            return math.nan

        if self.QuarterNum(sLastQ) == 4:
            return nDomNetProfLastQ

        if nDomNetProfLastQ_y1 == 0 :
            return math.nan

        dIncRate = (nDomNetProfLastQ - nDomNetProfLastQ_y1) / abs(nDomNetProfLastQ_y1)
        nDomNetProfPredQ = nDomNetProf_y1 + abs(nDomNetProf_y1)*dIncRate

        return math.trunc(nDomNetProfPredQ)

    # 영업이익
    def BsProfPredQ(self, sLastQ, nBsProf_y1, nBsProfLastQ, nBsProfLastQ_y1):
        if math.isnan(nBsProf_y1) or math.isnan(nBsProfLastQ) or math.isnan(nBsProfLastQ_y1):
            return math.nan

        if self.QuarterNum(sLastQ) == 4:
            return nBsProfLastQ

        if nBsProfLastQ_y1 == 0:
            return math.nan

        dIncRate = (nBsProfLastQ - nBsProfLastQ_y1) / abs(nBsProfLastQ_y1)
        nBsProfPredQ = nBsProf_y1 + abs(nBsProf_y1)*dIncRate
        return math.trunc(nBsProfPredQ)

    def DomCapPredQ(self, sLastQ, nDomCap_y1, nDomCapLastQ, nDomNetProfPredQ):
        if math.isnan(nDomCap_y1) or math.isnan(nDomCapLastQ) or math.isnan(nDomNetProfPredQ):
            return math.nan

        if self.QuarterNum(sLastQ) == 4:
            return nDomCapLastQ

        nDomCapPredQ = nDomCap_y1 + nDomNetProfPredQ

        return nDomCapPredQ

    # 비영업이익
    def NonBsProf_y1(self, nBsProfBefTax_y1, nBsProf_y1):
        if math.isnan(nBsProfBefTax_y1) or math.isnan(nBsProf_y1):
            return math.nan
        nNonBsProf_y1 = nBsProfBefTax_y1 - nBsProf_y1
        return nNonBsProf_y1

    def NonBsProfLastQ(self, nBsProfBefTaxLastQ, nBsProfLastQ):
        if math.isnan(nBsProfBefTaxLastQ) or math.isnan(nBsProfLastQ):
            return math.nan
        nNonBsProfLastQ = nBsProfBefTaxLastQ - nBsProfLastQ
        return nNonBsProfLastQ

    # 비영업이익 비율
    def NonBsRate_y1(self, nBsProf_y1, nNonBsProf_y1):
        if math.isnan(nBsProf_y1) or math.isnan(nNonBsProf_y1):
            return math.nan

        if nBsProf_y1 == 0:
            return  math.nan

        dNonBsRate_y1 = nNonBsProf_y1 / nBsProf_y1 * 100
        return round(dNonBsRate_y1,2)

    def NonBsRateLastQ(self, nBsProfLastQ, nNonBsProfLastQ ):
        if math.isnan(nBsProfLastQ) or math.isnan(nNonBsProfLastQ):
            return math.nan

        if nBsProfLastQ == 0:
            return math.nan

        dNonBsRateLastQ = nNonBsProfLastQ / nBsProfLastQ * 100
        return round(dNonBsRateLastQ,2)





    # ROE
    def RoePredQ(self, nDomNetProfPredQ, nDomCapLastQ):
        if math.isnan(nDomNetProfPredQ) or math.isnan(nDomCapLastQ):
            return math.nan

        if nDomCapLastQ == 0:
            return math.nan

        dRoePredQ = nDomNetProfPredQ / nDomCapLastQ * 100
        return round(dRoePredQ,2)


    def RoePredY(self, dRoe_y1, dRoe_y2, dRoe_y3):
        if math.isnan(dRoe_y1) or math.isnan(dRoe_y2) or math.isnan(dRoe_y3):
            return math.nan

        dRoePredY = math.nan
        # 실적이 갑자기 빵뜬 기업들에 대한 리스크가 크다
        # if self.HasTrend(dRoe_y1, dRoe_y2, dRoe_y3):
        #     dRoePredY = dRoe_y1
        # else:
        dTotalRoe = 0
        weight = 0
        for index, val in enumerate([dRoe_y3, dRoe_y2, dRoe_y1]):
            dTotalRoe = dTotalRoe + val * (index + 1)
            weight = weight + (index + 1)

        if weight == 0:
            return math.nan

        dRoePredY = dTotalRoe / weight

        return round(dRoePredY,2)

    def RoeBsProf(self, nBsProf, nDomCap ):
        if math.isnan(nBsProf) or math.isnan(nDomCap):
            return math.nan

        if nDomCap == 0:
            return math.nan

        dRoeBsProf= nBsProf / nDomCap * 100
        return round(dRoeBsProf,2)

    def RoeBsProfPredQ(self, nBsProfPredQ, nDomCapLastQ ):
        if math.isnan(nBsProfPredQ) or math.isnan(nDomCapLastQ):
            return math.nan

        if nDomCapLastQ == 0:
            return math.nan

        dRoeBsProfPredQ = nBsProfPredQ / nDomCapLastQ * 100
        return round(dRoeBsProfPredQ,2)

    # EPS
    def EpsPredQ(self, nDomNetProfPredQ, nStockCntTot, unit = 100000000 ):
        if math.isnan(nDomNetProfPredQ) or math.isnan(nStockCntTot):
            return math.nan

        if nStockCntTot == 0:
            return math.nan

        nEpsPredQ = nDomNetProfPredQ / nStockCntTot * unit
        return math.trunc(nEpsPredQ)

    def EpsPredY(self, nEps_y1, nEps_y2, nEps_y3):
        if math.isnan(nEps_y1) or math.isnan(nEps_y2) or math.isnan(nEps_y3):
            return math.nan

        nEpsPredY = math.nan
        # 실적이 갑자기 빵뜬 기업들에 대한 리스크가 크다
        # if self.HasTrend(nEps_y1, nEps_y2, nEps_y3):
        #     nEpsPredY = nEps_y3
        # else:
        dTotalEps = 0
        weight = 0
        for index, val in enumerate([nEps_y3, nEps_y2, nEps_y1]):
            dTotalEps = dTotalEps + val * (index + 1)
            weight = weight + (index + 1)

        if weight == 0:
            return math.nan

        nEpsPredY = dTotalEps / weight

        return math.trunc(nEpsPredY)

    def EpsBsProfPredQ(self, nBsProfPredQ, nStockCntTot, unit = 100000000 ):
        if math.isnan(nBsProfPredQ) or math.isnan(nStockCntTot):
            return math.nan

        if nStockCntTot == 0:
            return math.nan

        nEpsBsProfPredQ = nBsProfPredQ / nStockCntTot * unit
        return math.trunc(nEpsBsProfPredQ)

    def EpsBsProf(self, nBsProf, nStockCntTot, unit = 100000000 ):
        if math.isnan(nBsProf) or math.isnan(nStockCntTot):
            return math.nan

        if nStockCntTot == 0:
            return math.nan

        nEpsBsProf = nBsProf / nStockCntTot * unit
        return math.trunc(nEpsBsProf)

    #SRIM
    def SRim(self, nDomCap, dRoeRate, dBondRate, w):
        if math.isnan(nDomCap) or math.isnan(dRoeRate) or math.isnan(dBondRate):
            return math.nan

        if nDomCap < 0 :
            return math.nan

        nSrim = nDomCap \
                + (nDomCap * (dRoeRate/100 - dBondRate/100)) \
                * w / (1 + dBondRate/100 - w)

        return math.trunc(nSrim)

    def SRimPrice(self, nSRim, nStockCnt, unit = 100000000 ):
        if math.isnan(nSRim) or math.isnan(nStockCnt):
            return math.nan

        if nStockCnt == 0:
            return math.nan

        nSRimPrice = nSRim / nStockCnt * unit

        return math.trunc(nSRimPrice)

    def KPrice(self, nEps, dRoe):
        if math.isnan(nEps) or math.isnan(dRoe):
            return math.nan

        if nEps < 0 or dRoe < 0:
            return math.nan

        nKPrice = nEps*dRoe

        return math.trunc(nKPrice)


    ### Util Function ###
    def HasTrend(self, val_y1, val_y2, val_y3):
        # 증가 추세이거나 감소추세일때 변화폭 확인
        if math.isnan(val_y1) or math.isnan(val_y2) or math.isnan(val_y3):
            return False

        if (val_y1 > val_y2 and val_y2 > val_y3) \
                or (val_y1 < val_y2 and val_y2 < val_y3):
            return True

        return False

    def TrendInfo(self, dataList : []):
        if len(dataList) == 0:
            return math.nan

        bInc = True
        for i in range(len(dataList)-1):
            if math.isnan(dataList[i]):
                return ''

            if i==0:
                if dataList[i] <= dataList[i+1]:
                    bInc = True
                else:
                    bInc = False
            else:
                if bInc:
                    if dataList[i] <= dataList[i+1]:
                        continue
                    else:
                        return ''
                else:
                    if dataList[i] > dataList[i+1]:
                        continue
                    else:
                        return ''

        if bInc:
            return '증가추세'
        else:
            return '감소추세'


    def ExpReturnRate(self, nExpPrice, nLastPrice):
        if math.isnan(nExpPrice) or math.isnan(nLastPrice):
            return math.nan

        if nLastPrice == 0:
            return math.nan

        dExpReturnRate = (nExpPrice - nLastPrice) / abs(nLastPrice) * 100

        return round(dExpReturnRate,2)

    def DiffVal(self, val1, val2):
        if math.isnan(val1) or math.isnan(val2):
            return math.nan

        diffVal = val1 - val2
        return diffVal

    def CfPattern(self, nCfBs, nCfInv, nCfFin ):
        if math.isnan(nCfBs) or math.isnan(nCfInv) or math.isnan(nCfFin):
            return math.nan

        sCfPattern = ''
        if nCfBs > 0:
            sCfPattern += '+'
        else:
            sCfPattern += '-'

        if nCfInv > 0:
            sCfPattern += '+'
        else:
            sCfPattern += '-'

        if nCfFin > 0:
            sCfPattern += '+'
        else:
            sCfPattern += '-'

        return sCfPattern

    def Pegr(self, dEpsIncrRate, dPer):
        if math.isnan(dEpsIncrRate) or math.isnan(dPer):
            return math.nan
        if dEpsIncrRate == 0:
            return math.nan

        dPegr = dPer / dEpsIncrRate
        return round(dPegr,2)

    def CortaxCond(self, nCapTotal, nCapOrg):
        if math.isnan(nCapTotal) or math.isnan(nCapOrg):
            return math.nan

        bCortaxCond = self.IsCortax(nCapTotal, nCapOrg)
        sCortaxCond = ""
        if bCortaxCond:
            sCortaxCond = "TRUE"
        else:
            sCortaxCond = "FALSE"

        return sCortaxCond

    def IsCortax(self, nCapTotal, nCapOrg):
        if math.isnan(nCapTotal) or math.isnan(nCapOrg):
            return False

        if nCapTotal < nCapOrg :
            return True
        else:
            return False

    def IsBsProfLoss(self, nBsProf):
        if math.isnan(nBsProf):
            return False

        if nBsProf < 0:
            return True
        else:
            return False

    def IsCfBsLoss(self, nCfBs):
        if math.isnan(nCfBs):
            return False

        if nCfBs < 0:
            return True
        else:
            return False


    def Average(self, dataList):
        if len(dataList) == 0:
            return math.nan

        dataCnt = 0
        total = 0
        for val in dataList:
            if math.isnan(val):
                continue
            dataCnt += 1
            total += val

        if dataCnt == 0:
            return math.nan

        avg = total/dataCnt

        return round(avg,2)

    def FailReason(self, bBsProfLoss, bCortax, bCfBsLoss):
        reasonList = []
        if bBsProfLoss:
            reasonList.append('영업손실')

        if bCortax:
            reasonList.append('자본잠식')

        if bCfBsLoss:
            reasonList.append('현금흐름손실')

        return ','.join(reasonList)

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





