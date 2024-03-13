from tkinter import *
import tkinter as tk
from tkinter.font import Font
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import ImageTk, Image,ImageDraw
from functions import *


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

    
def create_circle_image(image_path, size):
    img = Image.open(image_path).resize((size, size))
    img = img.convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    img.putalpha(mask)
    return ImageTk.PhotoImage(img)


def home_button_hover(a):
    home_button.config(bg="red",fg="white")

def home_button_back(a):
    home_button.config(bg="black")


def iranian_food_button_hover(a):
    iranian_food_button.config(bg="red",fg="white")

def iranian_food_button_back(a):
    iranian_food_button.config(bg="black")


def fast_food_button_hover(a):
    fast_food_button.config(bg="red",fg="white")

def fast_food_button_back(a):
    fast_food_button.config(bg="black")


def chance_button_hover(a):
    chance_button.config(bg="red",fg="white")

def chance_button_back(a):
    chance_button.config(bg="black")

def drink_button_hover(a):
    drink_button.config(bg="red",fg="white")

def drink_button_back(a):
    drink_button.config(bg="black")

    

win = tb.Window(themename="pulse")
win.iconbitmap()
win.geometry("1010x600")
win.minsize(1010,600)
win.maxsize(1010,600)
win.iconbitmap("E:/uni/term5/object oriented/project/pic/resturant.ico")
win.title("Bas Food")


iconp = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
top=Toplevel()
top.config(bg="#ff3838")
top.geometry("300x200")
iconn = ImageTk.PhotoImage(iconp)
lbl=Label(top,text="سلام دوست عزیز\nبه بس فود خوش آمدید")
lbl.config(bg="#ff3838",fg="white",font="Helvetica 14 bold")
lblp=Label(top,image=iconn)
lblp.config(bg="#ff3838")
lblp.grid(row=1,column=2,padx=80)
lbl.grid(row=2,column=2,padx=80)
top.iconbitmap("E:/uni/term5/object oriented/project/pic/resturant.ico")
top.after(2000,lambda:top.destroy())

# Create a frame to hold the content
content_frame = tk.Frame(win, width=500)
content_frame.config(background="red")
content_frame.pack(expand=True, fill="both")


# Header
# Header - Black Row
black_row = tk.Frame(content_frame)
black_row.config(background="black", height=1, width=1)
black_row.grid(row=0, column=0, columnspan=7, sticky="nsew")


#menubar
icon = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((80, 80))
icon_main = ImageTk.PhotoImage(icon)
header_label = tk.Label(content_frame, image=icon_main)
header_label.config(background="black")
header_label.grid(row=0, column=0, sticky="nw")


t_icon=tk.Label(content_frame, text="Bas Food", font="@Gungsuh 14 bold")
t_icon.config(background="black",fg="red")
t_icon.grid(row=0, column=0,sticky="nw",padx=100,pady=25)


# Home button
home_button = tk.Button(content_frame, text="خانه", font="Morvarid 10 bold", command=home_button_clicked)
home_button.config(background="black")
home_button.grid(row=0, column=5, pady=20, sticky="e")

home_button.bind("<Enter>",home_button_hover)
home_button.bind("<Leave>",home_button_back)

# Iranian Foods button
iranian_food_button = tk.Button(content_frame, text="غذاهای ایرانی", font="Morvarid 10 bold", command=iranian_food_button_clicked)
iranian_food_button.config(background="black")
iranian_food_button.grid(row=0, column=4, pady=20,padx=10 ,sticky="e")

iranian_food_button.bind("<Enter>",iranian_food_button_hover)
iranian_food_button.bind("<Leave>",iranian_food_button_back)

# Fast Food button
fast_food_button = tk.Button(content_frame, text="فست فود", font="Morvarid 10 bold", command=fast_food_button_clicked)
fast_food_button.config(background="black")
fast_food_button.grid(row=0, column=3, pady=20, sticky="e")

fast_food_button.bind("<Enter>",fast_food_button_hover)
fast_food_button.bind("<Leave>",fast_food_button_back)

drink_button = tk.Button(content_frame, text="نوشیدنی",command=drink, font="Morvarid 10 bold")
drink_button.config(background="black")
drink_button.grid(row=0, column=2, pady=20, sticky="e",padx=10)

