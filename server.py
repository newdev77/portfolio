# 14-01 # 14-08 adding css and javascript files or static files
from flask import Flask,render_template,request,redirect;
import csv

app = Flask(__name__)
# print(__name__);
@app.route("/")
def index():
    return render_template('index.html');

@app.route("/<string:page_name>")
def page_name(page_name=None):
    return render_template(page_name+'.html');

#14-16 Building A Portfolio 4, #14-17 Building A Portfolio 5, #14-18 Building A Portfolio 6,14-19 Building A Portfolio 7
@app.route('/submit_message', methods=['POST', 'GET'])
def contact():
    # error = None
    if request.method == 'POST':
        data=request.form.to_dict();
        write_to_csv(data);
        return redirect('thank_you');

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email'];
        subject = data['subject'];
        message = data['message'];
        csv_writer = csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL);
        csv_writer.writerow([email,subject,message])


# @app.route("/works")
# def works():
#     return render_template('works.html');
#
# @app.route("/contact")
# def contact():
#     return render_template('contact.html');
#
# @app.route("/components")
# def components():
#     return render_template('components.html');



# 14-09 favicon,
# @app.route("/favicon.ico")
# def favicon():
#     return "<p>This is my blog about dogs in 2020</p>"

#14-10 #templating engine 14-11 url parameters,14-13 building a portfolio
# @app.route("/profile/<uname>")
# def profile(uname=None):
#     return render_template('profile.html', uname=uname);



