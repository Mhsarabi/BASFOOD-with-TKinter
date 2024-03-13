from tkinter import *
import tkinter as tk
from tkinter.font import Font
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import ImageTk, Image,ImageDraw
import random


k=0


def home_button_clicked():
    global iconf
    icont = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    top=Toplevel()
    top.config(bg="#ff3838")
    top.geometry("400x300")
    top.minsize(400,300)
    top.maxsize(400,300)
    iconf = ImageTk.PhotoImage(icont)
    lbl=Label(top,text="(:اینجا خانه شماست دوست من")
    lbl.config(bg="#ff3838",fg="white",font="Helvetica 14 bold")
    lblt=Label(top,image=iconf)
    lblt.config(bg="#ff3838")
    lblt.grid(row=2,column=2,padx=80)
    lbl.grid(row=3,column=2,padx=50)
    top.iconbitmap("pic/resturant.ico")
    top.after(2000,lambda:top.destroy())


def if_drink(food_name,price):
    global icona
    icont = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    top=Toplevel()
    top.config(bg="#ff3838")
    top.geometry("700x400")
    top.minsize(700,400)
    top.maxsize(700,400)
    icona = ImageTk.PhotoImage(icont)
    lblt=Label(top,image=icona)
    lblt.config(bg="white")
    lblt.grid(row=2,column=2,padx=80)
    top.iconbitmap("pic/resturant.ico")
    lbl=Label(top,text="آیا مایل به سفارش نوشیدنی هم هستید؟")
    lbl.config(bg="#ff3838",fg="white")
    lbl.grid(row=4,column=3,pady=10)
    drink_but_yes=tb.Button(master=top, text="بله", bootstyle="success,outline",command=lambda:[top.destroy(),drink(food_name,price)])
    drink_but_yes.grid(row=8, column=3, pady=10)
    drink_but_no=tb.Button(master=top, text="خیر", bootstyle="danger,outline",command=lambda:[top.destroy(),chance_second(food_name,price)])
    drink_but_no.grid(row=9, column=3, pady=10)

