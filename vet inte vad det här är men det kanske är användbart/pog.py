class Wares:
    def __init__(self, code, name, price, amount):
        self.code = code
        self.name = name
        self.price = price
        self.amount = amount


def scan_inventory():
    line_order = 0
    temp_list = []
    ware_list = []
    with open("wareList.txt", "r") as f:  # öppnar filen
        lines = f.readlines()  # gör en lista av raderna i textfilen
        for line in lines:
            line_order += 1
            temp_value = line.replace("\n", "")
            if line_order == 1:  # code
                temp_list.append(temp_value)
            if line_order == 2:  # name
                temp_list.append(temp_value)
            if line_order == 3:  # price and amount
                temp_value_split = temp_value.split(" ")
                temp_list.append(temp_value_split[0])
                temp_list.append(int(temp_value_split[1]))
                ware_class_temp = Wares(temp_list[0], temp_list[1], temp_list[2], temp_list[3])
                ware_list.append(ware_class_temp)
                temp_list = []
                line_order = 0
        return ware_list


def take_input(ware_list):
    scanned_information = [[], [], []]
    already_scanned_list = []  # these need to be initiated before the loop
    while True:
        recent_scan = input()
        if recent_scan == "#":  # if a pound is found, the loop is broken and the program continues
            break
        scanned_code, scanned_amount = assign_values(recent_scan)
        handle_scan(scanned_code, scanned_amount, ware_list, scanned_information, already_scanned_list)
    return scanned_information


def handle_scan(scanned_code, scanned_amount, ware_list, scanned_information,
                already_scanned_list):  # names, amounts, prices
    already_scanned = False
    valid_check = 0
    if scanned_amount != 0:  # if an invalid amount is entered (such as "iaulgwdagi"), the loop breaks and starts over from the input. (scanned_amount is assigned the value 0 if an invalid amount is entered)
        for i in range(len(ware_list)):  # search through all the wares
            if scanned_code == ware_list[i].code:  # for a matching code
                valid_check = 0

                if scanned_amount <= ware_list[
                    i].amount:  # you can only buy an amount that is smaller or equal to the amount availible

                    ware_list[i].amount -= scanned_amount  # remove the scanned amount from the amount in storage
                    already_scanned = already_scanned_func(already_scanned_list, scanned_amount, scanned_code,
                                                           scanned_information,
                                                           already_scanned)  # check if the code has already been scanned

                    if already_scanned:  # if it already has been scanned, dont append its value to the list
                        break
                    if already_scanned == False:
                        append_ware(scanned_amount, already_scanned_list, scanned_code, scanned_information, ware_list,
                                    i)
                        print(already_scanned_list)
                    already_scanned = False
                else:
                    print("insufficent amounts of the products currently in storage. Current amount is", end=" ")
                    print(ware_list[i].amount)
            else:
                valid_check += 1

        if valid_check == len(ware_list):
            # every time the loop is executed,
            # which in other words is every time a ware is checked in the database to see if the codes match, valid check increments.
            # if the amount of loops is equal to the amount of wares and no code match is found, then the code is invalid
            print("please enter a valid code")


def assign_values(recent_scan):
    split_scan = recent_scan.split(" ")  # split the input into two values, the code for the product and the amount
    scanned_code = split_scan[0]
    scanned_amount = assign_amount(split_scan)  # assign the correct amount
    return [scanned_code, scanned_amount]


def assign_amount(split_scan):
    if len(split_scan) == 1:
        return int(1)
    if len(split_scan) > 2:
        print("Too many inputs, please try again")
        return 0
    else:
        try:
            return int(split_scan[1])
        except ValueError:  # if the value entered is not applicaple, such as inte the case of a string, the program returns an error message
            print("please enter a valid amount")
            return 0


def already_scanned_func(already_scanned_list, scanned_amount, scanned_code, scanned_information, already_scanned):
    for j in range(len(already_scanned_list)):
        if already_scanned_list[j] == scanned_code:
            scanned_information[1][j] += scanned_amount  # Här är index väldigt viktig
            if scanned_information[1][j] <= 0:
                del already_scanned_list[j]
                del scanned_information[0][j]  # name
                del scanned_information[1][j]  # amount
                del scanned_information[2][j]  # price
            return True
    return False


def append_ware(scanned_amount, already_scanned_list, scanned_code, scanned_information, ware_list, i):
    if scanned_amount >= 1:
        already_scanned_list.append(scanned_code)
        print(already_scanned_list)
        scanned_information[0].append(ware_list[i].name)  # name
        scanned_information[1].append(scanned_amount)  # amount
        scanned_information[2].append(ware_list[i].price)  # price
    else:
        print("Please enter a positive value")


def print_receipt(scanned_information):
    total_amount = 0
    total_value = 0
    print("_______________________________________________")
    print("{0:<15}{1:<15}{2:<10}{3}".format("Varunamn", "Antal", "A-pris", "Summa"))
    print("-----------------------------------------------")
    if scanned_information != [[], [], []]:
        for i in range(len(scanned_information[0])):
            print("{0:<15}{1:<15}{2:<10.2f}{3:.2f}".format(scanned_information[0][i], scanned_information[1][i],
                                                           float(scanned_information[2][i]),
                                                           float(scanned_information[1][i]) * float(
                                                               scanned_information[2][i])))
            total_amount += scanned_information[1][i]
            total_value += float(scanned_information[1][i]) * float(scanned_information[2][i])
        print("===============================================")
        print("{0:<15}{1:<25}{2:.2f}".format("Total", total_amount, total_value))
    else:
        print("===============================================")


def save_information(ware_list, scanned_information):
    pass


def main():
    ware_list = scan_inventory()
    scanned_information = take_input(ware_list)
    print_receipt(scanned_information)


main()





