print("Starbucks Cash Tips Calculater")
print("")

tips = float(input("Total Amount of Tips in $: "))
hours = float(input("Total Tippable Hours: "))
tip_per_hour = tips/hours

print("")

print("Type 'DONE' as a partner name once all partners have been accounted for ")
print("")

name = " "
total_twenties = 0 
total_tens = 0 
total_fives = 0 
total_toonies = 0 
total_loonies = 0 
total_quarters = 0
total_dimes = 0 
total_nickels = 0 

def calculate_change(amount):
    # Define the value of each coin type
    
    twenty = 20
    ten = 10
    five = 5
    toonie = 2
    loonie = 1
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    

    # Calculate the number of each coin type needed
    num_twenties = amount // twenty
    amount %= twenty
    
    num_tens = amount // ten
    amount %= ten
    
    num_fives = amount // five
    amount %= five
    
    num_toonies = amount // toonie
    amount %= toonie
    
    num_loonies = amount // loonie
    amount %= loonie
    
    num_quarters = amount // quarter
    amount %= quarter

    num_dimes = amount // dime
    amount %= dime

    num_nickels = amount // nickel
    amount %= nickel

    


    return num_twenties, num_tens, num_fives, num_toonies, num_loonies, num_quarters, num_dimes, num_nickels

while True:
  name = str(input("Partner Name: "))
  if name == "DONE" or name == "done":
    break
  part_hours = float(input('Number of hours '+name+ ' worked: '))
  part_tip = part_hours * tip_per_hour
  part_tip = round(part_tip/0.05) * 0.05
  print(name, round(part_tip, 2))
  
  num_twenties, num_tens, num_fives, num_toonies, num_loonies, num_quarters, num_dimes, num_nickels = calculate_change(part_tip)
 
  total_twenties = total_twenties + num_twenties
  total_tens = total_tens + num_tens
  total_fives = total_fives + num_fives
  total_toonies = total_toonies + num_toonies
  total_loonies = total_loonies + num_loonies
  total_quarters = total_quarters + num_quarters
  total_dimes = total_dimes + num_dimes
  total_nickels = total_nickels + num_nickels

  print("")
  

print("Change needed for everyone to get least amount of coins")
print("# of 20s", total_twenties)
print("# of 10s", total_tens)
print("# of 5s", total_fives)
print("# of toonies", total_toonies)
print("# of loonies", total_loonies)
print("# of quarters", total_quarters)
print("# of dimes", total_dimes)
print("# of nickels", total_nickels)
