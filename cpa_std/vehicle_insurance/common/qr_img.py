from cpa_std.vehicle_insurance.common.tools import Tool

import shutil,os


class Qr:
    def __init__(self):
        self.t=Tool()
    def is_qr(self,pdf):
        qr_std = "http://eservice"
        images = self.t.save_page1_pics(pdf)
        for img in images:
            data = self.t.read_qr(img)
            if len(data) == 0:continue
            data2 = data[0]
            if len(data2)==0:continue
            data3=str(data2[0])
            if qr_std in data3:
                return img
        return  None
    def qr_path(self,pdf):
        img=self.is_qr(pdf)
        if img is not None:
            return img
        return None
    