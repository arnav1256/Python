import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
def inst(cmd):
    if 'forward' in cmd:
        t.forward(int(cmd[cmd.index('forward') + 1]))
    elif 'backward' in cmd:
        t.backward(int(cmd[cmd.index('backward') + 1]))
    elif 'left' in cmd:
        t.left(int(cmd[cmd.index('left') + 1]))
    elif 'right' in cmd:
        t.right(int(cmd[cmd.index('right') + 1]))
with open('source.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        cmd = line.split(' ')
        if 'repeat' in cmd:
            arr = []
            num = int(cmd[cmd.index('{\n') - 1])
            while '}' not in arr:
                if line == '':
                    break
                line = f.readline()
                arr.append(line.strip().split(' '))
                print(arr)
            for i in range(num):
                for i in range(len(arr)):
                    inst(arr[i])
        inst(cmd)
screen.mainloop()
