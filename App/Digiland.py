from tkinter import *
from tkinter import messagebox
import sys
from random import choice
from random import randint

class Question:

    def __init__(self, question, answer, damage):
        self.question= question
        self.answer = answer
        self.damage = damage

class Character:
    def __init__(self, tries, coins):
        self.name = ""
        self.age = ""
        self.shape = ""
        self.tries = tries
        self.coins = coins


def exit():
    exits = messagebox.askquestion('Exit', 'Are you sure you want to leave Digiland?', icon='warning')
    if exits == 'yes':
        sys.exit()
    else:
        pass

def quit():
    exits = messagebox.askquestion('Quit', 'Are you sure you want to leave Digiland without saving?', icon='warning')
    if exits == 'yes':
        sys.exit()
    else:
        pass


def save (username, places, items, coins, tries, water):
    with open("save_please.txt", "w") as file_object:
        file_object.write("name\n")
        file_object.write(username + "\n")
        file_object.write("visited\n")
        join_place = ",".join(places)
        join_place += "\n"
        file_object.write(join_place)
        file_object.write("items\n")
        join_it = ",".join(items)
        join_it += "\n"
        file_object.write(join_it)
        file_object.write("coins\n")
        num_coins = str(coins)
        num_coins += "\n"
        file_object.write(num_coins)
        file_object.write("tries\n")
        num_trys = str(tries)
        num_trys += "\n"
        file_object.write(num_trys)
        file_object.write("fountain\n")
        amount_water = str(water)
        amount_water += "\n"
        file_object.write(amount_water)
    file_object.close()

# No items are collected in add and sub land, so this version is used ot avoid saving an empty string in items, as this effects the functionality
# of the view_items function

def save_1 (username, places, coins, tries, water):
    with open("save_please.txt", "w") as file_object:
        file_object.write("name\n")
        file_object.write(username + "\n")
        file_object.write("visited\n")
        join_place = ",".join(places)
        join_place += "\n"
        file_object.write(join_place)
        file_object.write("coins\n")
        num_coins = str(coins)
        num_coins += "\n"
        file_object.write(num_coins)
        file_object.write("tries\n")
        num_trys = str(tries)
        num_trys += "\n"
        file_object.write(num_trys)
        file_object.write("fountain\n")
        amount_water = str(water)
        amount_water += "\n"
        file_object.write(amount_water)
    file_object.close()


def load_name():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    name = ""
    read_name = False
    for line in lines:
        line = line.strip()
        if read_name:
            name = line
            read_name = False

        if line == "name":
            read_name = True
    file_object.close()
    return name



def load_items():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    item = []
    read_items = False
    for line in lines:
        line = line.strip()
        if read_items:
            item = line.split(",")
            read_items = False

        if line == "items":
            read_items = True
    file_object.close()
    return item


def load_places():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    place = []
    read_place = False
    for line in lines:
        line = line.strip()
        if read_place:
            place = line.split(",")
            read_place = False

        if line == "visited":
            read_place = True
    file_object.close()
    return place


def load_coins():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    coins = ""
    read_coins = False
    for line in lines:
        line = line.strip()
        if read_coins:
            coins = line
            read_coins = False

        if line == "coins":
            read_coins = True
    file_object.close()
    return int(coins)


def load_tries():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    tries = ""
    read_tries = False
    for line in lines:
        line = line.strip()
        if read_tries:
            tries = line
            read_tries = False

        if line == "tries":
            read_tries = True
    file_object.close()
    return int(tries)


def load_fountain():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    fountain = ""
    read_fount = False
    for line in lines:
        line = line.strip()
        if read_fount:
            fountain = line
            read_fount = False

        if line == "fountain":
            read_fount = True
    if fountain =="":
        fountain= 0
    else:
        pass
    file_object.close()
    return int(fountain)

#the below functions are used in the menu bar:

def view_items():
    items= load_items()
    if len(items)==0:
        messagebox.showinfo(title= "Items", message= "You don't have any items in your bag yet!\nCarry on playing to see what you can find.")
    elif len(items) ==1:
        messagebox.showinfo(title="Items",
                            message=f"You have a {items[0]} in your bag")
    elif len(items) == 2:
        messagebox.showinfo(title="Items",
                            message=f"You have a {items[0]} and a {items[1]} in your bag")
    elif len(items) ==3:
        messagebox.showinfo(title="Items",
                            message=f"You have a {items[0]}, a {items[1]} and a{items[2]}  in your bag")


def view_places():
    places= load_places()
    if not places:
        messagebox.showinfo(title= "Places visited", message= "You haven't been anywhere yet!")
    elif "sub-land" not in places:
        messagebox.showinfo(title="Places visited",
                            message="So far you have visited Add-land.")
    elif "div-land" not in places:
        messagebox.showinfo(title="Places visited",
                            message="You'be been to Add-land and Sub-land.")

    elif "mult-land" not in places:
        messagebox.showinfo(title="Places visited",
                            message="You'be been to Add-land, Sub-land and Div-land.")

def view_water():
    water= load_fountain()
    if water == 0:
        messagebox.showinfo(title="Water level", message="You haven't won any water for the fountain yet.")
    else:
        messagebox.showinfo(title="Water level", message=f"You have won {water} litres of water for the fountain")

#used to update the coin and try tallies
def update():
    coin_count.set(f'Coins: {user.coins}')
    try_count.set(f'Tries: {user.tries}')

#used to update the number of coins so they can be reloaded
def add_coins(num):
    user.coins += num

#used to update the number of tries
def add_tries(num):
    user.tries += num

#adds a place to the list of visited places
def add_place(place):
    places.append(place)

#adds a certain amount of water to the fountain level
def add_water (water):
    global fountain_water
    fountain_water += water

#adds an item to the list of items
def add_item(item):
    items.append(item)

#removes an item
def remove_item(item):
    items.remove(item)

#the functions below update the textboxes in the different frames:

def add_update_text (text):
    output.set(f'{text}')

def sub_update_text(text):
    sub_output.set(f'{text}')

def div_update_text(text):
    div_output.set(f'{text}')
    
def mult_update_text(text):
    mult_output.set(f'{text}')

# removes a widget from the frame
def remove(widget):
    widget.grid_forget()

#adds a widget
def show(widget):
    widget.grid(row=2, column=0, pady=10)

#adds a widget one column along from the function above
def show_second(widget):
    widget.grid(row=3, column=0, pady=10)

#shows the 'next round' button in the battle frames
def show_next(widget):
    widget.grid(row=3, column=2, pady=10)

# the functions below create questions used in the battle frames:

def add_question():
    num1 = randint(20, 100)
    num2 = randint(20, 100)
    addquestion = Question(f"What is {num1} + {num2}?", num1 + num2, 2)
    return addquestion

def add_cal_question():
    num3 = randint(1, 30)
    num4 = randint(1, 30)
    calquestion = Question(f"What is {num3} + {num4}?", num3 + num4, 2)
    return calquestion

def sub_question():
    num1 = randint(20, 100)
    num2 = randint(20, 100)
    subquestion = Question(f"What is {num1} - {num2}?", num1 - num2, 2)
    return subquestion

def sub_cal_question():
    num3 = randint(1, 30)
    num4 = randint(1, 30)
    subquestion = Question(f"What is {num3} - {num4}?", num3 - num4, 2)
    return subquestion

def div_question():
    numbers0 = [80, 96, 128, 144, 160, 176]
    numbers1 = [4, 8, 16]
    num1 = choice(numbers0)
    num2 = choice(numbers1)
    divquestion = Question(f"What is {num1} / {num2}?: ", num1 / num2, 2)
    return divquestion


def div_cal_question():
    numbers2 = [4, 8, 12, 16, 20, 24, 28, 32]
    numbers3 = [2, 4]
    num3 = choice(numbers2)
    num4 = choice(numbers3)
    divquestion_cal = Question(f"What is {num3} / {num4}?: ", num3 / num4, 1)
    return divquestion_cal

def mult_question():
    num1 = randint(5, 20)
    num2 = randint(5, 20)
    multquestion = Question(f"What is {num1} x {num2}?", num1 * num2, 2)
    return multquestion

def mult_cal_question():
    num3 = randint(1, 10)
    num4 = randint(1, 10)
    multquestion_cal = Question(f"What is {num3} x {num4}?", num3 * num4, 2)
    return multquestion_cal

