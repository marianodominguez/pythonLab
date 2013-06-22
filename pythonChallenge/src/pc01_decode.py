from string import maketrans, translate

message="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url="http://www.pythonchallenge.com/pc/def/map.html";

table = maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
print translate(message, table)
print translate(url,table)



