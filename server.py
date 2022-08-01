from crypt import methods
from datetime import *
import random
from this import s
from time import strftime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="It's a secret sshhhh"

datetime =datetime.now

@app.route('/')
def index():
    if 'Your_Gold'not in session:
        session['Your_Gold']= 0
        session['Money_Log']=[]
    if 'farm' not in session:
        session['farm'] = 0
    if 'gold_amount' not in session:
        session['gold_amount']=0
    if 'cave' not in session:
        session['cave'] =0
    if 'house' not in session:
        session['house']=0
    if 'casino' not in session:
        session['casino']=0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():


    session['farm']= random.randint(10,20)
    session['cave']= random.randint(5,10)
    session['house']= random.randint(2,5)
    session['casino'] = random.randint(-50,50)

    if request.form['building'] == "farm":
        farm = session['farm']
        session['Your_Gold']+= session['farm']
        temp= session['Money_Log']
        temp.append(f'Earned {farm} golds from the farm!'+" "+ f'({date.today():%m/%d/%Y})')
        session['Money_Log']=temp
    elif request.form['building'] == "cave":
        cave = session['cave']
        session['Your_Gold']+= session['cave']
        temp = session['Money_Log']
        temp.append(f'Earned {cave} golds from the cave!'+" "+ f'({date.today():%m/%d/%Y})')
        print(session['cave'])
    elif request.form['building'] == 'house':
        session['Your_Gold']+= session['house']
        house = session['house']
        session['Your_Gold']+= session['house']
        temp = session['Money_Log']
        temp.append(f'Earned {house} golds from the house!'+" "+ f'({date.today():%m/%d/%Y})')
    elif request.form['building'] == 'casino':
        session['Your_Gold']+= session['casino']
        casino = session['casino']
        temp = session['Money_Log']
        if session['casino']>=0:
            temp.append(f'Earned {casino} golds from the casino!'+" "+ f'({date.today():%m/%d/%Y})')
        else:
            temp.append(f'Entered a casino and lost {casino} golds... Ouch..'+" "+ f'({date.today():%m/%d/%Y})')
    print(request.form)
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)