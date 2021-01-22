import os
import sys

aa = sys.argv[1]
print("\033[1;34;40m Input : "+ aa+"\n")

li = list(aa.split("."))
#print(*li)

FCom = "nasm -f elf64 "+li[0]+".asm -o "+li[0]+".o"
os.system(FCom)
#print(FCom)

SCom = "ld "+li[0]+".o -o "+li[0]
os.system(SCom)

TCom = "./"+li[0]  
os.system(TCom)
