from tkinter import *
from tkinter import messagebox
import mysql.connector
from abc import ABC, abstractmethod

# Database connection
mydb = mysql.connector.connect(host="localhost", user="root", password="6090", database="project")
my_cursor = mydb.cursor()

# Tkinter root setup
root = Tk()
root.geometry("628x520")
root.title("Project Restaurant")
root.config(bg="sky blue")


class Management(ABC):
    @abstractmethod
    def clear_frame(self):
        pass


class Food(Management):
    def __init__(self, root, my_cursor, mydb):
        self.root = root
        self.my_cursor = my_cursor
        self.mydb = mydb

    def add_food(self):
        self.clear_frame()
        l2 = Label(self.root, text="Name", bg="sky blue", font="Arial 30 bold")
        l2.pack(pady=10)
        name = Entry(self.root, font="Arial 20", width=30)
        name.pack()
        l3 = Label(self.root, text="Price", bg="sky blue", font="Arial 30 bold")
        l3.pack(pady=10)
        price = Entry(self.root, font="Arial 20", width=30)
        price.pack()

        def ok():
            self.my_cursor.execute(f"INSERT INTO menu(Dish, Price) VALUES ('{name.get()}', {price.get()})")
            self.mydb.commit()
            result_label.config(text="Successfully added to your Menu", font="Arial 15 bold", fg="Green")
        result_label = Label(self.root, text="", bg="sky blue")
        result_label.pack()
        ok1 = Button(self.root, text="Done", command=ok, height=3, width=13, borderwidth=5)
        ok1.pack()

        def back():
            result_label.destroy()
            ok1.destroy()
            back1.destroy()
            l2.destroy()
            name.destroy()
            l3.destroy()
            price.destroy()
            main()

        back1 = Button(self.root, text="Back", command=back)
        back1.pack(side=BOTTOM, pady=5)

    def delete_food(self):
        self.clear_frame()
        roll4 = Label(self.root, text="Enter a food id", bg="sky blue", font="Arial 20 bold")
        roll4.pack(pady=30)
        roll4_1 = Entry(self.root, font="Arial 20", width=20)
        roll4_1.pack()

        def back():
            result_label.destroy()
            roll4.destroy()
            roll4_1.destroy()
            delete1.destroy()
            back2.destroy()
            main()

        def delete():
            sql = f"DELETE FROM menu WHERE Id='{roll4_1.get()}'"
            self.my_cursor.execute(sql)
            self.mydb.commit()
            result_label.config(text="Successfully deleted this record", font="Arial 15 bold", fg="Green")
        result_label = Label(self.root, text="", bg="sky blue")
        result_label.pack()
        delete1 = Button(self.root, text="Delete this record", command=delete, height=3, width=20, borderwidth=5)
        delete1.pack(pady=30)
        back2 = Button(self.root, text="Back", command=back)
        back2.pack(side=BOTTOM, pady=5)

    def update_food(self):
        self.clear_frame()
        f3 = Frame(self.root, bg="sky blue")
        b5 = Button(f3, text="Update name", bg="Red", fg="White", font="Arial 15 bold",
                    height=3, width=13, borderwidth=5, command=self.update_name)
        b5.pack(side=LEFT, padx=10)
        b6 = Button(f3, text="Update price", bg="Red", fg="White", font="Arial 15 bold",
                    height=3, width=13, borderwidth=5, command=self.update_price)
        b6.pack(side=LEFT, padx=10)
        f3.pack(pady=150)

        def back():
            f3.destroy()
            back3.destroy()
            main()
        back3 = Button(self.root, text="Back", command=back)
        back3.pack(side=BOTTOM, pady=5)

    def update_name(self):
        self.clear_frame()
        roll1 = Label(self.root, text="Enter Dish Id", bg="sky blue", font="Arial 25 bold")
        roll1.pack(pady=10)
        roll_1 = Entry(self.root, font="Arial 20", width=20)
        roll_1.pack()
        set_name = Label(self.root, text="New Dish name", bg="sky blue", font="Arial 25 bold")
        set_name.pack(pady=10)
        set_name1 = Entry(self.root, font="Arial 20", width=30)
        set_name1.pack()

        def back():
            roll1.destroy()
            roll_1.destroy()
            set_name.destroy()
            set_name1.destroy()
            result_label.destroy()
            ok3_1.destroy()
            back3_1.destroy()
            main()
        back3_1 = Button(self.root, text="Back", command=back)
        back3_1.pack(side=BOTTOM, pady=5)

        def update1():
            sql = f"UPDATE Menu set Dish ='{set_name1.get()}' WHERE Id='{roll_1.get()}'"
            self.my_cursor.execute(sql)
            self.mydb.commit()
            result_label.config(text="Successfully updated name in your record", font="Arial 15 bold", fg="Green")

        result_label = Label(self.root, text="", bg="Sky blue")
        result_label.pack()
        ok3_1 = Button(self.root, text="Done", command=update1, height=3, width=20, borderwidth=5)
        ok3_1.pack()

    def update_price(self):
        self.clear_frame()
        roll2 = Label(self.root, text="Enter Id number", bg="sky blue", font="Arial 25 bold")
        roll2.pack(pady=15)
        roll_2 = Entry(self.root, font="Arial 20", width=15)
        roll_2.pack()
        set_price = Label(self.root, text="Update price", bg="sky blue", font="Arial 25 bold")
        set_price.pack(pady=15)
        set_price2 = Entry(self.root, font="Arial 20", width=20)
        set_price2.pack()

        def update2():
            sql = f"UPDATE menu set Price ='{set_price2.get()}' WHERE Id='{roll_2.get()}'"
            self.my_cursor.execute(sql)
            self.mydb.commit()
            result_label.config(text="Successfully updated price in your record", font="Arial 15 bold", fg="Green")

        result_label = Label(self.root, text="", bg="sky blue")
        result_label.pack()
        ok3_2 = Button(self.root, text="Done", command=update2, height=3, width=20, borderwidth=5)
        ok3_2.pack()

        def back():
            roll2.destroy()
            roll_2.destroy()
            set_price.destroy()
            set_price2.destroy()
            result_label.destroy()
            ok3_2.destroy()
            back3_2.destroy()
            main()
        back3_2 = Button(self.root, text="Back", command=back)
        back3_2.pack(side=BOTTOM, pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class Reservation(Management):
    def __init__(self, root, my_cursor):
        self.root = root
        self.my_cursor = my_cursor

    def check_reserve(self):
        self.clear_frame()
        listbox = Listbox(self.root, font="Arial 10", width=100)
        listbox.pack(pady=10)
        self.my_cursor.execute("SELECT * FROM reservations")
        reservations = self.my_cursor.fetchall()
        listbox.delete(0, END)
        for reservation in reservations:
            listbox.insert(END, f"No: {reservation[0]}, Name: {reservation[1]}, Phone: {reservation[2]},"
                                f" Date: {reservation[3]}, Time: {reservation[4]}, People: {reservation[5]}")

        def back():
            listbox.destroy()
            back4.destroy()
            main()
        back4 = Button(self.root, text="Back", command=back)
        back4.pack(side=BOTTOM, pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class Order(Management):
    def __init__(self, root, my_cursor, mydb):
        self.root = root
        self.my_cursor = my_cursor
        self.mydb = mydb

    def order(self):
        self.clear_frame()
        order_name = Label(self.root, text="Orders", bg="sky blue", font="Arial 20 bold underline")
        order_name.pack()
        listbox = Listbox(self.root, font="Arial 10", width=80)
        listbox.pack(pady=10)

        try:
            self.my_cursor.execute("SELECT * FROM confirm_order")
            orders = self.my_cursor.fetchall()
            listbox.delete(0, END)
            for order in orders:
                listbox.insert(END, f"Id:{order[0]},Dish:{order[1]},Price:{order[2]},"
                                    f"Quantity:{order[3]},Phone:{order[4]},Address:{order[5]}")

            def order_complete():
                my_cursor.execute("SELECT * FROM confirm_order")
                for x in my_cursor:
                   my_cursor.execute(f"INSERT INTO Order_detail(dish, price, quantity,phone,address)"
                                     f" VALUES('{x[1]}', {x[2]}, {x[3]}, {x[4]}, '{x[5]}')")
                mydb.commit()
                messagebox.showinfo("Order", "Order is delivered")
                self.my_cursor.execute("DROP TABLE confirm_order")
                self.my_cursor.execute("DROP TABLE order_1")
                self.my_cursor.execute("DROP TABLE order_2")

            def back():
                order_name.destroy()
                complete.destroy()
                listbox.destroy()
                back5.destroy()
                main()
            back5 = Button(self.root, text="Back", command=back)
            back5.pack(side=BOTTOM, pady=5)
            complete = Button(self.root, text="Order complete", command=order_complete)
            complete.pack()
        except mysql.connector.Error as err:
            def back():
                order_name.destroy()
                listbox.destroy()
                back5.destroy()
                main()
            back5 = Button(self.root, text="Back", command=back)
            back5.pack(side=BOTTOM, pady=5)
            messagebox.showinfo("Order", "Currently no order")
            print("Currently no order found")
            print(err)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class Details(Management):
    def __init__(self, root, my_cursor):
        self.root = root
        self.my_cursor = my_cursor

    def order_details(self):
        self.clear_frame()
        com_order = Label(self.root, text="Delivered orders", bg="sky blue", font="Arial 20 bold underline")
        com_order.pack()
        frame110 = Frame(root)
        scrollbar = Scrollbar(frame110, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(frame110, orient=HORIZONTAL)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        listbox3 = Listbox(frame110, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar.set,
                           font="Arial 15", width=100, height=13)
        scrollbar.config(command=listbox3.yview)
        scrollbar_x.config(command=listbox3.xview)
        listbox3.pack(pady=10)
        frame110.pack()
        try:
            self.my_cursor.execute("SELECT * FROM Order_detail")
            orders = self.my_cursor.fetchall()
            listbox3.delete(0, END)
            for order in orders:
                listbox3.insert(END, f"Id:{order[0]},Dish:{order[1]},Price:{order[2]},"
                                    f"Quantity:{order[3]},Phone:{order[4]},Address:{order[5]}")

            def back():
                com_order.destroy()
                frame110.destroy()
                back5.destroy()
                main()

            back5 = Button(self.root, text="Back", command=back)
            back5.pack(side=BOTTOM, pady=5)
        except mysql.connector.Error as err:
            def back():
                com_order.destroy()
                frame110.destroy()
                back5.destroy()
                main()
            back5 = Button(self.root, text="Back", command=back)
            back5.pack(side=BOTTOM, pady=5)
            messagebox.showinfo("Order", "Currently no order")
            print("Currently no order found")
            print(err)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
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
    Menu(menu, tearoff=0)
    menu.add_cascade(label="Licence", command=licence)
    root.config(menu=menu)

    # Taskbar
    taskbar = StringVar()
    taskbar.set("Contact\t\t\tPrivacy policy\t\tTerms & Conditions")
    s_bar = Label(root, textvariable=taskbar)
    s_bar.pack(side=BOTTOM, fill=X)
    s_bar = Label(root, text="2024 All Reserved Licence")
    s_bar.pack(side=BOTTOM, fill=X)
    # main
    l1 = Label(root, text="ONLINE RESTAURANT\nManagement", bg="sky blue", fg="navy", font="Stylus 40 bold")
    l1.pack()

    # Button
    f = Frame(root, bg="sky blue")
    food = Food(root, my_cursor, mydb)
    b1 = Button(f, text="Add dish", bg="white", fg="navy", font="Arial 15 bold", borderwidth=10,
                height=3, width=11, command=food.add_food)
    b1.pack(side=LEFT, padx=5, pady=10)
    b2 = Button(f, text="Delete dish", bg="white", fg="navy", font="Arial 15 bold", borderwidth=10,
                height=3, width=11, command=food.delete_food)
    b2.pack(side=LEFT, padx=5, pady=10)
    b3 = Button(f, text="Update dish", bg="white", fg="navy", font="Arial 15 bold", borderwidth=10,
                height=3, width=11, command=food.update_food)
    b3.pack(side=LEFT, padx=5, pady=10)
    f.pack()
    f2 = Frame(root, bg="sky blue")
    reservation = Reservation(root, my_cursor)
    b3 = Button(f2, text="Check\nReservation", bg="white", fg="navy", font="Arial 15 bold", borderwidth=10,
                height=3, width=11, command=reservation.check_reserve)
    b3.pack(side=LEFT, padx=5, pady=10)
    order = Order(root, my_cursor, mydb)
    b4 = Button(f2, text="Orders", bg="white", fg="navy", font="Arial 15 bold", borderwidth=10,
                height=3, width=11, command=order.order)
    b4.pack(side=LEFT, padx=5, pady=10)
    detail = Details(root, my_cursor)
    b5 = Button(f2, text="Complete\n orders\nDetails", bg="white", fg="navy", font="Arial 15 bold", borderwidth=10,
                height=3, width=11, command=detail.order_details)
    b5.pack(side=LEFT, padx=5, pady=10)
    f2.pack()
    b6 = Button(root, text="Exit", bg="white", fg="navy", font="Arial 15 bold", borderwidth=10,
                height=3, width=11, command=root.quit)
    b6.pack(padx=5, pady=10)


main()
root.mainloop()
