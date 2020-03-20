ctgry=["Accessories","Apparel","Cosmetics","Electronics","Furniture"]
Ac=["Bags","Earrings","Necklaces","Shoes","Watches"]
Ac2=["Ba","Ea","Ne","Sh","Wa"]
BEa1=BNe1=["Accessorize","Claires","Aeetee","Versace"]
BEa2=BNe2=["Acc","Cl","Ae","Ve"]
BSho1=BBa1=["Nike","Adidas","Louis Vitton","Gucci"]
BSho2=BBa2=["Ni","Ad","Lv","Gu"]
BWa1=["Emporio Armani","Titan","Michael Kors","Guess"]
BWa2=["Ea","Ti","Mk","Gs"]
Ac3=[BBa1,BEa1,BNe1,BSho1,BWa1]
Ac4=[BBa2,BEa2,BNe2,BSho2,BWa2]
Ap=["Dresses","Pants","Shirts","Sarees","Kurtis"]
Ap2=["Dr","Pa","Sh","Sa","Ku"]
BSh1=BPa1=BDr1=["United Colors Benetton","Nuon","AND","Mango"]
BSh2=BPa2=BDr2=["Ucb","Nu","And","Mn"]
BSa1=BKu1=["Sabyasachi","Meena Bazar","Satya Paul","Ritu Kumar"]
BSa2=BKu2=["Ss","Mb","Sp","Rp"]
Ap3=[BSh1,BPa1,BDr1,BSa1,BKu1]
Ap4=[BSh2,BPa2,BDr2,BSa2,BKu2]
Co=["Perfume","Lipsticks","Eye Makeup","Nail Paints","Face Cream"]
Co2=["Pe","Ls","Em","Np","Fc"]
BPe1=["Calvin Klein","Giorgio Armani","Christian Dior","Versace"]
BPe2=["Ck","Ga","Cd","Ve"]
BLi1=BEm1=BFc1=BNp1=["Mac","Lakme","Revlon","L'Oreal"]
BLi2=BEm2=BFc2=BNp2=["Ma","La","Re","Lo"]
Co3=[BPe1,BLi1,BEm1,BNp1,BFc1]
Co4=[BPe2,BLi2,BEm2,BNp2,BFc2]
El=["Air Conditioners","Laptops","Mobile Phones","Refrigerators","Television Sets"]
El2=["Ai","La","Mo","Re","Tv"]
BMo1=BTv1=BRe1=BLa1=BAi1=["Apple","Samsung","Sony","LG"]
BMo2=BTv2=BRe2=BLa2=BAi2=["Ap","Sa","So","Lg"]
El3=[BMo1,BTv1,BRe1,BLa1,BAi1]
El4=[BMo2,BTv2,BRe2,BLa2,BAi2]
Fu=["Beds","Chairs","Sofas","Tables","Wardrobes"]
Fu2=["Be","Ch","So","Ta","Wa"]
BTa1=BCh1=BWa1=BSo1=BBe1=["Century","Pacific Green","Decortie","Stylus"]
BTa2=BCh2=BWa2=BSo2=BBe2=["Ce","Pg","De","St"]
Fu3=[BTa1,BCh1,BWa1,BSo1,BBe1]
Fu4=[BTa2,BCh2,BWa2,BSo2,BBe2]
ctgry2=[Ac,Ap,Co,El,Fu]
ctgry3=[Ac2,Ap2,Co2,El2,Fu2]
ctgry4=["Ac","Ap","Co","El","Fu"]
ctgry5=[Ac3,Ap3,Co3,El3,Fu3]
ctgry6=[Ac4,Ap4,Co4,El4,Fu4]
Col=["Black","White","Silver","Blue"]
Col2=["Bla","Wh","Si","Blu"]
address,phone_number,choicec,choices,choiceb,q="","",0,0,0,0
class order:
    def __init__(self,order_no,phone_number,cat,subcat,brand,color,qty,price,ids):
        self.porder_no=order_no
        self.pphone_number=phone_number
        self.pcat=cat
        self.psubcat=subcat
        self.pbrand=brand
        self.pcolor=color
        self.pqty=qty
        self.pprice=price
        self.pids=ids
    def display(self):
        for i in range (len(ctgry4)):
            if (ctgry4[i]==self.pcat):
                k=i
        l=ctgry3[k]
        m=ctgry2[k]
        for i in range (len(l)):
            if (l[i]==self.psubcat):
                p=i
        o=ctgry5[k]
        t=ctgry6[k]
        q=o[p]
        r=t[p]
        flaghh=0
        for i in range (len(r)):
            if (r[i]==self.pbrand):
                a=i
        for i in range (len(Col2)):
            if (Col2[i]==self.pcolor):
                b=i
                flaghh=1
        if (flaghh==0):
            b="Nil"
            print ("Product ID:"+self.pids+" "+"Order number:"+str(self.porder_no)+" "+ctgry[k]+"/"+m[p]+"/"+q[a]+"/"+b+"/Qty: "+str(self.pqty)+" Price:"+str(self.pprice))
        else:
            print ("Product ID:"+self.pids+" "+"Order number:"+str(self.porder_no)+" "+ctgry[k]+"/"+m[p]+"/"+q[a]+"/"+Col[b]+"/Qty: "+str(self.pqty)+" Price:"+str(self.pprice))
        print ("--------------------------------------------------------------------------------------- ")
