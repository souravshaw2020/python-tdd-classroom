class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        input_str=input_str[::-1]
        return input_str

    def is_english_vowel(self, character):
        if(character=='a' or character=='A' or character=='e' or character=='E' or character=='i' or character=='I' or character=='o' or character=='O' or character=='u' or character=='U'):
            boo=True
        else:
            boo=False
        return boo

    def find_longest_word(self, sentence):
        longest=max(sentence.split(),key=len)
        return longest

    def get_word_lengths(self, text):
        word=text.split()
        length=[]
        for i in word:
            length.append(len(i))
        return length