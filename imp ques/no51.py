# 51.	Write a Python script to check if a given key already exists in a dictionary.

def check_key(dict,key):
    if key in dict:
        print("Present", end="")
        print("Value=",dict[key])
    else:
        print("not present")

dict={"a":100,"b":200,"c":300}
key= "b"
check_key(dict,key)
key="w"
check_key(dict,key)