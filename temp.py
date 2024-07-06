import pyqrcode
from PIL import Image
from sqlite3 import *
import datetime

con = connect('demo1.db')
cur = con.cursor()

a = "upi://pay?pa=kabilansathiya12345@oksbi&am="
b = ".00&cu=INR"
spt1 = " iSspays "
sp2 = spt1.center(75, "=")
spt="="
sp=spt.center(75,"=")
op =  ["Free Darshan","Special Darshan (50)" ,"VIP Darshan (100)" ,"Vehicle pooja (2 - Wheeler) (100)", " Vehicle Pooja (4 - Wheeler & Above) (200) ", "Show Record","Exit"]
def datalist():
    x = cur.execute('''select * from record''')
    for row in x:
        print(row)
def run1():
    c = Image.open("002.png")
    c.show()
    print(sp2)
    rate = 0
    rate2 = 0
    print(" Service Type \n 1.Free Darshan \n 2.Special Darshan (50) \n 3.VIP Darshan (100) \n 4.Vehicle pooja (2 - Wheeler) (100) \n 5.Vehicle Pooja (4 - Wheeler & Above) (200) \n 6. Show Record\n 7.Exit")
    print(sp)
    choice = int(input("Enter the Service Type :"))
    print("You have entered the option: " + op[int(choice)-1])
    if choice == 1:
        pass
    elif choice == 2:
        rate += 50
    elif choice == 3:
       rate += 100
    elif choice == 4:
        rate += 100
    elif choice == 5:
       rate += 200
    elif choice == 6:
        datalist()
        run1()
    else:
        exit()
    print(sp)
    Name = (input("Enter the Name of the Devotee :"))
    phno = int(input("Enter the Phone Number :"))
    dno = int(input("Enter the No of Devotee :"))
    rate = rate*dno
    if choice == 1:
        rate3 = str(rate)
        print("The Total Amount :"+ rate3)
        cur.execute("insert into record(Service,Name,Phno,Count,Amount,DateTime) values('{}','{}',{},{},{},'{}')".format(op[int(choice)-1],Name,phno,dno,rate3,datetime.datetime.now()))
        con.commit()
        print(row)
        run1()
    else:
        rate2 = str(rate)
        final = a+rate2+b
        print(sp)
        print("The Total Amount :"+ rate2)
        cur.execute("insert into record(Service,Name,Phno,Count,Amount,DateTime) values('{}','{}',{},{},{},'{}')".format(op[int(choice)-1],Name,phno,dno,rate2,datetime.datetime.now()))
        con.commit()
        print(sp)
        qr1 = pyqrcode.create(final)
        qr1.png("001.png",scale=100)
        c = Image.open("001.png")
        c.show()
        f=input("Press Enter to continue")
        print(sp)
        print('''
        
        
        ''')
        run1()
if __name__ == "__main__":
    run1()
