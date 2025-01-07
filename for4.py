hasil = 0

for w in range(1, 6):
    hasil += w
    
    if w < 5:
        print(w, '+', end=' ')
    else:
        print(w, '=', end=' ')
    
print(hasil)