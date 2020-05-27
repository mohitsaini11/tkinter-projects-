from tkinter import *
import tkinter.font as font
import math
root = Tk()
root.geometry("520x600")
frame = LabelFrame(root, text='calculator frame', padx=25, pady=24)
frame.grid(padx=30, pady=35)
inputbar = Entry(frame, text='write something here', width=50, borderwidth=10)
inputbar.grid(row=0, column=0, columnspan=5, pady=22, padx=0)
initialadd=0
initialsub=0
initialmul=0
initialpower=0
initialdiv=0
def insertfun(no):
    global inputbar
    add = inputbar.get()
    inputbar.delete(0, END)
    inputbar.insert(0, str(add) + str(no))
ado=ddo=sdo=pdo=mdo=0
thedivnumber=1
theaddnumber = 0
themulnumber = 1
divcount=0
addcount=0
mulcount=0
subcount=0
powercount=0
def add():
    global addcount
    global theaddnumber

    if theaddnumber==0:
        add1 = giver()
        theaddnumber += add1
        cleaning()

    else:

        theaddnumber=giver()
        cleaning()
    addcount+=1

def repeathandler():
    global initialadd
    global initialsub
    global initialmul
    global initialpower
    global initialdiv
    global ado
    global mdo
    global pdo
    global sdo
    global ddo
    global theaddnumber
    global themulnumber
    global thedivnumber
    global thesubnumber
    global thepowerno
    if ado>=1:
        add2 =initialadd
        theaddnumber += add2
        cleaning()
        inserter(theaddnumber)
    elif ddo>=1:
        div2 = initialdiv
        thedivnumber = thedivnumber / div2
        cleaning()
        inserter(thedivnumber)
    elif mdo>=1:
        mul2 = initialmul
        themulnumber = themulnumber * mul2
        cleaning()
        inserter(themulnumber)
    elif pdo>=1:
        power2 = initialpower
        thepowerno = thepowerno ** power2
        cleaning()
        inserter(thepowerno)
    elif sdo>=1:
        sub2 = initialsub
        thesubnumber = thesubnumber - sub2
        cleaning()
        inserter(thesubnumber)





def cleaning():
    inputbar.delete(0,END)
def giver():
    return float(inputbar.get())
def  inserter(ins):
    inputbar.insert(0,ins)
def caller():
    global initialadd
    global initialsub
    global initialmul
    global initialpower
    global initialdiv
    global addcount
    global mulcount
    global divcount
    global subcount
    global powercount
    global theaddnumber
    global themulnumber
    global thedivnumber
    global thesubnumber
    global thepowerno
    global ado
    global mdo
    global pdo
    global sdo
    global ddo
    if addcount >= 1:

        add2 = giver()
        initialadd = add2
        theaddnumber += initialadd
        cleaning()
        inserter(theaddnumber)
        addcount = 0
        ado+=1

    elif mulcount >= 1:
        mul2 = giver()
        initialmul=mul2
        themulnumber = themulnumber * initialmul
        cleaning()
        inserter(themulnumber)
        mulcount = 0
        mdo+=1

    elif divcount >= 1:
        div2 = giver()
        initialdiv=div2
        thedivnumber = thedivnumber / initialdiv
        cleaning()
        inserter(thedivnumber)
        divcount = 0
        ddo+=1

    elif subcount >= 1:
        sub2 = giver()
        initialsub=sub2
        thesubnumber = thesubnumber - initialsub
        cleaning()
        inserter(thesubnumber)
        subcount = 0
        sdo+=1

    elif powercount >= 1:
        power2 = giver()
        initialpower=power2
        thepowerno = thepowerno ** initialpower
        cleaning()
        inserter(thepowerno)
        powercount = 0
        pdo+=1

    else:
        message='repeatation occured'
        return  message



def equals():
    mainvar=caller()
    if mainvar=='repeatation occured':
        repeathandler()


def multiply():
    global themulnumber
    global mulcount
    if themulnumber==1:
        nomul = giver()
        themulnumber = themulnumber * nomul
        print('the multiplied no is ',themulnumber)
        cleaning()
    else:
        themulnumber=giver()
        cleaning()
    mulcount+=1

def division():
    global divcount

    global thedivnumber
    if thedivnumber==1:
        div2=giver()
        thedivnumber=div2/thedivnumber
        cleaning()
    else:
        thedivnumber=giver()
        cleaning()
    divcount += 1

