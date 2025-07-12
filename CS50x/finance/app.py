import os


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user = session['user_id']

    user_shares = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM deals WHERE user_id = ? GROUP BY symbol", user)
    cash = db.execute("SELECT cash FROM users WHERE users.id = ?", user)[0]['cash']

    stock = []
    all_total = 0
    for item in user_shares:

        price = lookup(item['symbol'])['price']
        item['price'] = usd(price)
        total = item['shares'] * price
        item['total'] = usd(total)
        if user_shares[0]['shares'] > 0:
            stock.append(item)
        all_total += total
    all_total = usd(all_total + cash)

    return render_template("index.html", stock=stock, all_total=all_total, cash=usd(cash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    user = session['user_id']
    symbol = request.form.get("symbol")
    shares = request.form.get("shares")
    cash = db.execute("SELECT cash FROM users WHERE users.id = ?", user)[0]['cash']
    deal_type = 'buy'

    if request.method == 'POST':

        result = lookup(symbol)

        try:

            if not shares:
                return apology("At least 1 share to buy!", 400)
            elif int(shares) < 1:
                return apology("At least 1 share to buy!", 400)

            if not symbol:
                return apology("Provide a stock symbol!", 400)
            elif not result:
                return apology("Choose another stock symbol!", 400)
            else:
                expend = float(result['price']) * float(shares)

                if cash < expend:
                    return apology("Not enough money!", 400)

            db.execute("INSERT INTO deals(symbol, price, shares, user_id, deal_type) VALUES(?, ?, ?, ?, ?)",
                       result['symbol'], result['price'], shares, user, deal_type)

            cash = cash - expend
            print(expend)

            db.execute("UPDATE users SET cash = ? WHERE users.id = ?", cash, user)
            return redirect('/')
        except ValueError:
            return apology("Wrong number of shares!", 400)
    else:
        return render_template("buy.html", cash=usd(cash))


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user = session['user_id']

    deals = db.execute(
        "SELECT symbol, price, shares, deal_type, timestamp FROM deals WHERE user_id = ?", user)
    cash = db.execute("SELECT cash FROM users WHERE users.id = ?", user)[0]['cash']
    total_stock = 0
    history_deals = []

    for deal in deals:
        total_stock = total_stock + (deal['price'] * deal['shares'])
        deal['price'] = usd(deal['price'])
        history_deals.append('deal')

    total = total_stock + cash

    return render_template("history.html", deals=deals, cash=usd(cash), total_stock=usd(total_stock), total=usd(total))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    symbol = request.form.get("symbol")
    q_symbol = ''
    price = ''
    user = session['user_id']

    try:
        if request.method == 'POST':
            result = lookup(symbol)
            q_symbol = result['symbol']
            price = result['price']
            cash = db.execute("SELECT cash FROM users WHERE users.id = ?", user)[0]['cash']
            afford = int(cash / price)

            if not symbol:
                return apology("Provide a stock symbol!")
            elif not result:
                return apology("Choose another stock symbol!")
            else:

                return render_template("quoted.html", symbol=q_symbol, price=usd(price), cash=usd(cash), afford=afford)
        else:
            return render_template("quote.html")
    except TypeError:
        return apology("Provide a valid stock symbol!")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        password = request.form.get("password")
        username = request.form.get("username")
        confirmation = request.form.get("confirmation")
        hash = generate_password_hash(password, method='pbkdf2', salt_length=16)

        if password != confirmation:
            return apology("Password don't match!")

        if not username:
            return apology("Provide an username!")
        if not password:
            return apology("Provide a password!")

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
            return redirect("/")
        except ValueError:
            return apology("Already exists an user with this name")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user = session['user_id']
    symbol = request.form.get("symbol")
    shares = request.form.get("shares")
    cash = db.execute("SELECT cash FROM users WHERE users.id = ?", user)[0]['cash']
    deal_type = 'sell'

    user_shares = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM deals WHERE user_id = ? GROUP BY symbol", user)

    stock_shares = []

    for item in user_shares:
        if user_shares[0]['shares'] > 0:
            stock_shares.append(item['symbol'])

    selected_symbol = request.form.get("symbol")

    number_shares = db.execute(
        "SELECT SUM(shares) AS n_shares FROM deals WHERE user_id = ? AND symbol = ?", user, selected_symbol)

    print(shares, number_shares[0]['n_shares'])

    if request.method == 'POST':
        result = lookup(selected_symbol)
        try:
            if number_shares[0]['n_shares'] < int(shares):
                return apology("Not enough to sell!", 400)

            if not shares:
                return apology("At least 1 share to sell!", 400)
            elif int(shares) < 1:
                return apology("At least 1 share to sell!", 400)

            if not symbol:
                return apology("You don't have this share!", 400)
            elif not result:
                return apology("Choose another stock symbol!", 400)
            else:

                profit = float(result['price']) * float(shares)

                shares = float(shares) * -1.0

                db.execute("INSERT INTO deals(symbol, price, shares, user_id, deal_type) VALUES(?, ?, ?, ?, ?)",
                           result['symbol'], result['price'], shares, user, deal_type)

                cash = cash + profit

                db.execute("UPDATE users SET cash = ? WHERE users.id = ?", cash, user)

                return redirect('/')
        except ValueError:
            return apology("Wrong number of shares!", 400)
    else:
        return render_template("sell.html", stock_shares=stock_shares)
