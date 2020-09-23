# WAP to input cost of three product.
# Print total cost
# GST 18% 
# Discount 10%
# Net Amount..

print("Enter Cost of Products ")
p1 = int(input("Product 1 : "))
p2 = int(input("Product 2 : "))
p3 = int(input("Product 3 : "))

total = p1+p2+p3
gst = total * .18

net = total + gst
dis = net * .10

netamount = net - dis

print("Total Cost : ",total)
print("GST 18% : ",gst)
print("Net Total : ",net)
print("Discount 10% : ",dis)
print("Net Amount Pay : ",netamount)
