from cpa_std.vehicle_insurance_converter.common.tools import Tool
from cpa_std.vehicle_insurance_converter.common.which_company import WhichCom
from cpa_std.vehicle_insurance_converter.common.qr_img import Qr
from cpa_std.vehicle_insurance_converter.common.record import Record
from openpyxl import load_workbook

t = Tool()
w = WhichCom()
record = Record()
qr = Qr()

t.init()
for excel in t.all_files(t.converter):
    wb = load_workbook(excel)
    ws = wb["Table 1"]
    pdf = t.excel2pdf(excel)
    images = t.save_page1_pics(pdf)
    
    com = w.by_all_means(ws, images)
    m = w.dispatch(com, excel)
    
    baodanhao = m.bao_dan_hao(ws)
    jine = m.jin_e(ws)
    begin, end = m.begin_end_date(ws)
    cejia = m.ce_jia_hao(ws)
    fadongji = m.fa_dong_ji(ws)
    cepai = m.ce_pai_hao(ws)

    beibaoxianren = m.bei_bao_xian_ren(ws)
    cezu = m.ce_zu(ws)
    toubaoren = m.tou_bao_ren(ws)
    tebie = m.te_bie_tiao_kuan(ws)

    record.write_row(pdf, cepai, fadongji, cejia, baodanhao, begin, end, jine, toubaoren, cezu, beibaoxianren, tebie)
    t.cpy_rename_2res(pdf, baodanhao)

    qrpath = qr.get_qr(images)
    if qrpath is not None:
        record.write_qr(qrpath, cepai, begin, end, m.name, jine)
record.wb.save(record.res_excel)
record.doc.save(record.res_word)
