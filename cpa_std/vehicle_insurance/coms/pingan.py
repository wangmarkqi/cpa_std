from cpa_std.vehicle_insurance.common.tools import Tool
import re
from cpa_std.vehicle_insurance.common.methods_txt import MethodsTxt
# ：1、保单号；2、车牌号；3、保险起期；4、保险止期；5、承保公司；；实收保费
class PinAn:
    def __init__(self):
        self.t=Tool()
        self.mt=MethodsTxt()
        self.code="pingan"
        self.name = "平安保险"

    def bao_dan_hao(self,pdf):
        pat = r'保险单号(.*?)鉴于投保人'
        res = self.mt.find_patter_in_txt(pdf, pat)
        return res.replace(":", "").replace("：", "")
    def begin_end_date(self,pdf):
        k="保险期间"
        pat = r'自(.*?)00:00时起至(.*?)24:00时止'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res and len(res[0]) == 2:
            begin = res[0][0]
            end = res[0][1]
            return self.t.date_format(begin), self.t.date_format(end)
        return "", ""
    def ce_pai_hao(self,pdf):
        k='号牌号码'
        pat = r'号牌号码(.*?)发动机'
        res=self.mt.find_key_pat_in_tab(pdf,k,pat)
        if res==None or len(res)==0:return ""
        return res[0]
    def fa_dong_ji(self,pdf):
        k='发动机号码'
        pat = r'发动机号码(.*?)车架号'
        res=self.mt.find_key_pat_in_tab(pdf,k,pat)
        if res==None or len(res)==0:return ""
        return res[0]

    def ce_jia_hao(self, pdf):
        k = '车架号'
        res = self.mt.find_key_line_in_tab(pdf, k)
        l=res.split(k)
        return l[-1]
    def jin_e(self,pdf):
        k = '保险费合计'
        pat = r'RMB(.*?)元'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None : return ""
        return self.t.clean(res[0])

    def bei_bao_xian_ren(self, pdf):
        k = '被保险人'
        pat = r'^(.*?)正式名称'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None: return ""
        s=res[0].replace("有限公","有限公司")
        return self.t.clean(s)
    def ce_zu(self, pdf):
        pat = r'行驶证车主:(.*?)保险单号'
        res = self.mt.find_patter_in_txt(pdf, pat)
        if res == None: return ""
        return self.t.clean(res)
    def tou_bao_ren(self, pdf):
        return ""
       
    def te_bie_tiao_kuan(self, pdf):
        pat = r'保险费合计(.*?)收费确认时间'
        res = self.mt.find_patter_in_txt(pdf, pat)
        return res


        

    