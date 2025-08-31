from flask import Flask, jsonify, request, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)

# SQLite DB in the project folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lawsage.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

def seed_if_empty():
    if User.query.count() == 0:
        demo = [
            User(name="Ada Lovelace", email="ada@lawsage.test"),
            User(name="Alan Turing", email="alan@lawsage.test"),
            User(name="Grace Hopper", email="grace@lawsage.test"),
        ]
        db.session.add_all(demo)
        db.session.commit()

# Initialize DB immediately (Flask 3.x compatible)
with app.app_context():
    db.create_all()
    seed_if_empty()

@app.route("/")
def index():
    return render_template("index.html", title="Welcome to LawSage Test")

@app.route("/users", methods=["GET"])
def list_users():
    users = User.query.order_by(User.id.asc()).all()
    return jsonify([u.to_dict() for u in users])

@app.route("/search", methods=["GET"])
def search_users():
    name = request.args.get("name", "").strip()
    if not name:
        abort(400, description="Missing required query parameter: name")
    like = f"%{name}%"
    results = User.query.filter(
        or_(User.name.ilike(like), User.email.ilike(like))
    ).order_by(User.id.asc()).all()
    return jsonify([u.to_dict() for u in results])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
