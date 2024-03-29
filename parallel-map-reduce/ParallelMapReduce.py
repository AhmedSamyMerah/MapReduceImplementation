import multiprocessing
import string
import SimpleMapReduce
import time

def file_to_words(filename):
    STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in', 
            'is', 'it', 'i', 't','s','on','m','of', 'or', 'py', 'rst', 'that', 'the', 'but'
            ])
    TR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    print (multiprocessing.current_process().name, 'reading', filename)
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'): # Skip rst comment lines
                continue
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append( (word, 1) )
    return output


def count_words(item):
    word, occurances = item
    return (word, sum(occurances))


if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('*.txt')
    
    mapper = SimpleMapReduce.SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()
    
    print ('\nTOP 10 WORDS Kanye says\n')
    top10 = word_counts[:10]
    longest = max(len(word) for word, count in top10)
    for word, count in top10:
        print ('%-*s: %5s' % (longest+1, word, count))

#time in seconds
print(time.process_time(), " Seconds")