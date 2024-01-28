#Create a program that checks if a year is a leap year.
#i: number(int) o: boolean

def leap_year(year):
    #the year can be divisible by 4
    #except that it is divisible by 100
    #unless that it is also divisibl by 400
    
    #check with 4: no, not a leap year; 
    # yes, check with 100, yes, not a leap year; 
    # no, check with 400, yes, a leap year; no, not a leap year
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        


#test cases
# print(leap_year(2000)) #it should return true
# print(leap_year(1900)) #it should return false
# print(leap_year(2012)) #it should return true