drink_button.bind("<Enter>",drink_button_hover)
drink_button.bind("<Leave>",drink_button_back)

chance_button = tk.Button(content_frame, text="شانس",command=chance_first, font="Morvarid 10 bold")
chance_button.config(background="black")
chance_button.grid(row=0, column=1, pady=20, sticky="e",padx=10)

chance_button.bind("<Enter>",chance_button_hover)
chance_button.bind("<Leave>",chance_button_back)

fast_food1_button = tk.Button(content_frame, text="", font="Morvarid 10 bold", command=fast_food_button_clicked)
fast_food1_button.config(background="black")
fast_food1_button.grid(row=0, column=6, pady=20, sticky="e")


# Customer Information - Red Row
red_row = tk.Frame(content_frame)
red_row.config(background="red", height=40, width=1)
red_row.grid(row=1, column=0, columnspan=7, sticky="ns")


customer_name_label = tk.Label(red_row)
customer_name_label.config( background="red", foreground="orange")
customer_name_label.grid(row=1, column=7,sticky="e")  # Adjusted column and added sticky option

customer_inventory_label = tk.Label(red_row)
customer_inventory_label.config( background="red", foreground="orange")
customer_inventory_label.grid(row=1, column=5, padx=100,sticky="e")  # Adjusted column and added sticky option

factor_button = tb.Button(content_frame, text="فاکتور",command=factor,bootstyle="danger,outline")
factor_button.grid(row=1, column=0, sticky="w",padx=10)



# Create a Canvas for the food items
canvas = tk.Canvas(content_frame, width=2000)
canvas.grid(row=2, column=0, columnspan=9, sticky="nsew")

# Add a vertical scrollbar to the canvas
scrollbar = tk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=2, column=6, sticky="ns")
canvas.config(yscrollcommand=scrollbar.set)

# Bind the configure event to the canvas
canvas.bind("<Configure>", on_configure)

# Add a Frame to the Canvas
food_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=food_frame, anchor="nw", width=1500)


icon_m = Image.open("pic/bagheri fastfood site logo 1p WT BG.png").resize((200, 200))
icon_main1 = ImageTk.PhotoImage(icon_m)
header2_label = tk.Label(food_frame, image=icon_main1)
header2_label.config(background="white")
header2_label.grid(row=1, column=1, sticky="wnse")

text_label = tk.Label(food_frame, text="تو بس فود غذا خوردن\n ...رابس می کنی,نمی کنی   ", font="Morvarid 14 bold")
text_label.config(bg="white", foreground="orange")
text_label.grid(row=1, column=2, sticky="wnse")

# Create circular images
size = 100
chengeh_circle = create_circle_image("pic/chengeh.jpg", size)
pitza_circle = create_circle_image("pic/pitza.jpg", size)
noshabeh_circle = create_circle_image("pic/noshbeh.jpg", size)
dogh_circle = create_circle_image("pic/doogh.jpg", size)

# Label for chengeh
label_chengeh = tb.Label(master=food_frame, image=chengeh_circle, width=size)
label_chengeh.grid(row=1, column=3, columnspan=1, sticky="ns", padx=10)

# Label for pitza
label_pitza = tb.Label(master=food_frame, image=pitza_circle, width=size)
label_pitza.grid(row=1, column=4, columnspan=1, sticky="ns", padx=10)

# Label for noshabeh
label_noshabeh = tb.Label(master=food_frame, image=noshabeh_circle, width=size)
label_noshabeh.grid(row=1, column=5, columnspan=1, stick="ns", padx=10)

# Label for dogh
label_dogh = tb.Label(master=food_frame, image=dogh_circle, width=size)
label_dogh.grid(row=1, column=6, columnspan=1, stick="ns", padx=10)


# Food items (First row)
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

food_label = tk.Label(master=food_frame, text="غداهای ایرانی", font="Helvectica 18 bold")
food_label.config(fg="black")
food_label.grid(row=2, column=6, pady=0, sticky="ns")


price_zeresh = tb.Label(master=food_frame, text="   زرشک پلو با مرغ\nقیمت: ۱۰۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_zeresh.grid(row=4, column=1, pady=(0, 20), padx=10)

label_zeresh = tb.Label(master=food_frame, image=image1, width=50)
label_zeresh.grid(row=3, column=1, pady=(8, 20), padx=10)

zeresh_o_button = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="warning,outline",command=iranian_food_button_clicked)
zeresh_o_button.grid(row=5, column=1, pady=10)

