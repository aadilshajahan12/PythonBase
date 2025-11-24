# 8.Language Translator

# Define translate(word, lang)
# If word == "sun" and lang == "ml" → "സൂര്യൻ"
# If word == "sun" and lang == "fr" → "Soleil"
# Else → "Translation not available"

# def translate(word,lang):
#     if word=='sun' and lang=='ml':
#         print('സൂര്യൻ')
#     elif word=='sun' and lang=='fr':
#         print('Soleil')
#     else:
#         print('translation not available')
# translate('sun','ml')

def translate(word,lang):
    if word=='sun' and lang=='ml':
        return 'സൂര്യൻ'
    elif word=='sun' and lang=='fr':
        return 'Soleil'
    else:
        return 'translation not available'
print(translate('sun','fl'))