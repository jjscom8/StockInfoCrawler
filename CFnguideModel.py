import pandas as pd
import requests
from bs4 import BeautifulSoup
import math
import re
from selenium import webdriver


class CFnguideData:
    ### Data ###
    def __init__(self, sStockCode, sCompName, sIndustry = ""):
        self.__sStockCode = sStockCode
        self.__sCompName = sCompName
        self.__sIndustry = sIndustry

        ### Snapshot ###
        self.__sMarket =''
        self.__dRoe_y1 = math.nan
        self.__dRoe_y2 = math.nan
        self.__dRoe_y3 = math.nan
        self.__dRoeConsen = math.nan
        self.__nEps_y1 = math.nan
        self.__nEps_y2 = math.nan
        self.__nEps_y3 = math.nan
        self.__nEpsConsen = math.nan
        self.__nLastPrice = math.nan
        self.__nMarketCap = math.nan
        self.__nStockCntOrd = math.nan
        self.__nStockCntPref = math.nan
        self.__nStockCntTot = math.nan
        self.__dPer = math.nan
        self.__dIndusPer = math.nan
        self.__dPbr = math.nan
        self.__dDivIncome = math.nan

        ### Finance Statement ###
        self.__sLastQ = ""
        self.__nSales_y3 = math.nan
        self.__nSales_y2 = math.nan
        self.__nSales_y1 = math.nan
        self.__nSalesLastQ = math.nan
        self.__nSalesLastQ_y1 = math.nan
        self.__nBsProf_y3 = math.nan
        self.__nBsProf_y2 = math.nan
        self.__nBsProf_y1 = math.nan
        self.__nBsProfLastQ = math.nan
        self.__nBsProfLastQ_y1 = math.nan
        self.__nDomNetProf_y1 = math.nan
        self.__nDomNetProfLastQ = math.nan
        self.__nDomNetProfLastQ_y1 = math.nan
        self.__nNetProfLastQ = math.nan
        self.__nBsProfBefTax_y1 = math.nan
        self.__nBsProfBefTaxLastQ = math.nan
        self.__nCfBs_y1 = math.nan
        self.__nCfBsLastQ = math.nan
        self.__nCfInv_y1 = math.nan
        self.__nCfInvLastQ = math.nan
        self.__nCfFin_y1 = math.nan
        self.__nCfFinLastQ = math.nan
        self.__nCapTotalLastQ = math.nan
        self.__nCapOrgLastQ = math.nan
        self.__nDomCapLastQ = math.nan
        self.__nDomCap_y1 = math.nan
        self.__nAssetLastQ = math.nan
        self.__nDebtLastQ = math.nan

        ### Finance Rate ###
        self.__dEpsIncrRate = math.nan
        self.__dNetLoanRate = math.nan
        self.__dInterCovRate = math.nan


    def StockCode(self):
        return self.__sStockCode

    def CompName(self):
        return self.__sCompName

    def Industry(self):
        return self.__sIndustry

    ### Snapshot ###
    # Setter
    def SetMarket(self, sMarket):
        self.__sMarket = sMarket

    def SetIndustry(self, sIndustry):
        self.__sIndustry = sIndustry

    def SetRoe_y1(self, dRoe_y1):
        self.__dRoe_y1 = dRoe_y1

    def SetRoe_y2(self, dRoe_y2):
        self.__dRoe_y2 = dRoe_y2

    def SetRoe_y3(self, dRoe_y3):
        self.__dRoe_y3 = dRoe_y3

    def SetRoeConsen(self, dRoeConsen):
        self.__dRoeConsen = dRoeConsen

    def SetEps_y1(self, nEps_y1):
        self.__nEps_y1 = nEps_y1

    def SetEps_y2(self, nEps_y2):
        self.__nEps_y2 = nEps_y2

    def SetEps_y3(self, nEps_y3):
        self.__nEps_y3 = nEps_y3

    def SetEpsConsen(self, nEpsConsen):
        self.__nEpsConsen = nEpsConsen

    def SetLastPrice(self, nLastPrice):
        self.__nLastPrice = nLastPrice

    def SetMarketCap(self, nMarketCap):
        self.__nMarketCap = nMarketCap

    def SetStockCntOrd(self, nStockCntOrd):
        self.__nStockCntOrd = nStockCntOrd

    def SetStockCntPref(self, nStockCntPref):
        self.__nStockCntPref = nStockCntPref

    def SetStockCntTot(self, nStockCntTot):
        self.__nStockCntTot = nStockCntTot

    def SetPer(self, dPer):
        self.__dPer = dPer

    def SetIndusPer(self, dIndusPer):
        self.__dIndusPer = dIndusPer

    def SetPbr(self, dPbr):
        self.__dPbr = dPbr

    def SetDivIncome(self, dDivIncome):
        self.__dDivIncome = dDivIncome

    # Getter
    def Market(self):
        return self.__sMarket

    def Roe_y1(self):
        return self.__dRoe_y1

    def Roe_y2(self):
        return self.__dRoe_y2

    def Roe_y3(self):
        return self.__dRoe_y3

    def RoeConsen(self):
        return self.__dRoeConsen

    def Eps_y1(self):
        return self.__nEps_y1

    def Eps_y2(self):
        return self.__nEps_y2

    def Eps_y3(self):
        return self.__nEps_y3

    def EpsConsen(self):
        return self.__nEpsConsen

    def LastPrice(self):
        return self.__nLastPrice

    def MarketCap(self):
        return self.__nMarketCap

    def StockCntOrd(self):
        return self.__nStockCntOrd

    def StockCntPref(self):
        return self.__nStockCntPref

    def StockCntTot(self):
        return self.__nStockCntTot

    def Per(self):
        return self.__dPer

    def IndusPer(self):
        return self.__dIndusPer

    def Pbr(self):
        return self.__dPbr

    def DivIncome(self):
        return self.__dDivIncome

    ### Finance Statement ###
    # Setter
    def SetLastQ(self, sLastQ):
        self.__sLastQ = sLastQ

    def SetSales_y3(self,nSales_y3):
        self.__nSales_y3 = nSales_y3

    def SetSales_y2(self,nSales_y2):
        self.__nSales_y2 = nSales_y2

    def SetSales_y1(self,nSales_y1):
        self.__nSales_y1 = nSales_y1

    def SetSalesLastQ(self,nSalesLastQ):
        self.__nSalesLastQ = nSalesLastQ

    def SetSalesLastQ_y1(self,nSalesLastQ_y1):
        self.__nSalesLastQ_y1 = nSalesLastQ_y1

    def SetSales_y1(self,nSales_y1):
        self.__nSales_y1 = nSales_y1

    def SetBsProf_y3(self,nBsProf_y3):
        self.__nBsProf_y3 = nBsProf_y3

    def SetBsProf_y2(self,nBsProf_y2):
        self.__nBsProf_y2 = nBsProf_y2

    def SetBsProf_y1(self,nBsProf_y1):
        self.__nBsProf_y1 = nBsProf_y1

    def SetBsProfLastQ(self, nBsProfLastQ):
        self.__nBsProfLastQ = nBsProfLastQ

    def SetBsProfLastQ_y1(self, nBsProfLastQ_y1):
        self.__nBsProfLastQ_y1 = nBsProfLastQ_y1

    def SetDomNetProf_y1(self, nDomNetProf_y1):
        self.__nDomNetProf_y1 = nDomNetProf_y1

    def SetDomNetProfLastQ(self, nDomNetProfLastQ):
        self.__nDomNetProfLastQ = nDomNetProfLastQ

    def SetDomNetProfLastQ_y1(self, nDomNetProfLastQ_y1):
        self.__nDomNetProfLastQ_y1 = nDomNetProfLastQ_y1

    def SetNetProfLastQ(self, nNetProfLastQ):
        self.__nNetProfLastQ = nNetProfLastQ

    def SetBsProfBefTax_y1(self, nBsProfBefTax_y1):
        self.__nBsProfBefTax_y1 = nBsProfBefTax_y1

    def SetBsProfBefTaxLastQ(self, nBsProfBefTaxLastQ):
        self.__nBsProfBefTaxLastQ = nBsProfBefTaxLastQ

    def SetCfBs_y1(self, nCfBs_y1):
        self.__nCfBs_y1 = nCfBs_y1

    def SetCfBsLastQ(self, nCfBsLastQ):
        self.__nCfBsLastQ = nCfBsLastQ

    def SetCfInv_y1(self, nCfInv_y1):
        self.__nCfInv_y1 = nCfInv_y1

    def SetCfInvLastQ(self, nCfInvLastQ):
        self.__nCfInvLastQ = nCfInvLastQ

    def SetCfFin_y1(self, nCfFin_y1):
        self.__nCfFin_y1 = nCfFin_y1

    def SetCfFinLastQ(self, nCfFinLastQ):
        self.__nCfFinLastQ = nCfFinLastQ

    def SetCapTotalLastQ(self, nCapTotalLastQ):
        self.__nCapTotalLastQ = nCapTotalLastQ

    def SetCapOrgLastQ(self, nCapOrgLastQ):
        self.__nCapOrgLastQ = nCapOrgLastQ

    def SetDomCapLastQ(self, nDomCapLastQ):
        self.__nDomCapLastQ = nDomCapLastQ

    def SetDomCap_y1(self, nDomCap_y1):
        self.__nDomCap_y1 = nDomCap_y1

    def SetAssetLastQ(self, nAssetLastQ):
        self.__nAssetLastQ = nAssetLastQ

    def SetDebtLastQ(self, nDebtLastQ):
        self.__nDebtLastQ = nDebtLastQ

    #Getter
    def LastQ(self):
        return self.__sLastQ

    def Sales_y3(self):
        return self.__nSales_y3

    def Sales_y2(self):
        return self.__nSales_y2

    def Sales_y1(self):
        return self.__nSales_y1

    def SalesLastQ(self):
        return self.__nSalesLastQ

    def SalesLastQ_y1(self):
        return self.__nSalesLastQ_y1

    def BsProf_y3(self):
        return self.__nBsProf_y3

    def BsProf_y2(self):
        return self.__nBsProf_y2

    def BsProf_y1(self):
        return self.__nBsProf_y1

    def BsProfLastQ(self):
        return self.__nBsProfLastQ

    def BsProfLastQ_y1(self):
        return self.__nBsProfLastQ_y1

    def DomNetProf_y1(self):
        return self.__nDomNetProf_y1

    def DomNetProfLastQ(self):
        return self.__nDomNetProfLastQ

    def DomNetProfLastQ_y1(self):
        return self.__nDomNetProfLastQ_y1

    def NetProfLastQ(self):
        return self.__nNetProfLastQ

    def BsProfBefTax_y1(self):
        return self.__nBsProfBefTax_y1

    def BsProfBefTaxLastQ(self):
        return self.__nBsProfBefTaxLastQ

    def CfBs_y1(self):
        return self.__nCfBs_y1

    def CfBsLastQ(self):
        return self.__nCfBsLastQ

    def CfInv_y1(self):
        return self.__nCfInv_y1

    def CfInvLastQ(self):
        return self.__nCfInvLastQ

    def CfFin_y1(self):
        return self.__nCfFin_y1

    def CfFinLastQ(self):
        return self.__nCfFinLastQ

    def CapTotalLastQ(self):
        return self.__nCapTotalLastQ

    def CapOrgLastQ(self):
        return self.__nCapOrgLastQ

    def DomCapLastQ(self):
        return self.__nDomCapLastQ

    def DomCap_y1(self):
        return self.__nDomCap_y1

    def AssetLastQ(self):
        return self.__nAssetLastQ

    def DebtLastQ(self):
        return self.__nDebtLastQ

    ### Finance Rate ###
    # Setter
    def SetEpsIncrRate(self, dEpsIncrRate):
        self.__dEpsIncrRate = dEpsIncrRate

    def SetNetLoanRate(self, dNetLoanRate):
        self.__dNetLoanRate = dNetLoanRate

    def SetInterCovRate(self, dInterCovRate):
        self.__dInterCovRate = dInterCovRate

    # Getter
    def EpsIncrRate(self):
        return self.__dEpsIncrRate

    def NetLoanRate(self):
        return self.__dNetLoanRate

    def InterCovRate(self):
        return self.__dInterCovRate

