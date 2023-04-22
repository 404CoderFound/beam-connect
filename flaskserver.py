from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route('/edit')
def edit():
  filename = request.args.get('filename')
  if not filename:
    return 'Filename is required'

  with open(filename) as f:
    content = f.read()

  return render_template('edit.html', filename=filename, content=content)


@app.route('/save', methods=['POST'])
def save():
  filename = request.form['filename']
  content = request.form['content']

  with open(filename, 'w') as f:
    f.write(content)

  return redirect('/edit?filename=' + filename + '&success=true')


if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', port='666')
