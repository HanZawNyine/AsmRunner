import os

#asm
os.system("sudo mv asm /usr/local/bin/ && sudo chmod +x /usr/local/bin/asm")
os.system("sudo mv asm64 /usr/local/bin/ && sudo chmod +x /usr/local/bin/asm64")

#asm.py
os.system("sudo mv asm.py /usr/local/bin ")
os.system("sudo chmod +x /usr/local/bin/asm.py")

os.system("sudo mv asm64.py /usr/local/bin ")
os.system("sudo chmod +x /usr/local/bin/asm64.py")

print("Assembly Runner added Successfully ! \n  usage : asm or asm64 (File Name).asm \n Developed By h4n24wny!n3")
