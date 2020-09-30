import csv

def csv_read():
    f = open("hello_world.csv",'w+')
    w = csv.writer(f)
    w.writerow(["hexiaohan",22])
    w.writerows([{"zhangsan",23},{"lisi",33}])
    f.close()
    pass
if __name__ == "__main__":
    f = open("hello_world.csv","r")
    r = csv.reader(f)
    print("this r is {} and the type of r is {}".format(r,type(r)))

    for data in r:
        print(data)
    pass

