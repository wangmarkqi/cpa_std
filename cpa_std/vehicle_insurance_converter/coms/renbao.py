from cpa_std.vehicle_insurance_converter.common.tools import Tool
import re
from cpa_std.vehicle_insurance_converter.common.methods_txt import MethodsTxt
from cpa_std.vehicle_insurance_converter.common.method_excel import MethodExcel


class RenBao:
    def __init__(self,excel):
        self.excel=excel
        self.t = Tool()
        self.mt = MethodsTxt()
        self.code= "renbao"
        self.name= "中国人保"
        self.me = MethodExcel()

    def bao_dan_hao(self, ws):
        cell = self.me.find_key_cell(ws, "保险单号")
        pat = r'保险单号(.*?)鉴于投保人'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if len(res) > 0:
            return  self.t.date_format(res[0])
        return ""
    
    def begin_end_date(self,ws):
        k="保险期间"
        cell = self.me.find_key_cell(ws, k)
        pat = r'自(.*?)0时起至(.*?)24时止'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res and len(res[0]) == 2:
            begin = res[0][0]
            end = res[0][1]
            return self.t.date_format(begin), self.t.date_format(end)
        return "",""
   

    def ce_pai_hao(self,ws):
        k='号牌号码'
        res=self.me.find_key_cell_right(ws,k)
        return res

    def fa_dong_ji(self, ws):
        k = '发动机号'
        res = self.me.find_key_cell_right(ws, k)
        return res

    def ce_jia_hao(self, ws):
        k = '车架号'
        res = self.me.find_key_cell_right(ws, k)
        return res
    def jin_e(self,ws):
        k = '保险费合计'
        cell=self.me.find_key_cell(ws,k)
        pat = r'¥：(.*?)元'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res == None : return ""
        return self.t.clean(res[0])



    def bei_bao_xian_ren(self, ws):
        k = '被保险人'
        res = self.me.find_key_cell_right(ws,k)
        if res == None: return ""
        return self.t.clean(res)

    def ce_zu(self, ws):
        k = '车主'
        res = self.me.find_key_cell_right(ws, k)
        if res == None: return ""
        return self.t.clean(res)

    def tou_bao_ren(self, ws):
        pat = r'本保单投保人为：(.*?)$'
        k = '本保单投保人为'
        cell = self.me.find_key_cell(ws, k)
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res == None: return ""
        return self.t.clean(res[0])

    def te_bie_tiao_kuan(self, ws):
        return self.me.find_max_cell(ws)
