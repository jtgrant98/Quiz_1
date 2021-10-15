import Practice as x

def main():
    
    Brand_helmet = input("What is the brand of helmet you wear?")
    Model_hemlet = input("what is the model of helmet you wear?")


    Head_protection = x.Helmet(Brand_helmet,Model_hemlet)

    print('Here is the data you entered about your helmet')
    print('Brand:', Head_protection.get_brand())
    print('Model:', Head_protection.get_model())

main()
