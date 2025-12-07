print("Enter Marks obtained in 4 Subjects: ")
Math = int(input("Math :"))
English = int(input("English :"))
Hindi = int(input("Hindi :"))
Science = int(input("Science :"))
sum = English+Hindi+Math+Science
print("sum of Math,English,Hindi and Science")
perc = (sum/400)*100
print(end="Percantage Mark = ")
print(perc)