def view_order():
    import pickle
    global phone_number
    t_price=0
    t_qty=0
    f=open("orders.dat","rb")
    try:
        while True:
            x=pickle.load(f)
            if (x.pphone_number==phone_number):
                x.display()
                t_price=t_price+(int(x.pprice)*int(x.pqty))
                t_qty=t_qty+int(x.pqty)
    except EOFError:
        pass
    print ()
    print ("Total number of products bought: "+str(t_qty))
    print ("Total expenditure: "+str(t_price))
    print ()
def choiceq():
    global choicec,choices,choiceb
    for i in range(len(ctgry)):
            print ("Press "+str(i+1)+" for "+ctgry[i])
    print ()
    while True:
        choicec=int(input("Enter choice:"))
        if (choicec<0 or choicec>5):
            print ("Please enter the choice correctly.")
            print ()
        else:
            break
    ct=ctgry2[choicec-1]
    r=ctgry5[choicec-1]
    print ()
    for i in range (len(ct)):
        print ("Press "+str(i+1)+" for "+ct[i])
    print ()
    while True:
        choices=int(input("Enter choice:")) 
        if (choices<0 or choices>5):
            print ("Please enter the choice correctly:")
            print ()
        else:
            break
    sct=r[choices-1]
    print ()
    for i in range (len(sct)):
        print ("Press "+str(i+1)+" for "+sct[i])
    print ()
    while True:
          choiceb=int(input("Enter choice:"))
          if (choiceb<0 or choiceb>4):
               print ("Please enter the choice correctly:")
               print ()
          else:
               break
def maximum_order():
    import pickle
    p=[]
    n=[]
    ml=[]
    f=open("orders.dat","rb")
    try:
        while True:
            x=pickle.load(f)
            if x.pids not in p:
                p.append(x.pids)
    except EOFError:
        pass
    f.close()
    for i in p:
        f2=open("orders.dat","rb")
        ctr=0
        try:
            while True:
                x=pickle.load(f2)
                if (x.pids==i):
                    ctr=ctr+int(x.pqty)
        except EOFError:
            pass
        n.append(ctr)
        f2.close()
    m=max(n)
    print ("Product(s) sold maximum,i.e., "+str(m)+" time(s) is/are:")
    for j in range(len(n)):
        if (n[j]==m):
            ml.append(p[j])
    for k in ml:
        f3=open("products.txt","r")
        while True:
            s=f3.readline()
            if not s:
                break
            l=s.split("#")
            if (k==l[6]):
                for i in range (len(ctgry4)):
                    if (ctgry4[i]==l[0]):
                        f=i
                g=ctgry3[f]
                n=ctgry2[f]
                for i in range (len(g)):
                    if (g[i]==l[1]):
                        p=i
                o=ctgry5[f]
                t=ctgry6[f]
                q=o[p]
                r=t[p]
                for i in range (len(r)):
                    if (r[i]==l[2]):
                        a=i
                flagkn=0
                for i in range (len(Col2)):
                    if (Col2[i]==l[3]):
                        b=i
                        flagkn=1
        if (flagkn==0):
            b="Nil"
            print (ctgry[f]+"/"+n[p]+"/"+q[a]+"/"+b)
        else:    
            print (ctgry[f]+"/"+n[p]+"/"+q[a]+"/"+Col[b])
        f3.close()
    print ()
    print ("--------------------------------------------------------------------------------------------")
