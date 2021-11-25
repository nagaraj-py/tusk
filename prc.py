import pandas as pd
import json
books={}
class bsm:

    def add_books():
        book = input("enter book:")
        df = pd.read_excel(book)
        bk = dict(zip(df["Bookname"],df["quantity"]))
        print(bk)
        with open('store.json', 'w') as outfile:
                json.dump(bk,outfile)
    def new_book():
        n = input("enter book :")
        qnt=int(input("enter quantity:"))
        books[n]=qnt
    
class cms:
    def display_books():
        f = open("store.json","r")
        file = f.read()
        obj = json.loads(file)
        books.update(obj)
        df=pd.DataFrame({"menu":books})
        print(df)

    def order_book():
        name=input("enter customer name: ")
        num=input("enter customer number: ")
        f = open("store.text","a")
        f.write(name)
        f.write(num)
        choice = input('Enter book title: ')
        if choice in books.keys():
            #q=int(input("enter no of copies:"))
            #if q in books.values():
            print("the "+choice," is issued to " +name, "number:"+num)
            init_num = books[choice]
            init_num -= 1
            books[choice] = init_num
            print()
            j=json.dumps(books)
            obj = open('store.json', 'w')
            obj.write(j)
            #else:
             #   print("not available")
        else:
            print("there is no book on this title")

def main():
    bs=bsm
    cm=cms
    while True:
        print("""menu
        1.add books
        2.display books
        3.order book
        4.newbook
        5.exit""")
        choice = int(input("enter choice:"))
        if choice == 1:
            bs.add_books()
        elif choice == 2:
            cm.display_books()
        elif choice == 3:
            cm.order_book()
        elif choice==5:
            break
        elif choice == 4:
            bs.new_book()
        else:
            continue
main()