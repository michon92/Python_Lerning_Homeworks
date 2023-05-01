def count_words(filename):
    """obliczanie przybliżonej liczby słów w pliku tekstowym (książce np)"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"przepraszamy nie ma takiego pliku {filename}")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Plik {filename} zawiera {num_words} słów.")


filenames = ['anna_wikipedia.txt']
for filename in filenames:
    count_words(filename)