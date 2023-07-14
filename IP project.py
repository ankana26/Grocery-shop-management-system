import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as mc
import datetime 
mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
if mycon.is_connected()==False:
    print("Connection not succesful")
cursor=mycon.cursor()
print()
print("Welcome To RADHE GROCERY")
print()
aa=input("Please enter your user ID- (Your Name in Capital letters)")
print()
bb=input("Please enter your password- (Your Name in Small letters)")
qrya="select * from login where userid='%s' and pass='%s'"%(aa,bb)
cursor.execute(qrya)
daata=cursor.fetchall()
countt=cursor.rowcount
print()

#18+2

import pymysql
from sqlalchemy import create_engine
engine=create_engine('mysql+pymysql://root:1234@localhost/grocery')
conn=engine.connect()


def item2():
    if a==2:
        df3=pd.read_sql("Select * from item2;",mycon)
        print(df3)
def item3():
    if a==3:
        df4=pd.read_sql("Select * from item3;",mycon)
        print(df4)
def item4():
    df5=pd.read_sql("Select * from item4;",mycon)
    print(df5)
    
     #33
def item5():
    df6=pd.read_sql("Select * from item5;",mycon)
    print(df6)

def item6():
    df7=pd.read_sql("Select * from item6;",mycon)
    print(df7)

def conti():
    print()
    b=(int(input("Enter SrNo for the required product")))
    print()
    c1=(int(input("Enter Quantity")))
    print()


    import mysql.connector as mc
    mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
    
    if mycon.is_connected()=='False':
        print("Error in connectivity")
    cursor=mycon.cursor()
    
    cursor.execute("Select price from item%s where SrNo=%s"%(a,b))
    data11=cursor.fetchall()
    
    for x in data11:
        
        res1 = int(''.join(map(str, x)))  #convert tuple to integer
        price1=res1*c1

        L3.append(res1)  #unit price
        
        L2.append(c1)    #quantity
        L1.append(price1)  #amount
        
    print("Your Amount is",price1)
    cursor.execute("select products from item%s where SrNo=%s"%(a,b))
    data11aa=cursor.fetchall()
    for x in data11aa:
        L4.append(x) #itemname (list of tuples)
    print()

    joker=input("Do you want anything else from the given list? (type 'Yes' for affirmation and 'No' for negation)")
    if joker=="Yes":
        conti()

       

def bill():
    
    import mysql.connector as mc
    import pandas as pd
    import datetime 
    mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
    if mycon.is_connected()==False:
        print("Connection Unsuccesful")
    cursor=mycon.cursor()
    import pymysql
    from sqlalchemy import create_engine
    engine=create_engine('mysql+pymysql://root:1234@localhost/grocery')
    conn=engine.connect()
    print("Your list is:")
    df=pd.DataFrame({"Itemname":L4,"Unit Price(Rs.)":L3,"Quantity":L2,"Amount":L1})

    index=df.index #gives range
    mall=len(index)
    My_list = [*range(1,mall+1,1)] #range to list of integers
    df.insert(0, "SrNo", My_list , True) 

    print(df)
    df.to_sql('bill',conn, index=True, if_exists='replace')
    import pymysql
    from sqlalchemy import create_engine
    engine=create_engine('mysql+pymysql://root:1234@localhost/grocery')
    conn=engine.connect()
    print()
    Delete=input("Do you want to remove any product from the list? (type 'Yes' for affirmation and 'No' for negation)")
    if Delete=='Yes':
        print()
        #100
        
        see=int(input('Enter the SrNo of the product you want to remove'))
        seri="delete from bill where SrNo=%s;"%(see)
        cursor.execute(seri)

        df=pd.read_sql("Select * from bill;",mycon)

        rock=df.index    #THIS IS USED TO CALCULATE AVERAGE
        hall=len(rock)   #length of index
        print()
        print("Your updated list is:")
        print()
        
        print(df)
        

        
        
        
    else:
        print("Okay.") 
    

    while Delete=='Yes':
        print()

        import mysql.connector as mc
        mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
        if mycon.is_connected()==False:
            print("Connection Unsuccesful")
        cursor=mycon.cursor()
        cat= "select Amount from bill where SrNo=%s;"%(see)
        cursor.execute(cat)
        daal=cursor.fetchall()
        count=cursor.rowcount
        #print(count)
            
        for x in daal:
                
            res1 = int(''.join(map(str, x))) #tuple to int
            cut=res1*count
            s=sum(L1)-cut
            tax=s*0.05     #5% tax
            net=s+tax    
         
            print()
          
        print('Thank you for being patient. Your bill is being processed.')    
    
        tax=s*0.05     #5% tax
        net=s+tax
        now=datetime.datetime.now()
        dtm=str(now)    #Current date and time converted to string
        print()
        print()
        print("Date:{0:>55s}".format(dtm))
        print("-"*60)
        
        print(df)
        print()
        print("Tax(5%):{0:>43.2f}".format(tax))
        print("-"*60)
        print("Amount Payable(Rs.):{0:>32.2f}".format(net))
            
        print()

         #148
       
        average=(s/hall)
        print("Your average amount is(Rs.):",average)

        print()
        input1=input("Do you want to tally your expenses? (type 'Yes' for affirmation and 'No' for negation)")
        if input1=="Yes":
        #
            import mysql.connector as mc
            mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
            if mycon.is_connected()==False:
                print("Connection Unsuccesful")
            cursor=mycon.cursor()
        
            bat= "select Itemname from bill where SrNo!=%s;"%(see)
            cursor.execute(bat)
            day=cursor.fetchall()    
            outer = [item for t in day for item in t]   #Convert tuple to list

            import mysql.connector as mc
            myc=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
            if mycon.is_connected()==False:
                print("Connection Unsuccesful")
            cure=myc.cursor()
        
            sat= "select amount from bill where SrNo!=%s;"%(see)
            cure.execute(sat)
         
            dent=cure.fetchall()    
            out = [item for t in dent for item in t]    #Convert tuple to list
 
            import matplotlib.pyplot as plt
            import pandas as pd
            plt.xlabel('Items bought by you')
            plt.ylabel('Total Amount of each item')
            plt.bar(outer,out)
            plt.show()
            
            print()
            print("Thank you. BE SAFE and WEAR MASK.")
                                                                        
                #
                
        else:
            print()
            print("Thank you. BE SAFE and WEAR MASK.")
            
        
        import pymysql
        from sqlalchemy import create_engine
        engine=create_engine('mysql+pymysql://root:1234@localhost/grocery')
        conn=engine.connect()
        break
        
       
