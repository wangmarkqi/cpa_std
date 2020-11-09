from cpa_std.vehicle_insurance.common.tools import Tool
from cpa_std.vehicle_insurance.coms.renbao import RenBao
from cpa_std.vehicle_insurance.coms.pingan import PinAn
from cpa_std.vehicle_insurance.coms.rensou import RenSou
from cpa_std.vehicle_insurance.coms.yangguang import YangGuang
from cpa_std.vehicle_insurance.coms.dadi import Dadi
from cpa_std.vehicle_insurance.coms.taipingyang import TaiPingYang
class WhichCom:
    def __init__(self):
        self.t=Tool()
        self.qr_std = "http://eservice.citic"
    
# use page1 txt
    def by_page1_txt(self,txt):
        
        if 'cpic.com' in txt:
            return "taipingyang"
        if '中国平安财产保险股份有限公司' in txt:
            return "pingan"
        # 不可以
        if "query.cic.cn" in txt:
            return "zonghua"
        if "www.picc.com.cn" in txt:
            return "renbao"
        if "中国人寿财产保险股份有限公司" in txt:
            return "rensou"
        if "众诚微信" in txt:
            return "zongceng"
        # 不可以
        if "guorenpcic.com" in txt:
            return "guoren"
        if "95590.cn" in txt:
            return "dadi"
        if "阳光财产保险" in txt:
            return "yangguang"
        return ""
#use image yongan
    def by_page1_pic_en(self,png):
        txt = self.t.read_img_en(png)
        if "YONG AN" in txt:
            return "yongan"
        return ""

    def by_page1_pic_chi(self,png):
        txt = self.t.read_img_cn(png)
        if "大" in txt and "和财产保险股份有限公司" in txt:
            return "yingda"
        return ""
    def by_all_means(self,f):
        txt = self.t.read_page1_txt(f)
        res = self.by_page1_txt(txt)
        if res!="":return res
        images = self.t.save_page1_pics(f)
        for img in images:
            res = self.by_page1_pic_en(img)
            if res!="":return res
            res = self.by_page1_pic_chi(img)
            if res!="":return res
        return ""
    
    def dispatch(self,com):
        if com=="taipingyang":
            return TaiPingYang()
        elif com=="pingan":
            return PinAn()
        elif com=="renbao":
            return RenBao()
        elif com=="rensou":
            return RenSou()
        elif com=="dadi":
            return Dadi()
        elif com=="yangguang":
            return YangGuang()
        else:
            return None

