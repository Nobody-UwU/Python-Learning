cardetail = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
}
print(cardetail["brand"])
print(len(cardetail))
print(type(cardetail))
x = cardetail.keys()
y= cardetail.values()
z= cardetail.items()
print(x,y,z)
cardetail["color"]="white"
print(x,y,z)
if "brand" in cardetail:
  print("Yes, 'model' is one of the keys in the cardetails dictionary")