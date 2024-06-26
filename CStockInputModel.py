from CFnguideModel import  CFnguideData
import pandas as pd
import os
import math

class CStockInputModel:

    def LoadLastQInputCsv(self, sInputPath):
        if not os.path.exists(sInputPath):
            print( ' - Error :: Invalid Path :: ',sInputPath)
            return False

        self.__lastQInput = pd.read_csv(sInputPath,encoding='CP949')

        # Indexing by Company name
        self.__lastQInput.set_index(self.__lastQInput[self.__sTagCompName],
                                    inplace=True)

        return True

    def InputComps(self):
        compList = self.__lastQInput[self.__sTagCompName].tolist()
        return compList

    def UpdateFnData(self, fnData: CFnguideData):
        sCompName = fnData.CompName()

        sLastQ = self.__lastQInput.loc[sCompName,self.__sTagLastQ]
        if sLastQ:
            fnData.SetLastQ(sLastQ)


        nAssetLastQ = self.__lastQInput.loc[sCompName,self.__sTagAssetLastQ]
        if not math.isnan(nAssetLastQ):
            fnData.SetAssetLastQ(nAssetLastQ)

        nDebtLastQ = self.__lastQInput.loc[sCompName,self.__sTagDebtLastQ]
        if not math.isnan(nDebtLastQ):
            fnData.SetDebtLastQ(nDebtLastQ)

        nCapOrgLastQ = self.__lastQInput.loc[sCompName,self.__sTagCapOrgLastQ]
        if not math.isnan(nCapOrgLastQ):
            fnData.SetCapOrgLastQ(nCapOrgLastQ)

        # 자본
        nCapTotalLastQ = self.__lastQInput.loc[sCompName,self.__sTagCapTotalLastQ]
        nOldCapTotalLastQ =  fnData.CapTotalLastQ()
        if not math.isnan(nCapTotalLastQ):
            fnData.SetCapTotalLastQ(nCapTotalLastQ)

        # 매출
        nSalesLastQ = self.__lastQInput.loc[sCompName,self.__sTagSalesLastQ]
        if not math.isnan(nSalesLastQ):
            fnData.SetSalesLastQ(nSalesLastQ)

        nSalesLastQ_y1 = self.__lastQInput.loc[sCompName,self.__sTagSalesLastQ_y1]
        if not math.isnan(nSalesLastQ_y1):
            fnData.SetSalesLastQ_y1(nSalesLastQ_y1)

        # 지배주주자본: 지배/비지배 지분율 반영
        nDomCapLastQ = self.__lastQInput.loc[sCompName,self.__sTagDomCapLastQ]
        if math.isnan(nDomCapLastQ):
            domRatio = fnData.DomCapLastQ() / nOldCapTotalLastQ
            nDomCapLastQ = domRatio* nCapTotalLastQ

        fnData.SetDomCapLastQ(int(nDomCapLastQ))


        nBsProfLastQ = self.__lastQInput.loc[sCompName,self.__sTagBsProfLastQ]
        if not math.isnan(nBsProfLastQ):
            fnData.SetBsProfLastQ(nBsProfLastQ)

        nBsProfLastQ_y1 = self.__lastQInput.loc[sCompName,self.__sTagBsProfLastQ_y1]
        if not math.isnan(nBsProfLastQ_y1):
            fnData.SetBsProfLastQ_y1(nBsProfLastQ_y1)

        # 당기순이익
        nNetProfLastQ = self.__lastQInput.loc[sCompName,self.__sTagNetProfLastQ]
        nOldNetProfLastQ = fnData.NetProfLastQ()
        if not math.isnan(nNetProfLastQ):
            fnData.SetNetProfLastQ(nNetProfLastQ)

        # 지배순이익: 지배/비지배 지분율 반영
        nDomNetProfLastQ = self.__lastQInput.loc[sCompName,self.__sTagDomNetProfLastQ]
        if math.isnan(nDomNetProfLastQ):
            domRatio = fnData.DomNetProfLastQ() / nOldNetProfLastQ
            nDomNetProfLastQ = domRatio * nNetProfLastQ

        fnData.SetDomNetProfLastQ(int(nDomNetProfLastQ))

        nDomNetProfLastQ_y1 = self.__lastQInput.loc[sCompName,self.__sTagDomNetProfLastQ_y1]
        if not math.isnan(nDomNetProfLastQ_y1):
            fnData.SetDomNetProfLastQ_y1(nDomNetProfLastQ_y1)

        nBsProfBefTaxLastQ = self.__lastQInput.loc[sCompName,self.__sTagBsProfBefTaxLastQ]
        if not math.isnan(nBsProfBefTaxLastQ):
            fnData.SetBsProfBefTaxLastQ(nBsProfBefTaxLastQ)


        nCfBsLastQ = self.__lastQInput.loc[sCompName,self.__sTagCfBsLastQ]
        if not math.isnan(nCfBsLastQ):
            fnData.SetCfBsLastQ(nCfBsLastQ)

        nCfInvLastQ = self.__lastQInput.loc[sCompName,self.__sTagCfInvLastQ]
        if not math.isnan(nCfInvLastQ):
            fnData.SetCfInvLastQ(nCfInvLastQ)

        nCfFinLastQ = self.__lastQInput.loc[sCompName,self.__sTagCfFinLastQ]
        if not math.isnan(nCfFinLastQ):
            fnData.SetCfFinLastQ(nCfFinLastQ)

        return True

    __sTagCompName = '회사명'
    __sTagLastQ = '회계분기'

    __sTagCapTotalLastQ = '자본[Q](억)'
    __sTagDomCapLastQ = '지배주주자본[Q](억)'
    __sTagAssetLastQ = '자산[Q](억)'
    __sTagDebtLastQ = '부채[Q](억)'
    __sTagCapOrgLastQ = '자본금[Q](억)'

    __sTagSalesLastQ = '매출[Q](억)'
    __sTagSalesLastQ_y1 = '매출[Q-Y1](억)'

    __sTagBsProfLastQ = '영업이익[Q](억)'
    __sTagBsProfLastQ_y1 = '영업이익[Q-Y1](억)'

    __sTagNetProfLastQ = '당기순이익[Q](억)'
    __sTagDomNetProfLastQ = '지배순이익[Q](억)'
    __sTagDomNetProfLastQ_y1 = '지배순이익[Q-Y1](억)'
    __sTagBsProfBefTaxLastQ = '세전계속사업이익[Q](억)'

    __sTagCfBsLastQ = '영업CF[Q](억)'
    __sTagCfInvLastQ = '투자CF[Q](억)'
    __sTagCfFinLastQ = '재무CF[Q](억)'
