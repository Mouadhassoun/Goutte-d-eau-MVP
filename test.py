import os 

print("1 " + os.path.abspath(__file__))
print("2 " + os.getcwd())
print("3 " + os.path.dirname(os.path.abspath(__file__)))