def iranian_food_button_clicked():
    global iconb
    global image1
    global image2
    global image3
    global image4
    global image5
    icont = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    iran=Toplevel()
    iran.config(bg="red")
    iran.geometry("1000x600")
    iran.minsize(1000,600)
    iran.maxsize(1000,600)
    iconb = ImageTk.PhotoImage(icont)
    iran.iconbitmap("pic/resturant.ico")
    lblt=Label(iran,image=iconb)
    lblt.grid(row=2,column=0,padx=80)

    zereshk = Image.open("pic/zereshk.jpg").resize((100, 100))
    image1 = ImageTk.PhotoImage(zereshk)

    ghoemeh = Image.open("pic/ghormeh sabzi.jpg").resize((100, 100))
    image2 = ImageTk.PhotoImage(ghoemeh)

    gheymeh = Image.open("pic/gheymeh.jpg").resize((100, 100))
    image3 = ImageTk.PhotoImage(gheymeh)

    kabab = Image.open("pic/kabab-koubide-1.jpg").resize((100, 100))
    image4 = ImageTk.PhotoImage(kabab)

    gogeh = Image.open("pic/gogeh.webp").resize((100, 100))
    image5 = ImageTk.PhotoImage(gogeh)

    food_label = tk.Label(master=iran, text="غداهای ایرانی", font="Helvectica 18 bold")
    food_label.config(fg="white",bg="red")
    food_label.grid(row=3, column=6, pady=0, sticky="ns")

    price_zeresh = tk.Label(master=iran, text="   زرشک پلو با مرغ\nقیمت: ۱۰۰۰۰ تومان", font="Morvarid 12 bold")
    price_zeresh.config(bg="red",fg="white")
    price_zeresh.grid(row=5, column=1, pady=(0, 20), padx=10)

    label_zeresh = tb.Label(master=iran, image=image1, width=50)
    label_zeresh.grid(row=4, column=1, pady=(8, 20), padx=10)

    zeresh_o_button = tb.Button(master=iran, text="سفارش دادن", bootstyle="warning,outline",command=lambda: [iran.destroy(),if_drink("زرشک پلو با مرغ", 10000)])
    zeresh_o_button.grid(row=6, column=1, pady=10)

    # Additional information for ghormeh
    label_ghormeh = tb.Label(master=iran, image=image2, width=50)
    label_ghormeh.grid(row=4, column=2, pady=(8, 20), padx=10)

    price_ghormeh = tk.Label(master=iran, text="    قرمه سبزی \n قیمت: ۱۵۰۰۰ تومان", font="Morvarid 12 bold")
    price_ghormeh.config(bg="red",fg="white")
    price_ghormeh.grid(row=5, column=2, pady=(0, 20), padx=10)

    ghormeh_o_button = tb.Button(master=iran, text="سفارش دادن", bootstyle="warning,outline",command=lambda: [iran.destroy(),if_drink("قرمه سبزی", 15000)])
    ghormeh_o_button.grid(row=6, column=2, pady=10)

    # Additional information for geymeh
    label_gheymeh = tb.Label(master=iran, image=image3, width=50)
    label_gheymeh.grid(row=4, column=3, pady=(8, 20), padx=10)

    price_gheymeh = tk.Label(master=iran, text="   قیمه با سیب زمینی\nقیمت: ۲۰۰۰۰ تومان", font="Morvarid 12 bold")
    price_gheymeh.config(bg="red",fg="white")
    price_gheymeh.grid(row=5, column=3, pady=(0, 20), padx=10)

    gheymeh_o_button = tb.Button(master=iran, text="سفارش دادن", bootstyle="warning,outline",command=lambda: [iran.destroy(),if_drink("قیمه با سیب زمینی", 20000)])
    gheymeh_o_button.grid(row=6, column=3, pady=10)


    price_kebab = tk.Label(master=iran, text="     کباب با مخلفات\nقیمت: ۱۰۰۰۰ تومان", font="Morvarid 12 bold")
    price_kebab.config(bg="red",fg="white")
    price_kebab.grid(row=5, column=0, pady=(0, 20), padx=20)

    label_kebab = tb.Label(master=iran, image=image4, width=50)
    label_kebab.grid(row=4, column=0, pady=(8, 20), padx=10)

    kebab_o_button = tb.Button(master=iran, text="سفارش دادن", bootstyle="warning,outline",command=lambda:[ iran.destroy(),if_drink("کباب با مخلفات", 10000)])
    kebab_o_button.grid(row=6, column=0, pady=10)

    price_gogeh = tk.Label(master=iran, text="     جوجه با مخلفات \nقیمت: ۱۰۰۰۰ تومان", font="Morvarid 12 bold")
    price_gogeh.config(bg="red",fg="white")
    price_gogeh.grid(row=5, column=5, pady=(0, 20), padx=20)

    label_gogeh = tb.Label(master=iran, image=image5, width=50)
    label_gogeh.grid(row=4, column=5, pady=(8, 20), padx=10)

    gogeh_o_button = tb.Button(master=iran, text="سفارش دادن", bootstyle="warning,outline",command=lambda: [iran.destroy(),if_drink("جوجه با مخلفات", 10000)])
    gogeh_o_button.grid(row=6, column=5, pady=10)




