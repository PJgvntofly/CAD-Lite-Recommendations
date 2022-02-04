from multiprocessing.connection import wait
import recommendations

call_type = input("Enter the call type:")
grid = input("Enter the fire grid:")

print(recommendations.recommendations(call_type,grid))

input('Hit enter to close')