def subtraction():

    global subcount
    global thesubnumber

    if subcount==0:
        thesubnumber=0
        subno=giver()
        thesubnumber=subno-thesubnumber
        cleaning()
    else:
        thesubnumber=giver()
        cleaning()
    subcount += 1

def powerfun():
    global thepowerno
    global powercount
    if powercount==0:
        thepowerno = 1
        power2=giver()
        thepowerno=power2**thepowerno
        cleaning()
    else:
        thepowerno=giver()
        cleaning()
    powercount+=1

def squareroot():
    sqrno=giver()
    sqrt=sqrno**0.5
    cleaning()
    inserter(sqrt)

def clear():
    global theaddnumber
    global themulnumber
    global thedivnumber
    global thepowerno
    global thesubnumber
    cleaning()
    theaddnumber=0
    themulnumber=1
    thesubnumber=0
    thepowerno=1
    thedivnumber=1


def More():
    thelastnumber=0
    top=Toplevel()
    frame1 = LabelFrame(top, text='More options ', padx=25, pady=24)
    frame1.grid(padx=30, pady=35)
    def logarithm10():
        global thelastnumber
        thelastnumber = regainer_taker()
        no=giver2()
        cleaner()
        inserter2(math.log(10,no))
    def logarithme():
        global thelastnumber
        thelastnumber = regainer_taker()
        no = giver2()
        cleaner()
        inserter2(math.log(2.71828, no))

    def cleaner():
        inputbar1.delete(0, END)

    def giver2():
        return float(inputbar1.get())

    def converter(ins):
        ins = (ins * 3.14) / 180
        return ins

    def tenpower():
        global thelastnumber
        thelastnumber = regainer_taker()
        no=giver2()
        cleaner()
        inserter2(10**no)

    def sinfun():
        global thelastnumber
        thelastnumber=regainer_taker()
        nono=giver2()
        nono=converter(nono)
        thesinnumber=math.sin(nono)
        cleaner()
        inserter2(thesinnumber)
    def cosfun():
        global thelastnumber
        thelastnumber = regainer_taker()
        regainer_taker()
        nono=giver2()
        nono=converter(nono)
        thecosnumber=math.cos(nono)
        cleaner()
        inserter2(thecosnumber)
    def tanfun():
        global thelastnumber
        thelastnumber = regainer_taker()
        regainer_taker()
        nono=giver2()
        nono=converter(nono)
        thetannumber=math.tan(nono)
        cleaner()
        inserter2(thetannumber)
    def cotfun():
        global thelastnumber
        thelastnumber = regainer_taker()
        regainer_taker()
        nono=giver2()
        nono=converter(nono)
        thecotnumber=math.tan(nono)
        thecotnumber=1/thecotnumber
        cleaner()
        inserter2(thecotnumber)

    def secfun():
        global thelastnumber
        thelastnumber = regainer_taker()
        regainer_taker()
        nono=giver2()
        nono=converter(nono)
        thesecnumber=math.cos(nono)
        thesecnumber=1/thesecnumber
        cleaner()
        inserter2(thesecnumber)

    def cosecfun():
        global thelastnumber
        thelastnumber = regainer_taker()

        nono=giver2()
        nono=converter(nono)
        thecosecnumber=math.sin(nono)
        thecosecnumber=1/thecosecnumber
        cleaner()
        inserter2(thecosecnumber)

    def factorial():
        global thelastnumber
        thelastnumber = regainer_taker()
        no=int(giver2())
        if no>=0:
            factorial = math.factorial(no)
            cleaner()
            inserter2(factorial)
        else:
            cleaner()
            inserter2('the factorial do not exist!!!')

    def regainer_taker():
        lastno=giver2()
        return lastno

    def regainer_enter():
        global thelastnumber
        cleaner()
        inserter2(thelastnumber)

    def transfer():
        thedata = giver2()
        cleaning()
        inserter(thedata)
        top.destroy()

    inputbar1 = Entry(frame1,text='here', width=50, borderwidth=10)
    inputbar1.grid(row=0, column=0, columnspan=5, pady=22, padx=0)
    cleaner()
    def inserter2(ins1):
        inputbar1.insert(0,ins1)

    number = inputbar.get()
    inserter2(number)

    def buttons2():
        buttonlog = Button(frame1, text='log( )', width=9, padx=10, pady=22,command=logarithm10).grid(row=1, column=0)
        buttonfactorial = Button(frame1, text='n!', width=9, padx=10, pady=22,command=factorial).grid(row=1, column=2)
        buttonln = Button(frame1, text='ln( )', width=9, padx=10, pady=22,command=logarithme).grid(row=1, column=1)
        buttonsin = Button(frame1, text='sin( )', width=9, padx=10, pady=22,command=sinfun).grid(row=2, column=0)
        buttoncos = Button(frame1, text='cos( )', width=9, padx=10, pady=22,command=cosfun).grid(row=2, column=1)
        buttontan = Button(frame1, text='tan( )', width=9, padx=10, pady=22,command=tanfun).grid(row=2, column=2)
        buttoncot = Button(frame1, text='cot( )', width=9, padx=10, pady=22,command=cotfun).grid(row=3, column=0)
        buttonssec = Button(frame1, text='sec( )', width=9, padx=10, pady=22,command=secfun).grid(row=3, column=1)
        buttoncosec = Button(frame1, text='cosec( )', width=9, padx=10, pady=22,command=cosecfun).grid(row=3, column=2)
        buttonbrac1 = Button(frame1, text='REGAIN', width=9, padx=10, pady=22,command=regainer_enter).grid(row=1, column=3)
        buttonbrac2 = Button(frame1, text='EMPTY', width=9, padx=10, pady=22).grid(row=2, column=3)
        buttontenpower = Button(frame1, text='10**', width=9, padx=10, pady=22,command=tenpower ).grid(row=3, column=3)
        buttondestroy=Button(frame1,text='Close this window',command=top.destroy , width=25, borderwidth=5,pady=10).grid(row=4,columnspan=2,column=0)
        button_equal1 = Button(frame1, text="<<<PASS", pady=10, padx=10, width=25, borderwidth=5,command=transfer).grid(row=4,columnspan=2,column=2)

    buttons2()


