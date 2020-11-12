from pywinauto import Application
import pyautogui as auto
import time
import os
class Converter:
    def __init__(self):
        self.exe="C://Program Files (x86)/Auntec/嗨格式PDF转换器/HiPdfConvert.exe"
        self.app = Application(backend="uia")
        # self.app.start(self.exe)
        self.app.connect(path=self.exe)
        
        # time.sleep(8)
    def windows(self):
        s1=self.app.window(best_match='嗨格式PDF转换器1.0')
        s2=s1["pdf转文件"]
        s2.print_control_identifiers()
        s3=s2.child_window(title="文件名称", control_type="Text")
        s3.type_keys("afda")
        
        s4=s2.child_window(title="开始转换", control_type="Text")
        s4.type_keys("{ENTER}")


    def open(self):
        auto.hotkey("alt","tab")
        # auto.moveTo(x=980, y=990)
        # auto.click()
        auto.moveTo(x=580, y=251)
        auto.click()
        f="D://mygit/cpa_std/cpa_std/vehicle_insurance/data/pdf/eacd2c918f264f568096f4cea0e698f0.pdf"
        f=os.path.abspath(f)
        auto.typewrite(message=f)
        auto.press("enter")
        auto.moveTo(x=1400, y=911)
        auto.click()
        auto.moveTo(x=700, y=611)
        auto.click()
        # auto.hotkey("alt","tab")


if __name__ == '__main__':
    c=Converter()
    c.open()
    