def openFile(name):
    tab = []
    file = open(name, "r")
    lines = file.readlines()
    for line in lines:
        surface = float(line.split()[0])
        prx = float(line.split()[1])
        tab.append([surface, prx])
    return tab


