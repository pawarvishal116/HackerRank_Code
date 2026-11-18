file = "First python tutorial [first] #1.py"
number = file.split("#")[1].split(".")[0]
print(number)
word = file.split("[")[1].split("]")[0]
print(word)

files = [
    "Python Tutorial #15 ｜ English.mp4",
    "Python Tutorial #16 ｜ English.mp4",
    "Python Tutorial #17 ｜ English.mp4"
]

for file in files:
    number = file.split("#")[1].split(" ")[0]
    print(number)