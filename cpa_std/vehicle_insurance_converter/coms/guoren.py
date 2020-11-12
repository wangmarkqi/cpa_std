from cpa_std.vehicle_insurance_converter.common.tools import Tool
import re
from cpa_std.vehicle_insurance_converter.common.methods_txt import MethodsTxt
from cpa_std.vehicle_insurance_converter.common.method_excel import MethodExcel
class GuoRen:
    def __init__(self,excel):
        self.excel=excel
        self.t=Tool()
        self.pdf=self.t.excel2pdf(excel)
        self.mt=MethodsTxt()
        self.code="guoren"
        self.name = "国任"
        self.me = MethodExcel()

    def bao_dan_hao(self,ws):
        cell=self.me.find_key_cell(ws,"保险单号")
        pat = r'保险单号(.*?)$'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if len(res) > 0:
            res1 = self.t.date_format(res[0])
            return res1
        return ""
        
    def begin_end_date(self,ws):
        k="保险期间"
        cell = self.me.find_key_row(ws, k)
        pat = r'保险期间：(.*?)00分起至(.*?)00'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res and len(res[0]) == 2:
            begin = res[0][0]
            end = res[0][1]
            return self.t.date_format(begin), self.t.date_format(end)
        return "",""
    def ce_pai_hao(self,ws):
        k='号牌号码'
        res=self.me.find_key_cell(ws,k)
        res=res.replace(k,"")
        return self.t.date_format(res)

    def fa_dong_ji(self,ws):
        k = '发动机号'
        res=self.me.find_key_cell(ws,k)
        res=res.replace(k,"")
        return self.t.date_format(res)

    def ce_jia_hao(self,ws):
        k = 'VIN码/车架号'
        res=self.me.find_key_cell(ws,k)
        res=res.replace(k,"")
        return self.t.date_format(res)

    def jin_e(self,ws):
        k = '保险费合计'
        cell=self.me.find_key_cell(ws,k)
        pat = r'¥：(.*?)元'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res == None : return ""
        return self.t.clean(res[0])



    def bei_bao_xian_ren(self, ws):
        k = '被保险人'
        res = self.me.find_key_cell(ws, k)
        res = res.replace(k, "")
        return self.t.date_format(res)

    def ce_zu(self,ws):
        k = '行驶证车主'
        res = self.me.find_key_cell(ws,k)
        res=res.replace(k,"")
        return self.t.date_format(res)

    def tou_bao_ren(self,ws):
        return ""
        

    def te_bie_tiao_kuan(self,ws):
        k= '特别约定'
        res = self.me.find_key_cell(ws,k)
        return res
