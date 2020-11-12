from cpa_std.vehicle_insurance_converter.common.tools import Tool
import re
from cpa_std.vehicle_insurance_converter.common.methods_txt import MethodsTxt
from cpa_std.vehicle_insurance_converter.common.method_excel import MethodExcel
# ：1、保单号；2、车牌号；3、保险起期；4、保险止期；5、承保公司；；实收保费
class PinAn:
    def __init__(self,excel):
        self.excel=excel
        self.t=Tool()
        self.mt=MethodsTxt()
        self.code="pingan"
        self.name = "平安保险"
        self.me=MethodExcel()

    def bao_dan_hao(self,ws):
        cell=self.me.find_key_cell(ws,"保险单号")
        pat = r'保险单号:(.*?)$'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if len(res) > 0:
            res1 = self.t.clean(res[0])
            return res1
        return ""
    def begin_end_date(self,ws):
        k=["00:00时", "24:00时止"]
        cell=self.me.find_keys_cell(ws,k)
        pat = r'自(.*?)00:00时起至(.*?)24:00时止'
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res and len(res[0]) == 2:
            begin = res[0][0]
            end = res[0][1]
            return self.t.date_format(begin), self.t.date_format(end)
        return "", ""
    def ce_pai_hao(self,ws):
        k='发动机号码'
        res=self.me.find_key_cell_left(ws,k)
        return res
    def fa_dong_ji(self,ws):
        k='发动机号码'
        res=self.me.find_key_cell_right(ws,k)
        return res

    def ce_jia_hao(self,ws):
        k = '车架号'
        res = self.me.find_key_cell_right(ws, k)
        return res
    def jin_e(self,ws):
        k = '保险费合计'
        cell= self.me.find_key_cell_right(ws, k)
        pat = r'RMB(.*?)元'
        res = re.findall(pat,cell, flags=re.DOTALL)
        if res == None : return ""
        return self.t.clean(res[0])

    def bei_bao_xian_ren(self, ws):
        k = '统一社会信用代码'
        pat = r'^名称:(.*?)证件'
        cell= self.me.find_key_cell(ws, k)
        res = re.findall(pat, cell, flags=re.DOTALL)
        if res == None: return ""
        s=res[0].replace("有限公","有限公司")
        return self.t.clean(s)
    def ce_zu(self,ws):
        k= '行驶证车主'
        cell= self.me.find_key_cell_right(ws, k)
        return  cell
    def tou_bao_ren(self,ws):
        return ""
       
    def te_bie_tiao_kuan(self, ws):
        k='无其它特别约定'
        res = self.me.find_key_cell(ws,k)
        return res


        

    