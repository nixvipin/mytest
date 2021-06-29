from bottle import route, run

@route('/alpha')
def sysdig():
  return '<body style="background color: powerblue;"><h1>My APP using CI/CD!</h1><h3>Whatssss UP!!!</h3>'

run(host='0.0.0.0', port=8001, debug=True)
