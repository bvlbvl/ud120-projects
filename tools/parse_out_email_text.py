#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f, second_part=0):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        if second_part == 0:
            words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        elif second_part == 1:
            print "i'm in 2nd part"
            text_string_split = text_string.split(" ")
            #print text_string_split
            from nltk.stem.snowball import SnowballStemmer
            stemmer = SnowballStemmer("english")
            for word in text_string_split:
                word = stemmer.stem(word)
                #print word
                words+=" "+ word
                
        else:
            from nltk.stem.snowball import SnowballStemmer
            stemmer = SnowballStemmer("english")
            words = ' '.join([stemmer.stem(w.strip()) for w in text_string.split()])




    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text
    text = parseOutText(ff, second_part=1)
    print text
    text = parseOutText(ff, second_part=2)
    print text



if __name__ == '__main__':
    main()

