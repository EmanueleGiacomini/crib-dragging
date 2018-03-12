
def xorstr(str1, str2):
    return "".join(chr(ord(x)^ord(y)) for x, y in zip(str1, str2))

def cribdrag(cipher, word):
    result = []
    cipher_len = len(cipher)
    word_len = len(word)
    for i in range(cipher_len - word_len+1):
        result.append(xorstr(cipher[i:i+word_len], word).encode("Base64"))
        print result[i]

cyphers = ["4de61dd9dab5e0701f5e664ff522de12bd588051da4d3f62df",
           "3c3303e696139af0280308f5720d5e45efaa03bc6d37d84294",
           "06b25cded0e2fb74045f681bd4378a5bba10901fd6513b2cc0",
           "343c0aa3c6138df02d1f46e63a090d07f3b602bc653bcd5ad1",
           "00fa5890c4f0e062175d2348bd30c25dbb44c951c0503f6fd8",
           "3d3114b28e1390b4611146e53a091c45f8bc01f56f2ac1459f",
           "07be1dc2ccf8fc67131a3355f326c957ba438403cc03362adf",
           "213b14b5ca5290b537155aa1680d0b54eff916bc7e3fcc06d1",
           "15fc5990c1f4e574565b665cf22cce12ac5e8a04d24b7a3dca",
           "3b3a09abc60191a533134da17c070c07eeb803fd207efc4294",
           "54f552dccdb5fd64115d234fbd2ad912eb7d841fc142372adc",
           "3c324684871599b92f0340ee68065c09"]


#r1 = "4de61dd9dab5e0701f5e664ff522de12bd588051da4d3f62df"
#r2 = "3c3303e696139af0280308f5720d5e45efaa03bc6d37d84294"

r1 = "4de61dd9dab5e0701f5e664ff522de12bd588051da4d3f62df".decode("hex")
r2 = "3c3303e696139af0280308f5720d5e45efaa03bc6d37d84294".decode("hex")


cyph = xorstr(r1, r2)
#print "searching for gold nugget"
cribdrag(cyph, "the")





