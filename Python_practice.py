print("Hello World")
counties = ["arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties:
    print(county)
    
for i in range(len(counties)):
    print(counties[i])