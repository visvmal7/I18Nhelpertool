from simplecrypt import encrypt, decrypt
import datetime
import bz2
import base64

print("\n   Report generator CLI for CodeCruncher tool")
print("_______________________________________________\n")

file=open("Tokens_for_code_crunchers.log","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    # print (k, v)
    print(str(bz2.decompress(base64.b64decode(bytes(k, encoding='utf-8')))).split('+'),v)
file.close();
##################################
print("--------------------------------------------------------------------------------------------------------------------------------------------------")



