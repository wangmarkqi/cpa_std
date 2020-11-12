from cpa_std.vehicle_insurance_converter.common.tools import Tool
import re
from cpa_std.vehicle_insurance_converter.common.methods_txt import MethodsTxt
from cpa_std.vehicle_insurance_converter.common.method_excel import MethodExcel
class Yongan:
    def __init__(self,excel):
        self.excel=excel
        self.t=Tool()
        self.pdf=self.t.excel2pdf(excel)
        self.mt=MethodsTxt()
        self.code="yingda"
        self.name = "英大"
        self.me = MethodExcel()

    def bao_dan_hao(self,ws):
        cell=self.me.find_key_cell(ws,"保险单号")
        pat = r'保险单号(.*?)投保确认码'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if len(res) > 0:
            res1 = self.t.date_format(res[0])
            return res1
        return ""
        
    def begin_end_date(self,ws):
        return "",""
    def ce_pai_hao(self,ws):
        k='号牌号码'
        res=self.me.find_key_cell_right(ws,k)
        return res

    def fa_dong_ji(self,ws):
        k = '发动机号码'
        res=self.me.find_key_cell_right(ws,k)
        return res

    def ce_jia_hao(self,ws):
        k = '车辆识别代码'
        res=self.me.find_key_cell_right(ws,k)
        return res

    def jin_e(self,ws):
        return ""
      



    def bei_bao_xian_ren(self, ws):
        return ""
       

    def ce_zu(self,ws):
        k = '行驶证车主：'
        res = self.me.find_key_cell(ws,k)
        if res == None: return ""
        return res.replace(k,"")

    def tou_bao_ren(self,ws):
        k = '本保单投保人：'
        res = self.me.find_key_cell(ws,k)
        if res == None: return ""
        return res.replace(k,"")

    def te_bie_tiao_kuan(self,ws):
        return ""
        
