def checkingDataType(variablename):
    if type(variablename) == int:
        print("variable type is int and value is ",variablename)
    elif type(variablename) == float:
        print("variable type is float and value is ",variablename)
    elif type(variablename) == complex:
        print("variable type is complex and value is ",variablename)
    elif type(variablename) == list:
        print("variable type is list and value is ",variablename)
    elif type(variablename) == tuple:
        print("variable type is tuple and value is ",variablename)
    elif type(variablename) == bool:
        print("variable type is bool and value is ",variablename)
    elif type(variablename) == set:
        print("variable type is set and value is ",variablename)

checkingDataType(10)
checkingDataType(14.6)
checkingDataType(True)
checkingDataType(complex(3,5))
checkingDataType([3,5,6])
checkingDataType((9,1,19.0))
checkingDataType({"Raghu","Satya","priya","Bhanu"})






