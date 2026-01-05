word='hello bjkg kbjv jggg'
word.split()
print(word)
w=list(map(lambda x:''.join(x),word))
print(w)
# l=[[i,w.count(i)]  if i in 'aeiou' else [i,w.count(i) ]for i in w]
# print(l)