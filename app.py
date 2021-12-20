# This is a sample Python script.
from flask import Flask, request, jsonify, render_template
import sys
app=Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/runcode', methods=['POST'])
def runcode():
    if request.method == "POST":
        codeareadata = request.form['codearea']
        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render_template('index.html',code=codeareadata ,output=output)

if __name__ == '__main__':
    print('The app is working')
    app.run()

