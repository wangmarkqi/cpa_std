import pdfplumber
import shutil
from changeOffice import Change
import fitz
import pytesseract as pt

import os
from pyzbar import pyzbar
from PIL import Image


# If you don't have tesseract executable in your PATH, include the following:

class Tool:
    def __init__(self):
        self.root = "D://mygit/cpa_std/cpa_std/vehicle_insurance"
        self.data=f"{self.root}/data"
        self.raw = f"{self.data}/pdf"
        self.temp = f"{self.data}/temp"
        self.tess = f"{self.data}/asset/tess"
        self.res = f"{self.data}/res"
        self.res_pdf = f"{self.res}/pdf"
        self.res_err = f"{self.res}/err"
        pt.pytesseract.tesseract_cmd = f"{self.root}/data/asset/tess/tesseract.exe"
        self.err_list = [
            "zonghua",
            "zongceng",
            "guoren",
            "yongan",
            "yingda",
        ]
    
    def init(self):
        if os.path.exists(self.res):
            shutil.rmtree(self.res)
        os.makedirs(self.res_pdf, exist_ok=True)
        os.makedirs(self.res_err, exist_ok=True)

    def all_pdfs(self, root):
        c = Change(root)
        return c.get_allPath()
    
    def path_baodanhao(self, p):
        f = os.path.basename(p)
        return f[:-4]
    
    def read_page1_table(self, f):
        with pdfplumber.open(f) as pdf:
            page = pdf.pages[0]
            tab = page.extract_table()
            return tab
    
    def read_page1_txt(self, f):
        with pdfplumber.open(f) as pdf:
            page = pdf.pages[0]
            txt = page.extract_text(x_tolerance=3, y_tolerance=3)
            # if "太平洋" in f: print (txt)
            return txt
    
    # use page1 txt
    def read_qr(self, qr_path):
        if os.path.exists(qr_path):
            data = pyzbar.decode(Image.open(qr_path))
            return data
    
    def save_page1_pics(self, pdf):
        doc = fitz.open(pdf)
        baodan = self.path_baodanhao(pdf)
        img_path = []
        for i in range(len(doc)):
            for index, img in enumerate(doc.getPageImageList(i)):
                xref = img[0]
                path = f"{self.temp}/{baodan}_{i}_{index}.png"
                # 保存以前先删除
                if os.path.exists(path): os.remove(path)
                pix = fitz.Pixmap(doc, xref)
                if pix.n < 5:  # this is GRAY or RGB
                    pix.writePNG(path)
                else:  # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG(path)
                img_path.append(path)
        return img_path
    
    def read_img_en(self, file):
        img = Image.open(file)
        txt = pt.image_to_string(img)
        return txt
    
    def read_img_cn(self, file):
        img = Image.open(file)
        txt = pt.image_to_string(img, lang="chi_sim")
        return txt
    
    def clean(self, s):
        res = s.replace("\n", "").replace(" ", "").replace("\r","")
        return res
    
    def date_format(self, s):
        res = s.replace("年", "-").replace("月", "-").replace("日", "").replace(":", "").replace("：", "")
        return res
    
    def cpy_origin_2err(self, pdf, com):
        file = os.path.basename(pdf)
        dst = f"{self.res_err}/{file}"
        shutil.copy2(pdf, dst)
    
    def cpy_rename_2res(self, pdf, baodanhao):
        dst = f"{self.res_pdf}/{baodanhao}.pdf"
        shutil.copy2(pdf, dst)
