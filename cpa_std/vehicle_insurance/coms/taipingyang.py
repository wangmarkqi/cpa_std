from cpa_std.vehicle_insurance.common.tools import Tool
from cpa_std.vehicle_insurance.common.methods_txt import MethodsTxt
class TaiPingYang:
    def __init__(self):
        self.t=Tool()
        self.mt = MethodsTxt()
        self.code= "taipingyang"
        self.name= "太平洋"


    def bao_dan_hao(self, pdf):
        pat = r'保险单号(.*?)鉴于投保人'
        res = self.mt.find_patter_in_txt(pdf, pat)
        return res.replace(":", "").replace("：", "")
    def begin_end_date(self, pdf):
        k = "保险期间"
        pat = r'保险期间(.*?)00时起至(.*?)24时止'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res and len(res[0]) == 2:
            begin = res[0][0]
            end = res[0][1]
            return self.t.date_format(begin), self.t.date_format(end)
        return "", ""
    def ce_pai_hao(self, pdf):
        k = '号牌号码'
        pat = r'号牌号码(.*?)厂牌'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None or len(res) == 0: return ""
        s=self.t.clean(res[0]).replace(":","").replace("：","")
        return s

    def fa_dong_ji(self, pdf):
        k = '发动机号'
        pat = r'发动机号(.*?)初次'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None or len(res) == 0: return ""
        s=res[0]
        return s.replace("：","")
    def ce_jia_hao(self, pdf):
        k = '车架号'
        res = self.mt.find_key_line_in_tab(pdf, k)
        l=res.split(k)
        s = l[-1].replace("：", "")
        return s
    def jin_e(self, pdf):
        k = '保险费合计'
        pat = r'¥：(.*?)元'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None: return ""
        return self.t.clean(res[0])

    def bei_bao_xian_ren(self, pdf):
        k = '被保险人'
        pat = r'被保险人(.*?)手机号'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None: return ""
        return self.t.clean(res[0])

    def ce_zu(self, pdf):
        pat = r'车主(.*?)投保人'
        k = '车主'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None: return ""
        return self.t.clean(res[0])

    def tou_bao_ren(self, pdf):
        pat = r'投保人：(.*?)$'
        k = '投保人：'
        res = self.mt.find_key_pat_in_tab(pdf, k, pat)
        if res == None: return ""
        return self.t.clean(res[0])
        

    def te_bie_tiao_kuan(self, pdf):
        pat = r'24时止(.*?)保险合同争议解决方式'
        res = self.mt.find_patter_in_txt(pdf, pat)
        return res

