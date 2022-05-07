def readFiles(filename):
    rule =[]
    mylines = []
    with open(filename) as file:
        mylines = file.readlines()
        for myline in mylines:
          if myline.strip():
            if not myline.startswith('#'):
                address = myline.split(',')[1]
                rule.append(address)
        return rule
libyrule = readFiles("Liby.list")
nobydarule = readFiles("AdRule.list")
for address in libyrule:
    if address not in nobydarule:
        with open("Liby.list") as file:
            mylines = file.readlines()
            for myline in mylines:
              if myline.strip():
                if not myline.startswith('#'):
                  if address == myline.split(',')[1]:
                    print(myline)
