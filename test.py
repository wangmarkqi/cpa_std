import setuptools
print (setuptools.find_packages())
from cpa_std.ledger.account_name import AccountName
def test_simidic():
    s = SimiDic(0.9)
    s["yy"] = 9
    s["yauuufa"] = 8
    s["x"] = 7
    print(s["yauu ufa"])
def std():
    s=AccountName()
    print (s.all)
std()