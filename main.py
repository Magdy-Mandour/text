text = input('send message to magdy: ')
shopping_list = ["milk","eggs","toast","cheese","beef",
"chiken","pads","toilte paper","tea","coffee","tuna",
"bread","bread", "oil", "meat", "fish", "ice cream", "burger"]
x = []
def groceray(text):
    for i in shopping_list:
        if i in text:
            x = i
            print(x, end = " ")
groceray(text)
print('\nok,shut up, I will get it.')