def fast_food_button_clicked():
    global iconx
    global image6
    global image7
    global image8
    global image9
    global image10
    iconc = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    top=Toplevel()
    top.config(bg="#f39c12")
    top.geometry("1000x600")
    top.minsize(1000,600)
    top.maxsize(1000,600)
    iconx = ImageTk.PhotoImage(iconc)
    top.iconbitmap("pic/resturant.ico")
    lblt=Label(top,image=iconx)
    lblt.grid(row=2,column=0,padx=80)

    chicken = Image.open("pic/chicken-kentucky.jpg").resize((100, 100))
    image6 = ImageTk.PhotoImage(chicken)

    Pizza = Image.open("pic/Pizza.jpg").resize((100, 100))
    image7 = ImageTk.PhotoImage(Pizza)

    hamburger = Image.open("pic/hamburger.jpg").resize((100, 100))
    image8 = ImageTk.PhotoImage(hamburger)

    cheesburger = Image.open("pic/cheeseburger.jpg").resize((100, 100))
    image9 = ImageTk.PhotoImage(cheesburger)

    cheesburger = Image.open("pic/hotdog.jpg").resize((100, 100))
    image10 = ImageTk.PhotoImage(cheesburger)

    food_label_2 = tk.Label(master=top, text="فست فود", font="Helvectica 18 bold")
    food_label_2.config(fg="black",bg="#f39c12")
    food_label_2.grid(row=3, column=6, pady=0, sticky="ns")

    # Additional information for the chicken
    price_chicken = tk.Label(master=top, text="   مرغ کنتاکی\nقیمت: ۲۵۰۰۰ تومان", font="Morvarid 12 bold")
    price_chicken.config(bg="#f39c12")
    price_chicken.grid(row=5, column=0, pady=(0, 20), padx=10)

    label_chicken = tb.Label(master=top, image=image6, width=50)
    label_chicken.grid(row=4, column=0, pady=(8, 20), padx=10)

    chicken_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="danger,outline",command=lambda:[top.destroy(), if_drink("مرغ کنتاکی", 25000)])
    chicken_o_button.grid(row=6, column=0, pady=10)

    # Additional information for the pizza
    price_Pizza = tk.Label(master=top, text="   پیتزا\nقیمت: ۳۰۰۰۰ تومان", font="Morvarid 12 bold")
    price_Pizza.config(bg="#f39c12")
    price_Pizza.grid(row=5, column=1, pady=(0, 20), padx=10)

    label_Pizza = tb.Label(master=top, image=image7, width=50)
    label_Pizza.grid(row=4, column=1, pady=(8, 20), padx=10)

    pizza_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="danger,outline",command=lambda: [top.destroy(),if_drink("پیتزا", 30000)])
    pizza_o_button.grid(row=6, column=1, pady=10)

    # Additional information for the burger
    price_hamburger = tk.Label(master=top, text="    همبرگر\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold")
    price_hamburger.config(bg="#f39c12")
    price_hamburger.grid(row=5, column=2, pady=(0, 20), padx=10)

    label_hamburger = tb.Label(master=top, image=image8, width=50)
    label_hamburger.grid(row=4, column=2, pady=(8, 20), padx=10)

    hamburger_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="danger,outline", command=lambda: [top.destroy(),if_drink("همبرگر", 35000)])
    hamburger_o_button.grid(row=6, column=2, pady=10)

    price_cheezburger = tk.Label(master=top, text="     چیزبرگر\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold")
    price_cheezburger.config(bg="#f39c12")
    price_cheezburger.grid(row=5, column=3, pady=(0, 20), padx=10)

    label_cheesburger = tb.Label(master=top, image=image9, width=50)
    label_cheesburger.grid(row=4, column=3, pady=(8, 20), padx=10)

    cheezburger_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="danger,outline", command=lambda:[top.destroy(), if_drink("چیزبرگر", 35000)])
    cheezburger_o_button.grid(row=6, column=3, pady=10)

    label_hotdog = tb.Label(master=top, image=image10, width=50)
    label_hotdog.grid(row=4, column=4, pady=(8, 20), padx=10)

    price_hotdog = tk.Label(master=top, text="    هات داگ\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold")
    price_hotdog.config(bg="#f39c12")
    price_hotdog.grid(row=5, column=4, pady=(0, 20), padx=10)

    hotdog_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="danger,outline", command=lambda: [top.destroy(),if_drink("هات داگ", 35000)])
    hotdog_o_button.grid(row=6, column=4, pady=10)


    


