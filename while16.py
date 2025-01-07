i = 0
huruf = 'a'

while i in range(5):
    print(huruf*5)
    huruf = chr(ord(huruf)+1)
    i += 1