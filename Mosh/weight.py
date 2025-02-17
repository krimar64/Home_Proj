weight = float(input("What is your weight: "))
unit = input("(K)g or (P)ounds? ")
if unit.upper() == "K":
    weight_conv = weight * 2
else:
    weight_conv = weight / 2
print("weight_conv= " + str(weight_conv) + " Kg")