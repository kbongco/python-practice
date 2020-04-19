#Working through array leetcode explore
#Check if N and its double exist

def checkIfExist(self, arr) -> bool:
    double = set()
    for x in arr: 
        if x not in double:
            double.add(2*x)
            double.add(x/2)
        else:
            return True
    return False