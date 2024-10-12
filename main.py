# This program is designed to identify shared ingredients between two distinct skincare products.

from collections import Counter

'''Snail Secretion Filtrate, Betaine, Butylene Glycol, 1,2-Hexanediol, Sodium Hyaluronate, 
    Panthenol, Arginine, Allantoin, Ethyl Hexanediol, 
    Sodium Polyacrylate, Carbomer, Phenoxyethanol'''

'''Aqua (Water), Glycerin, Alcohol Denat, Ethylhexyl Palmitate, Hexylene Glycol, 
    Triethanolamine, Betaine, Sodium Ascorbyl Phosphate (Vitamin C), Niacinamide (Vitamin B3), 
    Tocopheryl Acetate (Vitamin E), Calcium Pantothenate (Vitamin B5), Pyridoxine Hydrochloride (Vitamin B6), 
    Panthenol (Pro-Vitamin B5), Maltodextrin, Sodium Starch Octenylsuccinate, Silica, 
    Prunus Amygdalus Dulcis (Sweet Almond) Oil, Vitis Vinifera (Grape) Seed Oil, 
    Persea Gratissima (Avocado) Oil, Carbomer, Parfum (Fragrance), 
    Salicylic Acid, Disodium EDTA, Phenoxyethanol, Ethylhexylglycerin, 
    Citral, Citronellol, Hexyl Cinnamal, 
    Limonene, Linalool'''
# Asking the user to input names and ingredients in the products

# Product 1's name and ingredients
prodname1 = input('Please enter the name of first product: ') 
str1 = input(f'Enter ingredients of {prodname1}: ')

# Product 2's name and ingredients
prodname2 = input('Please enter the name of second product: ') # product name 2
str2 = input(f'\nEnter ingredients of {prodname2}: ')

def Common_ing_extractor(product1, product2):

    newstr1 = str1.replace(",", "") # Removes the comma from the list of ingredients
    newstr2 = str2.replace(",", "")
    counter = Counter(newstr1.split()) + Counter(newstr2.split())
    common_words = [word for word, count in counter.items() if count > 1] # Extracts the words that have occured more than once
    

    print(f'The ingredients used in both {prodname1} and {prodname2} are: ')
    print('\n'.join(common_words))


# calling the function
print(f'---- Common Ingredients Extractor ----\nWelcome to the program that extracts the ingredients that have occured in both the products.\n')
Common_ing_extractor(str1, str2)

