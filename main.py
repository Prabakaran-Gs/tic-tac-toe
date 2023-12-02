import threading
from flask import Flask , render_template , redirect ,url_for
from logic import invalid , check_win , check_draw , min_max

board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def ai_move():
    global board
    res,mov = min_max(board)
    row,col = mov
    board[row][col] = 'O'

opt = []
ai = threading.Thread(target=ai_move)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',board = board)

@app.route('/update/<arg>')
def update(arg):
    global board
    global opt
    row,col = arg.split(',')
    print(opt)
    print(row,col)
    if invalid(row,col,opt):
        return redirect(url_for('index'))
    board[int(row)][int(col)] = 'X'
    print(opt)
    opt.append((row,col))
    print(board)

    if check_win(board,'X'):
        return render_template('win.html',board = board)
    if check_draw(board):
        return render_template('draw.html',board = board)
    ai_move()
    if check_win(board , 'O'):
        return render_template('lose.html',board = board)        
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global board
    global opt
    board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]
    opt =[]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)