#the class below is for the main frame of the app:

class Digilandapp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self,*args,**kwargs)
        Tk.config(self,bg='#8DEFFF')
        Tk.geometry(self,"{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self,"./d.ico")
        Tk.title(self,"Digiland")

        container= Frame(self,bg='#8DEFFF')
        container.grid(row=0, column= 0)
        container.grid_columnconfigure(0, weight= 1)
        container.grid_rowconfigure(0, weight=1)

        # the code below configures the other frames
        self.frames={}
        for F in (MenuPage, UserGuide, NewGame,GameOver, AddLand, AddBattle, AddWin, SubLand, SubBattle,
                  SubWin, DivLand, DivBattle, DivWin, MultLand, MultBattle, WinGame, LoadGame):
            frame= F(container, self)
            self.frames[F]= frame
            frame.config(bg='#8DEFFF')
            frame.grid(row=0, column=0, sticky="nsew")

            # the code below creates the menu:
            main_menu = Menu(self)
            self.configure(menu=main_menu)

            options = Menu(main_menu)
            main_menu.add_cascade(label="Options", menu=options)
            options.add_command(label="View your items", command=view_items)
            options.add_command(label="View places visited", command=view_places)
            options.add_command(label="View water level", command=view_water)

            leave = Menu(main_menu)
            main_menu.add_cascade(label="Exit", menu=leave)
            leave.add_command(label="Quit without saving", command=quit)

        #sets the opening frame as the Menu page:
        self.show_page(MenuPage)

        # sets the functionality of the 'X' button:
        def changex():
            quit()

        self.protocol('WM_DELETE_WINDOW', changex)

    # used to control which frame is showing:
    def show_page(self, cont):
        frame= self.frames[cont]
        frame.tkraise()

    #used to access the functions within a given frame:
    def get_page(self, page_class):
        return self.frames[page_class]


class MenuPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller= controller
        self.photo= PhotoImage(file= "./menu.PNG")


        title = Label(self, text="DIGILAND", font=("ms sans serif", 65), bg='#8DEFFF')
        title.grid(row = 1, column= 1 , columnspan= 3, padx= 400)


        btn1 = Button(self, text="Start a new game", font=("ariel", 15), borderwidth=4,command= lambda: controller.show_page(NewGame))
        btn1.grid(row= 2, column= 1, pady= 120)
        btn2 = Button(self, text="Load a previous game", font=("ariel", 15), borderwidth=4,command= lambda: controller.show_page(LoadGame))
        btn2.grid(row= 2, column= 2, pady=120)
        btn3 = Button(self, text="Learn about Digiland", font=("ariel", 15), borderwidth=4, command= lambda: controller.show_page(UserGuide))
        btn3.grid(row=2, column= 3,pady=120)

        canvas = Canvas(self,width= 1200, height=400,bg= '#8DEFFF',highlightthickness=0)
        canvas.grid(row=5, column= 1, columnspan=4, pady=20, padx=150)
        img= self.photo
        image = canvas.create_image(0,0, image=img, anchor= NW)



class UserGuide(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.photo = PhotoImage(file="./Orgs.PNG")
        title = Label(self, text="About Digiland", font=("ms sans serif", 25), bg='#8DEFFF')
        title.grid(row = 0, column= 0 , columnspan= 2)

        text = Text(self, height=15, width=210)
        text.tag_configure('font', font=("ariel, 14"))
        intro = """Digiland was once a land of prosperity and knowledge, where numbers and functions walked together hand-in hand.\nHowever, it has been invaded by enemies from the land of Zorg who have been stealing water from the Fountain of Knowledge,\nmaking the inhabitants forget their sums! You have been brought to fight the enemies and refill the Fountain of Knowledge.\nYou need to visit the 4 countries Add-land, Sub-land, Div-land and Mult-land to conquer the enemies that have landed there.\nTo win the battles, you will need to use your math’s knowledge to answer questions.\nEvery set of questions you get right will win back some water for the fountain.\nDuring each battle, you will have a certain number of chances to answer a question correctly.\nYou will be given the chance to collect gold coins along the way which can be used to buy the help of the Calculator,\nmaking the questions easier for you if you get stuck."""
        text.insert(INSERT, intro, 'font')
        text.grid(row=2, column=0, columnspan=3, padx=(10,10))

        canvas = Canvas(self, width=1200, height=300, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=5, column= 0, columnspan=3)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)

        menu = Button(self, text="Return to Menu", font=("ariel, 15"), command=lambda: controller.show_page(MenuPage))
        menu.grid(row=6, column=0, sticky = SW)


# The if/else statement is based on what lands are saved. If they havent been to sub-land yet,
#the game will start there etc.
class LoadGame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global places

        places = load_places()

        if "add-land" not in places:
            output= Label(self, text="Sorry, there is no previous game to load.\nPlease return to the main menu to start a new game.",font=("ariel, 20"),bg='#8DEFFF', justify=LEFT)
            output.grid(row=0, column=1, columnspan=3, pady=10, padx=10)
            menu = Button(self, text="Return to Menu", font=("ariel, 15"),
                          command=lambda: controller.show_page(MenuPage))
            menu.grid(row=2, column=1)
        else:
            name = load_name()
            coins = load_coins()
            items = load_items()
            tries = load_tries()
            fountain = load_fountain()
            user.name = name
            user.coins= coins
            user.tries= tries
            update()

            title = Label(self, text=f"Welcome back, {user.name}", font=("ms sans serif", 40), bg='#8DEFFF')
            title.grid(row=0, column=1, columnspan=2, padx=(350,0))

            coin_label = Label(self, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                               relief="ridge")
            coin_label.grid(row=0, column=3, sticky=NE, padx=350)

            try_label = Label(self, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                              relief="ridge")
            try_label.grid(row=0, column=3, sticky=NE, padx=350, pady=30)


            if "sub-land" not in places:
                message= Label(self, text="The next land you need to visit is Sub-land.\nAre you ready to go?",font=("ariel", 14), bg='#8DEFFF')
                message.grid(row=1, column=2,pady=(100,10))
                button= Button(self, text="I'm ready!", font=("ariel", 14), command= lambda: [update(),controller.get_page(SubLand).update_user(),controller.show_page(SubLand)])
                button.grid(row=2, column=2 )
                button2= Button(self, text="Return to Menu", font=("ariel", 14),command= lambda: controller.show_page(MenuPage))
                button2.grid(row=3, column=2, pady=10)

            elif "div-land" not in places:
                message = Label(self, text="The next land you need to visit is Div-land.\nAre you ready to go?",
                                font=("ariel", 14), bg='#8DEFFF')
                message.grid(row=1, column=2,pady=(100,10))
                button = Button(self, text="I'm ready!", font=("ariel", 14), command= lambda: [update(),controller.get_page(DivLand).update_user(),controller.show_page(DivLand)])
                button.grid(row=2, column=2)
                button2 = Button(self, text="Return to Menu", font=("ariel", 14),
                                 command=lambda: controller.show_page(MenuPage))
                button2.grid(row=3, column=2, pady=10)

            elif "mult-land" not in places:
                message = Label(self, text="The next land you need to visit is Mult-land.\nAre you ready to go?",
                                font=("ariel", 14), bg='#8DEFFF')
                message.grid(row=1, column=2,pady=(100,10))
                button = Button(self, text="I'm ready!", font=("ariel", 14), command= lambda: [update(),controller.get_page(MultLand).update_user(),controller.show_page(MultLand)])
                button.grid(row=2, column=2)
                button2 = Button(self, text="Return to Menu", font=("ariel", 14),
                                 command=lambda: controller.show_page(MenuPage))
                button2.grid(row=3, column=2, pady=10)


class NewGame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        global user
        user = Character(3, 5)
        global places
        global items
        global fountain_water
        items = []
        fountain_water = 0

        # allocates a special bonus depending on which shape they choose
        def bonus():
            if user.shape == "Star":
                user.coins += 5  # if star is chosen, the player will start with 5 extra coins
            elif user.shape== "Square":
                user.coins += 10
                  # if the circle is chosen, the player starts with a spade in their bag
            elif user.shape == "Triangle":
                user.tries += 1  # if the triangle is chosen, they will start with an extra free go
            else:
                user.tries +=2
                  # if a square is chosen they start with 10 extra coins
            global places
            places = []
            update()

        title = Label(self, text="Welcome!", font=("ms sans serif", 35), bg='#8DEFFF')
        title.grid(row = 1, column= 2, columnspan= 3, padx= (100,500))

        ask_name= Label(self, text="What's your name?", font=("ariel", 14),bg='#8DEFFF')
        ask_name.grid(row= 2, column= 1, pady= (110, 10), sticky = E)
        global name
        name= Entry(self, width= 20,font=("ariel", 14))
        name.grid(row=2, column= 2, pady=(110, 10))


        ask_age = Label(self, text="How old are you?", font=("ariel", 14), bg='#8DEFFF')
        ask_age.grid(row=3, column=1, pady=10, sticky = E)
        global age
        age = Entry(self, width=20, font=("ariel", 14))
        age.grid(row=3, column=2, pady=10)


        ask_shape = Label(self, text="To enter Digiland, you must choose a shape:", font=("ariel", 14), bg='#8DEFFF')
        ask_shape.grid(row=4, column=1,pady=10, sticky = E)
        global chosen
        chosen= StringVar()
        shape = OptionMenu(self, chosen,  "Circle", "Square", "Star", "Triangle")
        shape.config(font=("ariel", 14), width=17)
        shape.grid(row=4, column=2,pady=10)

        # creates the pop-up box to make sure thye are happy to delete any previous game
        def check():
            message= messagebox.askquestion(title="Are you sure?", message="Are you sure you want to start a new game?\nAny previous details will be erased.")
            if message== "yes":
                submit_details()
            else:
                pass

        #deletes the content in the .txt file and takes the user input
        #opens a pop-up box to confirm their bonus then leads to add-land
        def submit_details():
            f = open('save_please.txt', 'r+')
            f.truncate(0)
            user.name = name.get()
            user.age = age.get()
            user.shape = chosen.get()
            user.coins= 5
            user.tries = 3
            bonus()
            global message
            if user.shape== "Star":
                message ="As you chose a star, you start with 5 extra gold coins! Let's get going to Add-Land."
            elif user.shape== "Square":
                message= "As you chose a Square, you start with 10 extra gold coins! Let's get going to Add-Land."
            elif user.shape== "Triangle":
                message= "As you chose a triangle , you get to start the game with an extra free go! Let's get going to Add-Land."
            else:
                message= "As you chose a Circle, you get to start the game with two extra go's! Let's get going to Add-Land. "
            messagebox.showinfo(title="Bonus!", message = message)
            controller.get_page(AddLand).update_user()
            age.delete(0, "end")
            name.delete(0, "end")
            controller.show_page(AddLand)




        submit= Button(self, text="Submit",font=("ariel, 15"), command = check)
        submit.grid(row=5, column= 2, pady= (40,10))


        menu = Button(self, text="Return to Menu", font=("ariel, 15"), command=lambda: controller.show_page(MenuPage))
        menu.grid(row=6, column=2)


class AddLand(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.photo= PhotoImage(file="./AddLand.png")
        global user

        frame1= Frame(self, bg='#8DEFFF')
        frame1.grid(row=0, column=0)

        frame2 = Frame(self, bg='#8DEFFF')
        frame2.grid(row=1, column=0)

        global coin_count
        coin_count = StringVar(self, f'Coins: {user.coins}')
        coin_label = Label(frame1, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth= 5,relief= "ridge")
        coin_label.grid(row=0, column=3, sticky= NE, padx= 190)

        global try_count
        try_count = StringVar(self, f'Tries: {user.tries}')
        try_label = Label(frame1, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF',borderwidth= 5, relief= "ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=190, pady= 30)


        canvas = Canvas(frame1, width=400, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=1, columnspan=2, padx= (500,100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor= NW)

        global output
        output=StringVar()
        self.output_box = Label(frame2, textvariable= output, font=("ariel, 14"), bg= "white", justify="left")
        self.output_box.grid(row=0, column=0)

        button1= Button(frame2, text="Continue",font=("ariel", 14), command= lambda: [add_update_text('Oh no! An Eazorg has crept up behind you!\nIt\'s time for your first battle!!'),remove(button1),show(button2)])
        button1.grid(row=2, column=0, pady=10)

        button2 = Button(frame2, text="Let's battle!",font=("ariel", 14), command= lambda: [update(),controller.show_page(AddBattle)])



        remove(button2)

     #this is called just before the frame is raised ot update the text box to the text below:
    def update_user(self):
        add_update_text(f'You arrive safely in Add-Land.\nThe Eazorgs are roaming here, so keep an eye out {user.name}.\nYou carry on past some strange looking trees...')


class AddBattle(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self,parent)
        self.controller = controller
        self.photo= PhotoImage(file="./eazorg.png")
        global user


        coin_label = Label(self, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                           relief="ridge")
        coin_label.grid(row=0, column=3, sticky=NE, padx=(230,0))

        try_label = Label(self, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5, relief="ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=(230,0), pady=30)


        canvas = Canvas(self, width=360, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=1, columnspan=2, padx=(500, 100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)


        global question1
        global question_box
        global cal_question1
        cal_question1 = add_cal_question()
        question1= add_question()
        question_box1= Label(self, text= question1.question,font=("ariel, 16"), bg='#8DEFFF')
        question_box1.grid(row=1,column=2)

        global answer_box
        answer_box=Entry(self,width= 20,font=("ariel", 14))
        answer_box.grid(row=2,column=2)

        #This passes the answer of a question if the calculator is used:
        def check_cal_answer(question, question_box, next_round,submit_button, cal_question):
            remove(submit_button)
            global answer_box
            try:
                answer= int(answer_box.get())
            except ValueError:
                message= messagebox.showinfo(title="Error", message="You must enter a whole number")
                answer_box.delete(0,"end")
                submit_button = Button(self, text="Submit", font=("ariel", 14),
                                       command=lambda: check_cal_answer(question, question_box, next_round,
                                                                        submit_button, cal_question))
                submit_button.grid(row=3, column=2, pady=10)
                return
            if answer!= cal_question.answer:
                user.tries -= 1
                update()
                if user.tries > 0:
                    reply = f"That was wrong, you have {user.tries} tries left!\n{cal_question.question} "
                    question_box["text"] = reply
                    answer_box = Entry(self, width=20, font=("ariel", 14))
                    answer_box.grid(row=2, column=2)
                    submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_cal_answer(question, question_box, next_round,
                                                                        submit_button, cal_question))
                    submit_button.grid(row=3, column=2, pady=10)
                else:
                    controller.show_page(GameOver)
            else:
                reply = "That was right! Click next round."
                question_box["text"] = reply
                answer_box.delete(0, 'end')
                remove(submit_button)
                show_next(next_round)

        #this takes the answer given and checks it to see if it is correct or not.
        #If it isn't, if they have enough coins they are offered the use of the calculator
        #if it is, they go on to the next round.
        def check_answer(question, question_box, next_round, submit_button, cal_question):
            global answer_box
            remove(submit_button)
            try:
                answer= int(answer_box.get())
            except ValueError:
                messagebox.showinfo(title="Error", message="You must enter a whole number")
                answer_box.delete(0,"end")
                submit_button = Button(self, text="Submit", font=("ariel", 14),
                                       command=lambda: check_answer(question, question_box, next_round,
                                                                        submit_button, cal_question))
                submit_button.grid(row=3, column=2, pady=10)
                return
            if answer!= question.answer:
                user.tries -= 1
                update()
                if user.tries > 0:
                    if user.coins >= 8:
                        message= messagebox.askquestion("Calculator", "That was wrong, would you like to use the calculator and spend 8 gold coins?")
                        if message == 'yes':
                            user.coins -= 8
                            update()
                            print(user.coins)
                            reply = f"Ok, here's an easier question.\n{cal_question.question}"
                            question_box["text"] = reply
                            answer_box = Entry(self, width=20, font=("ariel", 14))
                            answer_box.grid(row=2, column=2)
                            submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                   command=lambda: check_cal_answer(question, question_box, next_round,
                                                                                submit_button, cal_question))
                            submit_button.grid(row=3, column=2, pady=10)
                        else:
                            answer_box.delete(0,'end')
                            submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                   command=lambda: check_answer(question, question_box,
                                                                                    next_round,
                                                                                    submit_button, cal_question))
                            submit_button.grid(row=3, column=2, pady=10)
                    else:
                        reply = f"That was wrong, you have {user.tries} tries left!\n{question.question} "
                        question_box["text"] = reply
                        answer_box = Entry(self, width=20, font=("ariel", 14))
                        answer_box.grid(row=2, column=2)
                        submit_button = Button(self, text="Submit", font=("ariel", 14), command= lambda: check_answer(question, question_box, next_round,submit_button, cal_question))
                        submit_button.grid(row=3, column=2,pady=10)
                else:
                    controller.show_page(GameOver)
            else:
                reply= "That was right! Click next round."
                question_box["text"]= reply
                answer_box.delete(0,'end')
                show_next(next_round)
                remove(submit_button)

        #allocates a question for the second round
        def round_two():
            remove(next_round_1)
            remove(question_box1)
            global question_box2
            question2= add_question()
            cal_question2= add_cal_question()
            question_box2 = Label(self, text=question2.question, font=("ariel, 16"), bg='#8DEFFF')
            question_box2.grid(row=1, column=2)
            submit_button = Button(self, text="Submit", font=("ariel", 14), command= lambda:check_answer(question2, question_box2, next_round_2,submit_button, cal_question2))
            submit_button.grid(row=3, column=2,pady=10)

        #allocates a question for the third and final round
        def round_three():
            remove(next_round_2)
            remove(question_box2)
            question3= add_question()
            cal_question3 = add_cal_question()
            question_box3 = Label(self, text=question3.question, font=("ariel, 16"), bg='#8DEFFF')
            question_box3.grid(row=1, column=2)
            submit_button = Button(self, text="Submit", font=("ariel", 14), command= lambda:check_answer(question3, question_box3, next_round_3,submit_button, cal_question3))
            submit_button.grid(row=3, column=2,pady=10)

        global submit_button
        submit_button=Button(self, text="Submit",font=("ariel", 14), command= lambda: check_answer(question1, question_box1,next_round_1,submit_button, cal_question1))
        submit_button.grid(row=3, column=2, pady=10)

        global next_round_1
        next_round_1= Button(self, text="Next round",font=("ariel", 14), command= round_two)


        global next_round_2
        next_round_2 = Button(self, text="Next round", font=("ariel", 14), command=round_three)


        global next_round_3
        next_round_3 = Button(self, text="Next round", font=("ariel", 14), command= lambda: [update(),controller.show_page(AddWin)])



class AddWin(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller

        title = Label(self, text="Congratulations!", font=("ms sans serif", 65), bg='#8DEFFF')
        title.grid(row=1, column=1, columnspan=3, padx=400)

        text= Label(self, text= "You defeated the Eazorg and won 10 litres of water for the fountain, as well as 5 gold coins and an extra free try!\nYou need 90 more litres to win. You can save and continue to carry on to Sub-land, or save and quit.", font=("ariel", 17), bg='#8DEFFF', justify= "left")
        text.grid(row=2, column=1, columnspan=3, pady= 50)

        #if they save and continue, subland is raised
        save_cont= Button(self, text= "Save and continue", font=("ariel", 14), command= lambda: [add_coins(5),
        add_tries(1), add_place("add-land"),add_water(10), update(),save_1(user.name, places, user.coins, user.tries, fountain_water),controller.get_page(SubLand).update_user(), controller.show_page(SubLand)])
        save_cont.grid(row=3, column=1, pady=50, padx=100)

        #if they save nd quit, the information is saved and exit() is called
        save_quit= Button(self, text="Save and quit", font=("ariel", 14),
                           command=lambda: [add_coins(5),
        add_tries(1),add_place("add-land"),add_water(10),update(),save_1(user.name, places, user.coins, user.tries, fountain_water),
                                            exit()])
        save_quit.grid(row=3, column=2, pady=50)



class SubLand(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.photo = PhotoImage(file="./subland.png")
        global user
        frame1 = Frame(self, bg='#8DEFFF')
        frame1.grid(row=0, column=0)

        coin_label = Label(frame1, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                           relief="ridge")
        coin_label.grid(row=0, column=3, sticky=NE, padx=350)


        try_label = Label(frame1, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5, relief="ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=350, pady=30)

        canvas = Canvas(frame1, width=200, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=0, padx=(500, 100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)

        frame2 = Frame(self,bg='#8DEFFF')
        frame2.grid(row=1, column= 0)
        global sub_output
        sub_output = StringVar()
        self.output_box = Label(frame2, textvariable= sub_output, font=("ariel, 14"), bg="white", justify="left")
        self.output_box.grid(row=1, column=0)

        button1 = Button(frame2, text="Yes", font=("ariel", 14), command=lambda: [pick_up(),
            remove(button1), remove(button2)])
        button1.grid(row=2, column=0, pady=10)

        button2 = Button(frame2, text="No", font=("ariel", 14),
                         command=lambda: [sub_update_text("You decide to leave them there- someone might be coming back for them"),remove(button1), remove(button2), show(button3)])
        button2.grid(row=3, column=0, pady=10)

        button3= Button(frame2, text="Continue", font=("ariel", 14), command= lambda: [sub_update_text("You walk past a cafe and decide to go in."
                                    "\nThere are a few scared looking people huddled round tables.\nThe Barman looks like he wants to talk\nDo you want to speak with him?"), remove(button3), show(button4), show_second(button5)])


        button4 = Button(frame2, text="Yes", font=("ariel", 14), command=lambda: [speak(),
                                                   remove(button4), remove(button5)])

        button5 = Button(frame2, text="No", font=("ariel", 14),
                         command=lambda: [
                             sub_update_text("You decide to ignore him- he doesn't look trustworthy!\nYou are about to sit down when you hear a loud crash behind you!\nA Demizorg has crashed into the cafe and it's time to fight!"),
                             remove(button4), remove(button5), show(button6)])


        button6= Button(frame2, text="Let's battle!",font=("ariel", 14),
                         command=lambda: [controller.show_page(SubBattle)])

        #If they pick up the coins, this is called:
        def pick_up():
            user.coins +=5
            update()
            sub_update_text("You found 5 coins! You add them to your collection.")
            battle= Button(frame2, text="Let's battle!",font=("ariel", 14), command= lambda: controller.show_page(SubBattle))
            battle.grid(row=2, column=0, pady=10)
            remove(battle)
            next= Button(frame2, text="Continue", font=("ariel", 14), command= lambda: [sub_update_text("Uh oh, it looks like they belonged to a Demizorg\nand he's come to investigate!\nHe's attacked you and it's time to battle!"), remove(next), show(battle)])
            next.grid(row=3, column=0, pady=10)

        #If they speak to the barman, this is called:
        def speak():
            user.coins += 10
            update()
            sub_update_text(f"'Hi, {user.name.title()}, I heard you were here to help,\n"
        "and I hear you defeated the Eazorgs over in Add-land.\n"
    "I want to give you this to say thanks (and the milkshake is on the house!'\nHe Hands you a pouch with 10 gold coins inside!\n"
    f"You say thank you and count your coins. You now have {user.coins} coins in total.")
            button1 = Button(frame2, text="continue", font=("ariel", 14), command= lambda: [sub_update_text("As you put your coins away you hear a huge crashbehind you.\nA Demizorg has entered and it's time to fight!"), remove(button1), show(button2)])
            button1.grid(row=2, column=0, pady=10)

            button2 = Button(self, text="Let's battle!", font=("ariel", 14),
                            command=lambda: controller.show_page(SubBattle))
            button2.grid(row=2, column=0, pady=10)

            remove(button2)


    def update_user(self):
        sub_update_text(
            f'You arrive in Sub-land. The talk on the town is that the Demi-zorgs have landed here, {user.name}.\nYou walk on and see some gold coins on the floor.\nDo you want to pick them up?')


class SubBattle(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self,parent)
        self.controller = controller
        self.photo= PhotoImage(file="./Demizorg.png")
        global user


        coin_label = Label(self, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                           relief="ridge")
        coin_label.grid(row=0, column=3, sticky=NE, padx=300)

        try_label = Label(self, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5, relief="ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=300, pady=30)


        canvas = Canvas(self, width=250, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=1, columnspan=2, padx=(500, 100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)

        global subquestion1
        global sub_question_box
        global sub_cal_question1
        sub_cal_question1 = sub_cal_question()
        subquestion1= sub_question()
        sub_question_box= Label(self, text= subquestion1.question,font=("ariel, 16"), bg='#8DEFFF')
        sub_question_box.grid(row=1,column=2)

        global sub_answer_box
        sub_answer_box=Entry(self,width= 20,font=("ariel", 14))
        sub_answer_box.grid(row=2,column=2)

        def check_cal_answer(question, sub_question_box, next_round,sub_submit_button, cal_question):
            global sub_answer_box
            remove(sub_submit_button)
            try:
                answer= int(sub_answer_box.get())
            except ValueError:
                message= messagebox.showinfo(title="Error", message="You must enter a whole number")
                sub_answer_box.delete(0,"end")
                sub_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_cal_answer(question, sub_question_box, next_round,
                                                                            sub_submit_button, cal_question))
                sub_submit_button.grid(row=3, column=2, pady=10)
                return
            if answer!= cal_question.answer:
                user.tries -= 1
                update()
                if user.tries > 0:
                    reply = f"That was wrong, you have {user.tries} tries left!\n{cal_question.question} "
                    question_box["text"] = reply
                    sub_answer_box = Entry(self, width=20, font=("ariel", 14))
                    sub_answer_box.grid(row=2, column=2)
                    sub_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_cal_answer(question, sub_question_box, next_round,
                                                                        sub_submit_button, cal_question))
                    sub_submit_button.grid(row=3, column=2, pady=10)
                else: controller.show_page(GameOver)
            else:
                reply = "That was right! Click next round."
                sub_question_box["text"] = reply
                sub_answer_box.delete(0, 'end')
                show_next(next_round)
                remove(sub_submit_button)


        def check_answer(question, sub_question_box, next_round, sub_submit_button, cal_question):
            global sub_answer_box
            remove(sub_submit_button)
            try:
                answer= int(sub_answer_box.get())
            except ValueError:
                message= messagebox.showinfo(title="Error", message="You must enter a whole number")
                sub_answer_box.delete(0,"end")
                sub_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_answer(question, sub_question_box,
                                                                        next_round,
                                                                        sub_submit_button,
                                                                        cal_question))
                sub_submit_button.grid(row=3, column=2, pady=10)
                return
            if answer!= question.answer:
                user.tries -= 1
                update()
                if user.tries > 0:
                    if user.coins >= 6:
                        message= messagebox.askquestion("Calculator", "That was wrong, would you like to use the calculator and spend 6 gold coins?")
                        if message == 'yes':
                            user.coins -= 6
                            update()
                            reply = f"Ok, here's an easier question.\n{cal_question.question}"
                            sub_question_box["text"] = reply
                            sub_answer_box = Entry(self, width=20, font=("ariel", 14))
                            sub_answer_box.grid(row=2, column=2)
                            sub_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                   command=lambda: check_cal_answer(question, sub_question_box, next_round,
                                                                                sub_submit_button, cal_question))
                            sub_submit_button.grid(row=3, column=2, pady=10)
                        else:
                            sub_answer_box.delete(0,'end')
                            answer_box.delete(0, 'end')
                            sub_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                      command=lambda: check_answer(question, sub_question_box,
                                                                                       next_round,
                                                                                       sub_submit_button,
                                                                                       cal_question))
                            sub_submit_button.grid(row=3, column=2, pady=10)
                    else:
                        reply = f"That was wrong, you have {user.tries} tries left!\n{question.question} "
                        sub_question_box["text"] = reply
                        sub_answer_box = Entry(self, width=20, font=("ariel", 14))
                        sub_answer_box.grid(row=2, column=2)
                        sub_submit_button = Button(self, text="Submit", font=("ariel", 14), command= lambda: check_answer(question, sub_question_box, next_round,sub_submit_button, cal_question))
                        sub_submit_button.grid(row=3, column=2,pady=10)
                else:

                    controller.show_page(GameOver)
            else:
                reply= "That was right! Click next round."
                sub_question_box["text"]= reply
                sub_answer_box.delete(0,'end')
                show_next(next_round)
                remove(sub_submit_button)


        def round_two():
            remove(sub_next_round_1)
            remove(sub_question_box)
            global sub_question_box2
            sub_question2= sub_question()
            sub_cal_question2= sub_cal_question()
            sub_question_box2 = Label(self, text=sub_question2.question, font=("ariel, 16"), bg='#8DEFFF')
            sub_question_box2.grid(row=1, column=2)
            sub_submit_button = Button(self, text="Submit", font=("ariel", 14), command= lambda:check_answer(sub_question2, sub_question_box2, sub_next_round_2,sub_submit_button, sub_cal_question2))
            sub_submit_button.grid(row=3, column=2,pady=10)

        def round_three():
            remove(sub_next_round_2)
            remove(sub_question_box2)
            sub_question3= sub_question()
            sub_cal_question3 = sub_cal_question()
            sub_question_box3 = Label(self, text=sub_question3.question, font=("ariel, 16"), bg='#8DEFFF')
            sub_question_box3.grid(row=1, column=2)
            sub_submit_button = Button(self, text="Submit", font=("ariel", 14), command= lambda:check_answer(sub_question3, sub_question_box3, sub_next_round_3,sub_submit_button, sub_cal_question3))
            sub_submit_button.grid(row=3, column=2,pady=10)

        global sub_submit_button
        sub_submit_button=Button(self, text="Submit",font=("ariel", 14), command= lambda: check_answer(subquestion1, sub_question_box ,sub_next_round_1,sub_submit_button, sub_cal_question1))
        sub_submit_button.grid(row=3, column=2, pady=10)

        global sub_next_round_1
        sub_next_round_1= Button(self, text="Next round",font=("ariel", 14), command= round_two)

        global sub_next_round_2
        sub_next_round_2 = Button(self, text="Next round", font=("ariel", 14), command=round_three)
       

        global sub_next_round_3
        sub_next_round_3 = Button(self, text="Next round", font=("ariel", 14), command= lambda: controller.show_page(SubWin))
      

class SubWin(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller

        title = Label(self, text="Congratulations!", font=("ms sans serif", 65), bg='#8DEFFF')
        title.grid(row=1, column=1, columnspan=3, padx=400)

        text= Label(self, text= "You defeated the Demizorg and won 20 litres of water for the fountain, as well as 5 gold coins and an extra free try!\nYou need 70 more litres to win. You can save and continue to carry on to Div-land, or save and quit.", font=("ariel", 17), bg='#8DEFFF', justify= "left")
        text.grid(row=2, column=1, columnspan=3, pady= 50)

        save_cont= Button(self, text= "Save and continue", font=("ariel", 14), command= lambda: [add_coins(5), add_tries(1),add_place("add-land"),add_place("sub-land"),add_water(30),update()
        ,save_1(user.name, places, user.coins, user.tries, fountain_water)
        ,controller.get_page(DivLand).update_user(), controller.show_page(DivLand)])
        save_cont.grid(row=3, column=1, pady=50, padx=100)

        save_quit= Button(self, text="Save and quit", font=("ariel", 14),
                           command=lambda: [add_coins(5), add_tries(1),add_place("add-land"),add_place("sub-land"),add_water(30),update(),save_1(user.name, places,user.coins, user.tries, fountain_water),
                                            exit()])
        save_quit.grid(row=3, column=2, pady=50)


class DivLand(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.photo=PhotoImage(file= './divland.png')

        frame1 = Frame(self, bg='#8DEFFF')
        frame1.grid(row=0, column=0)
        coin_label = Label(frame1, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                           relief="ridge")
        coin_label.grid(row=0, column=3, sticky=NE, padx=350)

        try_label = Label(frame1, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                          relief="ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=350, pady=30)

        canvas = Canvas(frame1, width=200, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=0, padx=(500, 100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)

        frame2 = Frame(self, bg='#8DEFFF')
        frame2.grid(row=1, column=0)

        def climb():
            div_update_text(f"You climb up the tree and go higher and higher until you finally reach the top!\n"
         f"A bird hops over to you and says 'Hi {user.name},It's great to meet you.\n"
        "I've heard so much about what you've achieved so far\nand I'd love to give you my golden calculator.\n"
        "It's very old so will only work once,\nbut if you're stuck you can use it to make the question easier!\n"
                            "You thank the bird, put the calculator in your bag and climb back down the tree.")
            add_item("Golden Calculator")
            fountain_water = 30
            save(user.name, places, items, user.coins, user.tries, fountain_water)
            button1 = Button(self, text="Continue",font=("ariel", 14),command= lambda:[lake(), remove(button1)])
            button1.grid(row=2, column=0, pady=10)

        def lake():
            div_update_text("You arrive at a clearing a see a huge lake.\n"
                            "You see something by the side of the lake and decide to investigate.\n"
                            "It's a key! You pick it up and add it to your bag")
            add_item("Key")
            fountain_water = 30
            save(user.name, places, items, user.coins, user.tries, fountain_water)
            button1 = Button(frame2, text="Continue", font=("ariel", 14),
                             command=lambda: [
                                 div_update_text("Just as you stand up from examining the key,\na Centorg knocks you down!\n"
                                                 "It's time to battle!"),
                                 remove(button1), show(button2)])
            button1.grid(row=2, column=0, pady=10)

            button2= Button(frame2, text="Let's battle!",font=("ariel", 14),
                         command=lambda: [controller.show_page(DivBattle)])

        global div_output
        div_output = StringVar()
        self.output_box = Label(frame2, textvariable= div_output, font=("ariel, 14"), bg="white", justify="left")
        self.output_box.grid(row=1, column=0)

        button1 = Button(frame2, text="Yes", font=("ariel", 14), command=lambda: [climb(),
                                                                                remove(button1), remove(button2)])
        button1.grid(row=2, column=0, pady=10)

        button2 = Button(frame2, text="No", font=("ariel", 14),
                         command=lambda: [
                             div_update_text("You decide to carry on."),
                             remove(button1), remove(button2), show(button3)])
        button2.grid(row=3, column=0, pady=10)

        button3= Button(frame2, text= "Continue",font=("ariel", 14),
                         command=lambda: [lake(),
                             remove(button3)])

    def update_user(self):
        div_update_text(
            f'You arrive in Div-land to be surrounded by huge redwood trees.'
            f'\nBe careful, the Centorgs are roaming here, {user.name}.'
            f'\nYou carry on through the shadowy trees and see something glittering at the top of one.'
            f'\nDo you want to climb it and see what\'s there?')


class DivBattle(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller

        self.photo = PhotoImage(file="./centorg.png")
        global user

        # close = Button(self, text="Exit", font=("ariel", 10), command=quit)
        # close.grid(column=0, row=0, sticky=NW)

        coin_label = Label(self, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                           relief="ridge")
        coin_label.grid(row=0, column=3, sticky=NE, padx=300)

        try_label = Label(self, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5, relief="ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=300, pady=30)

        canvas = Canvas(self, width=250, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=1, columnspan=2, padx=(500, 100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)

        global divquestion1
        global div_question_box
        global div_cal_question1
        div_cal_question1 = div_cal_question()
        divquestion1 = div_question()
        div_question_box = Label(self, text=divquestion1.question, font=("ariel, 16"), bg='#8DEFFF')
        div_question_box.grid(row=1, column=2)

        global div_answer_box
        div_answer_box = Entry(self, width=20, font=("ariel", 14))
        div_answer_box.grid(row=2, column=2)

        def check_cal_answer(question, div_question_box, next_round, div_submit_button, cal_question):
            global div_answer_box
            remove(div_submit_button)
            try:
                answer = int(div_answer_box.get())
            except ValueError:
                message = messagebox.showinfo(title="Error", message="You must enter a whole number")
                div_answer_box.delete(0, "end")
                div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_cal_answer(question, div_question_box, next_round,
                                                                            div_submit_button, cal_question))
                div_submit_button.grid(row=3, column=2, pady=10)
                return

            if answer != cal_question.answer:

                user.tries -= 1
                update()
                if user.tries > 0:
                    reply = f"That was wrong, you have {user.tries} tries left!\n{cal_question.question} "
                    div_question_box["text"] = reply
                    div_answer_box = Entry(self, width=20, font=("ariel", 14))
                    div_answer_box.grid(row=2, column=2)
                    div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                               command=lambda: check_cal_answer(question, div_question_box,
                                                                                next_round,
                                                                                div_submit_button, cal_question))
                    div_submit_button.grid(row=3, column=2, pady=10)
                else:
                    controller.show_page(GameOver)
            else:
                reply = "That was right! Click next round."
                div_question_box["text"] = reply
                div_answer_box.delete(0, 'end')
                show_next(next_round)
                remove(div_submit_button)


        def check_answer(question, div_question_box, next_round, div_submit_button, cal_question):
            global div_answer_box
            remove(div_submit_button)
            try:
                answer = int(div_answer_box.get())
            except ValueError:
                message = messagebox.showinfo(title="Error", message="You must enter a whole number")
                div_answer_box.delete(0, "end")
                div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_answer(question, div_question_box,
                                                                        next_round,
                                                                        div_submit_button,
                                                                        cal_question))
                div_submit_button.grid(row=3, column=2, pady=10)
                return
            if answer != question.answer:
                user.tries -= 1
                update()
                if user.tries > 0:
                    if user.coins >= 4:
                        message = messagebox.askquestion("Calculator",
                                                         "That was wrong, would you like to use the calculator and spend 4 gold coins?")
                        if message == 'yes':
                            user.coins -= 4
                            update()
                            reply = f"Ok, here's an easier question.\n{cal_question.question}"
                            div_question_box["text"] = reply
                            div_answer_box = Entry(self, width=20, font=("ariel", 14))
                            div_answer_box.grid(row=2, column=2)
                            div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: check_cal_answer(question, div_question_box,
                                                                                        next_round,
                                                                                        div_submit_button,
                                                                                        cal_question))
                            div_submit_button.grid(row=3, column=2, pady=10)
                        else:
                            div_answer_box.delete(0, 'end')
                            answer_box.delete(0, 'end')
                            div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: check_answer(question, div_question_box,
                                                                                    next_round,
                                                                                    div_submit_button,
                                                                                    cal_question))
                            div_submit_button.grid(row=3, column=2, pady=10)
                    elif "Golden Calculator" in items:
                        message= messagebox.askquestion("Golden Calculator",f"That was wrong,you have {user.tries} tries left! Do you want to use the Golden Calculator?")
                        if message == 'yes':
                            reply = f"Ok, here's an easier question.\n{cal_question.question}"
                            div_question_box["text"] = reply
                            div_answer_box = Entry(self, width=20, font=("ariel", 14))
                            div_answer_box.grid(row=2, column=2)
                            div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: [remove_item("Golden Calculator"),add_item("Empty Calculator Case"),save(user.name, places, items, user.coins, user.tries, fountain_water),check_cal_answer(question,
                                                                                        div_question_box,
                                                                                        next_round,
                                                                                        div_submit_button,
                                                                                        cal_question)])
                            div_submit_button.grid(row=3, column=2, pady=10)
                        else:
                            div_answer_box.delete(0, 'end')
                            answer_box.delete(0, 'end')
                            div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: check_answer(question, div_question_box,
                                                                                    next_round,
                                                                                    div_submit_button,
                                                                                    cal_question))
                            div_submit_button.grid(row=3, column=2, pady=10)
                    else:
                        reply = f"That was wrong, you have {user.tries} tries left!\n{question.question} "
                        div_question_box["text"] = reply
                        div_answer_box = Entry(self, width=20, font=("ariel", 14))
                        div_answer_box.grid(row=2, column=2)
                        div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                   command=lambda: check_answer(question, div_question_box,
                                                                                next_round, div_submit_button,
                                                                                cal_question))
                        div_submit_button.grid(row=3, column=2, pady=10)
                else:
                    controller.show_page(GameOver)
            else:
                reply = "That was right! Click next round."
                div_question_box["text"] = reply
                div_answer_box.delete(0, 'end')
                show_next(next_round)
                remove(div_submit_button)


        def round_two():
            remove(div_next_round_1)
            remove(div_question_box)
            global div_question_box2
            div_question2 = div_question()
            div_cal_question2 = div_cal_question()
            div_question_box2 = Label(self, text=div_question2.question, font=("ariel, 16"), bg='#8DEFFF')
            div_question_box2.grid(row=1, column=2)
            div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                       command=lambda: check_answer(div_question2, div_question_box2, div_next_round_2,
                                                                    div_submit_button, div_cal_question2))
            div_submit_button.grid(row=3, column=2, pady=10)

        def round_three():
            remove(div_next_round_2)
            remove(div_question_box2)
            div_question3 = div_question()
            div_cal_question3 = div_cal_question()
            div_question_box3 = Label(self, text=div_question3.question, font=("ariel, 16"), bg='#8DEFFF')
            div_question_box3.grid(row=1, column=2)
            div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                       command=lambda: check_answer(div_question3, div_question_box3, div_next_round_3,
                                                                    div_submit_button, div_cal_question3))
            div_submit_button.grid(row=3, column=2, pady=10)

        global div_submit_button
        div_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                   command=lambda: check_answer(divquestion1, div_question_box, div_next_round_1,
                                                                div_submit_button, div_cal_question1))
        div_submit_button.grid(row=3, column=2, pady=10)

        global div_next_round_1
        div_next_round_1 = Button(self, text="Next round", font=("ariel", 14), command=round_two)

        global div_next_round_2
        div_next_round_2 = Button(self, text="Next round", font=("ariel", 14), command=round_three)

        global div_next_round_3
        div_next_round_3 = Button(self, text="Next round", font=("ariel", 14),
                                  command=lambda: controller.show_page(DivWin))

