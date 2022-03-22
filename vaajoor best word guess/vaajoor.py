from tkinter import W
import pandas as pd



def Best():
    dictionary = pd.read_excel(r'C:\Users\asus\Desktop\MAHDI,Central\Programming\github\Repositories\python-project\vaajoor best word guess\فایل-فرهنگ-فارسی.xlsx')
    words = dictionary['word']

    freq = "اینردمهوتبسشکزلگقفخعکحجآپچضطصغظثذذئژ"
    highScore = 1000000

    for word in words:

        word = word.replace(" ", "")
        if len(word) != 5:
            continue
        if len(set(list(word))) != 5:
            continue

        score = 0
        for char in word:
            if char in freq:
                score += freq.index(char)
            else:
                score += 100
        
        if score < highScore:
            print(word, score)
            highScore = score



def specific():
    dictionary = pd.read_excel(r'C:\Users\asus\Desktop\MAHDI,Central\Programming\github\Repositories\python-project\vaajoor best word guess\فایل-فرهنگ-فارسی.xlsx')
    words = dictionary['word']

    for word in words:

        word = word.replace(" ", "")
        if len(word) != 5:
            continue
        
        if len(set(list(word))) != 5:
            continue
        

# Best()
specific()








