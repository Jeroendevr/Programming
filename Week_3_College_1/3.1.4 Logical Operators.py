__author__ = 'jeroendevries'
chipkaart = [124576
       ,795834
       ,890432
       ,907251]
for x in chipkaart:
    if ("4" in str(x)) and (x % 3 == 0):
        print(str(x) + " Korting")
    else:
        print(x)