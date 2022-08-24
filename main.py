# Mongo1C by hack0#5784
import pymongo
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox


def add():
    def addquit():
        if messagebox.askyesno("Mongo1C", "Вы действительно хотите выйти?"):
            addwindow.destroy()
        else:
            pass
    def insert():
        user = {}
        user['type'] = str(addtype.get())
        user['name'] = str(addname.get())
        user['amount'] = str(addspin.get())
        user['company'] = str(addcompany.get())
        try:
            collections.insert_one(user)
            messagebox.showinfo("Mongo1C", "Товар добавлен!")
            addwindow.destroy()
        except Exception as e:
            messagebox.showerror("Mongo1C", e)
    addwindow = Toplevel(root)
    addwindow.title("Mongo1C Добавление товара")
    addwindow.protocol("WM_DELETE_WINDOW", addquit)
    Label(addwindow, text="Тип:").grid(row=0, column=0)
    Label(addwindow, text="Наименование:").grid(row=0, column=1)
    Label(addwindow, text="Кол-во:").grid(row=0, column=2)
    Label(addwindow, text="Предприятие:").grid(row=0, column=3)
    addtype = Combobox(addwindow)
    addtype['values'] = ("Продажа", "Поставка")
    addtype.current(1)
    addtype.grid(row=1, column=0)
    addname = Entry(addwindow, width=10)
    addname.grid(row=1, column=1)
    addvar = IntVar()
    addvar.set(1)
    addspin = Spinbox(addwindow, from_=0, to=100, width=2, textvariable=addvar)
    addspin.grid(row=1, column=2)
    addcompany = Entry(addwindow, width=20)
    addcompany.grid(row=1, column=3)
    addbtn = Button(addwindow, text="Сохранить", command=insert)
    addbtn.grid(row=0, column=4)



def rem():
    def delete():
        user = {}
        user['id'] = str(e.get())
        try:
            collections.delete_one(user)
            messagebox.showinfo("Mongo1C", "Товар удалён!")
            remwindow.destroy()
        except Exception as ex:
            messagebox.showerror("Mongo1C", ex)
    remwindow = Toplevel(root)
    Label(remwindow, text="Идентификатор удаляемого товара:").pack()
    e = Entry(remwindow, width=20)
    e.pack()
    Button(remwindow, text="Удалить", command=delete).pack()


def edit():
    def continue_():
        def continue__():
            new = {}
            new['type'] = str(addtype.get())
            new['name'] = str(addname.get())
            new['amount'] = str(addspin.get())
            new['company'] = str(addcompany.get())
            user = {}
            for users in collections.find({}):
                if product['name'] == users['name']:
                    user['type'] = users['type']
                    user['name'] = users['name']
                    user['amount'] = users['amount']
                    user['company'] = users['company']
            collections.update_one(user, {"$set": new})


        contwindow = Toplevel(editwindow)


        Label(contwindow, text="Тип:").grid(row=0, column=0)
        Label(contwindow, text="Наименование:").grid(row=0, column=1)
        Label(contwindow, text="Кол-во:").grid(row=0, column=2)
        Label(contwindow, text="Предприятие:").grid(row=0, column=3)
        addtype = Combobox(contwindow)
        addtype['values'] = ("Продажа", "Поставка")
        addtype.current(1)
        addtype.grid(row=1, column=0)
        addname = Entry(contwindow, width=10)
        addname.grid(row=1, column=1)
        addvar = IntVar()
        addvar.set(1)
        addspin = Spinbox(contwindow, from_=0, to=100, width=2, textvariable=addvar)
        addspin.grid(row=1, column=2)
        addcompany = Entry(contwindow, width=20)
        addcompany.grid(row=1, column=3)
        addbtn = Button(contwindow, text="Сохранить", command=continue__)
        addbtn.grid(row=0, column=4)


        product = {}
        product["name"] = enter1
        old_product = {}
        for users in collections.find({}):
            if product["name"] == users["name"]:
                for i in types:
                    old_product[i] = users[i]
                break
        if str(old_product["type"]) == "Продажа":
            addtype.current(1)
        else:
            addtype.current(2)
        addname.insert(str(old_product["name"]))
        addvar.set(int(old_product["amount"]))


    editwindow = Toplevel(root)
    Label(editwindow, text="Наименование изменяемого товара").grid(row=0, column=0)
    enter1 = Entry(editwindow, width=20)
    enter1.grid(row=0, column=1)
    btn1 = Button(editwindow, text="Продолжить", fg="green", command=continue_)
    btn1.grid(row=0, column=2)


