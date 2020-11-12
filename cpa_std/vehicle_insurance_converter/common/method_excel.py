
class MethodExcel:
    def clean(self, s):
        if s is not None:
            res = s.replace("\n", "").replace(" ", "").replace("\r", "")
            return res
        return ""

    def find_max_cell(self, ws):
        res=""
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    v = self.clean(v)
                    if len(v)>len(res):
                        res=v
        return res

    def find_keys_cell(self, ws, ks):
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    v=self.clean(v)
                    score=[]
                    for k in ks:
                        if k in v:
                            score.append(k)
                    if len(score)==len(ks):
                        return self.clean(v)
        
    def find_key_cell(self, ws, k):
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    v=self.clean(v)
                    if k in v:
                        return self.clean(v)
    
    def find_key_cell_left(self, ws, k):
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    if k in v:
                        v = self.clean(v)
                        while c-1>=1:
                            left = ws.cell(row=r, column=c -1).value
                            if left is not None:
                                return self.clean(left)
                            c=c-1
    
    def find_key_cell_right(self, ws, k):
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    v=self.clean(v)
                    if k in v:
                        start=c
                        # 起始位置+20列
                        while c+1<=start+20:
                            right= ws.cell(row=r, column=c +1).value
                            if right is not None:
                                return self.clean(str(right))
                            c=c+1

    def find_key_cell_right_origin(self, ws, k):
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    v = self.clean(v)
                    if k in v:
                        start = c
                        # 起始位置+20列
                        while c + 1 <= start + 20:
                            right = ws.cell(row=r, column=c + 1).value
                            if right is not None:
                                return right
                            c = c + 1
    
    def find_key_cell_down(self, ws, k):
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if isinstance(v, str):
                    v=self.clean(v)
                    if k in v:
                        down = ws.cell(row=r + 1, column=c).value
                        return self.clean(down)
    def find_key_row(self, ws, k):
        for r in range(1, ws.max_row + 1):
            row_str=""
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if v is not None:
                    row_str=row_str+str(v)
            if k in row_str:
                row = self.clean(row_str)
                return self.clean(row)
