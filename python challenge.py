import string

text = "map g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alfabet1 = "abcdefghijklmnopqrstuvwxyz"
alfabet2 = "cdefghijklmnopqrstuvwxyzab"
trance = str.maketrans(alfabet1, alfabet2)
print(text.translate(trance))
