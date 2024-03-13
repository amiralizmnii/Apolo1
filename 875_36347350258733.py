#معرفي کلاس باکس به عنوان کلاس والد
class Box:
#تعيين ويژگي براي کلاس والد(باکس)
    Size="Each Side Of 10 cm."
    Shape="Cube"
    Color="Black"
    Serial_Number=231432
#معرفي کلاس وابسته يا تاس که از کلاس والد(باکس) ارث بري مي کند
class dice(Box):
    pass
#تعريف کردن يک کلاس جديد با نام سي  براي فراخواني ويژگي هاي کلاس والد
C=dice()
#فراخواني ويژگي هاي کلاس والد
print(C.Size)
print(C.Shape)