###############
    while Delete=='No':
        print()
        print('Thank you for being patient. Your bill is being processed.')    
        s=sum(L1)
        tax=s*0.05     #5% tax
        net=s+tax
        now=datetime.datetime.now()
        dtm=str(now)
        print()  #200
        print()
        print("Date:{0:>55s}".format(dtm))
        print("-"*60)
        
        print(df)
        print()
        print("Tax(5%):{0:>43.2f}".format(tax))
        print("-"*60)
        print("Amount Payable(Rs.):{0:>32.2f}".format(net))
        
        print()
        avgc=df.count()
        avg=avgc[0]
        av=0
        for x in L1: #L1 is amount
            av=av+x
        average=av/avg
        print("Your average amount is(Rs.):",average)

        
        print()
        input1=input("Do you want to tally your expenses? (type 'Yes' for affirmation and 'No' for negation)")
        ##
        if input1=="Yes":
        #
            import mysql.connector as mc
            mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
            if mycon.is_connected()==False:
                print("Connection Unsuccesful")
            cursor=mycon.cursor()
        
            bat= "select Itemname from bill"
            cursor.execute(bat)
            day=cursor.fetchall()    
            outer = [item for t in day for item in t]

            import mysql.connector as mc
            myc=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
            if mycon.is_connected()==False:
                print("Connection Unsuccesful")
            cure=myc.cursor()
        
            sat= "select Amount from bill"
            cure.execute(sat)
         
            dent=cure.fetchall()
            out = [item for t in dent for item in t]
            
            import numpy as np
            import matplotlib.pyplot as plt
            import pandas as pd
            plt.xlabel('Items bought by you')
            plt.ylabel('Total Amount(Rs.) of each item')
            plt.bar(outer,out)
            plt.show()
            
            print()
            print("Thank you. BE SAFE and WEAR MASK.")

            



       ##
        else:
            print()
            print("Thank you. BE SAFE and WEAR MASK.") #253
       
        import pymysql
        from sqlalchemy import create_engine
        engine=create_engine('mysql+pymysql://root:1234@localhost/grocery')
        conn=engine.connect()
        break
        

    
        
if countt==1:
    print('logged successfully')
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import mysql.connector as mc
    import datetime 
    mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
    if mycon.is_connected()=='False':
        print("Error in connectivity")
    cursor=mycon.cursor()
    print()
    print("Hello! Enter the itemno you want to buy from the menu card")

    df1=pd.read_sql("Select * from item;",mycon)
    print()
    print(df1)
    print()      

    a=int(input("Enter itemno"))
    print()

    df2=pd.read_sql("Select * from item%s"%(a),mycon)
    print(df2)


    print()
    b=int(input("Enter SrNo for the required product"))
    print()
    c=int(input("Enter Quantity"))
    print()

    L1=[]
    L2=[]
    L2.append(c)  #Quantity
    L3=[]
    L4=[]

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import mysql.connector as mc
    import datetime 
    mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
    if mycon.is_connected()=='False':
        print("Error in connectivity")
    cursor=mycon.cursor()    
    qry=cursor.execute("Select price from item%s where SrNo=%s"%(a,b)) #300

    data11=cursor.fetchall()
    for x in data11:
        res = int(''.join(map(str, x))) #tuple to int
        price=res*c
        L3.append(res)  #Unit price
        
        L1.append(price)  #amount
        
    print("Your Amount(Rs.) is",price)
