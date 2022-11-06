import json
from product import *

CATEGORIES = [
    'Телівізор',
    'Холодильник',
    'Пральна машина',
]
BRANDS = [
    'Samsung',
    'Lg',
    'ElectroLux',
    'Gorenie',
    'Mulinex',
    'Sony'
]

WELCOMEMSG = """\
#---------------------------------------#
# Welcome to MYSHOP.UA                  #
#---------------------------------------#
# Make your choice:                     #
#   1.Print DB                          #
#   2.Load DB from file                 #
#   3.Save DB to file                   #
#   4.Add a new record to DB            #
#   5.Search in DB                      #
#   0.Exit                              #
#---------------------------------------#\
"""

DBFILENAME = 'DB.json'


def clean():
    print('\n' * 25)


def main():
    recordsList = []
    running = True
    while running:
        clean()
        print(WELCOMEMSG)
        choice = input('>')
        #
        if not choice.isdigit():
            continue
        choice = int(choice)
        if choice > 5 or choice < 0:
            continue

        # EXIT
        if choice == 0:
            print('GOOD BUY!!!')
            running = False
            continue

            # PRINT DB
        elif choice == 1:
            clean()
            if len(recordsList) == 0:
                print('DB is empty. Please load Db from file or add a new records')
                input()
                continue

            print('#-------------------------------------------------------------------------------#')
            print('# We have such goods in stock                                                   #')
            print('#-------------------------------------------------------------------------------#')
            for line in recordsList:
                print(f'#> {line}')
            input()

        # ADD A NEW LINE TO DB
        elif choice == 4:
            clean()
            while True:
                print("Please make choice category of product:")
                for i, cat in enumerate(CATEGORIES):
                    print(f'{i}> {cat}')
                catNum = int(input('->'))
                print("Please make choice brand of product:")
                for i, brn in enumerate(BRANDS):
                    print(f'{i}> {brn}')
                brandNum = int(input('->'))
                print("Please enter model of product:")
                model = input('->')
                print("Please enter price of product:")
                price = int(input('->'))
                print("Please enter quantity of product:")
                qty = int(input('->'))

                # TV
                if catNum == 0:
                    print("Please enter <diagonal>:")
                    diag = int(input("->"))
                    print("Please enter <resolution>:")
                    reso = str(input("->"))
                    newObj = Tv(CATEGORIES[catNum], BRANDS[brandNum], model, price, qty, diag, reso)

                    # Refrigerator
                elif catNum == 1:
                    print("Please enter <Volume>:")
                    volume = int(input("->"))
                    print("Please enter <Height>:")
                    height = int(input("->"))
                    newObj = Refrigerator(CATEGORIES[catNum], BRANDS[brandNum], model, price, qty, volume, height)

                # Washer
                elif catNum == 2:
                    print("Please enter <maxWeight>:")
                    maxW = int(input("->"))
                    print("Please enter <Class>:")
                    klass = input("->")
                    newObj = Washer(CATEGORIES[catNum], BRANDS[brandNum], model, price, qty, maxW, klass)

                recordsList.append(newObj)
                print("A new record was successfully added")
                print("Would you like to add one more record?(y/n):")
                if input("->") != 'y':
                    break


        # SAVE DB
        elif choice == 3:
            if len(recordsList) == 0:
                print("!!!We have no records to save!!!")
                input()
                continue
            try:
                with open(DBFILENAME, 'w') as DB:
                    json.dump(recordsList, DB, cls=CustomEncoder, indent=4)
            except:
                print("!!!ERROR!!!")
                input()
                continue
            print("DB was saved")


        # LOAD DB
        elif choice == 2:
            try:
                with open(DBFILENAME, 'r') as DB:
                    jsonData = json.load(DB)
                recordsList = []
            except:
                print("ERROR")
                input()
                continue
            # parse json
            for item in jsonData:
                newObj = decode(item)
                recordsList.append(newObj)

        # SEARCH IN DB
        elif choice == 5:
            clean()
            if len(recordsList) == 0:
                print('DB is empty. Please load DB from file or add a new records')
                input()
                continue

            print("Please make choice category of product:")
            for i, cat in enumerate(CATEGORIES):
                print(f'{i}> {cat}')
            catNum = int(input('->'))

            filterList = []
            for item in recordsList:
                if item.__dict__['category'] == CATEGORIES[catNum]:
                    filterList.append(item)

            if len(filterList) == 0:
                print('!!!We have no such records!!!')
                input()
                continue
            print(f'it was found {len(filterList)}')
            for item in filterList:
                print(f'# {item}')

            filterBy = dict(filterList[0].__dict__)
            filterBy.pop('category')
            filterBy = list(filterBy.keys())
            print("You can filter by:")
            for i, item in enumerate(filterBy):
                print(f'{i}> {item}')
            filterCat = int(input("->"))

            subResults = []
            for item in filterList:
                subResults.append(item.__dict__[filterBy[filterCat]])
            subResults = list(set(subResults))

            print(f'filtering by: {filterBy[filterCat]}')
            print(*subResults, sep='\n')
            print('Please choose one:')
            subFilter = input('->')
            for item in filterList:
                if str(item.__dict__[filterBy[filterCat]]) == subFilter:
                    print(item)
            input()


if __name__ == "__main__":
    main()
