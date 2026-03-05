grocery_list=[]
choice=0
print("Welocme to your shopping List!")
while choice!=4:
    print("1) Add item")
    print("2) Check off item")
    print("3) Print list")
    print("4) Exit")

    choice=int(input("Enter a choice: "))

    if choice==1:
        item=input("What will you add to the list?: ")
        grocery_list.append(item)

    elif choice==2:
        if len(grocery_list)!=0:
            check_out=int(input("Which item will you check off?: "))
            index=check_out-1

            if 0<= index < len(grocery_list):
                item=grocery_list[index]

                if len(item) > 2:
                    middle="-" * (len(item)-2)
                    item=item[0] + middle + item[-1]

                grocery_list[index] = item

    elif choice == 3:
          if len(grocery_list)!=0:
              print("Here is your list:")
              i=0
              while i < len(grocery_list):
                  print(str(i+1) + ") " + grocery_list[i])
                  i += 1
    else:
          print("Goodbye!")
    
