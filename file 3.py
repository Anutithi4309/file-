file=open('anu.txt','r')
Counter=0
Content=file.read()
CoList=Content.split("\n")
for i in CoList:
    if i:
        Counter+=1
print("this is the number of lines in this files")
print(Counter)
             
