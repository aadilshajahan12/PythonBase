def greet(name,lang):
    if lang=='en':
        print('Hello',name)
    elif lang=='ml':
        print("നമസ്കാരം",name)
    elif lang=='ar':
        print('مرحبا',name)
    else:
        print('error')
greet('anandu','ar')