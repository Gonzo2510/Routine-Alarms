from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association Table for the Many-to-Many Relationship
routine_alarms = db.Table('routine_alarms', db.metadata,
    db.Column('routine_id', db.Integer, db.ForeignKey('routines.id'), primary_key=True),
    db.Column('alarm_id', db.Integer, db.ForeignKey('alarms.id'), primary_key=True)
)

class Routine(db.Model):
    __tablename__ = 'routines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    alarms = db.relationship('Alarm', secondary=routine_alarms, back_populates='routines')

    def __repr__(self):
        return f'<Routine {self.name}>'

class Alarm(db.Model):
    __tablename__ = 'alarms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    time = db.Column(db.Time, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    routines = db.relationship('Routine', secondary=routine_alarms, back_populates='alarms')

    def __repr__(self):
        return f'<Alarm {self.name} at {self.time}>'
