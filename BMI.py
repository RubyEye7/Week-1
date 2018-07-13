def Response(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi <= 25:
        print("Average")
    elif bmi > 25:
        print("Overweight")


def BMImetric():
    height = float(input("enter height(m):"))
    weight = float(input("enter weight(kg):"))
    bmi = weight / height ** 2
    Response(bmi)
    print(bmi)


def BMIcustomary():
     height = float(input("enter height(in):"))
     weight = float(input("enter weight(lbs):"))
     bmi = (weight / height ** 2) * 703
     Response(bmi)
     print(bmi)


Unit = input("Customary or Metric:")
if Unit == "Customary":
    BMIcustomary()
elif Unit == "Metric":
    BMImetric()
