from app import db

class User(db.Model):
    __tablename__ = "usertable"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String)
    email = db.Column('email',db.String(50),unique=True , index=True)
    team = db.Column('team',db.String(120))
    firstName=db.Column('firstName',db.String(120))
    lastName=db.Column('lastName',db.String(120))
    costCentre=db.Column('costCentre',db.String(120))
    registered_on = db.Column('registered_on' , db.DateTime)
    sources=db.relationship('Data',backref='user',lazy='dynamic')

    def __init__(self, username, password, email, team, firstName, lastName, costCentre):
        self.username = username
        self.set_password(password)
        self.email = email
        self.team = team
        self.firstName= firstName
        self.lastName = lastName
        self.costCentre = costCentre
        self.registered_on = datetime.utcnow()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Data(db.Model):
    __tablename__ = 'datasources'
    id = db.Column('stream_id', db.Integer, primary_key=True)
    uploadDescription = db.Column('uploadDescription', db.String(60), nullable=True)
    uploadName = db.Column('uploadName', db.String, nullable=True)
    upload_date = db.Column('upload_date',  db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'))
    eventName = db.Column("eventName", db.String(256))
    eventDescription = db.Column("eventDescription", db.String(512))
    sourceName = db.Column("sourceName",db.String(256))
    ingestionMethod = db.Column("ingestionMethod", db.String(64))
    logStructure = db.Column("logStructure", db.String(128), nullable=True)
    eventFormat = db.Column("eventFormat", db.String(128))
    delimiter = db.Column("delimiter", db.String(64), nullable=True)
    sampleEventsAvailable = db.Column("sampleEventsAvailable", db.String(8))
    ipFieldPresent = db.Column("ipFieldPresent", db.String(8))
    ipFieldName = db.Column("ipFieldName", db.String(64), nullable=True)
    userFieldPresent = db.Column("userFieldPresent", db.String(8))
    userFieldName = db.Column("userFieldName", db.String(64), nullable=True)
    schemas = db.relationship('Schema',backref='data', lazy='dynamic')

    def __init__(self, uploadDescription, uploadName, eventName, eventDescription, sourceName, ingestionMethod, logStructure, eventFormat, delimiter, sampleEventsAvailable, ipFieldPresent, ipFieldName, userFieldPresent, userFieldName):
        self.uploadDescription = uploadDescription
        self.uploadName = uploadName
        self.upload_date = datetime.utcnow()
        self.eventName = eventName
        self.eventDescription = eventDescription
        self.sourceName = sourceName
        self.ingestionMethod = ingestionMethod
        self.logStructure = logStructure
        self.eventFormat = eventFormat
        self.delimiter = delimiter
        self.sampleEventsAvailable = sampleEventsAvailable
        self.ipFieldPresent = ipFieldPresent
        self.ipFieldName = ipFieldName
        self.userFieldPresent = userFieldPresent
        self.userFieldName = userFieldName

class AzureAPI(db.Model):
    __tablename__='azure_api'
    id= db.Column('api_id', db.Integer, primary_key=True)
    resourceGroup=db.Column('resourceGroup', db.String(128))
    workspaceID=db.Column('workspaceID', db.String(128))
    subscriptionID=db.Column('subscriptionID', db.String(128))
    tenantID=db.Column('tenantID',db.String(128))
    applicationID=db.Column('applicationID',db.String(128))
    clientSecret=db.Column('clientSecret',db.String(128))
    query=db.Column('query',db.String(128))

    def __init__(self, resourceGroup, workspaceID, subscriptionID, tenantID, applicationID, clientSecret, query):
        self.resourceGroup=resourceGroup
        self.workspaceID=workspaceID
        self.subscriptionID=subscriptionID
        self.tenantID=tenantID
        self.applicationID=applicationID
        self.clientSecret=clientSecret
        self.query=query

class Schema(db.Model):
    __tablename__ = 'schemas'
    id = db.Column('schema_id', db.Integer, primary_key=True)
    schema=db.Column('schema',db.JSON)
    datasource_id = db.Column(db.Integer, db.ForeignKey('datasources.stream_id'))

    def __init__(self, schema):
        self.schema= schema
