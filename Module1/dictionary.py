# dictionary
car= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1990,
  "price": 1000000,
}
car["color"] = "red"
print(car)
print(car.keys())
itemList =car.items()
print(itemList)
if("milage" in car) :
    print(f"cars price is {car['price']}.")
else:
    print("This sections info is not provided.")

# can update a value
car.update({"year" : 2001})
del car["model"]
car.pop("color")
car.popitem() # pops the last inserted element
print(car)

# ways to copy dict
#newCar= car.copy()
#newCar= dict(car)