class DivWin(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title = Label(self, text="Congratulations!", font=("ms sans serif", 65), bg='#8DEFFF')
        title.grid(row=1, column=1, columnspan=3, padx=400)

        text = Label(self,
                     text="You defeated the Centorg and won 30 litres of water for the fountain, as well as 5 gold coins and 2 extra free tries!\nYou need 40 more litres to win. You can save and continue to carry on to Mult-land, or save and quit.",
                     font=("ariel", 17), bg='#8DEFFF', justify="left")
        text.grid(row=2, column=1, columnspan=3, pady=50)

        save_cont = Button(self, text="Save and continue", font=("ariel", 14),
                           command=lambda: [add_coins(5), add_tries(1),add_place("add-land"),add_place("sub-land"),add_place("div-land"),add_water(60), update(),save(user.name, places, items, user.coins, user.tries, fountain_water),
                                            controller.get_page(MultLand).update_user(), controller.show_page(MultLand)])
        save_cont.grid(row=3, column=1, pady=50, padx=100)

        save_quit = Button(self, text="Save and quit", font=("ariel", 14),
                           command=lambda: [add_coins(5), add_tries(1),add_place("add-land"),add_place("sub-land"),add_place("div-land"),add_water(60),update(),save(user.name, places, items, user.coins, user.tries, fountain_water),
                                            exit()])
        save_quit.grid(row=3, column=2, pady=50)


class MultLand(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.photo= PhotoImage(file='./multland .png')

        frame1 = Frame(self, bg='#8DEFFF')
        frame1.grid(row=0, column=0)

        coin_label = Label(frame1, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                           relief="ridge")
        coin_label.grid(row=0, column=3, sticky=NE, padx=380)

        try_label = Label(frame1, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5, relief="ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=380, pady=30)

        canvas = Canvas(frame1, width=200, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=1, padx=(500, 100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)

        frame2 =Frame(self, bg='#8DEFFF')
        frame2.grid(row=1, column=0)

        global mult_output
        mult_output = StringVar()
        self.output_box = Label(frame2, textvariable= mult_output, font=("ariel, 14"), bg="white", justify="left")
        self.output_box.grid(row=1, column=0)



        button1= Button(frame2, text="Continue",font=("ariel, 14"), command= lambda: [remove(button1), mult_update_text("You carry on walking and finally make it to the town square.\nYou see the fountain of knowledge in the centre.\n"
                                                                                                                     "There are crowds of people around and next to the fountain is a small chest.\n"
                                                                                                                     "As you reach it you remember the key you found earlier!\n"
                                                                                                                     "You try it in the lock and open the chest...\nInside are 10 gold coins!!\n"
                                                                                                                     "Just as you are putting them away, Zorgatron appears!"), show(button2), add_coins(10), update() ])
        button1.grid(row=2, column=0, pady=10)

        button2= Button(frame2, text="Continue",font=("ariel, 14"), command= lambda: [remove(button1), mult_update_text(f"'Hi {user.name},I am Zorgatron.\n I hear you have managed to beat the Orgs,\n and take back knowledge for the people here, but not any more!!\n"
    "It's time to fight me, I hope you're ready!'"), remove(button2),show(button3)])

        button3= Button(self, text="Let's battle!",font=("ariel", 14),
                         command=lambda: [controller.show_page(MultBattle)])


    def update_user(self):
        items=load_items()
        if "Golden Calculator" not in items:
            if "Empty Calculator Case" not in items:
                mult_update_text(
                    f'You arrive in Mult-land and the Mayor Max-A-Million is there to greet you!\n'
                    f'"Hi {user.name}, I\'m Max-A-Million, the mayor of Digiland.\n'
                    f'I can\'t thank you enough for everything you\'ve done so far to help save our land,\nbut I know it\'s not finished yet.\n'
                    f'Here in Mult-land the leader of the Zorgs has taken over.\n'
                    f'It isn\'t until you\'ve beaten him that the Fountain of Knowledge will be fully replenished.\n'
                    f'He knows that you\'re here and is waiting to battle you,\nso you will need to meet him in the town square to finish this off.\n'
                    f'This isn\'t going to be easy,\nso I\'d like to give you my golden calculator to use if you run out of coins and get stuck.\n'
                    f'It\'s very old so you\'ll only be able to use it once,\nso choose your timing wisely!"\nYou thank Max-A-Million and put the calclator in your bag')
                add_item("Golden Calculator")
            else:
                mult_update_text('You arrive in Mult-land and the Mayor Max-A-Million is there to greet you!\n'
                                f'"Hi {user.name}, I\'m Max-A-Million, the mayor of Digiland. It\'s such an honor to finally meet you!\n'
                                f'I can\'t thank you enough for everything you\'ve done so far to help save our land, but I know it\'s not finished yet.\n'
                                f'Here in Mult-land the leader of the Zorgs has taken over.\n'
                                f'It isn\'t until you\'ve beaten him that the Fountain of Knowledge will be completely replenished.\n'
                                f'He knows that you\'re here and is waiting to battle you, so you will need to meet him in the town square to finish this off.\n'
                                f'This isn\'t going to be easy, so I\'d like to give you this as a gift to help out...\nHe hands you a pouch that has 10 gold coins inside!\nYou thank him and put the coins away')
                user.coins += 10
                update()
        else:
            mult_update_text('You arrive in Mult-land and the Mayor Max-A-Million is there to greet you!\n'
                            f'"Hi {user.name}, I\'m Max-A-Million, the mayor of Digiland. It\'s such an honor to finally meet you!\n'
                            f'I can\'t thank you enough for everything you\'ve done so far to help save our land, but I know it\'s not finished yet.\n'
                            f'Here in Mult-land the leader of the Zorgs has taken over.\n'
                            f'It isn\'t until you\'ve beaten him that the Fountain of Knowledge will be completely replenished.\n'
                            f'He knows that you\'re here and is waiting to battle you, so you will need to meet him in the town square to finish this off.\n'
                            f'This isn\'t going to be easy, so I\'d like to give you this as a gift to help out...\nHe hands you a pouch that has 10 gold coins inside!\nYou thank him and put the coins away')
            user.coins += 10
            update()


class MultBattle(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.photo = PhotoImage(file="./zorgatron.png")
        global user


        coin_label = Label(self, textvariable=coin_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5,
                           relief="ridge")
        coin_label.grid(row=0, column=3, sticky=NE, padx=300)

        try_label = Label(self, textvariable=try_count, font=("ariel", 14), bg='#8DEFFF', borderwidth=5, relief="ridge")
        try_label.grid(row=0, column=3, sticky=NE, padx=300, pady=30)

        canvas = Canvas(self, width=250, height=200, bg='#8DEFFF', highlightthickness=0)
        canvas.grid(row=0, column=1, columnspan=2, padx=(500, 100), pady=5)
        img = self.photo
        image = canvas.create_image(0, 0, image=img, anchor=NW)

        global multquestion1
        global mult_question_box
        global mult_cal_question1
        mult_cal_question1 = mult_cal_question()
        multquestion1 = mult_question()
        mult_question_box = Label(self, text=multquestion1.question, font=("ariel, 16"), bg='#8DEFFF')
        mult_question_box.grid(row=1, column=2)

        global mult_answer_box
        mult_answer_box = Entry(self, width=20, font=("ariel", 14))
        mult_answer_box.grid(row=2, column=2)

        def check_cal_answer(question, mult_question_box, next_round, mult_submit_button, cal_question):
            global mult_answer_box
            remove(mult_submit_button)
            try:
                answer = int(mult_answer_box.get())
            except ValueError:
                message = messagebox.showinfo(title="Error", message="You must enter a whole number")
                mult_answer_box.delete(0, "end")
                mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_cal_answer(question, mult_question_box, next_round,
                                                                            mult_submit_button, cal_question))
                mult_submit_button.grid(row=3, column=2, pady=10)
                return

            if answer != cal_question.answer:
                    user.tries -= 1
                    update()
                    if user.tries > 0:
                        reply = f"That was wrong, you have {user.tries} tries left!\n{cal_question.question} "
                        question_box["text"] = reply
                        mult_answer_box = Entry(self, width=20, font=("ariel", 14))
                        mult_answer_box.grid(row=2, column=2)
                        mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                   command=lambda: check_cal_answer(question, mult_question_box,
                                                                                    next_round,
                                                                                    mult_submit_button, cal_question))
                        mult_submit_button.grid(row=3, column=2, pady=10)
                    else:
                        controller.show_page(GameOver)
            else:
                reply = "That was right! Click next round."
                mult_question_box["text"] = reply
                mult_answer_box.delete(0, 'end')
                show_next(next_round)
                remove(mult_submit_button)

        def check_answer(question, mult_question_box, next_round, mult_submit_button, cal_question):
            global mult_answer_box
            remove(mult_submit_button)
            try:
                answer = int(mult_answer_box.get())
            except ValueError:
                messagebox.showinfo(title="Error", message="You must enter a whole number")
                mult_answer_box.delete(0, "end")
                mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                           command=lambda: check_answer(question, mult_question_box,
                                                                        next_round,
                                                                        mult_submit_button,
                                                                        cal_question))
                mult_submit_button.grid(row=3, column=2, pady=10)
                return

            if answer != question.answer:
                user.tries -= 1
                update()
                if user.tries > 0:
                    if user.coins >= 2:
                        message = messagebox.askquestion("Calculator",
                                                         "That was wrong, would you like to use the calculator and spend 2 gold coins?")
                        if message == 'yes':
                            user.coins -= 2
                            update()
                            reply = f"Ok, here's an easier question.\n{cal_question.question}"
                            mult_question_box["text"] = reply
                            mult_answer_box = Entry(self, width=20, font=("ariel", 14))
                            mult_answer_box.grid(row=2, column=2)
                            mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: check_cal_answer(question, mult_question_box,
                                                                                        next_round,
                                                                                        mult_submit_button,
                                                                                        cal_question))
                            mult_submit_button.grid(row=3, column=2, pady=10)
                        else:
                            mult_answer_box.delete(0, 'end')
                            answer_box.delete(0, 'end')
                            mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: check_answer(question, mult_question_box,
                                                                                    next_round,
                                                                                    mult_submit_button,
                                                                                    cal_question))
                            mult_submit_button.grid(row=3, column=2, pady=10)
                    elif "Golden Calculator" in items:
                        message = messagebox.askquestion("Golden Calculator",
                                                         f"That was wrong,you have {user.tries} tries left! Do you want to use the Golden Calculator?")
                        if message == 'yes':
                            remove_item("Golden Calculator")
                            add_item("Empty Calculator Case")
                            reply = f"Ok, here's an easier question.\n{cal_question.question}"
                            mult_question_box["text"] = reply
                            mult_answer_box = Entry(self, width=20, font=("ariel", 14))
                            mult_answer_box.grid(row=2, column=2)
                            mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: check_cal_answer(question,
                                                                                        mult_question_box,
                                                                                        next_round,
                                                                                        mult_submit_button,
                                                                                        cal_question))
                            mult_submit_button.grid(row=3, column=2, pady=10)
                        else:
                            mult_answer_box.delete(0, 'end')
                            answer_box.delete(0, 'end')
                            mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                       command=lambda: check_answer(question, mult_question_box,
                                                                                    next_round,
                                                                                    mult_submit_button,
                                                                                    cal_question))
                            mult_submit_button.grid(row=3, column=2, pady=10)
                    else:
                        reply = f"That was wrong, you have {user.tries} tries left!\n{question.question} "
                        mult_question_box["text"] = reply
                        mult_answer_box = Entry(self, width=20, font=("ariel", 14))
                        mult_answer_box.grid(row=2, column=2)
                        mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                                   command=lambda: check_answer(question, mult_question_box,
                                                                                next_round, mult_submit_button,
                                                                                cal_question))
                        mult_submit_button.grid(row=3, column=2, pady=10)
                else:
                    controller.show_page(GameOver)
            else:
                reply = "That was right! Click next round."
                mult_question_box["text"] = reply
                mult_answer_box.delete(0, 'end')
                show_next(next_round)
                remove(mult_submit_button)

        def round_two():
            remove(mult_next_round_1)
            remove(mult_question_box)
            global mult_question_box2
            mult_question2 = mult_question()
            mult_cal_question2 = mult_cal_question()
            mult_question_box2 = Label(self, text=mult_question2.question, font=("ariel, 16"), bg='#8DEFFF')
            mult_question_box2.grid(row=1, column=2)
            mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                       command=lambda: check_answer(mult_question2, mult_question_box2, mult_next_round_2,
                                                                    mult_submit_button, mult_cal_question2))
            mult_submit_button.grid(row=3, column=2, pady=10)

        def round_three():
            remove(mult_next_round_2)
            remove(mult_question_box2)
            mult_question3 = mult_question()
            mult_cal_question3 = mult_cal_question()
            mult_question_box3 = Label(self, text=mult_question3.question, font=("ariel, 16"), bg='#8DEFFF')
            mult_question_box3.grid(row=1, column=2)
            mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                       command=lambda: check_answer(mult_question3, mult_question_box3, mult_next_round_3,
                                                                    mult_submit_button, mult_cal_question3))
            mult_submit_button.grid(row=3, column=2, pady=10)

        global mult_submit_button
        mult_submit_button = Button(self, text="Submit", font=("ariel", 14),
                                   command=lambda: check_answer(multquestion1, mult_question_box, mult_next_round_1,
                                                                mult_submit_button, mult_cal_question1))
        mult_submit_button.grid(row=3, column=2, pady=10)

        global mult_next_round_1
        mult_next_round_1 = Button(self, text="Next round", font=("ariel", 14), command=round_two)

        global mult_next_round_2
        mult_next_round_2 = Button(self, text="Next round", font=("ariel", 14), command=round_three)

        global mult_next_round_3
        mult_next_round_3 = Button(self, text="Next round", font=("ariel", 14),
                                  command=lambda: controller.show_page(WinGame))


