from flask import Flask, render_template,redirect,request

from users import User

app=Flask(__name__)


@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def users():
# return to user page and looking for users in User class
    return render_template('users.html',users=User.get_all())

@app.route('/user/new')
def new():
    return render_template('new_user.html')

@app.route('/user/create',methods=['POST'])
def create():
    # User.validate(request.form) 
    User.save(request.form)
    return redirect ('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data={
        'id':id
    }
    return render_template ('edit_user.html',user=User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/remove/<int:id>')
def remove(id):
    data={
        'id':id
    }
    User.remove(data)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data={
        'id':id
    }
    return render_template ('show_user.html',user=User.get_one(data))

if __name__== '__main__':
    app.run(debug=True,port=8000)