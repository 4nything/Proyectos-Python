mainText = ["On monday at 7:30pm, I was walking to ",
            " when I met my cousin ",
            " , and we started to talk. After 15 minutes talking, I remembered that I left the ",
            " in the oven, so I started to run to ",
            ". When I arrived there, a ",
            " was looking at me in a curious way. Then I realized that I have no cloth put on, so I covered with a ",
            " that I found on the ",
            ". All the people around were looking at me and laughing.",
            " After all, it was just a dream!!"]

arrWords = []

print("Welcome to 4nything-Mad-Libs! We can start playing!\nStart below: ")

arrWords.append(str(input("Give a place: ")))
arrWords.append(str(input("Give a name: ")))
arrWords.append(str(input("Give an object: ")))
arrWords.append(str(input("Give a place: ")))
arrWords.append(str(input("Give an animal: ")))
arrWords.append(str(input("Give an object: ")))
arrWords.append(
    str(input("Give an object that you can put something on it: ")))

finalText = mainText[0] + arrWords[0] + mainText[1] + arrWords[1] + mainText[2] + arrWords[2] + mainText[3] + arrWords[3] + mainText[4] + arrWords[4] + mainText[5] + arrWords[5] + mainText[6] + arrWords[6] + mainText[7] + mainText[8]

print("AND THE FINAL TEXT IS: \n"+finalText)