myFont = font.Font(family='Courier', size=9, weight='bold')
def buttons():
    button1 = Button(frame, text='1', width=9, padx=10, pady=22, command=lambda: insertfun(1)).grid(row=3, column=0)
    button2 = Button(frame, text='2', width=9, padx=10, pady=22, command=lambda: insertfun(2)).grid(row=3, column=1)
    button3 = Button(frame, text='3', width=9, padx=10, pady=22, command=lambda: insertfun(3)).grid(row=3, column=2)
    button4 = Button(frame, text='4', width=9, padx=10, pady=22, command=lambda: insertfun(4)).grid(row=2, column=0)
    button5 = Button(frame, text='5', width=9, padx=10, pady=22, command=lambda: insertfun(5)).grid(row=2, column=1)
    button6 = Button(frame, text='6', width=9, padx=10, pady=22, command=lambda: insertfun(6)).grid(row=2, column=2)
    button7 = Button(frame, text='7', width=9, padx=10, pady=22, command=lambda: insertfun(7)).grid(row=1, column=0)
    button8 = Button(frame, text='8', width=9, padx=10, pady=22, command=lambda: insertfun(8)).grid(row=1, column=1)
    button9 = Button(frame, text='9', width=9, padx=10, pady=22, command=lambda: insertfun(9)).grid(row=1, column=2)
    button0 = Button(frame, text='0', width=9, padx=10, pady=22, command=lambda: insertfun(0)).grid(row=4, column=0)
    buttonadd = Button(frame, text='+', width=9, padx=10, pady=22, command=add).grid(row=1, column=4)
    buttonsub = Button(frame, text='-', width=9, padx=10, pady=22,command=subtraction).grid(row=2, column=4)
    button3mul = Button(frame, text='*', width=9, padx=10, pady=22,command=multiply).grid(row=3, column=4)
    button4div = Button(frame, text='/', width=9, padx=10, pady=22,command=division).grid(row=4, column=4)
    buttonsqrt = Button(frame, text='SQRT', width=9, padx=10, pady=22,command=squareroot).grid(row=4, column=1)
    buttonpower = Button(frame, text='^', width=9, padx=10, pady=2,command=powerfun).grid(row=4, column=2)
    buttonclear = Button(frame, text='CLEAR', width=55, borderwidth=5,command=clear,padx=4).grid(row=6, column=0, columnspan=5)

    buttonmore = Button(frame, text='MORE', padx=2, pady=22, width=10, borderwidth=9,command=More).grid(row=5, column=4)
    button_equal = Button(frame, text="=", pady=20, padx=68, width=20, borderwidth=10, command=equals,activebackground='orange')
    button_equal['font'] = myFont
    button_equal.grid(row=5,columnspan=4,column=0)
buttons()


mainloop()
