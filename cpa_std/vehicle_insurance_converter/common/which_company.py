from cpa_std.vehicle_insurance_converter.common.tools import Tool
from cpa_std.vehicle_insurance_converter.coms.renbao import RenBao
from cpa_std.vehicle_insurance_converter.coms.pingan import PinAn
from cpa_std.vehicle_insurance_converter.coms.rensou import RenSou
from cpa_std.vehicle_insurance_converter.coms.yangguang import YangGuang
from cpa_std.vehicle_insurance_converter.coms.dadi import Dadi
from cpa_std.vehicle_insurance_converter.coms.taipingyang import TaiPingYang
from cpa_std.vehicle_insurance_converter.coms.yingda import Yingda
from cpa_std.vehicle_insurance_converter.coms.guoren import GuoRen
from cpa_std.vehicle_insurance_converter.coms.zonghua import Zonghua
from cpa_std.vehicle_insurance_converter.coms.zongceng import Zongceng
from cpa_std.vehicle_insurance_converter.coms.yongan import Yongan


class WhichCom:
    def __init__(self):
        self.t = Tool()
    
    # use page1 txt
    def judge(self, ws):
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    res = self.by_page1_txt(v)
                    if res is not None:
                        return res
    
    def by_page1_txt(self, txt):
        txt = txt.replace(" ", "")
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
        if "英大" in txt:
            return "yingda"
        if "国任" in txt:
            return "guoren"
        if "中华联合" in txt:
            return "zonghua"
        if "众诚" in txt:
            return "zongceng"
        return None
    
    # use image yongan
    def by_page1_pic_en(self, images):
        for img in images:
            txt = self.t.read_img_en(img)
            if "YONG AN" in txt:
                return "yongan"
        return None
    
    def by_page1_pic_cn(self, images):
        for img in images:
            txt = self.t.read_img_cn(img)
            if "永安" in txt:
                return "yongan"
        return None
    
    def by_all_means(self, ws, images):
        res = self.judge(ws)
        if res is not None:
            return res
        res = self.by_page1_pic_cn(images)
        if res is not None:
            return res
        res = self.by_page1_pic_en(images)
        if res is not None:
            return res
        return None
    
    def dispatch(self, com, excel):
        if com == "taipingyang":
            return TaiPingYang(excel)
        elif com == "pingan":
            return PinAn(excel)
        elif com == "renbao":
            return RenBao(excel)
        elif com == "rensou":
            return RenSou(excel)
        elif com == "dadi":
            return Dadi(excel)
        elif com == "yangguang":
            return YangGuang(excel)
        elif com == "yingda":
            return Yingda(excel)
        elif com == "guoren":
            return GuoRen(excel)
        elif com == "zonghua":
            return Zonghua(excel)
        elif com == "zongceng":
            return Zongceng(excel)
        elif com == "yongan":
            return Yongan(excel)
        else:
            return None
