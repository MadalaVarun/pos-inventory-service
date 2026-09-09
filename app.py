"""Transactional POS inventory domain by Varun Madala."""
import sqlite3,uuid
def db(path="pos.db"):
 c=sqlite3.connect(path); c.row_factory=sqlite3.Row; c.executescript("CREATE TABLE IF NOT EXISTS products(sku TEXT PRIMARY KEY,name TEXT,price REAL,stock INTEGER); CREATE TABLE IF NOT EXISTS sales(id TEXT PRIMARY KEY,sku TEXT,qty INTEGER,total REAL);"); return c
def add_product(sku,name,price,stock,path="pos.db"):
 if price<0 or stock<0: raise ValueError("price and stock cannot be negative")
 c=db(path); c.execute("INSERT OR REPLACE INTO products VALUES(?,?,?,?)",(sku,name,price,stock)); c.commit()
def sell(sku,qty,path="pos.db"):
 if qty<=0: raise ValueError("quantity must be positive")
 c=db(path)
 with c:
  row=c.execute("SELECT * FROM products WHERE sku=?",(sku,)).fetchone()
  if not row: raise KeyError("unknown sku")
  if row["stock"]<qty: raise ValueError("insufficient stock")
  sid=str(uuid.uuid4()); total=round(row["price"]*qty,2)
  c.execute("UPDATE products SET stock=stock-? WHERE sku=?",(qty,sku)); c.execute("INSERT INTO sales VALUES(?,?,?,?)",(sid,sku,qty,total))
 return {"sale_id":sid,"sku":sku,"qty":qty,"total":total}
def stock(sku,path="pos.db"): return db(path).execute("SELECT stock FROM products WHERE sku=?",(sku,)).fetchone()[0]
