from cpa_std.vehicle_insurance.common.tools import Tool
from cpa_std.vehicle_insurance.common.which_company import WhichCom
from cpa_std.vehicle_insurance.common.qr_img import Qr
from cpa_std.vehicle_insurance.common.record import  Record

t=Tool()
w=WhichCom()
q=Qr()
record=Record()



t.init()
for pdf in t.all_pdfs(t.raw):
    com=w.by_all_means(pdf)
    if com in t.err_list:
        t.cpy_origin_2err(pdf,com)
        continue
    m=w.dispatch(com)
    jine = m.jin_e(pdf)
    
    baodanhao=m.bao_dan_hao(pdf)
    begin,end=m.begin_end_date(pdf)
    cejia=m.ce_jia_hao(pdf)
    fadongji=m.fa_dong_ji(pdf)
    cepai=m.ce_pai_hao(pdf)
    
    beibaoxianren=m.bei_bao_xian_ren(pdf)
    cezu=m.ce_zu(pdf)
    toubaoren=m.tou_bao_ren(pdf)
    tebie=m.te_bie_tiao_kuan(pdf)
    record.write_row( pdf,cepai, fadongji, cejia, baodanhao, begin, end, jine, toubaoren, cezu, beibaoxianren, tebie)
    t.cpy_rename_2res(pdf,baodanhao)
    qrpath=q.qr_path(pdf)
    if qrpath!=None:
        record.write_qr(qrpath,cepai,begin,end,m.name,jine)
record.wb.save(record.res_excel)
record.doc.save(record.res_word)
    


