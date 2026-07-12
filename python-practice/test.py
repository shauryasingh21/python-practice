#  text = "Python is awesome"
# upperCase= text.upper()
# lowerCase= text.lower()
# print("uppercase: "+upperCase+" and lowerCase: "+lowerCase)
# new_text= text.replace("awesome", "great")
# print("text: ", text)
# print(new_text)
# words=text.split()
# print("words: ",words)
# text1 = "   Some spaces around   "
# stripped_text=text1.strip()
# print("stripped_text:",stripped_text)

# text = "Python is awesome"
# if 'is' in text:
#     print("substring is present in the string")
# num1=10
# num2=8
# result=num1//num2
# print(result)
# result1=num1%num2
# print(result1)
# x=20
# def my_function():
#     x=10
#     print(x)
# my_function()
# print(x)

# def greet(name):
#     return f"this is my function, {name}!"
# message= greet("shaurya")
# print(message)

# import my_module
# result=module.square(5)
# print(result)
# print(module.pi)

# x=int(input("Enter the value:"))
# if x>10:
#     print("x is greater")
# elif(x==10):
#     print("x is equal to 10")
# else:
#     print("x is less than 10")

# x=[1,2,3,4,5]
# print(len(x))
# x.append(6)
# print(x)
# x.remove(2)
# print(x)
# subset=x[0:3]
# print(subset)
count = 0
# while count < 5:
#     print("Shaurya")
#     count+=1

# num=[1,2,3,4,5]
# for num in num:
#     if num==3:
#         break
#     print(num)

# num=[1,2,3,4,5]
# for num in num:
#     if num==3:
#         continue
#     print(num)

# log_file = [
#    "INFO: Operation successful",
#    "ERROR: File not found",
#    "DEBUG: Connection established",
#    "ERROR: Database connection failed",
# ]
# for line in log_file:
#     if "ERROR" in line:
#         print(line)

import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()