def display_order():
    import os
    global choicec,choices,choiceb
    choiceq()
    flagnn=0
    ct2=ctgry4[choicec-1]
    l1=ctgry6[choicec-1]
    p1=ctgry3[choicec-1]
    sct2=p1[choices-1]
    l2=l1[choices-1]
    b=l2[choiceb-1]
    f=open("products.txt","r")
    while True:
        s=f.readline()
        if not s:
            break
        l=s.split("#")
        if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
            if (l[3]=="Nil"):
                idss=l[6]
                flagnn=1
                break
    f.close()
    if (flagnn==0):
        for i in range(len(Col)):
            print ("Press "+str(i+1)+" for "+Col[i]+" colour")
        print ()
        choicecol=int(input("Please enter choice:"))
        color=Col2[choicecol-1]
        f=open("products.txt","r")
        while True:
            s=f.readline()
            if not s:
                break
            l=s.split("#")
            if (l[0]==ct2 and l[1]==sct2 and l[2]==b and l[3]==color):
                idss=l[6]
                break
        f.close()
    import pickle
    f2=open("orders.dat","rb")
    try:
        while True:
            x=pickle.load(f2)
            if (x.pids==idss):
                x.display()
    except EOFError:
        pass
    print ("-----------------------------------------------------------------------------------------------------") 
    f2.close()
def modify_price():
    import os
    global choicec,choices,choiceb
    choiceq()
    ct2=ctgry4[choicec-1]
    l1=ctgry6[choicec-1]
    p1=ctgry3[choicec-1]
    sct2=p1[choices-1]
    l2=l1[choices-1]
    b=l2[choiceb-1]
    f1=open("products.txt","r")
    t=open("temp.txt","w")
    while True:
        s=f1.readline()
        if not s:
            break
        l=s.split("#")
        if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
            print ("Existing price is: "+l[4])
            print ()
            break
    f1.close()
    newprice=input("Please enter new price:")
    print ()
    f2=open("products.txt","r")
    while True:
        s=f2.readline()
        if not s:
            break
        l=s.split("#")
        if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
            t.write(l[0]+"#"+l[1]+"#"+l[2]+"#"+l[3]+"#"+newprice+"#"+l[5]+"#"+l[6]+"#\n")
        else:
            t.write(s)
    print ("The price of the product selected has been modified to: "+newprice)
    print ()
    f2.close()
    t.close()
    os.remove("products.txt")
    os.rename("temp.txt","products.txt")
    print ("-----------------------------------------------------------------------------------------------------")
