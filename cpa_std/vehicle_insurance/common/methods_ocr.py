import re
def date(self, pdf):
    tab = self.t.read_page1_table(pdf)
    for row in tab:
        row = [i for i in row if i != None]
        s = "".join(row)
        if "保险期间" in s:
            pat = r'自(.*?)00:00时起至(.*?)24:00时止'
            res = re.findall(pat, s, flags=re.DOTALL)
            if len(res) > 0 and len(res[0]) == 2:
                begin = self.t.clean(res[0][0])
                end = self.t.clean(res[0][1])
                return self.t.date_format(begin), self.t.date_format(end)
    return "", ""