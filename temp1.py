import pyqrcode
from PIL import Image
from sqlite3 import *

con = connect('demo1.db')
cur = con.cursor()
type = ['Free','Special','VIP','Vehicle pooja 2 wheeler','Vehicle pooja 2 wheeler']

a = "upi://pay?pa=kabilansathiya12345@oksbi&am="
b = ".00&cu=INR"
spt1 = " iSspays "
sp2 = spt1.center(75, "=")
spt = "="
sp = spt.center(75, "=")
op = ["Free Darshan", "Special Darshan (50)", "VIP Darshan (100)", "Vehicle pooja (2 - Wheeler) (100)",
      " Vehicle Pooja (4 - Wheeler & Above) (200) ", "Exit"]
op = ["Free Darshan", "Special Darshan (50)", "VIP Darshan (100)", "Vehicle pooja (2 - Wheeler) (100)",
      " Vehicle Pooja (4 - Wheeler & Above) (200) ", "Exit"]


def datalist():
    x = cur.execute('select * from record')
    for row in x:
        print(row)


def run1():
    c = Image.open("002.png")
    c.show()
    print(sp2)
    rate = 0
    rate2 = 0
    print(
        "Service Type \n 1.Free Darshan \n 2.Special Darshan (50) \n 3.VIP Darshan (100) \n 4.Vehicle pooja (2 - Wheeler) (100) \n 5.Vehicle Pooja (4 - Wheeler & Above) (200) \n 6.Exit")
    print(sp)
    choice = (input("Enter the Service Type :"))
    if choice ==7:
        datalist()
        run1()
    else:
        run1()
    print("You have entered the option: " + op[int(choice) - 1])
    if choice == '1':
        pass
    elif choice == '2':
        rate += 50
    elif choice == '3':
        rate += 100
    elif choice == '4':
        rate += 100
    elif choice == '5':
        rate += 200
    elif choice == '7':
        print("database list")
        datalist()
    else:
        exit()
    print(sp)
    Name = (input("Enter the Name of the Devotee :"))
    phno = int(input("Enter the Phone Number :"))
    dno = int(input("Enter the No of Devotee :"))
    rate = rate * dno
    if choice == '1':
        rate3 = str(rate)
        print("The Total Amount :" + rate3)
        run1()
    else:
        rate2 = str(rate)
        final = a + rate2 + b
        print(sp)
        print("The Total Amount :" + rate2)
        print(sp)
        qr1 = pyqrcode.create(final)
        qr1.png("001.png", scale=100)
        c = Image.open("001.png")
        c.show()
        f = input("Press Enter to continue")
        print(sp)
        print('''


        ''')

        cur.execute("insert into record values('{}','{}',{},{},{})".format(type[int(choice)-1],Name,phno,dno,rate))
        con.commit()

        run1()



if __name__ == "__main__":
    run1()