def modify_quantity():
    flago=0
    import os
    global choicec,choices,choiceb
    choiceq()
    ct2=ctgry4[choicec-1]
    l1=ctgry6[choicec-1]
    p1=ctgry3[choicec-1]
    sct2=p1[choices-1]
    l2=l1[choices-1]
    b=l2[choiceb-1]
    f1=open("products.txt","r")
    t=open("temp.txt","w")
    while True:
        s=f1.readline()
        if not s:
            break
        l=s.split("#")
        if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
            if (l[3]=="Nil"):
                break
            else:
                flago=1
                break
    f1.close()
    f2=open("products.txt","r")
    if (flago==0):
        f=open("products.txt","r")
        while True:
            s=f.readline()
            if not s:
                break
            l=s.split("#")
            if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
                print ("Existing quantity is: "+l[5])
        f.close()
        newqty=input("Please enter new quantity:")
        while True:
            s=f2.readline()
            if not s:
                break
            l=s.split("#")
            if l[0]==ct2 and l[1]==sct2 and l[2]==b:
                t.write(l[0]+"#"+l[1]+"#"+l[2]+"#"+l[3]+"#"+l[4]+"#"+newqty+"#"+l[6]+"#\n")
                print ("The quantity of the selected product has been changed to: "+newqty)
            else:
                t.write(s)
        f2.close()
        t.close()
        os.remove("products.txt")
        os.rename("temp.txt","products.txt")
    if (flago==1):
        print ("Press 1 if you want to change the quantity of a particular color of the desired product.")
        print ("Press 2 if you want to change the quantity of all colors of the desired product.")
        choicetr=int(input("Please enter choice:"))
        print ()
        if (choicetr==2):
            f=open("products.txt","r")
            while True:
                s=f.readline()
                if not s:
                    break
                l=s.split("#")
                if l[0]==ct2 and l[1]==sct2 and l[2]==b:
                    for i in range(len(Col2)):
                        if (Col2[i]==l[3]):
                            cols=Col[i]
                    print ("Quantity in stock of color "+cols+" is "+l[5])
            f.close()
            newqty=input("Please enter new quantity:")
            print ("The quantity of the selected product of the color: "+cols+" has been changed to: "+newqty)
            print ()
            while True:
                s=f2.readline()
                if not s:
                    break
                l=s.split("#")
                if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
                    t.write(l[0]+"#"+l[1]+"#"+l[2]+"#"+l[3]+"#"+l[4]+"#"+newqty+"#"+l[6]+"#\n")
                else:
                    t.write(s)
            f2.close()
            t.close()
            os.remove("products.txt")
            os.rename("temp.txt","products.txt")
        if (choicetr==1):
            for i in range(len(Col)):
                print ("Press "+str(i+1)+" for "+Col[i]+" color.")
            choicecol=int(input("Please enter choice:"))
            print ()
            color=Col2[choicecol-1]
            f=open("products.txt","r")
            while True:
                s=f.readline()
                if not s:
                    break
                l=s.split("#")
                if (l[0]==ct2 and l[1]==sct2 and l[2]==b and l[3]==color):
                    print ("Quantity in stock is: "+l[5])
            f.close()
            newqty=input("Please enter new quantity:")
            print ("The quantity of the selected product has been changed to: "+newqty)
            while True:
                s=f2.readline()
                if not s:
                    break
                l=s.split("#")
                if (l[0]==ct2 and l[1]==sct2 and l[2]==b and l[3]==color):
                    t.write(l[0]+"#"+l[1]+"#"+l[2]+"#"+l[3]+"#"+l[4]+"#"+newqty+"#"+l[6]+"#\n")    
                else:
                    t.write(s)
        else:
            print ("Please enter choice correctly:")
            f2.close()
            t.close()
            os.remove("products.txt")
            os.rename("temp.txt","products.txt")
    print ()
    print ("-----------------------------------------------------------------------------------------------------")
def quantity_left():
    flagm=0
    global choicec,choices,choiceb
    choiceq()
    ct2=ctgry4[choicec-1]
    l1=ctgry6[choicec-1]
    p1=ctgry3[choicec-1]
    sct2=p1[choices-1]
    l2=l1[choices-1]
    b=l2[choiceb-1]
    f1=open("products.txt","r")
    while True:
        s=f1.readline()
        if not s:
            break
        l=s.split("#")
        if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
            if (l[3]=="Nil"):
                print ("Quantity left in stock: "+l[5])
                break
            else:
                flagm=1
                break
            print ()
    f1.close()
    if (flagm==1):
        print ("Press 1 if you want to check the quantity for a specific color of the chosen product.")
        print ("Press 2 if you want to check the quantity for all colors of the chosen product.")
        choicekk=int(input("Please enter choice:"))
        print ()
        if (choicekk==2):
            f=open("products.txt","r")
            while True:
                s=f.readline()
                if not s:
                    break
                l=s.split("#")
                if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
                    for i in range(len(Col2)):
                        if (Col2[i]==l[3]):
                            cols=Col[i]
                    print ("Quantity left in stock for "+cols+" is "+l[5])
            f.close()
        elif (choicekk==1):
            for i in range(len(Col)):
                print ("Press "+str(i+1)+" for "+Col[i]+" color.")
            choicecol=int(input("Please enter choice:"))
            print ()
            color=Col2[choicecol-1]
            f=open("products.txt","r")
            while True:
                s=f.readline()
                if not s:
                    break
                l=s.split("#")
                if (l[0]==ct2 and l[1]==sct2 and l[2]==b and l[3]==color):
                    print ("Quantity left in stock is: "+l[5])
        else:
            print ("Please enter choice correctly:")
            f.close()
        print ()
    print ("-----------------------------------------------------------------------------------------------------")
