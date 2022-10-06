stringa = input('scrivi una stringa:')
#rende maiuscoli tutti i caratteri
stringa = stringa.upper()
#rende minuscole le vocali
stringa = stringa.replace('A', 'a').replace('E', 'e').replace('I', 'i').replace('O', 'o').replace('U', 'u')
print(stringa)
parole = stringa.split(' ')
vocali = ['a', 'e', 'o',  'i','u']
d = {'a':(), 'e':(), 'i':(), 'o':(), 'u':()} #creo il dizionario vuoto
for p in parole:
    for v in vocali:
        i = p.find(v)
        if i >= 0:
            t = d[v]
            t_upd = t + (p,)
            d[v] = t_upd
            #print('la vocale', v, 'è nella parola', p, 'indice ', i)
print('il dizionario finale è:', d)