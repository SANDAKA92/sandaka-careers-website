from flask import Flask, render_template, jsonify

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


JOBS = [
  {
 'id': 1,
 'title': 'Computer Programmer',
 'location': 'Kelaniya',
 'salary': 'Rs. 100000'
},
{
  'id': 2,
 'title': 'Computer Programmer2',
 'location': 'Kelaniya2',
 'salary': 'Rs. 200000'
},
{
  'id': 3,
 'title': 'System Analyst',
 'location': 'Peradeniya',
 'salary': 'Rs. 300000'
}
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