def buy_product():
    import os
    import pickle
    flagl=0
    fr=open("order_nos.txt","r")
    tr=open("temp.txt","w")
    while True:
        s=fr.readline()
        if not s:
            break
        order_no=int(s)+1
        tr.write(str(order_no))
    tr.close()
    fr.close()
    os.remove("order_nos.txt")
    os.rename("temp.txt","order_nos.txt")
    while True:
        flagk=0
        flagx=0
        import pickle
        global choicec,choices,choiceb,phone_number,q,address
        choiceq()
        ct2=ctgry4[choicec-1]
        l1=ctgry6[choicec-1]
        p1=ctgry3[choicec-1]
        sct2=p1[choices-1]
        l2=l1[choices-1]
        b=l2[choiceb-1]
        f1=open("products.txt","r")
        while True:
            s=f1.readline()
            if not s:
                break
            l=s.split("#")
            if l[0]==ct2 and l[1]==sct2 and l[2]==b:
                print ("The product to be purchased is amounting to be: "+l[4])
                print ()
                print ("Press 1 to continue the purchase.")
                print ("Press 2 to discontinue.")
                choice=int(input("Kindly enter your choice:"))
                print ()
                if (choice==2):
                    break
                elif (choice==1):
                    if (l[3]=="Nil"):
                        if (int(l[5])==0):
                            print ("Product unavailable. Kindly choose another product.")
                            print ()
                            break
                        else:
                            while True:
                                q=int(input("Please enter the quantity of the product to be bought:"))
                                if q>int(l[5]):
                                    print ("This product is not available in this quantity.")
                                    print ("Only "+l[5]+" of these products are available at the moment.")
                                    print ("Press 1 to change the quantity of the product.")
                                    print ("Press 2 to change the product itself.")
                                    choicea=int(input("Please enter your choice:"))
                                    if (choicea==2):
                                        flagk=1
                                        f1.close()
                                        break
                                else:
                                    price=l[4]
                                    ids=l[6]
                                    print ()
                                    print ("This product will be delivered to the address: "+address)
                                    print ("Press 1 if you want to continue with the current address.")
                                    print ("Press 2 if you want the item(s) to be delivered at a different address.")
                                    choiceadd=int(input("Please enter choice:"))
                                    if (choiceadd==1):
                                        pass
                                    elif (choiceadd==2):
                                        newadd=input("Enter new address:")
                                        print ("The product(s) will be delivered to the address: "+newadd)
                                    else:
                                        print ("Please enter choice correctly:")
                                    print ("Cost of each product: "+l[4])
                                    print ("Total expenditure: "+str(int(l[4])*q))
                                    print ("Thank you for shopping with us!")
                                    print ("-----------------------------------------------------------------------------")
                                    flagl=1
                                    flagk=1
                                    f1.close()
                                    f3=open("products.txt","r")
                                    t1=open("temp.txt","w")
                                    while True:
                                        s=f3.readline()
                                        if not s:
                                            break
                                        l=s.split("#")
                                        if (l[0]==ct2 and l[1]==sct2 and l[2]==b):
                                            newqty=int(l[5])-q
                                            t1.write(l[0]+"#"+l[1]+"#"+l[2]+"#"+l[3]+"#"+l[4]+"#"+str(newqty)+"#"+l[6]+"#\n")
                                        else:
                                            t1.write(s)
                                    f3.close()
                                    t1.close()
                                    os.remove("products.txt")
                                    os.rename("temp.txt","products.txt")
                                    f4=open("orders.dat","ab")
                                    color="Nil"
                                    obj=order(order_no,phone_number,ct2,sct2,b,color,q,price,ids)
                                    pickle.dump(obj,f4)
                                    f4.close()
                                    break
                    else:
                        flagx=1
                        flagk=1
                        f1.close()
                    
            if (flagk==1):
                break
        if (flagx==1):
            flagr=0
            while True:
                print ()
                for i in range(len(Col)):
                    print ("Press "+str(i+1)+" for "+Col[i]+" color.")
                print ()
                choicecol=int(input("Please enter choice:"))
                color=Col2[choicecol-1]
                f2=open("products.txt","r")
                flagt=0
                while True:
                    s=f2.readline()
                    if not s:
                        break
                    l=s.split("#")
                    if l[0]==ct2 and l[1]==sct2 and l[2]==b and l[3]==color:
                        if (int(l[5])==0):
                            print ("Product unavailable. Kindly choose another product")
                            print ()
                            flagt=1
                            flagr=1
                        else:
                            while True:
                                q=int(input("Please enter the quantity of the desired product to be bought:"))
                                if q>int(l[5]):
                                    print ()
                                    print ("This product is not available in this quantity.")
                                    print ("Only "+l[5]+" of these products are available at the moment.")
                                    print ("Press 1 to change the quantity of the product.")
                                    print ("Press 2 to change the product itself.")
                                    print ("Press 3 to change the color of the product.")
                                    print ()
                                    choicea=int(input("Please enter your choice:"))
                                    if (choicea==2):
                                        flagt=1
                                        flagr=1
                                        break
                                    elif (choicea==3):
                                        flagt=1
                                        f2.close()
                                        break
                                else:
                                    price=l[4]
                                    ids=l[6]
                                    print ()
                                    print ("The product(s) will be delivered at the address: "+address)
                                    print ("Press 1 if you want to continue with the current address.")
                                    print ("Press 2 if you want the item(s) to be delivered at a different address.")
                                    choiceadd=int(input("Please enter choice:"))
                                    if (choiceadd==1):
                                        pass
                                    elif (choiceadd==2):
                                        newadd=input("Enter new address:")
                                        print ("This product will be delivered to the address:"+newadd)
                                    else:
                                        print ("Please enter choice correctly:")
                                    print ("Cost Of Each product is "+l[4])
                                    print ("Total expenditure: "+str(int(l[4])*q))
                                    print ("Thank you for shopping with us!")
                                    print ("-----------------------------------------------------------------------------")
                                    print ()
                                    flagr=1
                                    flagl=1
                                    flagt=1
                                    f2.close()
                                    f3=open("products.txt","r")
                                    t1=open("temp.txt","w")
                                    while True:
                                        s=f3.readline()
                                        if not s:
                                            break
                                        l=s.split("#")
                                        if (l[0]==ct2 and l[1]==sct2 and l[2]==b and l[3]==color):
                                            newqty=int(l[5])-q
                                            t1.write(l[0]+"#"+l[1]+"#"+l[2]+"#"+l[3]+"#"+l[4]+"#"+str(newqty)+"#"+l[6]+"#\n")
                                        else:
                                            t1.write(s)
                                    f3.close()
                                    t1.close()
                                    os.remove("products.txt")
                                    os.rename("temp.txt","products.txt")
                                    f4=open("orders.dat","ab")
                                    obj=order(order_no,phone_number,ct2,sct2,b,color,q,price,ids)
                                    pickle.dump(obj,f4)
                                    f4.close()
                                    break
                    if (flagt==1):
                        break
                if (flagr==1):
                    break
        if (flagl==1):
            break
