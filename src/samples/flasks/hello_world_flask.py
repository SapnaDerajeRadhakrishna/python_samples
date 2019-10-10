from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def hello_world():
# 	return "Hello World\n"

@app.route('/') 
def index(): 
   return render_template('index.html') 

# routing the decorator function hello_name 
@app.route('/hello/<name>')   
def include_help_welcome(name): 
  #return 'Hello {}, welcome to Include_help\n'.format(name) 
  return render_template('index.html',user_name=name)

@app.route("/jinja")
def jinja_test():
    return render_template('include_help.html', my_string="Include Help!", my_list=[0,1,2,3,4,5])
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

