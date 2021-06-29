#grading program
import pyfiglet
  
result = pyfiglet.figlet_format("Silent Bidding")
print(result)   
bidder_info={"Name":[],"price":[]}
n=0
while(True):
    n+=1
    name=input("Enter your name ")
    bid=input("Enter your bidding amount in $ ")
    bidder_info["Name"].append(name)
    bidder_info["price"].append(bid)
    choice=input("Do you want to ente more?")
    if(choice!="yes"):
        break

print(f'Highest bidder is {bidder_info["Name"][-1]} and highest bidding price is {bidder_info["price"][-1]}')


    