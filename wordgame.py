import random
import time


eng_words = ['Hi','Bye','Task', 'Programm']
tr_words = ['Merhaba','Hoşça kalın','Görev', 'Program']
score = 0
while True:
    mode = input("Bir mod seçin: Yeni kelimeler eklemek için 0, çeviri yapmak için 1,çıkmak için 2: \n")
    while ((mode!="1") and (mode!="2") and (mode!="0")):
        mode=input("Geçersiz. Yeni kelimeler eklemek için 0, çeviri yapmak için 1,çıkmak için 2: \n")
    if mode == "0":
        word = input("İngilizce bir kelime yazın: ")
        translate = input("Kelimenin tercümesini yazın: ")
        if len(word) > 0 and len(translate) > 0:
            eng_words.append(word)
            tr_words.append(translate)
            print("Kelime başarıyla eklendi!")
    elif mode == "1":
        print("Çevirebildiğiniz kadar kelime çevirin! 10 hakkınız var!")
        for i in range(10):
            number = random.randint(0, len(eng_words)-1)
            print("Tercümesi bu şekilde olmalı: " + eng_words[number])
            if input() == tr_words[number]:
                print("Harika!!!")
                score += 2
            else:
                print("Bir yanlışlık var... Doğru kelime - " + tr_words[number])
                score -= 1
    elif mode == "2":
        break
    time.sleep(0.5)
print("Tebrikler!! puanınız", score)
