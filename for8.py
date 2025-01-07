hasil = 0

for w in range(0, 11, 2):
    hasil += w
    
    if w < 10:
        print(w, '+', end=' ')
    else:
        print(w, '=', end=' ')
    
print(hasil)