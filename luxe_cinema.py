import mysql.connector
import csv

'''

Luxe-1,5
Luxe-1,20
Luxe-1,77
Luxe-1,97
luxe-1,99

'''

def read_file():
    seats_booked = []

    try:
        file = open(r'C:\Users\kisho\PycharmProjects\cross_platform_testing\cinema_luxe.csv')
        rows = csv.reader(file)
        for x in rows:
            seats_booked.append(int(x[1]))
        return seats_booked



    except Exception as e:
        print(e)


if __name__ == '__main__':
    seats_available = []
    seats_booked = read_file()
    print(seats_booked)
    for x in range(1, 101):
        if x in seats_booked:
            pass
        else:
            seats_available.append(x)
    print(seats_available)
