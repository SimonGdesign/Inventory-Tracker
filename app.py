from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "inventory.db"

# 1. Database Setup Function
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  name TEXT NOT NULL, 
                  quantity INTEGER NOT NULL, 
                  reorder_level INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

# Initialize DB when app starts
init_db()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    items = c.fetchall()
    conn.close()
    
    # Logic: Identify which items need reordering
    # We pass 'items' to the HTML. The HTML will do the visual alert.
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    qty = int(request.form['quantity'])
    level = int(request.form['reorder_level'])
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO products (name, quantity, reorder_level) VALUES (?, ?, ?)", 
              (name, qty, level))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
@app.route('/update/<int:id>', methods=['POST'])
def update_stock(id):
    action = request.form['action']
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # First get current quantity
    c.execute("SELECT quantity FROM products WHERE id = ?", (id,))
    result = c.fetchone()

    if result:
        current_qty = result[0]

        if action == 'sell':
            # Prevent negative stock
            if current_qty > 0:
                new_qty = current_qty - 1
            else:
                new_qty = 0

            c.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_qty, id))

        elif action == 'restock':
            new_qty = current_qty + 1
            c.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_qty, id))

    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_product(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
