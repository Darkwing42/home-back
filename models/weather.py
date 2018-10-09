from home_back import db
from datetime import datetime


class WeatherData(db.Model):


    __tablename__ = 'weather_data'

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    act_temp = db.Column(db.Float)
    min_temp = db.Column(db.Float)
    max_temp = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now)
    time = db.Column(db.DateTime, default=datetime.now)
    icon = db.Column(db.String(3))
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)

    def to_dict(self):
        return dict(
            id=self.id,
            city_id=self.city_id,
            act_temp=self.act_temp,
            min_temp=self.min_temp,
            max_temp=self.max_temp,
            date=self.date.strftime('%d-%m-%Y'),
            time=self.time.strftime('%H:%M'),
            icon=self.icon,
            humidity=self.humidity,
            pressure=self.pressure
        )
    def save(self):
        db.session.add(self)
        db.session.commit()



class City(db.Model):

    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(200), nullable=False)
    country_code = db.Column(db.String(6), nullable=False)
    weather_data = db.relationship('WeatherData', backref='City', lazy=True)

    def to_dict(self):
        return dict(
            id=self.id,
            city_name=self.city_name,
            country_code=self.country_code,
            weather_data=[data.to_dict for data in self.weather_data]
        )
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_by_name(cls, city_name):
        return cls.query.filter_by(city_name=city_name).first()
        

class WeatherConfig(db.Model):

    __tablename__ = 'weather_config'

    id = db.Column(db.Integer, primary_key=True)
    api_key=db.Column(db.String(200))

    def to_dict(self):
        return dict(
            id=self.id,
            api_key=self.api_key
        )

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_config(cls):
        return cls.query.filter_by(id=1).first()
