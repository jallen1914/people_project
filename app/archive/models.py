# app/models.py

#from app import db

 #Models and DB Structure
 class People(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), nullable=False)
     phone = db.Column(db.String(50), nullable=False)
     city = db.Column(db.String(50), nullable=False)
     state = db.Column(db.String(50), nullable=False)

     def __repr__(self):
         return f"People('{self.name}','{self.phone}','{self.city}','{self.state}')"
