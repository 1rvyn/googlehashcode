def parse_input(filename):
    good = []
    bad =[]
    current = {"bad", "good"}
    size = 0
    with open(filename) as file:
        size += int(file.readline())

        for size, line in enumerate(file):
            if size % 2 != 0 and size != 0:
                # print("odd")
                line.strip()
                line=line[1:].strip().split(' ')
                for i in line:
                    if i == "":
                        print("empty line")
                    else:
                        bad.append(i)
            elif size % 2 == 0:
                # print("even")
                line.strip()
                line=line[1:].strip().split(' ')
                for i in line:
                    good.append(i)
    for i in good:
        print("good " +i)  

    for i in bad:
        print("bad " + i)

parse_input("/Users/irvyn/Desktop/hashcode/input_data/d_difficult.in.txt")
