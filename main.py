from os import name
from pyfiglet import Figlet

def show_list():
    'please chose a number'


def shoe_menu():
    print('1-adad product')
    print('2-edit product')
    print('3-qrcode')
    print('4-delet')
    print('5-show list')
    print('6-search')
    print('7-buy')
def load():
    print('loading..')
my_file=open('database.txt','r')
data = my_file.read()
#print(my_file.read())
# my_file.close()
products_list = data.split('\n')
print(products_list)
PRODUCTS=[]

def ezafe_kardan_kala() :
    PRODUCTS.append(input(''))
    print(PRODUCTS)
   
   





for i in range(len(products_list)):
    prouduct_info=products_list[i].split(',')
    mydic={}
    mydic['id']=prouduct_info[0]
    mydic['name']=prouduct_info[1]
    mydic['price']=prouduct_info[2]
    mydic['count']=prouduct_info[3]
    PRODUCTS.append(mydic)



def virayesh_kala():
    id=(input('kodom kala ro mikhay edit koni'))
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==id :
            PRODUCTS[i]['name'] = input('new name: ')
            print(PRODUCTS)    
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==id :
            PRODUCTS[i]['PRICE'] = input('new price: ')
            print(PRODUCTS)  
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==id :
            PRODUCTS[i]['count'] = input('new count ')
            print(PRODUCTS) 



def qrcode():
    from pyqrcode import QRCode
    x=input('etelaat kala ra baraye sakht qr code vared konid')
    

    myQr=QRCode(x)



    myQr.png('qrcode1.png',scale=8)
        

def delet():
    print(PRODUCTS)
    id=input('kodom kala ro mikhay delet koni id ro benevis')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==id :
            del PRODUCTS[i]
            print(PRODUCTS)
            break
            
    else :
            print('hamchin kalayee vojod nadarad')


def search():
    w=input('name kala ra vared konid')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name']==w :

            print(PRODUCTS[i])


def buy():
    id=int(input('code kala ra vared konid'))
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==id :
             if PRODUCTS[i]['count']>count :
                print

                

    else:
        print('chenin kalayee vojod nadarad')



count=int(input('che meghdar: '))
if PRODUCTS[i]['count']==count:
...








load()
f=Figlet(font='standard')
print(f.renderText('helia store'))

shoe_menu()

choice=int(input('please chose a number'))

if choice==1 :
  ezafe_kardan_kala()
elif choice==2:
    virayesh_kala()
elif choice==3:
    qrcode()
elif choice ==4:
    delet()
elif choice ==5 :
    show_list
elif choice==6:
    search()
elif choice ==7:
   buy()
