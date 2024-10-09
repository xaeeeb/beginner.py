

while True :
    try:
        x= int(input("whats x ? "))
        


    except ValueError:
        print("X IS NOT AN INTEGER")

    else:
      break


print(f"x is {x}")