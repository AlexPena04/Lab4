a=input("how mant parts do you need?")
b=(input)("Is it 1 day, 3 day, 5 day or 7 day shipping?")
int_parts=int(a)
int_ship=int(b)
if int_parts <=9:
    part=29.95
    print("Your total for parts are 29.95")
    if int_ship==1:
        ship=29.94
        print("The shipping price is 29.94")
        print("Your total is")
        print(ship+part)
    if int_ship==3:
        ship=12.84
        print("The shipping price is 12.84")
        print("Your total is")
        print(ship+part)
    if int_ship==5:
        ship=9.60
        print("The shipping price is 9.60")
        print("Your total is")
        print(ship+part)
    if int_ship==7:
        ship=4.72
        print("The shipping price is 4.72")
        print("Your total is")
        print(ship+part)
if int_parts > 9 and int_parts <= 20:
    print("Your total for parts are 26.96")
    part1=26.96
    if int_ship==1:
        ship=29.94
        print("The shipping price is 29.94")
        print("Your total is")
        print(ship+part1)
    if int_ship==3:
        ship=12.84
        print("The shipping price is 12.84")
        print("Your total is")
        print(ship+part1)
    if int_ship==5:
        ship=9.60
        print("The shipping price is 9.60")
        print("Your total is")
        print(ship+part1)
    if int_ship==7:
        ship=4.72
        print("The shipping price is 4.72")
        print("Your total is:")
        print(ship+part1)

if int_parts >=21:
    part2=26.96
    print("Price for partsis 26.96")

    if int_ship==1:
        ship=36.81
        print("The shipping total is 36.81")
        print("Your total is")
        print(ship+part2)
    if int_ship==3:
        ship=16.46
        print("The shipping total is 16.46")
        print("Your total is")
        print(ship+part2)
    if int_ship==5:
        ship=17.50
        print("The shipping total is 17.50")
        print("Your total is")
        print(ship+part2)
    if int_ship==7:
        ship=10.94
        print("The shipping total is 10.94")
        print("Your total is")
        print(ship+part2)
