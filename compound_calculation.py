from prettytable import PrettyTable


#Table heading row
t = PrettyTable(['Years','Amount' ])

start_year = input("Starting Year(e.g. 2022): ")
start_amount = input("Starting principle amount: ")
percent = input("Percentage: ")
years = input("Total years: ")

try:
    start_year = int(start_year)
    start_amount = int(start_amount)
    percent = int(percent)
    years = int(years)
except Exception as f:
    print("Invalid input " + f)



def compound_cal(start_year,start_amount,percent,years):
    final_year = start_year + years
    t.add_row([start_year,"$"+str(f'{start_amount:,}')])

    while start_year <= final_year:
        interest = start_amount * percent // 100
        start_amount = interest + start_amount
        start_year+=1
        t.add_row([start_year,"$"+str(f'{start_amount:,}')])


    print(t)

if __name__ == '__main__':
    compound_cal(start_year,start_amount,percent,years)