def drink(food_name="",price=0,drink="",P_drink=0):
    global icond
    global image11
    global image12
    global image13
    icont = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    top=Toplevel()
    top.config(bg="#2980b9")
    top.geometry("990x600")
    top.minsize(990,600)
    top.maxsize(990,600)
    icond = ImageTk.PhotoImage(icont)
    top.iconbitmap("pic/resturant.ico")
    lblt=Label(top,image=icond)
    lblt.grid(row=0,column=0,padx=80)

    nooshabeh = Image.open("pic/nooshidan_nooshabeh.jpg").resize((100, 100))
    image11 = ImageTk.PhotoImage(nooshabeh)

    ddogh = Image.open("pic/ddogh.jpg").resize((100, 100))
    image12 = ImageTk.PhotoImage(ddogh)

    delester = Image.open("pic/delester.jpg").resize((100, 100))
    image13 = ImageTk.PhotoImage(delester)


    food_label_2 = tk.Label(master=top, text="نوشیدنی", font="Helvectica 18 bold")
    food_label_2.config(fg="white",bg="#2980b9")
    food_label_2.grid(row=2, column=6, pady=10, sticky="ns")
    # Additional information for the burger
    price_nooshabeh = tk.Label(master=top, text="  نوشابه\nقیمت: ۳0۰۰۰ تومان", font="Morvarid 12 bold")
    price_nooshabeh.config(fg="white",bg="#2980b9")
    price_nooshabeh.grid(row=5, column=1, pady=(0, 20), padx=10)

    label_nooshabeh = tb.Label(master=top, image=image11, width=50)
    label_nooshabeh.grid(row=4, column=1, pady=(8, 20), padx=10)

    nooshabeh_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="info,outline",command=lambda:[top.destroy(), chance_second(food_name,price,drink="نوشابه",p_drink= 30000)])
    nooshabeh_o_button.grid(row=6, column=1, pady=10)


    price_ddogh = tk.Label(master=top, text="   دوغ\nقیمت: 2۵۰۰۰ تومان", font="Morvarid 12 bold")
    price_ddogh.config(fg="white",bg="#2980b9")
    price_ddogh.grid(row=5, column=2, pady=(0, 20), padx=10)

    label_ddogh = tb.Label(master=top, image=image12, width=50)
    label_ddogh.grid(row=4, column=2, pady=(8, 20), padx=10)

    dogh_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="info,outline",command=lambda:[top.destroy(), chance_second(food_name,price,drink="دوغ ",p_drink= 25000)])
    dogh_o_button.grid(row=6, column=2, pady=10)


    price_delester = tk.Label(master=top, text="   دلستر\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold")
    price_delester.config(fg="white",bg="#2980b9")
    price_delester.grid(row=5, column=3, pady=(0, 20), padx=10)

    label_delester = tb.Label(master=top, image=image13, width=50)
    label_delester.grid(row=4, column=3, pady=(8, 20), padx=10)

    delester_o_button = tb.Button(master=top, text="سفارش دادن", bootstyle="info,outline",command=lambda: [top.destroy(),chance_second(food_name,price,drink="دلستر ",p_drink= 35000)])
    delester_o_button.grid(row=6, column=3, pady=10)


def factor(food_name="",price=0,drink="",p_drink=0,takhfif=0):
    global iconh
    global k
    k+=1
    icont = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    top=Toplevel()
    top.config(bg="white")
    top.geometry("800x500")
    top.minsize(800,500)
    top.maxsize(800,500)
    iconh = ImageTk.PhotoImage(icont)
    number=Label(top,text=f"{k}:شماره")
    number.config(bg="white",fg="red",font="Helvetica 14 bold")
    lbl=Label(top,text="فاکتور")
    lbl.config(bg="white",fg="black",font="Helvetica 14 bold")
    lblt=Label(top,image=iconh)
    lblt.config(bg="white")
    number.grid(row=2,column=5)
    lblt.grid(row=2,column=4,padx=200)
    lbl.grid(row=3,column=4,padx=200)
    top.iconbitmap("pic/resturant.ico")
    food=Label(top,text=f"نام غذا :{food_name}")
    food.config(bg="white",fg="black")
    Price=Label(top,text=f"قیمت نوشیدنی:{price}تومان")
    Price.config(bg="white",fg="black")
    Drink=Label(top,text=f"نوشیدنی :{drink}")
    Drink.config(bg="white",fg="black")
    P_drink=Label(top,text=f"قیمت نوشیدنی:{p_drink}تومان")
    P_drink.config(bg="white",fg="black")
    food.grid(row=5,column=4,padx=200)
    Price.grid(row=6,column=4,padx=200)
    Drink.grid(row=7,column=4,padx=200)
    P_drink.grid(row=8,column=4,padx=200)
    if takhfif==0:
        P_adrink=Label(top,text=f"قیمت کل:{price+p_drink}تومان")
        P_adrink.config(bg="white",fg="black")
        P_adrink.grid(row=9,column=4,padx=200)

    elif takhfif==1:
        P_adrink=Label(top,text=f"قیمت کل :{(p_drink+price)//2}")
        P_adrink.config(bg="white",fg="black")
        P_adrink.grid(row=9,column=4,padx=200)

    lbe=Label(top,text="به امید دیدار مجدد شما")
    lbe.config(bg="white",fg="black",font="Helvetica 14 bold")
    lbe.grid(row=10,column=4,padx=200)
    

    

