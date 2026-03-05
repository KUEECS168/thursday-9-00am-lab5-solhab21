planets=[]
mission_over= "n"

while mission_over != "y" and mission_over !="Y":
    name=input("Enter planet name: ")
    planets.append(name)

    mission_over=input("Is the mission over?(y/n): ")
    
find=input("Which planet do you want the neighbours for?: ")

print("Planets neignbouring" + find + ":")

i=0
found=False

while i< len(planets):
    if planets[i].lower() == find.lower():
        found=True

        if i - 1 >= 0:
            print("    " + planets[i-1])

        if i+1 <  len(planets):
            print("    " + planets[i+1])

    i +=1
    
print("Program ending...")    

        
    