# Additional information for ghormeh
label_ghormeh = tb.Label(master=food_frame, image=image2, width=50)
label_ghormeh.grid(row=3, column=2, pady=(8, 20), padx=10)

price_ghormeh = tb.Label(master=food_frame, text="        قرمه سبزی \n قیمت: ۱۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_ghormeh.grid(row=4, column=2, pady=(0, 20), padx=10)

ghormeh_o_button = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="warning,outline",command=iranian_food_button_clicked)
ghormeh_o_button.grid(row=5, column=2, pady=10)

# Additional information for geymeh
label_gheymeh = tb.Label(master=food_frame, image=image3, width=50)
label_gheymeh.grid(row=3, column=3, pady=(8, 20), padx=10)

price_gheymeh = tb.Label(master=food_frame, text="   قیمه با سیب زمینی\nقیمت: ۲۰۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_gheymeh.grid(row=4, column=3, pady=(0, 20), padx=10)

gheymeh_o_button = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="warning,outline",command=iranian_food_button_clicked)
gheymeh_o_button.grid(row=5, column=3, pady=10)


price_kebab = tb.Label(master=food_frame, text="     کباب با مخلفات\nقیمت: 40000 تومان", font="Morvarid 12 bold", bootstyle="default")
price_kebab.grid(row=4, column=4, pady=(0, 20), padx=20)

label_kebab = tb.Label(master=food_frame, image=image4, width=50)
label_kebab.grid(row=3, column=4, pady=(8, 20), padx=10)

kebab_o_button = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="warning,outline",command=iranian_food_button_clicked)
kebab_o_button.grid(row=5, column=4, pady=10)

price_gogeh = tb.Label(master=food_frame, text="     جوجه با مخلفات \nقیمت: 1۰۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_gogeh.grid(row=4, column=5, pady=(0, 20), padx=20)

label_gogeh = tb.Label(master=food_frame, image=image5, width=50)
label_gogeh.grid(row=3, column=5, pady=(8, 20), padx=10)

gogeh_o_button = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="warning,outline",command=iranian_food_button_clicked)
gogeh_o_button.grid(row=5, column=5, pady=10)

# Food items (Second row)
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

food_label_2 = tk.Label(master=food_frame, text="فست فود", font="Helvectica 18 bold")
food_label_2.config(fg="red")
food_label_2.grid(row=6, column=6, pady=10, sticky="ns")

# Additional information for the chicken
price_chicken = tb.Label(master=food_frame, text="        مرغ کنتاکی\nقیمت: ۲۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_chicken.grid(row=9, column=1, pady=(0, 20), padx=10)

label_chicken = tb.Label(master=food_frame, image=image6, width=50)
label_chicken.grid(row=7, column=1, pady=(8, 20), padx=10)

order_button_chicken = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="danger,outline")
order_button_chicken.grid(row=10, column=1, pady=10)

# Additional information for the pizza
price_Pizza = tb.Label(master=food_frame, text="           پیتزا\nقیمت: ۳۰۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_Pizza.grid(row=9, column=2, pady=(0, 20), padx=10)

label_Pizza = tb.Label(master=food_frame, image=image7, width=50)
label_Pizza.grid(row=7, column=2, pady=(8, 20), padx=10)

order_button_Pizza = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="danger,outline",command=fast_food_button_clicked)
order_button_Pizza.grid(row=10, column=2, pady=10)

# Additional information for the burger
price_hamburger = tb.Label(master=food_frame, text="          همبرگر\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_hamburger.grid(row=9, column=3, pady=(0, 20), padx=10)

label_hamburger = tb.Label(master=food_frame, image=image8, width=50)
label_hamburger.grid(row=7, column=3, pady=(8, 20), padx=10)

order_button_hamburger = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="danger,outline",command=fast_food_button_clicked)
order_button_hamburger.grid(row=10, column=3, pady=10)

price_cheezburger = tb.Label(master=food_frame, text="          چیزبرگر\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_cheezburger.grid(row=9, column=4, pady=(0, 20), padx=10)

label_cheesburger = tb.Label(master=food_frame, image=image9, width=50)
label_cheesburger.grid(row=7, column=4, pady=(8, 20), padx=10)

order_button_cheesburger = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="danger,outline",command=fast_food_button_clicked)
order_button_cheesburger.grid(row=10, column=4, pady=10)