#
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import mysql.connector as mc
    import datetime 
    mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
    if mycon.is_connected()=='False':
        print("Error in connectivity")
    cursor=mycon.cursor()

    cursor.execute("select products from item%s where SrNo=%s"%(a,b))
    data11a=cursor.fetchall()
    for x in data11a:
        
        L4.append(x)  #itemname(list of tuples)

    print()
    d=input("Do you want anything else from the given list? (type 'Yes' for affirmation and 'No' for negation)")

    while d=='No':
        print()
        f=input("Do you want to go back to the menu card? (type 'Yes' for affirmation and 'No' for negation)")
        if f=='Yes':

            #329
            print()
            print("Enter the itemno you want to buy from the menu card")
            print()
            df1=pd.read_sql("Select * from item;",mycon)
            print(df1)
            print()

            a=int(input("Enter itemno"))
            print()

            df2=pd.read_sql("Select * from item%s"%(a),mycon)
            print(df2)

            print()
            b=(int(input("Enter SrNo for the required product")))
            print()
            c1=(int(input("Enter Quantity")))
            print()

            import pandas as pd
            import numpy as np
            import matplotlib.pyplot as plt
            import mysql.connector as mc
            import datetime 
            mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
            if mycon.is_connected()=='False':
                print("Error in connectivity")
            cursor=mycon.cursor()
                
            cursor.execute("Select price from item%s where SrNo=%s"%(a,b))
            data11=cursor.fetchall()

            #358
        
            for x in data11:
            
                res1 = int(''.join(map(str, x))) #tuple to int
                price1=res1*c1

                L3.append(res1)  #unit price
                
                L2.append(c1)   #quantity
                L1.append(price1) #amount
                
            print("Your Amount(Rs.) is",price1)

            import pandas as pd
            import numpy as np
            import matplotlib.pyplot as plt
            import mysql.connector as mc
            import datetime 
            mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
            if mycon.is_connected()=='False':
                print("Error in connectivity")
            cursor=mycon.cursor()

            cursor.execute("select products from item%s where SrNo=%s"%(a,b))
            data11aa=cursor.fetchall()
            for x in data11aa:
                L4.append(x)   #itemname (list of tuples)
            
            print()
            e=input("Do you want anything else from the given list? (type 'Yes' for affirmation and 'No' for negation)")
            

            if e=='No':
                continue   ####3#####
            while e=='Yes':
                conti()
                break
                
            

        if f=='No':
            print()
            print("OKAY.")
            print()
            bill()
            break
        
        

       #330

        
        
        
        
            
    while d=="Yes":
        print()
        b=(int(input("Enter SrNo for the required product")))
        print()
        c1=(int(input("Enter Quantity")))
        print()
#400
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import mysql.connector as mc
        import datetime 
        mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
        if mycon.is_connected()=='False':
            print("Error in connectivity")
        cursor=mycon.cursor()
        
        cursor.execute("Select price from item%s where SrNo=%s"%(a,b))
        data11=cursor.fetchall()
        
        for x in data11:
            
            res1 = int(''.join(map(str, x))) #tuple to int
            price1=res1*c1

            L3.append(res1)  #unit price
            
            L2.append(c1)    #quantity
            L1.append(price1)  #amount
            
        print("Your Amount is",price1)

        #418

        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import mysql.connector as mc
        import datetime 
        mycon=mc.connect(host='localhost',user='root',passwd='1234',database='grocery')
        if mycon.is_connected()=='False':
            print("Error in connectivity")
        cursor=mycon.cursor()

        cursor.execute("select products from item%s where SrNo=%s"%(a,b))
        data11aa=cursor.fetchall()
        for x in data11aa:
            L4.append(x) #itemname (list of tuples)

        print()
        e=input("Do you want anything else from the given list? (type 'Yes' for affirmation and 'No' for negation)")
        
        
        if e=='Yes':
            continue
        
        
        print()
        f=input("Do you want to go back to the menu card? (type 'Yes' for affirmation and 'No' for negation)")
        print()
        
        if f=='Yes':
            print()
            print("Enter the itemno you want to buy from the menu card") #200
            print()
            df1=pd.read_sql("Select * from item;",mycon)
            print(df1)
            print()
            a=int(input("Enter itemno")) #a
            print()

        if f=='No':
            print()
            print("OKAY.")
            print()
            bill()
            break
        
        

            
        
        if a==2:
            item2()
        if a==3:
            item3()
        if a==4:
            item4()
        if a==5:
            item5()
        if a==6:
            item6()
            
else:
    print("login unsuccessful")

    

#466
