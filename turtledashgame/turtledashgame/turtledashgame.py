import turtle as t
import random
import time

screen = t.Screen()
screen.tracer(0)
t.Screen().setup(1.0, 1.0)
t.bgcolor('turquoise')

text = t.Turtle()
text.shape('turtle')
text.penup()
for _ in range(100):
    colors = ['gold', 'coral', 'hotpink', 'lime', 'orange', 'red']
    text.setheading(random.randrange(361))
    text.color(random.choice(colors))
    text.goto(random.randint(-900, 900), random.randint(-500, 500))
    text.stamp()

text.goto(0, 0)
text.color('#1e2b2e')
text.write('Turtle Dash', align = 'center', font=('Courier New', 50, 'bold'))
text.goto(0, -100)
text.write('нажмите пробел чтобы начать игру', align = 'center', font=('Arial', 20, 'bold'))

no_lost = True
moves = True

cocount = 0

def endgame():
    global restart
    global no_lost
    global moves
    no_lost = False
    moves = False
    t.tracer(0)
    t.bgcolor('turquoise')
    text.goto(0,0)
    text.write('LOSE', align='center', font=('Impact', 40, 'bold'))
    text.goto(0,-100)
    text.write('Нажмите пробел чтобы сыграть снова', align='center', font=('Verdana', 20, 'bold'))
    t.update()
    screen.onkeypress(start_game, ' ')
    restart = True

def move_up():
    global moves
    if moves:
        x, y = t.pos()
        if y < 400:
            t.goto(x, y + 200)
        screen.update()
    else:
        pass

def move_down():
    global moves
    if moves:
        x, y = t.pos()
        if y > -400:
            t.goto(x, y - 200)
        screen.update()
    else:
        pass

def coin_count(num, count_name):
    global cocount
    count_name.clear()
    count_name.goto(-870, -380)
    count_name.color('gold')
    count_name.stamp()
    count_name.goto(-835, -395)
    count_name.color('black')  
    count_name.write(num, align='center', font=('Courier New', 20, 'bold'))
    record = 0
    with open('C:\\Users\\ivang\\source\\repos\\turtledashgame\\turtledashrecord.txt', 'r+', encoding='utf-8') as record_file:
        record = int(record_file.read().rstrip())
        if cocount > record:
            record = cocount
            record_file.seek(0)
            record_file.truncate()
            record_file.write(str(record))
    count_name.goto(-850, -430)
    count_name.write(f'record: {record}', align='center', font = ('Consolas', 15, 'bold'))


def start_game():
    global restart
    global no_lost
    global moves
    global cocount
    if restart: 

        t.clearscreen()
        t.tracer(0)       
        moves = True
        restart = False
        no_lost = True
        screen.onkeypress(move_up, 'w')
        screen.onkeypress(move_down, 's')
        screen.onkeypress(move_up, 'W')
        screen.onkeypress(move_down, 'S') 
        t.bgcolor('turquoise')
        t.color('green')
        t.shape('turtle')
        t.shapesize(2)
        t.penup()
        t.st()
        t.clear()
        t.goto(-600, 0)

        count = t.Turtle()
        count.penup()
        count.shape('circle')
        count.shapesize(1.5)
        count.ht()

        coords = [-400, -200, 0, 200, 400]
        back = [1000, 1100, 1200, 1300, 1400, 1500]

        meteors = []
        for _ in range(3):
            met = t.Turtle()
            met.shape('turtle')
            met.color('red')
            met.left(180)
            met.shapesize(5)
            met.penup()
            met.goto(1000, random.choice(coords))

            met.speed_rate = random.randint(5, 12)
            meteors.append(met)

        coin = t.Turtle()
        coin.penup()
        coin.color('gold')
        coin.shape('circle')
        coin.shapesize(3)
        coin.goto(random.choice(back), random.choice(coords))
        coin.speed_rate = random.randint(5, 12)

        cocount = 0
        coin_count('0', count)
        speed_bonus = 0
    
        while no_lost:

            for met in meteors:
                speed_bonus += 0.001
                met.setx(met.xcor() - (met.speed_rate + speed_bonus))

                if met.xcor() < - 1000:
                    met.goto(random.choice(back), random.choice(coords))
                    met.speed_rate = random.randint(5, 12)

                if t.distance(met) < 50:
                    endgame()
                    break

            coin.setx(coin.xcor() - (coin.speed_rate + speed_bonus))

            if coin.xcor() < -1000:
                coin.goto(random.choice(back), random.choice(coords))
                coin.speed_rate = random.randint(5, 12)

            if t.distance(coin) < 30:
                coin.goto(random.choice(back), random.choice(coords))
                cocount += 1
                coin_count(str(cocount), count)

            screen.update()
            time.sleep(0.01)
        else:
            pass

screen.listen()
screen.onkeypress(start_game, ' ')
restart = True
t.done()