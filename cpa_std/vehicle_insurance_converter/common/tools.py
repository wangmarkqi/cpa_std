import shutil
from changeOffice import Change
import pdfplumber
import pytesseract as pt
import os
import fitz
from PIL import Image
class Tool:
    def __init__(self):
        self.root = "D://mygit/cpa_std/cpa_std/vehicle_insurance_converter"
        self.data=f"{self.root}/data"
        self.raw = f"{self.data}/pdf"
        self.temp = f"{self.data}/temp"
        self.converter=f"{self.data}/converter"
        self.tess = f"{self.data}/asset/tess"
        self.res = f"{self.data}/res"
        self.res_pdf = f"{self.res}/pdf"
        self.res_err = f"{self.res}/err"
        pt.pytesseract.tesseract_cmd = f"{self.root}/data/asset/tess/tesseract.exe"
    def init(self):
        if os.path.exists(self.res):
            shutil.rmtree(self.res)
        os.makedirs(self.res_pdf, exist_ok=True)
        os.makedirs(self.res_err, exist_ok=True)

    def all_files(self, root):
        c = Change(root)
        return c.get_allPath()
    # use page1 txt
    def read_img_en(self,file):
        img = Image.open(file)
        txt = pt.image_to_string(img)
        return txt

    def read_img_cn(self, file):
        img = Image.open(file)
        txt = pt.image_to_string(img, lang="chi_sim")
        return txt

    def clean(self, s):
        res = s.replace("\n", "").replace(" ", "").replace("\r", "")
        return res

    def date_format(self, s):
        s=self.clean(s)
        res = s.replace("年", "-").replace("月", "-").replace("日", "").replace(":", "").replace("：", "")
        return res

    def cpy_origin_2err(self, pdf, com):
        file = os.path.basename(pdf)
        dst = f"{self.res_err}/{file}"
        shutil.copy2(pdf, dst)

    def cpy_rename_2res(self, pdf, baodanhao):
        dst = f"{self.res_pdf}/{baodanhao}.pdf"
        shutil.copy2(pdf, dst)
    def excel2pdf(self,excel):
        file = os.path.basename(excel)
        file =file.replace(".xlsx",".pdf")
        pdf=f"{self.raw}/{file}"
        return pdf

    def save_page1_pics(self, pdf):
        doc = fitz.open(pdf)
        id = os.path.basename(pdf)
        img_path = []
        for i in range(len(doc)):
            for index, img in enumerate(doc.getPageImageList(i)):
                xref = img[0]
                path = f"{self.temp}/{id}_{i}_{index}.png"
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
    
    
 
