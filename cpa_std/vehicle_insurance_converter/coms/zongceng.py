from cpa_std.vehicle_insurance_converter.common.tools import Tool
import re
from cpa_std.vehicle_insurance_converter.common.methods_txt import MethodsTxt
from cpa_std.vehicle_insurance_converter.common.method_excel import MethodExcel
class Zongceng:
    def __init__(self,excel):
        self.excel=excel
        self.t=Tool()
        self.pdf=self.t.excel2pdf(excel)
        self.mt=MethodsTxt()
        self.code="zongceng"
        self.name = "众诚"
        self.me = MethodExcel()

    def bao_dan_hao(self,ws):
        cell=self.me.find_key_cell(ws,"保险单号")
        pat = r'保险单号码(.*?)鉴于投保人'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if len(res) > 0:
            res1 = self.t.date_format(res[0])
            return res1
        return ""
        
    def begin_end_date(self,ws):
        k="0时0分"
        cell = self.me.find_key_row(ws, k)
        pat = r'自(.*?)0时0分起至(.*?)0时0'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res and len(res[0]) == 2:
            begin = res[0][0]
            end = res[0][1]
            return self.t.date_format(begin), self.t.date_format(end)
        return "",""
    def ce_pai_hao(self,ws):
        k='号牌号码'
        res=self.me.find_key_cell_right(ws,k)
        return res.replace("联系电话","")

    def fa_dong_ji(self,ws):
        k = '发动机号'
        res=self.me.find_key_cell_right(ws,k)
        if len(res)>10:
            return res[:-10]

    def ce_jia_hao(self,ws):
        k = '车架号'
        pat = r'车架号(.*?)$'
        cell=self.me.find_key_cell(ws,k)
        res = re.findall(pat, cell, flags=re.DOTALL)
        if len(res)>0:return res[0][1:]

    def jin_e(self,ws):
        k = '保险费合计'
        cell=self.me.find_key_row(ws,k)
        pat = r'¥(.*?)元'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res == None : return ""
        if len(res)>0:   return self.t.clean(res[0])



    def bei_bao_xian_ren(self, ws):
        k = '投保人被保险人'
        res = self.me.find_key_cell_right_origin(ws,k)
        if res == None: return ""
        l=res.split(" ")
        if len(l)>=1:   return l[1]

    def ce_zu(self,ws):
        k = '行驶证车主'
        res = self.me.find_key_cell_right_origin(ws,k)
        if res == None: return ""
        l=res.split("\n")
        if len(l)>=2:return l[1]

    def tou_bao_ren(self,ws):
        k = '投保人被保险人'
        res = self.me.find_key_cell_right_origin(ws, k)
        if res == None: return ""
        l = res.split(" ")
        if len(l)>=1:   return l[0]
    def te_bie_tiao_kuan(self,ws):
        res = self.me.find_max_cell(ws)
        return res
