def count_vowels(text):
    vowels= set("aeiouAEIOU")
    count=0
    unique_vowels= set()
    for char in text:
        if char in vowels:
            count+=1
            unique_vowels.add(char.lower())
    return count , unique_vowels
