#just printing out some vars
var1 = "test"
var2 = "test2"
var3 = "test3"
print(var1, var2, var3)
#Print 3 lands hoved stad med x, y, z
x, y, z  = "Oslo", "Køpenhavn", "Stockholm"
print(z, y, z)
#Print en liste med land
land = ["Norge", "Danmark", "Svergie"]
x, y, x = land
print(x, y, z)

#Globale veriabler 
x = "Viego er best"
def myfunc():
    print("hvem er best? " + x)
myfunc()
#Det globale nøkkelordet
def myfunc2():
    global x
    x = "Norge er kult"
myfunc2()
print("hvilket land er kult? " + x)
#Data typer
x0 = b"hello"
print(type(x0))
x1 = "Hello World"
print(type(x1))
x2 = 2
print(type(x2))
x3 = 2.5
print(type(x3))
x4 = range(8)
print(type(x4))