flag = input("what flag do you want to check for (case senstive):\n")
newfile = open(flag+".json", "w")

newfile.write("[")
with open("raw.txt") as fileobject:
  for line in fileobject:
      if flag in line:
        print(line)
        newline = line.rstrip("\r\n") + ",\n"
        newfile.write(newline)

newfile.write("]")
newfile.close()