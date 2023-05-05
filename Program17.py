a = []
b = []
cd = []
for i in range(8):
    a.append(['.','.','.','.','.','.','.','.'])
    b.append(['.','.','.','.','.','.','.','.'])
    cd.append(['.','.','.','.','.','.','.','.'])
def choice():
    for j in range(1,3):    
        for i in range(10):
            print('Player', j)
            r = int(input('What row?'))
            c = int(input('What column?'))
            
            if j == 1:
                while c>9 or r>9 or c<0 or r<0:
                    r = int(input('What row?'))
                    c = int(input('What column?'))
                while a[r-1][c-1] == 'T': 
                    r = int(input('What row?'))
                    c = int(input('What column?'))
                a[r-1][c-1] = 'T'
                for i in range(8):
                    print(a[i])
            else:
                while c>9 or r>9 or c<0 or r<0:
                    r = int(input('What row?'))
                    c = int(input('What column?'))
                while b[r-1][c-1] == 'T':
                    r = int(input('What row?'))
                    c = int(input('What column?'))
                b[r-1][c-1] = 'T'
                for i in range(8):
                    print(b[i])     
choice()
def game():
    while a != cd or b != cd :
        for i in range(1,3):
            print('Player', i)
            aa = int(input('Enter the row: '))
            bb = int(input('Enter the column: '))
            while aa>8 or bb>8 or aa<1 or bb<1:
                    r = int(input('What row?'))
                    c = int(input('What column?'))
            if i == 1 and b[aa-1][bb-1] == 'T':
                b[aa-1][bb-1] = '.'
                print('Hit')
                for i in range(8):
                    print(a[i])
            elif i == 1 and b[aa-1][bb-1] != 'T':
                b[aa-1][bb-1] = '.'
                print('Miss')
                for i in range(8):
                    print(a[i])
            elif i == 2 and a[aa-1][bb-1] == 'T':
                a[aa-1][bb-1] = '.'
                print('Hit')
                for i in range(8):
                    print(b[i])
            elif i == 2 and a[aa-1][bb-1] != 'T':
                a[aa-1][bb-1] = '.'
                print('Miss')
                for i in range(8):
                    print(b[i])
    if a == cd :
        print('Player 1 has won the game.')
    elif b == cd :
        print('Player 2 has won the game.')
game()