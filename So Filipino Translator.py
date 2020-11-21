import csv

while True:
    display = input('Mabuhay! Press enter to continue ')
    print('-------------------- Mabuhay Sa Main Menu -------------------- \n\
        Enter an option of your choice \n\
        1. English to Tagalog (most common dialect) \n\
        2. English to Bisaya/Cebuano (predominantly spoken in the Visayas region and parts of northern Mindanao, most notably the island of Cebu) \n\
        3. English to Waray (Predominantly spoken in the islands of Samar and Leyte')
    
    try:
        choice = int(input('Choice: '))

        if choice == 1:
            with open('English2Tagalog.csv','r') as eng:
                reader = csv.reader(eng, delimiter = ',')
                print('English to Tagalog')
                find_word = input('Enter a Word or Phrase: ')
                for line in reader:
                    if line[0] == find_word.lower() :
                        print(find_word.lower(), ':', line[1])

        elif choice == 2:
            with open('English2Bisaya.csv','r') as aln:
                reader = csv.reader(aln, delimiter = ',')
                print('English to Bisaya')
                find_word = input('Enter a Word or Phrase: ')
                for line in reader:
                    if line[0] == find_word.lower():
                        print(find_word, ':', line[1])

        elif choice == 3:
            with open('English2Waray.csv','r') as aln:
                reader = csv.reader(aln, delimiter = ',')
                print('English to Waray')
                find_word = input('Enter a Word or Phrase: ')
                for line in reader:
                    if line[0] == find_word.lower():
                        print(find_word, ':', line[1])
        
        else:
            print('Invalid entry. Please try again.')


    except ValueError:
        print('Invalid entry')
    except:
        print('An error has occured')