class CFnguideModel:
    def __init__(self, sStockCode, sCompName, sIndustry=""):
        self.__sStockCode = sStockCode
        self.__Data = CFnguideData(sStockCode, sCompName, sIndustry)

    def Data(self):
        return self.__Data

    def CrawlSnapshot(self):
        try:
            # Get Request
            url = 'http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{}' \
                  '&cID=&MenuYn=Y&ReportGB=D&NewMenuID=101&stkGb=701'\
                .format(self.__sStockCode)
            response = requests.get(url)

            ########## [Financial Highlight 테이블] ##########
            # 기본적으로 response.text는 Fnguide의 [+] 버튼 아래 숨겨진 문자들도 가지고 있다.
            # 그것까지 크롤링하려면,  displayed_only를 False로 지정하면 된다.
            fhDfList = pd.read_html(response.text, match=self.__sTagFhTableMark)
            fhDf = fhDfList[0].iloc[:, :5]

            # Dataframe Read후 열 전체 Data중 특정 행에서 하나라도 문자가 포함되면, 해당 열은 모두 Object(Str) Type으로 변환된다.
            # 따라서 모든 Data들을 숫자형식으로 변환하는 동시에 예외 시 NaN으로 변환한다.
            fhDf.iloc[:, 4] = pd.to_numeric(fhDf.iloc[:, 4], errors='coerce')
            fhDf.iloc[:, 3] = pd.to_numeric(fhDf.iloc[:, 3], errors='coerce')
            fhDf.iloc[:, 2] = pd.to_numeric(fhDf.iloc[:, 2], errors='coerce')
            fhDf.iloc[:, 1] = pd.to_numeric(fhDf.iloc[:, 1], errors='coerce')
            fhDf.iloc[:, 0] = fhDf.iloc[:, 0].str.replace(self.__sTagSpreadDum, "")
            fhDf.iloc[:, 0] = fhDf.iloc[:, 0].str.replace(self.__sTagEpsSnapshotDum, "",regex=False)

            # Column Name
            fhDf.set_index(fhDf.columns[0], inplace=True)

            sFhDfCol_y3 = fhDf.columns[0]
            sFhDfCol_y2 = fhDf.columns[1]
            sFhDfCol_y1 = fhDf.columns[2]
            sFhDfColConsen = fhDf.columns[3]

            # Get/Set Data
            dRoe_y1 = fhDf.loc[self.__sTagRoe, sFhDfCol_y1]
            dRoe_y2 = fhDf.loc[self.__sTagRoe, sFhDfCol_y2]
            dRoe_y3 = fhDf.loc[self.__sTagRoe, sFhDfCol_y3]
            dRoeConsen = fhDf.loc[self.__sTagRoe, sFhDfColConsen]

            self.__Data.SetRoe_y1(dRoe_y1)
            self.__Data.SetRoe_y2(dRoe_y2)
            self.__Data.SetRoe_y3(dRoe_y3)
            self.__Data.SetRoeConsen(dRoeConsen)

            nEps_y1 = fhDf.loc[self.__sTagEps, sFhDfCol_y1]
            nEps_y2 = fhDf.loc[self.__sTagEps, sFhDfCol_y2]
            nEps_y3 = fhDf.loc[self.__sTagEps, sFhDfCol_y3]
            nEpsConsen = fhDf.loc[self.__sTagEps, sFhDfColConsen]

            self.__Data.SetEps_y1(nEps_y1)
            self.__Data.SetEps_y2(nEps_y2)
            self.__Data.SetEps_y3(nEps_y3)
            self.__Data.SetEpsConsen(nEpsConsen)

            ########## [시세현황 테이블] ##########
            # 시세현황 테이블은 문자를 값으로 갖는 테이블이다.
            # 문자를 기반으로 처리한다.
            mpDfList = pd.read_html(response.text,
                                    match=self.__sTagMpTableMark)
            mpDf = mpDfList[0].iloc[:, :2]

            # Tag 이름으로 indexing
            mpDf.set_index(mpDf.columns[0], inplace=True)



            # Get/Set Datas
            sLastPrice = mpDf.loc[self.__sTagLastPrice][1]
            if isinstance(sLastPrice, str):
                sLastPrice = sLastPrice.split('/')[0]  # 최근종가
                sLastPrice = sLastPrice.replace(',', '')  # 최근종가
                nLastPrice = int(sLastPrice)
                self.__Data.SetLastPrice(nLastPrice)

            sMarketCap = mpDf.loc[self.__sTagMarketCap][1]
            if isinstance(sMarketCap, str):
                sMarketCap = sMarketCap.replace(',', '')
                nMarketCap = int(sMarketCap)
                self.__Data.SetMarketCap(nMarketCap)

            sStockCnt = mpDf.loc[self.__sTagStockCnt][1]
            if isinstance(sStockCnt, str):
                sStockCnt = sStockCnt.split('/')
                nStockCntOrd = int(sStockCnt[0].replace(',', ''))  # 발행주식수-보통주
                nStockCntPref = int(sStockCnt[1].replace(',', ''))  # 발행주식수-보통주
                nStockCntTot = nStockCntOrd + nStockCntPref

                self.__Data.SetStockCntOrd(nStockCntOrd)
                self.__Data.SetStockCntPref(nStockCntPref)
                self.__Data.SetStockCntTot(nStockCntTot)



            ########## [Top Info] ##########
            # Get Beautiful
            html = BeautifulSoup(response.text, 'html.parser')
            # KSE, KOSDAQ 정보
            market_str = html.select_one('#compBody '
                                         '> div.section.ul_corpinfo '
                                         '> div.corp_group1 > p '
                                         '> span.stxt.stxt1').string
            strMarket = market_str.split()[0]
            self.__Data.SetMarket(strMarket)
            # 업종
            industry_str = html.select_one('#compBody '
                                         '> div.section.ul_corpinfo '
                                         '> div.corp_group1 > p '
                                         '> span.stxt.stxt2').string
            self.__Data.SetIndustry(industry_str)


            sPer = html.select_one('#corp_group2 > dl:nth-child(1) > dd').string
            sPer = sPer.replace('-', '0')
            sPer = sPer.replace(',', '')
            dPer = float(sPer)
            self.__Data.SetPer(dPer)


            sIndusPer = html.select_one('#corp_group2 > dl:nth-child(3) > dd').string
            sIndusPer = sIndusPer.replace('-', '0')
            sIndusPer = sIndusPer.replace(',', '')
            dIndusPer = float(sIndusPer)
            self.__Data.SetIndusPer(dIndusPer)

            sPbr = html.select_one('#corp_group2 > dl:nth-child(4) > dd').string
            sPbr = sPbr.replace('-', '0')
            sPbr = sPbr.replace(',', '')
            dPbr = float(sPbr)
            self.__Data.SetPbr(dPbr)

            sDivIncome = html.select_one('#corp_group2 > dl:nth-child(5) > dd').string
            sDivIncome = sDivIncome.replace('%', '')
            sDivIncome = sDivIncome.replace('-', '0')
            dDivIncome = float(sDivIncome)
            self.__Data.SetDivIncome(dDivIncome)

            return True

        except ValueError:
            print("         # ValueError : {}".format(self.__sStockCode))
            print("           => pd.read_html() 실패 시 발생 가능. Table이 없는 Page")
            return False
        except KeyError:
            print("         # KeyError : {}".format(self.__sStockCode))
            print("           => df.loc[] 실패 시 발생 가능 ('해당 row/col Key가 없는 Table)")
            return False
        except IndexError:
            print("         # IndexError : {}".format(self.__sStockCode))
            return False


    def CrawlFinStat(self):
        try:
            # Get Request
            url = 'http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A{}' \
                  '&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701' \
                .format(self.__sStockCode)
            # ReportGB=D : 연결, ReportGB=B : 개별, ReportGB= : 디폴트
            # : 이거 디폴트로 해놓으면 가끔 개별로 열린다(DL이앤씨)
            # : 개별만 있는 기업은 연결에 분기 반영이 안되는 문제가 있다
            #   이런 기업들은 디폴트로 붙으면 개별로 열린다. 따라서, 디폴트로.
            response = requests.get(url)

            ########## [포괄손익계산서 테이블] ##########
            profDfList = pd.read_html(response.text,
                                    match=self.__sTagProfitTableMark,
                                    displayed_only=False)
            profDf = profDfList[0].iloc[:, :6]

            profDf.iloc[:, 5] = pd.to_numeric(profDf.iloc[:, 5], errors='coerce')
            profDf.iloc[:, 4] = pd.to_numeric(profDf.iloc[:, 4], errors='coerce')
            profDf.iloc[:, 3] = pd.to_numeric(profDf.iloc[:, 3], errors='coerce')
            profDf.iloc[:, 2] = pd.to_numeric(profDf.iloc[:, 2], errors='coerce')
            profDf.iloc[:, 1] = pd.to_numeric(profDf.iloc[:, 1], errors='coerce')
            profDf.iloc[:, 0] = profDf.iloc[:, 0].str.replace(self.__sTagSpreadDum, "")

            # Tag 이름으로 indexing
            profDf.set_index(profDf.columns[0], inplace=True)
            profDfIndexes = profDf.index.tolist()

            # Column Name
            sProfDfCol_y3 = profDf.columns[0]
            sProfDfCol_y2 = profDf.columns[1]
            sProfDfCol_y1 = profDf.columns[2]
            sProfDfColLastQ = profDf.columns[3]
            sProfDfColLastQ_y1 = profDf.columns[4]
            self.__Data.SetLastQ(sProfDfColLastQ)

            # Get/Set Data
            nSales_y3 = profDf.loc[self.__sTagSales, sProfDfCol_y3]
            nSales_y2 = profDf.loc[self.__sTagSales, sProfDfCol_y2]
            nSales_y1 = profDf.loc[self.__sTagSales, sProfDfCol_y1]
            nSalesLastQ = profDf.loc[self.__sTagSales, sProfDfColLastQ]
            nSalesLastQ_y1 = profDf.loc[self.__sTagSales, sProfDfColLastQ_y1]
            self.__Data.SetSales_y3(nSales_y3)
            self.__Data.SetSales_y2(nSales_y2)
            self.__Data.SetSales_y1(nSales_y1)
            self.__Data.SetSalesLastQ(nSalesLastQ)
            self.__Data.SetSalesLastQ_y1(nSalesLastQ_y1)

            nBsProf_y3 = profDf.loc[self.__sTagBsProf, sProfDfCol_y3]
            nBsProf_y2 = profDf.loc[self.__sTagBsProf, sProfDfCol_y2]
            nBsProf_y1 = profDf.loc[self.__sTagBsProf, sProfDfCol_y1]
            nBsProfLastQ = profDf.loc[self.__sTagBsProf, sProfDfColLastQ]
            nBsProfLastQ_y1 = profDf.loc[self.__sTagBsProf, sProfDfColLastQ_y1]
            self.__Data.SetBsProf_y3(nBsProf_y3)
            self.__Data.SetBsProf_y2(nBsProf_y2)
            self.__Data.SetBsProf_y1(nBsProf_y1)
            self.__Data.SetBsProfLastQ(nBsProfLastQ)
            self.__Data.SetBsProfLastQ_y1(nBsProfLastQ_y1)

            nNetProfLastQ = profDf.loc[self.__sTagNetProf, sProfDfColLastQ]
            self.__Data.SetNetProfLastQ(nNetProfLastQ)

            nDomNetProf_y1 = math.nan
            nDomNetProfLastQ = math.nan
            nDomNetProfLastQ_y1 = math.nan

            if self.__sTagDomNetProf in profDfIndexes:
                nDomNetProf_y1 = profDf.loc[self.__sTagDomNetProf, sProfDfCol_y1]
                nDomNetProfLastQ = profDf.loc[self.__sTagDomNetProf, sProfDfColLastQ]
                nDomNetProfLastQ_y1 = profDf.loc[self.__sTagDomNetProf, sProfDfColLastQ_y1]
            else:
                nDomNetProf_y1 = profDf.loc[self.__sTagNetProf, sProfDfCol_y1]
                nDomNetProfLastQ = profDf.loc[self.__sTagNetProf, sProfDfColLastQ]
                nDomNetProfLastQ_y1 = profDf.loc[self.__sTagNetProf, sProfDfColLastQ_y1]

            self.__Data.SetDomNetProf_y1(nDomNetProf_y1)
            self.__Data.SetDomNetProfLastQ(nDomNetProfLastQ)
            self.__Data.SetDomNetProfLastQ_y1(nDomNetProfLastQ_y1)

            nBsProfBefTax_y1 = profDf.loc[self.__sTagBsProfBefTax, sProfDfCol_y1]
            nBsProfBefTaxLastQ = profDf.loc[self.__sTagBsProfBefTax, sProfDfColLastQ]
            self.__Data.SetBsProfBefTax_y1(nBsProfBefTax_y1)
            self.__Data.SetBsProfBefTaxLastQ(nBsProfBefTaxLastQ)

            ########## [현금흐름표 테이블] ##########
            cfDfList = pd.read_html(response.text,
                                    match=self.__sTagCfTableMark,
                                    displayed_only=False)
            cfDf = cfDfList[0].iloc[:, :5]

            cfDf.iloc[:, 4] = pd.to_numeric(cfDf.iloc[:, 4], errors='coerce')
            cfDf.iloc[:, 3] = pd.to_numeric(cfDf.iloc[:, 3], errors='coerce')
            cfDf.iloc[:, 2] = pd.to_numeric(cfDf.iloc[:, 2], errors='coerce')
            cfDf.iloc[:, 1] = pd.to_numeric(cfDf.iloc[:, 1], errors='coerce')
            cfDf.iloc[:, 0] = cfDf.iloc[:, 0].str.replace(self.__sTagSpreadDum, "")

            # Tag 이름으로 indexing
            cfDf.set_index(cfDf.columns[0], inplace=True)

            # Column Name
            sCfCol_y1 = cfDf.columns[2]
            sCfColLastQ = cfDf.columns[3]

            # Get/Set Data
            nCfBs_y1 = cfDf.loc[self.__sTagCfBs, sCfCol_y1]
            nCfBsLastQ = cfDf.loc[self.__sTagCfBs, sCfColLastQ]
            self.__Data.SetCfBs_y1(nCfBs_y1)
            self.__Data.SetCfBsLastQ(nCfBsLastQ)

            nCfInv_y1 = cfDf.loc[self.__sTagCfInv, sCfCol_y1]
            nCfInvLastQ = cfDf.loc[self.__sTagCfInv, sCfColLastQ]
            self.__Data.SetCfInv_y1(nCfInv_y1)
            self.__Data.SetCfInvLastQ(nCfInvLastQ)

            nCfFin_y1 = cfDf.loc[self.__sTagCfFin, sCfCol_y1]
            nCfFinLastQ = cfDf.loc[self.__sTagCfFin, sCfColLastQ]
            self.__Data.SetCfFin_y1(nCfFin_y1)
            self.__Data.SetCfFinLastQ(nCfFinLastQ)

            ########## [재무상태표 테이블] ##########
            finStatDfList = pd.read_html(response.text,
                                         match=self.__sTagFinStatTableMark,
                                         displayed_only=False)
            finStatDf = finStatDfList[0].iloc[:, :5]

            finStatDf.iloc[:, 4] = pd.to_numeric(finStatDf.iloc[:, 4], errors='coerce')
            finStatDf.iloc[:, 3] = pd.to_numeric(finStatDf.iloc[:, 3], errors='coerce')
            finStatDf.iloc[:, 2] = pd.to_numeric(finStatDf.iloc[:, 2], errors='coerce')
            finStatDf.iloc[:, 1] = pd.to_numeric(finStatDf.iloc[:, 1], errors='coerce')

            finStatDf.iloc[:, 0] = finStatDf.iloc[:, 0].str.replace(self.__sTagSpreadDum,"")

            # Tag 이름으로 indexing
            finStatDf.set_index(finStatDf.columns[0], inplace=True)
            finStatDfIndexes = finStatDf.index.tolist()

            # Column Name
            sFinStatCol_y1 = finStatDf.columns[2]
            sFinStatColLastQ = finStatDf.columns[3]

            # Get/Set Data
            nCapTotalLastQ = finStatDf.loc[self.__sTagCapTotal, sFinStatColLastQ]
            self.__Data.SetCapTotalLastQ(nCapTotalLastQ)

            nCapOrgLastQ = finStatDf.loc[self.__sTagCapOrg, sFinStatColLastQ]
            self.__Data.SetCapOrgLastQ(nCapOrgLastQ)

            nDomCapLastQ = math.nan
            nDomCap_y1 = math.nan
            if self.__sTagDomCap in finStatDfIndexes:
                nDomCapLastQ = finStatDf.loc[self.__sTagDomCap, sFinStatColLastQ]
                nDomCap_y1 = finStatDf.loc[self.__sTagDomCap, sFinStatCol_y1]
            else:
                nDomCapLastQ = finStatDf.loc[self.__sTagCapTotal, sFinStatColLastQ]
                nDomCap_y1 = finStatDf.loc[self.__sTagCapTotal, sFinStatCol_y1]

            self.__Data.SetDomCapLastQ(nDomCapLastQ)
            self.__Data.SetDomCap_y1(nDomCap_y1)


            nAssetLastQ = finStatDf.loc[self.__sTagAsset, sFinStatColLastQ]
            self.__Data.SetAssetLastQ(nAssetLastQ)

            nDebtLastQ = finStatDf.loc[self.__sTagDebt, sFinStatColLastQ]
            self.__Data.SetDebtLastQ(nDebtLastQ)

            return True

        except ValueError:
            print("         # ValueError : {}".format(self.__sStockCode))
            print("           => pd.read_html() 실패 시 발생 가능. Table이 없는 Page")
            return False
        except KeyError:
            print("         # KeyError : {}".format(self.__sStockCode))
            print("           => df.loc[] 실패 시 발생 가능 ('해당 row/col Key가 없는 Table)")
            return False
        except IndexError:
            print("         # IndexError : {}".format(self.__sStockCode))
            return False



    def CrawlFinRate(self):
        try:
            # Get Request
            url = 'http://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A{}' \
                  '&cID=&MenuYn=Y&ReportGB=D&NewMenuID=104&stkGb=701' \
                .format(self.__sStockCode)
            response = requests.get(url)

            ########## [재무비율 테이블] ##########
            finRateDfList = pd.read_html(response.text,
                                      match=self.__sTagFinRateTableMark,
                                      displayed_only=False)
            finRateDf = finRateDfList[0].iloc[:, :6]

            finRateDf.iloc[:, 5] = pd.to_numeric(finRateDf.iloc[:, 5], errors='coerce')
            finRateDf.iloc[:, 4] = pd.to_numeric(finRateDf.iloc[:, 4], errors='coerce')
            finRateDf.iloc[:, 3] = pd.to_numeric(finRateDf.iloc[:, 3], errors='coerce')
            finRateDf.iloc[:, 2] = pd.to_numeric(finRateDf.iloc[:, 2], errors='coerce')
            finRateDf.iloc[:, 1] = pd.to_numeric(finRateDf.iloc[:, 1], errors='coerce')
            finRateDf.iloc[:, 0] = finRateDf.iloc[:, 0].str.replace(self.__sTagSpreadDum, "")
            finRateDf.iloc[:, 0] = finRateDf.iloc[:, 0].str.replace(self.__sTagEpsDum, "",regex=False)
            finRateDf.iloc[:, 0] = finRateDf.iloc[:, 0].str.replace(self.__sTagEpsIncRateDum, "",regex=False)
            finRateDf.iloc[:, 0] = finRateDf.iloc[:, 0].str.replace(self.__sTagNetLoanRateDum, "",regex=False)
            finRateDf.iloc[:, 0] = finRateDf.iloc[:, 0].str.replace(self.__sTagInterCovRateDum, "",regex=False)

            # Tag 이름으로 indexing
            finRateDf.set_index(finRateDf.columns[0], inplace=True)

            # Column Name
            sfinRateCol_y1 = finRateDf.columns[3]
            sfinRateColLastQ = finRateDf.columns[4]

            # Get/Set Data
            dEpsIncrRate = finRateDf.loc[self.__sTagEpsIncrRate, sfinRateColLastQ]
            self.__Data.SetEpsIncrRate(dEpsIncrRate)

            dNetLoanRate = finRateDf.loc[self.__sTagNetLoanRate, sfinRateColLastQ]
            self.__Data.SetNetLoanRate(dNetLoanRate)

            dInterCovRate = finRateDf.loc[self.__sTagInterCovRate, sfinRateColLastQ]
            self.__Data.SetInterCovRate(dInterCovRate)

            return True

        except ValueError:
            print("         # ValueError : {}".format(self.__sStockCode))
            print("           => pd.read_html() 실패 시 발생 가능 ('match'에 해당하는 Table이 없는 Page)")
            return False
        except KeyError:
            print("         # KeyError : {}".format(self.__sStockCode))
            print("           => df.loc[] 실패 시 발생 가능 ('해당 row/col Key가 없는 Table)")
            return False
        except IndexError:
            print("         # IndexError : {}".format(self.__sStockCode))
            return False

    #################### [Private Static Members] ####################
    # Additional Tag
    __sTagZeroCapDum = '완전잠식'
    __sTagSpreadDum = "계산에 참여한 계정 펼치기"
    __sTagEpsDum = '지배주주순이익 / 수정평균주식수 EPS'
    __sTagEpsSnapshotDum = '(원)'
    __sTagEpsIncRateDum = '((수정EPS / 수정EPS(-1Y)) - 1) * 100 EPS증가율'
    __sTagNetLoanRateDum = '(순차입부채 / 총자본) * 100 순차입금비율'
    __sTagInterCovRateDum = '(배)영업이익 / 이자비용(비영업) 이자보상배율'
    __sTagChromeDriverPath = 'chromedriver.exe'

    # 기본정보
    __sTagStockCode = '종목코드'
    __sTagCompName = '회사명'

    ### Snapshot ###
    # Financial Highlight
    __sTagFhTableMark = '지배주주지분'
    __sTagMarketPriceMark = '시가총액'
    __sTagRoe = 'ROE'
    __sTagEps = 'EPS'
    __sTagPrice = '종가'

    # 시세현황
    __sTagMpTableMark = '종가/ 전일대비'
    __sTagLastPrice = '종가/ 전일대비'
    __sTagMarketCap = '시가총액(보통주,억원)'
    __sTagStockCnt = '발행주식수(보통주/ 우선주)'

    # Top Info
    __sTagPer = 'PER'
    __sTagPbr = 'PBR'
    __sTagDividendIncome = '배당수익률'

    ### 재무제표 ###

    # 포괄손익계산서
    __sTagProfitTableMark = '영업이익'
    __sTagSales = '매출액'
    __sTagBsProf = '영업이익'
    __sTagDomNetProf = '지배주주순이익'
    __sTagNetProf = '당기순이익'
    __sTagBsProfBefTax = '세전계속사업이익'

    # 현금흐름
    __sTagCfTableMark = '영업활동으로인한현금흐름'
    __sTagCfBs = '영업활동으로인한현금흐름'
    __sTagCfInv = '투자활동으로인한현금흐름'
    __sTagCfFin = '재무활동으로인한현금흐름'

    # 재무상태표
    __sTagFinStatTableMark = '자본'
    __sTagCapTotal = '자본'
    __sTagCapOrg = '자본금'
    __sTagDomCap = '지배기업주주지분'
    __sTagAsset = '자산'
    __sTagDebt = '부채'

    ### 재무비율 ###
    # 재무비율
    __sTagFinRateTableMark = 'EPS증가율'
    __sTagEps = 'EPS'
    __sTagEpsIncrRate = 'EPS증가율'
    __sTagNetLoanRate = '순차입금비율'
    __sTagInterCovRate = '이자보상배율'





############################### [참고사항] ###############################

# 1) 테이블에서 빈칸을 읽으면 Nan으로 읽힌다.(기본적으로 문자열로 읽지만, 빈칸은 Nan이다)
# 2) Nan은 float()으로 Casting시 nan으로 변환되지만, int()로 변환 시 에러가 발생한다.


