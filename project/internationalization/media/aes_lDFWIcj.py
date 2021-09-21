# from os import urandom
# from hashlib import md5
# from Crypto.Cipher import AES

from simplecrypt import encrypt, decrypt
import datetime
import bz2
import base64

# ciphertext = encrypt('password', "plaintext")
print("\n   Token Generator CLI for CodeCruncher tool")
print("_______________________________________________")
# Read the token number from file - Can be encrypted if needed
token_file = open("./token.txt",'r+')
str_token_number = token_file.read(10)
token_file.close()
#str_token_number = "0000000001"
print("TokenNumber " + str_token_number)

# Increment and write back
str_token_number = int(str_token_number) + 1
str_token_number = str(str_token_number)
print ("Incremented token number: " + str_token_number)
token_file = open("./token.txt",'w')
token_file.write(str_token_number)
token_file.close()

# Input further info from user
str_user_name = input("User Name: ")
print(str_user_name)

str_tag_names = input("TAGS (e.g. JavaUI / NDMP): ")
print(str_tag_names)

str_source_path = input("Source Path: ")
print(str_source_path)

str_function_name = input("Function Name: ")
print(str_function_name)

str_function_imp = input("Importance (1-5) (5=Highest): ")
print(str_function_imp)

str_date_now = str(datetime.datetime.now().date())
print(str_date_now)
str_time_now = str(datetime.datetime.now().time())
print(str_time_now)

plaintext = str_token_number + "+" + str_user_name+ "+" +str_tag_names + "+" +str_source_path+ "+" + str_function_name + "+" + str_function_imp + "+" + str_date_now + "+" + str_time_now
print("PlainText: " + plaintext)

#############################################
# # Encrypt the string
# file = open("Sample.log","wb+")
# ciphertext = encrypt('password', plaintext)
# print (ciphertext)
# file.write(ciphertext)
# file.close()
#
# file = open("Sample.log","rb+")
# # Decrypt the string
# ciphertext = file.readlines()
# plaintext = decrypt('password', ciphertext)
# print(plaintext)
#############################################
# Alternate logic with compression and encoding
#############################################
file = open("Sample.log","wb+")
ctext = base64.b64encode(bz2.compress(bytes(plaintext,encoding='utf-8')))
print ("Ctext--------->")
print(ctext)
file.write(ctext)
file.close()
############
file = open("Sample.log","r+")
# # Decompress the string
ctext = file.readline()
plaintext = bz2.decompress(base64.b64decode(bytes(ctext,encoding='utf-8')))
print("Plaintext-------->")
print(plaintext)
###########
# print ("Testing other string...\n----------------\n")
# plaintext = decrypt('password', b"sc\x00\x02\x12\x8b\xff\x89\xc2\xb3\x9eqbf\xc4\x99\xcf\x87\xd7\xac\x9f4\xc7\x8aD\xef\xe4}\xc0Ki` \x8c\xadS\xb6r\xe3N\x07\x1f\xa9e\xebw\x8c\x93\xd7\x8b\xbb\x93\xd9\xfd\xc1\xa9\x01\x8fL\xb4\xec\x9a\xcd\xac^#\xf3[\xda>_p\xa8O\x1d\xb0\x8aL'\x8aHvT\xf4v\xc6\xb33\xa5\x82(\xd2\x90\xff\x8bV\x8f\xfc\xf6\n\xecZ\xf7\xc9\x8d\x03\x04\xd8\xd3%g<\xe1\xcc+m2L`\x84\x07\t\x92\x00\xd4z|\xe6j")
# plaintext = decrypt('password', b"ÿÂ³qbfÄÏ×¬4ÇDïä}ÀKi` ­S¶rãN©eëw×»ÙýÁ©L´ìÍ¬^#ó[Ú>_p¨O°L'HvTôvÆ³3¥(ÒÿVüö")
# print(plaintext)


