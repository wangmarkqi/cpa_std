from cpa_std.vehicle_insurance.common.tools import Tool
from cpa_std.vehicle_insurance.common.which_company import WhichCom
from cpa_std.vehicle_insurance.common.qr_img import Qr
from cpa_std.vehicle_insurance.common.record import  Record
from pdf2image import convert_from_path, convert_from_bytes
import pdfplumber
t=Tool()
w=WhichCom()
q=Qr()
record=Record()
import tempfile
for pdf in t.all_pdfs(t.raw):
    com = w.by_all_means(pdf)
    if com in t.err_list:
        print ("&&&&&&&&&&&&&&&",pdf)
        with pdfplumber.open(pdf) as f:
            for p in f.pages:
                txt = p.extract_text(x_tolerance=3, y_tolerance=3)
                print (txt)
