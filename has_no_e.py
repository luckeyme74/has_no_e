def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

word = "Jennifer"
print(has_no_e("Jennifer"))

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    print word

letter = "e"

fin = open('words.txt')
for line in fin:
    word = line.strip()
    find(word, letter)