def chance_challeng(food_name="",price=0,drink="",p_drink=0,takhfif=0):
    number=random.randint(0,100)
    golden_number=random.randint(0,100)
    if number==golden_number:
        tabrik.config(text="تبریک مییییگم\nشما برنده 50% تخفیف شدید",fg="green")
        takhfif=1
        factor(food_name,price,drink,p_drink,takhfif)


    else:
        tabrik.config(text="ای واااای\nاین بار نشد دفعه بعد حتما برنده میشی",fg="red")
        takhfif=0
        factor(food_name,price,drink,p_drink,takhfif)

    

def chance_first():
    global iconm
    icont = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    top=Toplevel()
    top.config(bg="#ff3838")
    top.geometry("400x300")
    top.minsize(400,300)
    top.maxsize(400,300)
    iconm = ImageTk.PhotoImage(icont)
    lbl=Label(top,text="(:شما اول بخر بعد با هم کنار میاییم")
    lbl.config(bg="#ff3838",fg="white",font="Helvetica 14 bold")
    lblt=Label(top,image=iconm)
    lblt.config(bg="#ff3838")
    lblt.grid(row=2,column=2,padx=80)
    lbl.grid(row=3,column=2,padx=50)
    top.iconbitmap("pic/resturant.ico")
    top.after(2000,lambda:top.destroy())


def chance_second(food_name="",price=0,drink="",p_drink=0):
    global iconm
    global tabrik
    icont = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
    top=Toplevel()
    top.config(bg="white")
    top.geometry("700x500")
    top.minsize(700,500)
    top.maxsize(700,500)
    iconm = ImageTk.PhotoImage(icont)
    lbl=Label(top,text="به بخش شانس و تخفیف خوش آمدی")
    lbl.config(bg="white",font="Helvetica 14 bold")
    lbn=Label(top,text="اینجا فقط یک نفر برنده میشه\n(:برای همینه که ما اینجا چند تا چند تا نداریم")
    lbn.config(fg="orange",bg="white",font="Helvetica 14 bold")
    lblt=Label(top,image=iconm)
    lblt.config(bg="white")
    lblt.grid(row=2,column=4,padx=80)
    lbl.grid(row=3,column=4,padx=50)
    lbn.grid(row=4,column=4,padx=50)
    top.iconbitmap("pic/resturant.ico")
    food=Label(top,text=f"نام غذا :{food_name}")
    food.config(bg="white",fg="black")
    Price=Label(top,text=f"قیمت نوشیدنی:{price}تومان")
    Price.config(bg="white",fg="black")
    Drink=Label(top,text=f"نوشیدنی :{drink}")
    Drink.config(bg="white",fg="black")
    P_drink=Label(top,text=f"قیمت نوشیدنی:{p_drink}تومان")
    P_drink.config(bg="white",fg="black")
    food.grid(row=5,column=4,padx=200)
    Price.grid(row=6,column=4,padx=200)
    Drink.grid(row=7,column=4,padx=200)
    P_drink.grid(row=8,column=4,padx=200)
    P_adrink=Label(top,text=f"قیمت نوشیدنی:{price+p_drink}تومان")
    P_adrink.config(bg="white",fg="black")
    P_adrink.grid(row=9,column=4,padx=200)
    number_button=tb.Button(master=top, text="می خوام شانسم را امتحان کنم", bootstyle="warning,outline",command=lambda:[top.after(2000,chance_challeng(food_name,price,drink,p_drink)),top.after(5000,lambda:top.destroy())])
    number_button.grid(row=10, column=4, padx=200)
    tabrik=Label(top,fg="black")
    tabrik.grid(row=11,column=4,padx=200)



    
    
    



