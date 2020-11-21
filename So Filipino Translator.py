        elif choice == 3:
            with open('English2Waray.csv','r') as aln:
                reader = csv.reader(aln, delimiter = ',')
                print('English to Waray')
                find_word = input('Enter a Word or Phrase: ')
                for line in reader:
                    if line[0] == find_word.lower():
                        print(find_word, ':', line[1])
