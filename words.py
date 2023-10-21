def print_upper_words(name, must_start_with):
    '''first pass in your list and then pass in the letters you need the words to start with and itll print them all upper case and will only print the words beginning in the letters you selected'''
    for n in name:
     for l in must_start_with:
       if n.startswith(l):
        print(n.upper())
  



