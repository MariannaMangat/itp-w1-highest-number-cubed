"""This is the entry point of the program."""


# def highest_number_cubed(limit):
#     num = 1
#     while num <= limit:
#         num = num **3
#         num += 1
        
#     return limit
        
def highest_number_cubed(limit):
    prenum = 1
    
    while True:
        nownum = prenum +1
        if nownum **3 > limit:
            return prenum
            
        prenum = nownum
        