class WinGame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        title = Label(self, text="You Won!!", font=("ms sans serif", 65), bg='#8DEFFF')
        title.grid(row=1, column=1, columnspan=3, padx=400, pady=20)
        user.name= load_name()
        text = Label(self,
                     text= f"Congratulations, {user.name}! You won the battle and defeated the Orgs!\nThanks to your hard work, Digiland is safe again!",
                     font=("ariel", 17), bg='#8DEFFF', justify="left")
        text.grid(row=2, column=1, columnspan=3, pady=50)
        exit = Button(self, text="Leave Digiland", font=("ariel", 17), command=sys.exit)
        exit.grid(row=3, column=2, pady=100, padx=100)


class GameOver(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        title = Label(self, text="Game Over", font=("ms sans serif", 65), bg='#8DEFFF')
        title.grid(row=1, column=1, columnspan=3, padx=400, pady=20)

        text = Label(self,
                     text="You ran out of tries and the Org won the battle.\nThank you for visiting Digiland, better luck next time!.",
                     font=("ariel", 17), bg='#8DEFFF', justify="left")
        text.grid(row=2, column=1, columnspan=3, pady=50)

        exit= Button(self, text="Leave Digiland",font=("ariel", 17), command= sys.exit)
        exit.grid(row=3, column=2, pady=100, padx=100)



app = Digilandapp()
app.mainloop()


