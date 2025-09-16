
text = """It gave me a queer feeling. Yesterday or the day before, while I had been going about my business, quietly and in private, some unknown person -- some stranger -- had gone to the trouble of marking my name onto this envelope. Who was it who had had his mind's eye on me while I hadn't suspected a thing?

Still in my coat and hat, I sank onto the stair to read the letter. (I never read without making sure I am in a secure position. I have been like this ever since the age of seven when, sitting on a high wall and reading The Water Babies, I was so seduced by the descriptions of underwater life that I unconsciously relaxed my muscles. Instead of being held buoyant by the water that so vividly surrounded me in my mind, I plummeted to the ground and knocked myself out. I can still feel the scar under my fringe now. Reading can be dangerous.)

I opened the letter and pulled out a sheaf of half a dozen pages, all written in the same laborious script. Thanks to my work, I am experienced in the reading of difficult manuscripts. There is no great secret to it. Patience and practice are all that is required. That and the willingness to cultivate an inner eye. When you read a manuscript that has been damaged by water, fire, light or just the passing of the years, your eye needs to study not just the shape of the letters but other marks of production. The speed of the pen. The pressure of the hand on the page. Breaks and releases in the flow. You must relax. Think of nothing. Until you wake into a dream where you are at once a pen flying over vellum and the vellum itself with the touch of ink tickling your surface. Then you can read it. The intention of the writer, his thoughts, his hesitations, his longings and his meaning. You can read as clearly as if you were the very candlelight illuminating the page as the pen speeds over it.

Not that this letter was anything like as challenging as some. It began with a curt "Miss Lea"; thereafter the hieroglyphs resolved themselves quickly into characters, then words, then sentences.

"""


text = text.lower().split()

print(text)

for word in text:
    if len(word) >= 2:
        print(word)


import random

numbers1 = []
numbers2 = []
numbers = []

for i in range(30):
    numbers1.append(random.randint(100, 1000))


# print(numbers1)


def functie1():
    numbers_1 = [10, 20]
    numbers_2 = [30, 40]
    numbers_3 = [100]
    numbers_4 = [1000]
    return numbers_1, numbers_2, numbers_3, numbers_4

rezultat, rezultat_2, rezultat_3, rezultat_final = functie1()
print(rezultat_final)

n = []
n.sort()