def change_details():
    global phone_number
    while True:
        print ("Press 1 if you would like to change your address.")
        print ("Press 2 if you would like to change your password.")
        choicek=int(input("Kindly enter your choice:"))
        if (choicek in [1,2]):
            break
        else:
            print ()
            print ("Please enter choice correctly:")
    f=open("members.txt","r")
    t=open("temp.txt","w")
    import os
    while True:
        s=f.readline()
        if not s:
            break
        l=s.split("#")
        if (l[1]==phone_number):
            if (choicek==1):
                print ()
                newaddress=input("Please enter your new address:")
                t.write(l[0]+"#"+l[1]+"#"+newaddress+"#"+l[3]+"#"+l[4]+"#"+l[5]+"#\n")
                print ("Your address has been changed to: "+newaddress)
                print ()
            elif (choicek==2):
                while True:
                    print ()
                    newpassword=input("Enter new password:")
                    if (newpassword.isalnum()==False):
                        print ("Password should contain only alphabets and digits. No special characters are allowed.")
                    if (len(newpassword)<7):
                        print ("Password should have atleast seven characters.")
                    else:
                        break
                t.write(l[0]+"#"+l[1]+"#"+l[2]+"#"+newpassword+"#"+l[4]+"#"+l[5]+"#"+"#\n")
                print ("Your password has been changed to: "+newpassword)
                print ()
        else:
            t.write(s)
    f.close()
    t.close()
    os.remove("members.txt")
    os.rename("temp.txt","members.txt")
    print ("-----------------------------------------------------------------------------------------------------")
