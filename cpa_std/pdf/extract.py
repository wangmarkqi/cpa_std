from pdfminer.high_level import extract_text,extract_pages
from pdfminer.layout import LTTextContainer, LTChar,LAParams
f="./a.pdf"
def page():
    layout= extract_pages(f)
    for i in layout:
        if isinstance(i, LTTextContainer):
            print(i.get_text())
            for text_line in i:
                for character in text_line:
                    if isinstance(character, LTChar):
                        print(character.fontname)
                        print(character.size)
def text():
    txt=extract_text(f)
    print (txt)
text()