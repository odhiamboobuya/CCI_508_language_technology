# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from data_cleaning import clean_data

file_path = "TweetRaw.csv"


def main():
    condition = True
    while condition:
        print("""
        1.Data Cleaning
        2.POS tagging 
        3.Named Entity Recognition
        4.Parsing
        5.Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            clean_data(file_path)
        elif ans == "2":
            print("\n Pending implementation")
        elif ans == "3":
            print("\n Pending implementation")
        elif ans == "4":
            print("\n Pending implementation")
        elif ans == "5":
            print("\n Goodbye")
            condition = False
        else:
            print("\n Invalid selection. Please try again")


if __name__ == '__main__':
    main()