def search():
    def products():
        productsroot = Toplevel(chooseroot)
        for user in collections.find({}):
            txt = "Идентификатор: {}. Тип: {}. Наименование: {}. Количество: {}, Предприятие: {}.".format(user['id'], user["type"], user["name"], user["amount"], user["company"])
            Label(productsroot, text=txt).pack()


    def postavki():
        productsroot = Toplevel(chooseroot)
        for user in collections.find({}):
            if user['type'] == 'Поставка':
                txt = "Идентификатор: {}. Наименование: {}. Количество: {}, Предприятие: {}.".format(user['id'], user["name"], user["amount"], user["company"])
                Label(productsroot, text=txt).pack()


    def prodaji():
        productsroot = Toplevel(chooseroot)
        for user in collections.find({}):
            if user['type'] == "Продажа":
                txt = "Идентификатор: {}. Наименование: {}. Количество: {}, Предприятие: {}.".format(user['id'], user["name"], user["amount"], user["company"])
                Label(productsroot, text=txt).pack()


    def companies():
        def com():
            companiesroot = Toplevel(comroot)
            for user in collections.find({}):
                if user['company'] == e.get():
                    txt = "Идентификатор: {}. Тип: {}. Наименование: {}. Количество: {}, Предприятие: {}.".format(user['id'], user["type"],
                                                                                               user["name"],
                                                                                               user["amount"],
                                                                                               user["company"])
                    Label(companiesroot, text=txt).pack()



        comroot = Toplevel(chooseroot)
        Label(comroot, text="Введите наименование компании").pack()
        e = Entry(comroot, width=10)
        e.pack()
        Button(comroot, text="Поиск", command=com).pack()


    def searchproduct():
        def s():
            sroot = Toplevel(eroot)
            for user in collections.find({}):
                if user['name'] == ee.get():
                    txt = "Идентификатор: {}. Тип: {}. Наименование: {}. Количество: {}, Предприятие: {}.".format(user['id'], user["type"],
                                                                                               user["name"],
                                                                                               user["amount"],
                                                                                               user["company"])
                    Label(sroot, text=txt).pack()

        eroot = Toplevel(chooseroot)
        Label(eroot, text="Введите ИД товара").pack()
        ee = Entry(eroot, width=10)
        ee.pack()
        Button(eroot, text="Поиск", command=s).pack()


    chooseroot = Toplevel(root)
    Button(chooseroot, text="Отчёт по предприятию", command=companies).pack()
    Button(chooseroot, text="Отчёт по идентификатору", command=searchproduct).pack()
    Button(chooseroot, text="Отчёт по базе", command=products).pack()
    Button(chooseroot, text="Отчёт по продажам", command=prodaji).pack()
    Button(chooseroot, text="Отчёт по поставкам", command=postavki).pack()



def settings():
    def close():
        global mongourl
        mongourl = settingsurl.get()
        settingswindow.destroy()

    settingswindow = Toplevel(root)
    settingswindow.title("Настройки Mongo1C")
    settingswindow.protocol("WM_DELETE_WINDOW", close)
    settingsurl = Entry(settingswindow, width=15)
    settingsurl.insert(0, "localhost:27017")
    txt1 = Label(settingswindow, text="MongoDB Cluster URL")
    txt1.pack()
    settingsurl.pack()


#def ids():


def main():
    global root
    global collections
    global mongourl
    global types
    global ids


    root = Tk()
    root.title("Mongo 1C")
    root['bg'] = 'gray22'
#    root.state('zoomed')


    # Переменные...
    types = ["type", "name", "amount", "company"]


    # Кнопки и т.д.
    Button(root, text="+", fg="green", font="Arial 15", command=add).grid(column=0, row=0)
    Button(root, text="-", fg="red", font="Arial 15", command=rem).grid(column=1, row=0)
    Button(root, text="🛠", fg="gray", font="Arial 15", command=edit).grid(column=2, row=0)
    Button(root, text="🔍", fg="black", font="Arial 15", command=search).grid(column=3, row=0)
    Button(root, text="⚙", fg="black", font="Arial 15", command=settings).grid(column=4, row=0)


    # База данных
    mongourl = "localhost:27017"
    collections = pymongo.MongoClient(mongourl)["Mongo1C"]["Mongo1C Premium"]
    coll = pymongo.MongoClient(mongourl)["Mongo1C"]["Mongo1C Data"]
    #if coll.find({}) != {}:
    #    ids = coll.find({})[0]['ids']


    root.mainloop()


if __name__ == '__main__':
    main()