label_hotdog = tb.Label(master=food_frame, image=image10, width=50)
label_hotdog.grid(row=7, column=5, pady=(8, 20), padx=10)

price_hotdog = tb.Label(master=food_frame, text="          هات داگ\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_hotdog.grid(row=9, column=5, pady=(0, 20), padx=10)

order_button_hotdog = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="danger,outline",command=fast_food_button_clicked)
order_button_hotdog.grid(row=10, column=5, pady=10)



fastFood_label = tk.Label(master=food_frame, text="فست فود", font="Helvectica 18 bold")
fastFood_label.config(fg="black")
fastFood_label.grid(row=6, column=6, pady=10, sticky="ns")

# Additional information for the chicken
price_chicken = tb.Label(master=food_frame, text="        مرغ کنتاکی\nقیمت: ۲۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_chicken.grid(row=9, column=1, pady=(0, 20), padx=10)

label_chicken = tb.Label(master=food_frame, image=image6, width=50)
label_chicken.grid(row=7, column=1, pady=(8, 20), padx=10)

order_button_chicken = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="danger,outline",command=fast_food_button_clicked)
order_button_chicken.grid(row=10, column=1, pady=10)

# Additional information for the pizza
price_Pizza = tb.Label(master=food_frame, text="           پیتزا\nقیمت: ۳۰۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_Pizza.grid(row=9, column=2, pady=(0, 20), padx=10)

label_Pizza = tb.Label(master=food_frame, image=image7, width=50)
label_Pizza.grid(row=7, column=2, pady=(8, 20), padx=10)

order_button_Pizza = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="danger,outline",command=fast_food_button_clicked)
order_button_Pizza.grid(row=10, column=2, pady=10)

nooshabeh = Image.open("pic/nooshidan_nooshabeh.jpg").resize((100, 100))
image11 = ImageTk.PhotoImage(nooshabeh)

ddogh = Image.open("pic/ddogh.jpg").resize((100, 100))
image12 = ImageTk.PhotoImage(ddogh)

delester = Image.open("pic/delester.jpg").resize((100, 100))
image13 = ImageTk.PhotoImage(delester)


food_label_2 = tk.Label(master=food_frame, text="نوشیدنی", font="Helvectica 18 bold")
food_label_2.config(fg="black")
food_label_2.grid(row=11, column=6, pady=10, sticky="ns")
# Additional information for the burger
price_nooshabeh = tb.Label(master=food_frame, text="          نوشابه\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_nooshabeh.grid(row=13, column=3, pady=(0, 20), padx=10)

label_nooshabeh = tb.Label(master=food_frame, image=image11, width=50)
label_nooshabeh.grid(row=12, column=3, pady=(8, 20), padx=10)

order_button_nooshabeh = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="info,outline",command=drink)
order_button_nooshabeh.grid(row=14, column=3, pady=10)


price_Dough = tb.Label(master=food_frame, text="             دوغ\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_Dough.grid(row=13, column=2, pady=(0, 20), padx=10)

label_Dough = tb.Label(master=food_frame, image=image12, width=50)
label_Dough.grid(row=12, column=2, pady=(8, 20), padx=10)

order_button_Dough = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="info,outline",command=drink)
order_button_Dough.grid(row=14, column=2, pady=10)


price_beer = tb.Label(master=food_frame, text="             دلستر\nقیمت: ۳۵۰۰۰ تومان", font="Morvarid 12 bold", bootstyle="default")
price_beer.grid(row=13, column=4, pady=(0, 20), padx=10)

label_beer = tb.Label(master=food_frame, image=image13, width=50)
label_beer.grid(row=12, column=4, pady=(8, 20), padx=10)

order_button_beer = tb.Button(master=food_frame, text="سفارش دادن", bootstyle="info,outline",command=drink)
order_button_beer.grid(row=14, column=4, pady=10)

# Configure row and column weights for centering
content_frame.columnconfigure(0, weight=1)
content_frame.rowconfigure(1, weight=0)  # Remove fixed height for the red row
content_frame.rowconfigure(2, weight=1)
win.mainloop()