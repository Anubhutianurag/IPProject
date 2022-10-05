import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con=sqlt.connect(host="localhost",user="root",password="jaimatadi",database="library")
cursor=con.cursor()
def book_input():
    bookid=input("Enter book id")
    bname=input("Enter book name")
    author=input("Enter author")
    price=float(input("Enter price"))
    copies=int(input("Enter copies"))
    qry="insert into book values({},'{}','{}',{},{},{});".format(bookid,bname,author,price,copies,copies)
    cursor.execute(qry)
    con.commit()
    print("Added successfully..")
def book_edit():
    x=int(input("Enter book ID"))
    qry="select * from book where bookid={};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        y=float(input("Enter new price"))
        qry="update book set price={} where bookid={};".format(y,x)
        cursor.execute(qry)
        con.commit()
        print("Edited sucessfully ")
    else:
        print("Wrong book id")
def book_delete():
    x = int(input("Enter book ID"))
    qry = "select * from book where bookid={};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        qry = "delete from book where bookid={};".format(x)
        cursor.execute(qry)
        con.commit()
        print("Deleted sucessfully ")
    else:
        print("Wrong id")
def customer_input():
    customid=int(input("Enter customer id"))
    cname=input("Enter customer name")
    caddress=input("Enter address")
    phone=input("Enter phone number")
    qry="insert into customer values({},'{}','{}','{}');".format(customid,cname,caddress,phone)
    cursor.execute(qry)
    con.commit()
    print("Added successfully..")
def customer_edit():
    x=int(input("Enter customer ID"))
    qry="select * from customer where customid={};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        y=input("Enter new phone")
        qry="update customer set phone={} where customid={};".format(y,x)
        cursor.execute(qry)
        con.commit()
        print("Edited sucessfully ")
    else:
        print("Wrong customer id")
def customer_delete():
    x = int(input("Enter customer ID"))
    qry = "select * from customer where customid={};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        qry = "delete from customer where customid={};".format(x)
        cursor.execute(qry)
        con.commit()
        print("Deleted sucessfully ")
    else:
        print("Wrong id")
def customer_search():
    x=int(input("Enter customer id"))
    qry="select* from customer where customid={};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        df=pd.read_sql(qry,con)
        print(tabulate(df, headers= 'keys', tablefmt='psql',showindex=False))
    else:
        print("wrong customid")
def book_output():
    df=pd.read_sql("select* from book",con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
def customer_output():
    df=pd.read_sql("select * from customer",con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
def return_output():
    df=pd.read_sql("select* from returns",con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
def issue_output():
    df=pd.read_sql("select* from issue",con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
def book_issue():
    q="select max(issueid) from issue;"
    cursor.execute(q)
    r=cursor.fetchone()[0]
    if r:
        issueid=r+1
    else:
        issueid=1
    x=int(input("enter customid"))
    q1="select * from customer where customid={};".format(x)
    cursor.execute(q1)
    r=cursor.fetchone()
    if r:
        y=int(input("Enter book id"))
        q2="select bookid,book_rem from book where bookid={};".format(y)
        cursor.execute(q2)
        r=cursor.fetchone()
        if r:
            if r[1]>0:
                issuedate=input("Enter issue date")
                copies=int(input("Enter no of copies"))
                book_rem=r[1]-copies
                q3="insert into issue value({},'{}',{},{},{});".format(issueid,issuedate,x,y,book_rem)
                cursor.execute(q3)
                q4="update book set book_rem={} where bookid={}".format(book_rem,y)
                cursor.execute(q4)
                con.commit()
                print("Book issued")
            else:
                print("Book unavailable")
        else:
            print("Incorrect book id")
    else:
        print("Wrong customer  id")
def book_return():
    q = "select max(returnid) from returns;"
    cursor.execute(q)
    r = cursor.fetchone()[0]
    if r:
        returnid = r + 1
    else:
        returnid = 1
    x = int(input("Enter customer id"))
    q1 = "select * from customer where customid={};".format(x)
    cursor.execute(q1)
    r = cursor.fetchone()
    if r:
        y = int(input("Enter book id"))
        q2 = "select bookid,book_rem from book where bookid={};".format(y)
        cursor.execute(q2)
        r = cursor.fetchone()
        if r:

            returndate = input("Enter return date")
            copies = int(input("Enter no of copies"))
            book_rem = r[1] + copies
            q3 = "insert into returns value({},'{}',{},{},{});".format(returnid, returndate, x, y, book_rem)
            cursor.execute(q3)
            q4 = "update book set book_rem={} where bookid={}".format(book_rem, y)
            cursor.execute(q4)
            con.commit()
            print("Book Returned")

        else:
            print("Incorrect book id")
    else:
        print("Wrong customer  id")
while(True):
    print("="*80)
    print("\t\t\tWELCOME TO LIBRARY MANAGMENT")
    print("Enter Your Choice\n1.Book Details\n2.customer Details\n3.Transaction\n4.Report\n5.Exit")
    choice=int(input())
    if choice==1:
        while (True):
            print("Enter your choice\n1.Add book details\n2.Edit a book\n3.Delete a book\n4 back to main menu")
            choice=int(input())
            if choice == 1:
                book_input()
            elif choice == 2:
                book_edit()
            elif choice == 3:
                book_delete()
            elif choice == 4:
                break
    elif choice == 2:
        while (True):
           print("Enter your Choice\n1.Add customer details\n2.Edit a customer\n3.Delete a customer\n4.search a customer"
                 "\n5.back to main menu")
           choice=int(input())
           if choice == 1:
               customer_input()
           elif choice == 2:
               customer_edit()
           elif choice == 3:
               customer_delete()
           elif choice == 4:
               customer_search()
           elif choice == 5:
               break
    elif choice == 3:
        while (True):
           print("Enter your Choice\n1.Issue book\n2.Return book\n3.Back to main menu")
           choice = int(input())
           if choice == 1:
               book_issue()
           elif choice == 2:
               book_return()
           elif choice == 3:
               break
    elif choice == 4:
        while (True):
            print("Enter your Choice\n1.Book details\n2.Customer details\n3.Issue details\n4.return details\n5.Back to main menu")
            choice = int(input())
            if choice == 1:
                book_output()
            elif choice == 2:
                customer_output()
            elif choice == 3:
                issue_output()
            elif choice == 4:
                return_output()
            elif choice == 5:
                break
    elif choice == 5:
        break