def customer2():
    while True:
        print ("We would like to know the reason for your visit.")
        print ("Press 1 if you would like to buy new products.")
        print ("Press 2 if you want to change customer details.")
        print ("Press 3 if you want to view all the products you've placed an order for.")
        print ("Press 4 to exit.")
        print ()
        choice3=int(input("Please enter your choice:"))
        print ("--------------------------------------------------------------------------------------------------")
        if (choice3==1):
            print ()
            buy_product()
        elif (choice3==2):
            print ()
            change_details()
        elif (choice3==3):
            print ()
            view_order()
        elif (choice3==4):
            break
        else:
            print ("Please enter choice correctly:")
def add_member():
    global phone_number,address
    while True:
        phone_number=input("Please enter your phone number:")
        if (phone_number.isdigit()==False):
            print ("Phone number should contain only digits.")
        elif (len(phone_number)!=10):
            print ("Phone number should contain only 10 digits.")
        else:
            break
    f=open("members.txt","r")
    flag=0
    while True:
        s=f.readline()
        if not s:
            break
        r=s.split("#")
        if (r[1]==phone_number):
            print ("An account with this phone number already exists. Please check the number or enter a new one.")
            flag=1
            break
    f.close()
    if (flag==0):
        name=input("Enter full name:")
        address=input("Enter your address:")
        print ()
        print ("Password should contain only alphabets and digits. No special characters are allowed.")
        print ("Password should contain atleast seven characters.")
        while True:
            password=input("Enter Password:")
            if (password.isalnum()==False):
                print ("No special characters are allowed")
            if (len(password)<7):
                print ("Password should have atleast seven characters.")
            else:
                break
        print ()
        print ("--------------------------------------------------------------------------------------------------")
        print ("We'd like you to choose a hint question for you to answer if you ever forget your password in the future. Here are your options:")
        ctrh=1
        print ()
        fh=open("hintquestions.txt","r")
        while True:
            s=fh.readline()
            if not s:
                break
            print ("Press "+str(ctrh)+" for "+s[:-1])
            ctrh=ctrh+1
        choicehq=int(input("Please enter choice:"))
        answer=input("Please enter answer:")
        fh.close()
        f=open("members.txt","a")
        f.write(name+"#"+phone_number+"#"+address+"#"+password+"#"+str(choicehq)+"#"+answer+"#\n")
        print ()
        print ("--------------------------------------------------------------------------------------------------")
        print ("Welcome to Olivander's, "+name)
        print ()
        f.close()
        customer2()
def hint_question():
    global phone_number
    flag=0
    f=open("members.txt","r")
    while True:
        s=f.readline()
        if not s:
            break
        r=s.split("#")
        if (r[1]==phone_number):
            n=int(r[4])
            break
    f.close()
    fh=open("hintquestions.txt","r")
    ctrhq=1
    while True:
        s=fh.readline()
        if not s:
            break
        if ctrhq==n:
            print (s)
            break
        else:
            ctrhq=ctrhq+1
    f=open("members.txt","r")
    while True:
        s=f.readline()
        if not s:
            break
        r=s.split("#")
        if (r[1]==phone_number):
            for i in range(5):
                answer=input("Enter your answer:")
                if (r[5].upper()==answer.upper()):
                    print ("Welcome back, "+r[0])
                    print ("For future reference, your password is: "+r[3])
                    name=r[0]
                    address=r[2]
                    flag=1
                    break
                else:
                    print ("The answer entered in incorrect!")
                    if ((4-i)!=0):
                        print ("WARNING: "+str(4-i)+" attempts remaining.")
                    elif (4-i)==0:
                        print ("Acess denied.")
                        print ("Please try again later.")
                        print ("--------------------------------------------------------------------------------------")
    f.close()  
    if (flag==1):
        print ("--------------------------------------------------------------------------------------------------")
        customer2()
