from flask import *
import resources.modules.database as db


def storeFeedback_(request):
    # Get Data from all contact forms
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('Subject')
    message = request.form.get('message')
    db.runDBQuery(
        db.users_db, f'INSERT INTO FeedBack ("email", "Subject", "message", "Name") VALUES' f' ("{email}", "{subject}", "{message}", "{name}");')

    return render_template('/ParentDashboard/success.html')

def getLessonData(subject, dbpath, classId):
    # Get lesson data from database
    lessonData = db.runDBQuery(dbpath, f'SELECT * FROM P{classId};')
    print(lessonData)


# Store data from form into inventory table
def storeInventory_(request):
    # Get Data from all contact forms
    itemname = request.form.get('itemname')
    itemprice = request.form.get('itemprice')
    itemquantity = request.form.get('itemquantity')
    itemdetails = request.form.get('itemdetails')
    itemimage = request.form.get('itemimage')
    db.runDBQuery(
        '/Sales.db3', f'INSERT INTO Inventory ("ItemName", "ItemPrice", "ItemQauntity", "ItemDetails", "ItemImage") VALUES' f' ("{itemname}", "{itemprice}", "{itemquantity}", "{itemdetails}", "{itemimage}");')

    return render_template('/ParentDashboard/success.html')

# Get data from inventory table
def getInventoryData():
    # Get inventory from database
    inventoryData = db.runDBQuery('databank/Sales.db3', f'SELECT * FROM Inventory;')
    return inventoryData


# Store sales data from form into bookshop sales table
def storeBookShopSales_(request):
    # Get Data from all contact forms
    buyer = session.get('user')
    itemname = request.args.get('itemname')
    price = request.args.get('price')
    quantity = request.args.get('quantity')
    contactdetails = request.args.get('contactdetails')
    db.runDBQuery(
        db.users_db, f'INSERT INTO BookShopSales ("ItemName", "Price", "Quantity", "Buyer", "ContactDetails") VALUES' f' ("{itemname}", "{price}", "{quantity}", "{buyer}", "{contactdetails}");')

    return render_template('/ParentDashboard/success.html')

# Get unique teacher users
def getTeacherUsers(dbpath):
    return db.runDBQuery(dbpath, f'''SELECT DISTINCT sender FROM chats WHERE receiver="session['user'']";''')
