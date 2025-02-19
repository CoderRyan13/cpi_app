from datetime import datetime
from db import db
from models.collector_assignment import AssignmentModel

class CollectorOutletModel(db.Model):

    __tablename__ = 'collector_outlet'

    id = db.Column(db.Integer, primary_key=True)
    cpi_outlet_id = db.Column(db.Integer, unique=True, nullable=True)
    est_name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    note = db.Column(db.String(1000), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    area_id = db.Column(db.Integer, db.ForeignKey("collector_area.id"), nullable=False)
    operating_hours = db.Column(db.String(255), nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
 
    area = db.relationship("CollectorAreaModel", backref="outlets")

    def __init__(self, est_name, address, phone, area_id, lat, long, note, operating_hours, image, cpi_outlet_id=None, _id=None, ):

        self.id = _id
        self.cpi_outlet_id = cpi_outlet_id
        self.est_name = est_name
        self.address = address
        self.phone = phone
        self.area_id = area_id
        self.lat = lat
        self.long = long
        self.note = note
        self.operating_hours = operating_hours
        self.image = image
        

    def __str__(self):
        return str(self.json())


    def json(self):
        return {
            'id': self.id,
            'cpi_outlet_id': self.cpi_outlet_id,
            'est_name': self.est_name,
            'lat': self.lat,
            'long': self.long,
            'note': self.note,
            'address': self.address,
            'phone': self.phone,
            'area_id': self.area_id,
            "area_name": self.area.name if self.area else None,
            "operating_hours": self.operating_hours,
            "image": self.image
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def find_by_id(cls, id):
            return cls.query.filter_by(id=id).first()

    # @classmethod
    # def find_by_id(cls, cpi_outlet_id):
    #         return cls.query.filter_by(cpi_outlet_id=cpi_outlet_id).first()

    @classmethod
    def find_by_cpi_outlet_id(cls, cpi_outlet_id):
        return cls.query.filter_by(cpi_outlet_id=cpi_outlet_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def update(self, new_outlet):
        self.est_name = new_outlet.est_name
        self.address = new_outlet.address
        self.phone = new_outlet.phone
        self.area_id = new_outlet.area_id
        self.lat = new_outlet.lat
        self.long = new_outlet.long
        self.note = new_outlet.note
        self.operating_hours = new_outlet.operating_hours
        self.image = new_outlet.image
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def cpi_to_collector_outlet(cls, outlet):
        new_outlet = cls(
            cpi_outlet_id=outlet[0],
            est_name=outlet[1],
            note=outlet[2],
            address=outlet[3],
            lat=outlet[4],
            _long=outlet[5],
            phone=outlet[6],
            area_id=outlet[7],
            operating_hours=outlet[8],
            image=outlet[9]
        )
        
        return new_outlet
    
    @classmethod
    def find_by_area(cls, area_id):
        return cls.query.filter_by(area_id=area_id).all()
        

    @classmethod
    def insert_many(cls, outlets):

        for outlet in outlets:

            new_outlet = cls(
                outlet['est_name'],
                outlet['address'],
                outlet['phone'],
                outlet['area_id'],
                outlet['lat'] if outlet['lat'] else 0,
                outlet['long'] if outlet['long'] else 0,
                outlet['note'],
                outlet['operating_hours'],
                outlet['image']
            )
            db.session.add(new_outlet)
            db.session.commit()
            outlet['id'] = new_outlet.id           
        
        return outlets

    @classmethod
    def update_many(cls, outlets):

        for outlet in outlets:

            new_outlet = cls.find_by_id(outlet['mobile_id'])

            new_outlet.est_name = outlet['est_name'],
            new_outlet.address = outlet['address'],
            new_outlet.phone = outlet['phone'],
            new_outlet.area_id = outlet['area_id'],
            new_outlet.lat = outlet['lat'] if outlet['lat'] else 0,
            new_outlet.long = outlet['long'] if outlet['long'] else 0,
            new_outlet.note = outlet['note'],
            new_outlet.operating_hours = outlet['operating_hours']
            new_outlet.image = outlet['image']
            
            db.session.commit()
        
        return outlets
            


        

       
       