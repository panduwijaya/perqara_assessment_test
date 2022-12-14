from libs.fraud_notification import fraudNotif
from libs.queen import queen

# example
print("Fraud Test Case 1: ", fraudNotif(3, [10, 20, 30, 40, 50]))
# sample input 0 
print("Fraud Test Case 2: ", fraudNotif(5, [2, 3, 4, 2, 3, 6, 8, 4, 5]))
# sample input 1
print("Fraud Test Case 3: ", fraudNotif(4, [1, 2, 3, 4, 4]))

# sample input
obs = [[5,5], [4,2], [2,3]]
print("Queen Attack Test Case: ",queen(5, 3, 4, 3, obs))