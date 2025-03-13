newarray = ["IT", "ECE", "SWE", "WRE","ME", "MRE", "EE","ICE","A","CE"]
newarraylen =len(newarray)
new_array =[]
for index in range(newarraylen):
    elements = newarray[index]
    new_array.append(elements.lower())
for secondindex in range(len(new_array)):
    print(new_array[secondindex])