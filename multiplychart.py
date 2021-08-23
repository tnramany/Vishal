sourcenum=int(input("enter sourcenumber="))
startnum=int(input("enter startnumber="))
endnum=int(input("enter endnumber="))

for i in range(startnum,endnum+1,1):

    print(sourcenum, " * ", i ," = ", sourcenum * i)
