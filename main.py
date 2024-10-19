# This program is designed to extracts common ingredients used among two products.

from collections import Counter
import csv


# Function to read ingredients from the csv file
def read_ingredients_from_file(file_path):
   products = {}
   with open(file_path, newline='') as csvfile:
       reader = csv.reader(csvfile)
       next(reader) # skipping the header
       for row in reader: 
           products[row[0]] = row[1]

   return products
           

def common_ing_extractor(prod1_ingredients, prod2_ingredients):
    newstr1 = prod1_ingredients.replace(",", "") # Removes the comma from the list of ingredients
    newstr2 = prod2_ingredients.replace(",", "")
    counter = Counter(newstr1.split()) + Counter(newstr2.split())
    common_words = [word for word, count in counter.items() if count > 1] # Extracts the words that have occured more than once
    print(f'The ingredients used in both products are: ')
    print('\n'.join(common_words))


def main():
    file_path = 'products.csv'
    products = read_ingredients_from_file(file_path)
    
    prod1_name = input('Please enter the name of the first product: ')
    prod2_name = input('Please enter the name of the second product: ')

    if prod1_name in products and prod2_name in products:
        str1 = products[prod1_name]
        str2 = products[prod2_name]
       # print(f'Ingredients of {prod1_name}: {str1}')
       # print(f'Ingredients of {prod2_name}: {str2}')
        common_ing_extractor(str1, str2)
    else:
        print('One or both products not found in the CSV file.')

# Calling the main function
if __name__ == "__main__":
    print(f'---- Common Ingredients Extractor ----\nA program that simplifies and displays the similar products used in skin care as well as hair care products.\n')
    main()
