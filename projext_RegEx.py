import re

def search_a_dig(x):
#Find all digit characters:
    l = re.findall("\d", x)
    if l ==[] :
        return True
    else :
        return False
def search_word(w,txt):
    return re. search(w,txt)
def just_dig(txt):
    return bool(re.search(r'\d', txt))
def remplacer(txt):
    return re.sub("\s","-",txt)
def numberphone(ph):
     return bool(re.match(r'^\d{2}-\d{3} \d{4}$', ph))
def verifie_format(email):
    return bool(re.match(r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$', email))

