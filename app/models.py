from app import db

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Cattle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    loss = db.Column(db.Float)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)  # Added quantity attribute

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)  # Added quantity attribute

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)  # Added quantity attribute

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class MilkProduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    milk_produced = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)  # Added quantity attribute
    price = db.Column(db.Float, nullable=False)  # Added price attribute

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class MilkSales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)  # Added quantity attribute

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class MaintenanceCosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
