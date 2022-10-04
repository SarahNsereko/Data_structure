lists = [["KATUKUNDA Rochelle","A94169","S21B23/016"],["NAJJOBA Tracy","A95681","S21B23/034"],
    ["MUGANGA Charles","A96447","J22B23/032"],
    ["NKATA Joshua Luyombya","A94161","S21B23/008"],
    ["MUKISA Isaiah","A94160","S21B23/007"],["Afghanistan",93],["Tiji",679],["Bahamas","1-242"],["Tanzania",255],["Saint Vincent and the Grenadines","1-784"],["Ukraine",380]]

def linearsearch(lists,value):
    for i in (lists):
        for j in i:#To iterate through the items of each individual list
            if value == j:
                return i #Return the entire list
    return "Not in the list" #If not found


print (linearsearch(lists,7))
print(linearsearch(lists,'A94160')) 
print(linearsearch(lists,380))
print(linearsearch(lists,"Doe"))

    
            