def check_member():
    global phone_number,address
    while True:
        phone_number=input("Please enter your phone number:")
        if (phone_number.isdigit()==False):
            print ("Phone number should contain only digits.")
        elif (len(phone_number)!=10):
            print ("Phone number should contain 10 digits.")
        else:
            break
    f=open("members.txt","r")
    flag=0
    flagmm=0
    flagmn=0
    while True:
        s=f.readline()
        if not s:
            break
        r=s.split("#")
        if (r[1]==phone_number):
            for i in range(5):
                password2=input("Confirm password:")
                if (r[3]==password2):
                    print ()
                    print ("-----------------------------------------------------------------------------------------")
                    print ()
                    print ("Welcome back to Olivander's, "+r[0])
                    name=r[0]
                    address=r[2]
                    flag=1
                    flagmn=1
                    break
                else:
                    print ("The password entered is incorrect!")
                    if ((4-i)!=0):
                        print ("WARNING: "+str(4-i)+" attempts remaining.")
                    if ((4-i)==0):
                        print ()
                        print ("Press 1 if you have forgotten your password.")
                        print ("Press 2 if you want to sign in/sign up with a different number.")
                        choicepq=int(input("Please enter choice:"))
                        if (choicepq==1):
                            hint_question()
                            flag=1
                            break
                        elif (choicepq==2):
                            flagmm=1
                            flag=1
                            break
                        else:
                            print ("Please enter choice correctly:")
                                
    f.close()
    if (flagmm==1):
        print ()
        customer()
    if (flagmn==1):
        print ()
        customer2()
    if (flag==0):
        print ("This phone number does not exist.")
        while True:
            print ("Press 1 if you want to enter another number.")
            print ("Press 2 if you want to sign up.")
            choice2=int(input("Enter your choice:"))
            if (choice2==2):
                print ()
                print ("--------------------------------------------------------------------------------------------")
                add_member()
                break
            if (choice2==1):
                check_member()
                break
            elif choice not in [1,2]:
                print ("Please enter choice correctly.")
def customer():
    while True:
        print ("Press 1 if you're already a member.")
        print ("Press 2 if you want to sign up.")
        choice1=int(input("Please enter your choice:"))
        if choice1 not in [1,2]:
            print ("Please enter choice correctly:")
        else:
            break
    if (choice1==1):
        print ()
        check_member()
    elif (choice1==2):
        print ()
        add_member()
def administrator():
    while True:
        print ("Press 1 to modify the price for any product.")
        print ("Press 2 to modify the quantity for any product.")
        print ("Press 3 to find the quantity left in stock for any product.")
        print ("Press 4 to find the product with maximum number of orders.")
        print ("Press 5 to display the list of all orders placed for any product.")
        print ("Press 6 to exit.")
        print ()
        choiceA=int(input("Enter choice:"))
        if (choiceA==1):
            print ()
            modify_price()
        elif (choiceA==2):
            print ()
            modify_quantity()
        elif (choiceA==3):
            print ()
            quantity_left()
        elif (choiceA==4):
            print ()
            maximum_order()
        elif (choiceA==5):
            print ()
            display_order()
        elif (choiceA==6):
            break
        else:
            print ("Please enter choice correctly:")
def password():
    for i in range(5):
        code=input("Enter the access code:")
        if (code=="admn_11"):
            print ("Access granted!")
            print ()
            administrator()
            break
        else:
            print ("Access denied.",4-i," attempts remaining.")
            if (4-i==0):
                print ("System locked. Please try again later.")
    print ("-----------------------------------------------------------------------------------------------------")
print ("\t\t\t\t\tWelcome to Olivander's!")
print ("\t\t\t\t\t An alley for all.")
while True:
     print ("Press 1 if you're the Administrator.")
     print ("Press 2 if you're a Customer.")
     choice0=int(input("Please provide your choice:"))
     print ()
     if (choice0==1):
          password()
          print ()
          break
     elif (choice0==2):
          customer()
          print ()
          break
     else:
          print ("Please enter choice correctly:")
