from cpa_std.vehicle_insurance_converter.common.tools import Tool
from cpa_std.vehicle_insurance_converter.common.methods_txt import MethodsTxt
import re
from cpa_std.vehicle_insurance_converter.common.method_excel import MethodExcel

class YangGuang:
    def __init__(self,excel):
        self.excel=excel
        self.t = Tool()
        self.pdf = self.t.excel2pdf(excel)
        self.mt = MethodsTxt()
        self.code= "yangguang"
        self.name= "阳光保险"
        self.me = MethodExcel()

    def bao_dan_hao(self,ws):
        pdf=self.pdf
        pat = r'保险单号(.*?)保单生成时间'
        res = self.mt.find_patter_in_txt(pdf, pat)
        return res.replace(":", "").replace("：", "")
    
    def begin_end_date(self,ws):
        pdf=self.pdf
        pat = r'保险期间自(.*?)24:00:00'
        res=self.mt.find_patter_in_txt(pdf,  pat)
        pat = r'(.\d+)年(.\d+)月(.\d+)日'
        res = re.findall(pat, res, flags=re.DOTALL)
        by=res[0][0][-4:]
        ey=res[1][0][-4:]
        begin=f"{by}-{res[0][1]}-{res[0][2]}"
        end=f"{ey}-{res[1][1]}-{res[1][2]}"
        return begin ,end

    def ce_pai_hao(self,ws):
        pdf=self.pdf
        pat = r'号牌号码(.*?)机动车种类'
        res = self.mt.find_patter_in_txt(pdf, pat)
        if res == None or len(res) == 0: return ""
        return res

    def fa_dong_ji(self,ws):
        pdf=self.pdf
        pat = r'发动机号码(.*?)车辆识别代码'
        res = self.mt.find_patter_in_txt(pdf, pat)
        if res == None or len(res) == 0: return ""
        return res

    def ce_jia_hao(self,ws):
        pdf=self.pdf
        pat = r'车辆识别代码(.*?)险'
        res = self.mt.find_patter_in_txt(pdf, pat)
        if res == None or len(res) == 0: return ""
        return res

    def jin_e(self,ws):
        pdf=self.pdf
        pat = r'￥(.*?)元'
        res = self.mt.find_patter_in_txt(pdf,  pat)
        if res == None: return ""
        return self.t.clean(res).replace("：","")
    def bei_bao_xian_ren(self,ws):
        pdf=self.pdf
        pat = r'被名  称(.*?)保证件类型'
        res = self.mt.find_patter_in_txt(pdf, pat)
        if res == None: return ""
        return self.t.clean(res)
    def ce_zu(self,ws):
        pdf=self.pdf
        pat = r'行驶证车主：(.*?)本保单投保人：'
        res = self.mt.find_patter_in_txt(pdf, pat)
        if res == None: return ""
        return self.t.clean(res)
    def tou_bao_ren(self,ws):
        pdf=self.pdf
        pat = r'本保单投保人：(.*?)被名'
        res = self.mt.find_patter_in_txt(pdf, pat)
        if res == None: return ""
        return self.t.clean(res)
    def te_bie_tiao_kuan(self,ws):
        pdf=self.pdf
        pat = r'保险期间自(.*?)保险合同争议解决方式'
        res = self.mt.find_patter_in_txt(pdf, pat)
        return res
        
