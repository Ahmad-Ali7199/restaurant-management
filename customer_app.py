from tkinter import *
from abc import ABC, abstractmethod
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import re
# Database connection
mydb = mysql.connector.connect(host="localhost", user="root", password="6090", database="project")
my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE IF NOT EXISTS order_2(id int PRIMARY KEY, dish VARCHAR(255), price int, quantity int)")

# Tkinter root setup
root = Tk()
root.geometry("628x520")
root.title("Project Restaurant")
root.config(bg="orange")


class Management(ABC):
    @abstractmethod
    def clear_frame(self):
        pass


class OurMenu(Management):
    def __init__(self, root, my_cursor, mydb):
        self.root = root
        self.my_cursor = my_cursor
        self.mydb = mydb

    def display_menu(self):
        self.clear_frame()
        frame110 = Frame(root)
        scrollbar = Scrollbar(frame110)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(frame110, yscrollcommand=scrollbar.set, font="Arial 15", width=50, height=10)
        scrollbar.config(command=listbox.yview)
        listbox.pack(padx=10, pady=10)
        frame110.pack()
        sql = "SELECT * FROM Menu"
        self.my_cursor.execute(sql)
        menu_items = self.my_cursor.fetchall()
        listbox.delete(0, END)
        for item in menu_items:
            listbox.insert(END, f"             Id:{item[0]}   , Dish: {item[1]}   , Price: {item[2]}")

        def place_order():
            self.my_cursor.execute(f"SELECT * FROM menu WHERE Id={e1.get()}")
            for x in self.my_cursor:
                self.my_cursor.execute(
                    f"INSERT INTO order_2(id, dish, price, quantity) "
                    f"VALUES({x[0]}, '{x[1]}', {x[2]}, {e2.get()})")
                self.mydb.commit()

        def yes():
            self.my_cursor.execute(
                "CREATE TABLE IF NOT EXISTS order_1(phone VARCHAR(15) NOT NULL, address VARCHAR(255))")
            self.my_cursor.execute(f"INSERT INTO order_1(phone, address) VALUES({contact_entry.get()}, '{e_2.get()}')")
            self.mydb.commit()
            self.my_cursor.execute("CREATE TABLE IF NOT EXISTS confirm_order AS SELECT "
                                   "order_2.id, order_2.dish, order_2.price, order_2.quantity,"
                                   " order_1.phone, order_1.address FROM order_2 JOIN order_1")
            messagebox.showinfo("Your order", "Your order added to your cart")
            result.config(text="Your order added to your cart", font="Arial 13 bold", fg="purple")

        f6 = Frame(self.root)
        l11 = Label(f6, text="Enter id")
        l11.grid(row=1, column=0, pady=10)
        e1 = Entry(f6)
        e1.grid(row=1, column=1)
        l12 = Label(f6, text="Enter Quantity")
        l12.grid(row=2, column=0)
        e2 = Entry(f6)
        e2.grid(row=2, column=1)
        done = Button(f6, text="Place order", command=place_order)
        done.grid(row=3, column=0, columnspan=2, pady=2)
        label_21 = Label(f6, text=f"The address where \nyou want it delivered")
        label_21.grid(row=4, column=0, padx=10, pady=10)
        e_2 = Entry(f6)
        e_2.grid(row=4, column=1, padx=10, pady=10)
        contact_label = Label(f6, text="Contact Number")
        contact_label.grid(row=5, column=0, padx=10, pady=10)
        contact_entry = Entry(f6)
        contact_entry.grid(row=5, column=1, padx=10, pady=10)
        order = Button(f6, text="Order", command=yes)
        order.grid(row=6, column=0, columnspan=2, pady=2)
        result = Label(f6, text="")
        result.grid(row=7)
        f6.pack()

        def back():
            frame110.destroy()
            f6.destroy()
            listbox.destroy()
            back1.destroy()
            main2()

        back1 = Button(self.root, text="Back", command=back)
        back1.pack()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class Cart(Management):
    def __init__(self, root, my_cursor):
        self.root = root
        self.my_cursor = my_cursor

    def display_cart(self):
        self.clear_frame()
        frame110 = Frame(root)
        scrollbar = Scrollbar(frame110)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox2 = Listbox(frame110, yscrollcommand=scrollbar.set, font="Arial 15", width=100, height=8)
        scrollbar.config(command=listbox2.yview)
        listbox2.pack(pady=10)
        frame110.pack()

        try:
            self.my_cursor.execute("SELECT * FROM confirm_order")
            orders = self.my_cursor.fetchall()
            listbox2.delete(0, END)
            for order in orders:
                listbox2.insert(END, f"             Id:{order[0]}   , Dish: {order[1]}   , Price: {order[2]}")

            f3 = Frame(self.root, bg="orange")
            t = 0
            self.my_cursor.execute("SELECT * FROM confirm_order")
            for x in self.my_cursor:
                t += x[2] * x[3]
            label_2 = Label(f3, text=f"Total bill : {t}")
            label_2.grid(row=1, column=0)

            def order_confirm():
                messagebox.showinfo("Order", "Successfully placed your order")

            def back():
                label_2.destroy()
                frame110.destroy()
                listbox2.destroy()
                back2.destroy()
                confirm_order.destroy()
                main2()

            back2 = Button(self.root, text="Back", command=back)
            back2.pack(side=BOTTOM, pady=5)
            confirm_order = Button(f3, text="Order confirm", command=order_confirm)
            confirm_order.grid(row=5, column=0, columnspan=2, pady=5)
            f3.pack()

        except mysql.connector.Error as err:
            def back():
                frame110.destroy()
                listbox2.destroy()
                back2.destroy()
                main2()

            back2 = Button(self.root, text="Back", command=back)
            back2.pack(side=BOTTOM, pady=5)
            messagebox.showinfo("Order", "Currently you have not not place any order")
            print("Currently no order found")
            print(err)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class Reservation(Management):
    def __init__(self, root, my_cursor, mydb):
        self.root = root
        self.my_cursor = my_cursor
        self.mydb = mydb

    def reserve_table(self):
        self.clear_frame()
        f5 = Frame(self.root)
        name_label = Label(f5, text="Name")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = Entry(f5)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        contact_label = Label(f5, text="Contact Number")
        contact_label.grid(row=1, column=0, padx=10, pady=10)
        contact_entry = Entry(f5)
        contact_entry.grid(row=1, column=1, padx=10, pady=10)

        date_label = Label(f5, text="Date (YYYY-MM-DD)")
        date_label.grid(row=2, column=0, padx=10, pady=10)
        date_entry = Entry(f5)
        date_entry.grid(row=2, column=1, padx=10, pady=10)

        time_label = Label(f5, text="Time (HH:MM)")
        time_label.grid(row=3, column=0, padx=10, pady=10)
        time_entry = Entry(f5)
        time_entry.grid(row=3, column=1, padx=10, pady=10)

        people_label = Label(f5, text="Number of People")
        people_label.grid(row=4, column=0, padx=10, pady=10)
        people_var = StringVar()
        people_combobox = ttk.Combobox(f5, textvariable=people_var)
        people_combobox['values'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        people_combobox.grid(row=4, column=1, padx=10, pady=10)

        def submit_reservation():
            name = name_entry.get().strip()
            contact = contact_entry.get().strip()
            date = date_entry.get().strip()
            time = time_entry.get().strip()
            people = people_var.get()
            if not (name and contact and date and time and people):
                messagebox.showerror("Error", "All fields are required")
                return
            if not re.match(r'^\+?[0-9]{10,15}$', contact):
                messagebox.showerror("Error", "Please enter a valid contact number")
                return
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                messagebox.showerror("Error", "Please enter date in YYYY-MM-DD format")
                return
            if not re.match(r'^\d{2}:\d{2}$', time):
                messagebox.showerror("Error", "Please enter time in HH:MM format")
                return

            self.my_cursor.execute(f"INSERT INTO reservations(name, phone, date, time, people) "
                                   f"VALUES('{name}', {contact}, '{date}', '{time}', {people})")
            self.mydb.commit()
            messagebox.showinfo("Success", f"Reservation confirmed for {people} people on {date} at {time}")
            status_label.config(text="Reservation successful", font="Arial 13 bold", fg="purple")

        submit_button = Button(f5, text="Reserve Table", command=submit_reservation)
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)

        status_label = Label(f5, text="", fg="red")
        status_label.grid(row=6, column=0, columnspan=2, pady=10)
        f5.pack(pady=10)

        def back():
            f5.destroy()
            back3.destroy()
            main2()

        back3 = Button(self.root, text="Back", command=back)
        back3.pack(side=BOTTOM, pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def main2():
    def licence():
        messagebox.showinfo("Licence", "Government of [Pakistan/Punjab/South-Asia]\n"
                                       "Department of Health and Safety\n"
                                       "Restaurant Management License\nLicense Number: [123456789]"
                                       "\nDate of Issue: [12-04-2023]\n"
                                       "Expiration Date: [12-4-2028]\n"
                                       "This is to certify that the restaurant detailed below has been"
                                       " granted a license to operate as a food establishment"
                                       " in accordance with the health and safety"
                                       " regulations prescribed by the Department of Health and Safety.")

    # Menu bar
    menu = Menu(root)
    m1 = Menu(menu, tearoff=0)
    menu.add_cascade(label="Licence", command=licence)
    root.config(menu=menu)

    # taskbar
    taskbar = StringVar()
    taskbar.set("Contact\t\t\tPrivacy policy\t\tTerms & Conditions")
    s_bar = Label(root, textvariable=taskbar)
    s_bar.pack(side=BOTTOM, fill=X)
    s_bar = Label(root, text="2024 All Reserved Licence")
    s_bar.pack(side=BOTTOM, fill=X)

    # main
    l1 = Label(root, text="ONLINE RESTAURANT", bg="orange", font="Stylus 40 bold")
    l1.pack()

    # Picture
    frame1 = Frame(root, bg="black")
    photo = PhotoImage(file=r"C:\Users\Ahmad\Downloads\11.png", height=200, width=300)
    pic = Label(frame1, image=photo, bg="black")
    pic.image = photo
    pic.pack()
    frame1.pack()

    # Buttons
    frame2 = Frame(root, bg="orange")
    b1 = Button(frame2, text="Reservation", bg="Black", fg="White", height=2, width=10, font="Arial 15 bold",
                command=lambda: Reservation(root, my_cursor, mydb).reserve_table())
    b1.pack(side=LEFT, padx=10, pady=10)
    b2 = Button(frame2, text=" Our menu ", bg="Black", fg="White", height=2, width=10, font="Arial 15 bold",
                command=lambda: OurMenu(root, my_cursor, mydb).display_menu())
    b2.pack(side=LEFT, padx=10, pady=10)
    b3 = Button(frame2, text="   Cart   ", bg="Black", fg="White", height=2, width=10, font="Arial 15 bold",
                command=lambda: Cart(root, my_cursor).display_cart())
    b3.pack(side=LEFT, padx=10, pady=10)
    frame2.pack()
    b4 = Button(root, text="   Exit   ", bg="Black", fg="White", height=2, width=10, font="Arial 15 bold",
                command=root.quit)
    b4.pack(padx=10, pady=10)


main2()
root.mainloop()
