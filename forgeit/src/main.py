from flask import Flask, request, render_template
from forge import Forge

app = Flask('app')

@app.route('/', methods = ["GET", "POST"])
def index_get():
	if request.method != "POST":
		return render_template("userFacing/index.html")

	forger = Forge(
		attacker_limiteds = request.form.get('attackerLimiteds').strip().split(','),
		victim_limiteds = request.form.get('victimLimiteds').strip().split(','),
		victim_username = request.form.get('uname').strip()
	)

	try:
		return forger.forge_trade_page()
	except Exception as _:
		return render_template("userFacing/index.html")
	

if __name__ == "__main__":
	app.run(port = 3000, debug = True)
	# app.run(host="0.0.0.0") # for replit 
