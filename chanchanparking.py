def info_push(Day, Time, Area, Plate):
    parkinginfo.append([str(Day), str(Time), str(Area), str(Plate)])
    calculatefee_start.append([str(Day), str(Time), str(Plate)])
    return

def info_output(Day, Time, Plate, i):
    calculatefee_finish.append([str(Day), str(Time), str(Plate)])
    parkinginfo.pop(i)
    return

def park(Day, Time, Area, Plate):
    #駐車開始
    for i in range(n+1):
        if Area in park_Area:    
            if Area not in parkinginfo[i][2] and Plate not in parkinginfo[i][3]:
                if i == len(parkinginfo) - 1:
                    print(Day, Time, Plate + " has parked at " + Area + ".")
                    info_push(Day, Time, Area, Plate)
                    break
                else:
                    continue
            elif Area in parkinginfo[i][2]:
                print(Day, Time + " Error: " + Area + " is occupied.")
            elif Plate in parkinginfo[i][3]:
                print(Day, Time + " Error: " + Plate + " is duplicated.")
            else:
                continue
        else:
            print(Day, Time + " Error: " + Area + " does not exist.")
        return
 
def unpark(Day, Time, Area, Plate):
    #駐車終了
    for i in range(n+1):
        if Area in park_Area:    
            if Area in parkinginfo[i][2] and Plate in parkinginfo[i][3]:
                print(Day, Time, Plate + " has unparked at " + Area + ".")
                info_output(Day, Time, Plate, i)
                break
            elif Area not in parkinginfo[i][2]:
                if i == len(parkinginfo) - 1:
                    print(Day, Time + " Error: " + Area + " is empty.")
                    break
                else:
                    continue
            elif Plate not in parkinginfo[i][3]:
                if i == len(parkinginfo) - 1:
                    print(Day, Time + " Error: " + Plate + " does not match.")
                    break
                else:
                    continue
            else:
                continue
        else:
            print(Day, Time + " Error: " + Area + " does not exist.")
        return

def calculatefee(Day, Time, Plate):
    #料金計算
    firstprice = 100
    for i in range(len(calculatefee_start)):
        if Plate in calculatefee_start[i][2]:
            for j in range(len(calculatefee_finish)):
                if Plate in calculatefee_finish[j][2]:
                    

                    print(Day, Time, Plate + " needs to pay " + str(price) + " (entered at " 
                        + calculatefee_start[i][0], calculatefee_start[i][1] + ").")
                else:
                    if j == len(calculatefee_finish) -1:
                        price = 100
                        print(Day, Time, Plate + " needs to pay a" + str(price) + " (entered at " 
                            + calculatefee_start[i][0], calculatefee_start[i][1] + ").")
                    else:
                        continue
        else:
            if i == len(calculatefee_start) -1:
                print(Day, Time, Plate + " has not unsettled fee.")
            else:
                continue
    return

def pay (Day, Time, Area, Plate):
    print("Hello world")

def pay_later(Day, Time, Area, Plate):
    print("Hello world")
    
def calculate_sales(Day, Time, Area, Plate):
    print("Hellow world")

n = int(input())
park_Area = []
for i in range(n):
    r = input()
    park_Area.append(r)
parkinginfo = [[''] * 4]
calculatefee_start = [[''] * 3]
calculatefee_finish = [[''] * 3]

while True:
    try:
        data = input().split()
        if not data:
            break  # 入力がもうない場合はループを終了
        if len(data) == 5:
            Type, Day, Time, Area, Plate = map(str, data)
        else:
            Type, Day, Time, Plate = map(str, data)
        
        if Type == 'park':
            park(Day, Time, Area, Plate)
        elif Type == 'unpark':
            unpark(Day, Time, Area, Plate)
        elif Type == 'calculate-fee':
            calculatefee(Day, Time, Plate)
        elif Type == 'pay':
            pay(Day, Time, Area, Plate)
        elif Type == 'pay-later':
            pay_later(Day, Time, Area, Plate)
        elif Type == 'calculate-sales':
            calculate_sales(Day, Time, Area, Plate)
        else:
            continue
    except EOFError:
        break  # EOFErrorが発生した場合はループを終了






