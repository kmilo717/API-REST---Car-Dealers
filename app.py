from flask import Flask, request

app = Flask(__name__)

#JSON dictionary
carDealers = [
    {
        "nameDealer": "Example Dealer",
        "products": [
            {
                "nameProduct": "Example Car",
                "price": 0.00
            }
        ]
    }
]

#Query all the dealers list with their products
@app.get("/dealer")
def getCarDealer():
    return {"Dealers": carDealers}


#Add a new dealer
@app.post("/dealer")
def createCarDealer():
    requestData = request.get_json()
    newDealer = {"nameDealer": requestData ["nameDealer"], "products": []}
    carDealers.append(newDealer)
    return newDealer, 201


#Add products to a dealer
@app.post("/dealer/<string:nameDealer>/products")
def createProduct(nameDealer):
    requestData = request.get_json()
    for dealer in carDealers:
        if dealer["nameDealer"] == nameDealer:
            newProduct = {"nameProduct": requestData["nameProduct"], "price": requestData["price"]}
            dealer["products"].append(newProduct)
            return newProduct
    return {"message": "Dealer not found"}, 404


#Query a particular dealer
@app.get("/dealer/<string:nameDealer>")
def getStore(nameDealer):
    for dealer in carDealers:
        if dealer["nameDealer"] == nameDealer:
            return dealer
    return {"message": "Dealer not found"}, 404


#Query the products of a dealer
@app.get("/dealer/<string:nameDealer>/products")
def getProductInDealer(nameDealer):
    for dealer in carDealers:
        if dealer["nameDealer"] == nameDealer:
            return {"products": dealer["products"]}
    return {"message": "Dealer not found"}, 404