from cpa_std.vehicle_insurance.common.tools import Tool
import re,os,shutil

class MethodsTxt:
    def __init__(self):
        self.t=Tool()
    def find_patter_in_txt(self,pdf,pat):
        txt = self.t.read_page1_txt(pdf)
        txt=self.t.clean(txt)
        res=re.findall(pat, txt,flags=re.DOTALL)
        if len(res)>0:
            res1=self.t.clean(res[0])
            return res1
        return ""
    def find_key_line_in_tab(self,pdf,key):
        tab = self.t.read_page1_table(pdf)
        if tab == None: return ""
        for row in tab:
            row = [i for i in row if i != None]
            s = "".join(row)
            s = self.t.clean(s)
            if key in s:
                return s
    def find_key_pat_in_tab(self,pdf,key,pat):
        tab = self.t.read_page1_table(pdf)
        if tab==None: return ""
        
        for row in tab:
            row=[i for i in row if i!=None]
            s="".join(row)
            s = self.t.clean(s)
            
            if key in s:
                res = re.findall(pat, s, flags=re.DOTALL)
                if len(res) > 0:
                    return res
        return None

