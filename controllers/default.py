@auth.requires_login()
def upload():
    return dict()

@auth.requires_login()
def save():
    submitted_upload = request.vars.upload
    submitted_details = request.vars.details
    submitted_profile = request.vars.profile 
    submitted_house_type = request.vars.house_type
    submitted_title= request.vars.title
    submitted_location= request.vars.location
    submitted_amount = request.vars.amount
    submitted_contact = request.vars.contact
     

    results = db.uploads.insert(      
        db_upload = submitted_upload,    
        db_details = submitted_details,  
        db_profile = submitted_profile, 
        db_house_type = submitted_house_type, 
        db_title = submitted_title, 
        db_location = submitted_location,
        db_amount = submitted_amount, 
        db_contact = submitted_contact, 
                      )

    if results: 
        session.flash = "House Added Successful"     
        redirect(URL('home'))   
    else:       
        redirect(URL('upload'))   
        

def download():
    return response.download(request,db)
    
def home():
    uploads =db().select(db.uploads.ALL)
    return dict(uploads=uploads)

@auth.requires_login()
def details():
    parameters = request.args
    submitted_id = parameters[0]
    upload=db(db.uploads.id == submitted_id).select()[0]
    return dict(upload=upload)    
    

def searchresult():
    keyword=request.vars.keyword
    title_query = db.uploads.db_details.contains(keyword)
    uploads=db(title_query).select()
    return locals()
    

def user():
    return dict(form=auth())


def store():
    firstname = request.vars.firstname
    lastname = request.vars.lastname
    email = request.vars.email
    username = request.vars.username
    password = request.vars.password

    user = auth.register_bare(
        first_name=firstname, last_name=lastname, email=email,username=username,password=password
        )
    if user:
        session.flash = "sign up Successful"
        redirect(URL('login'))
    else:
        redirect(URL('register'))

def register():
    return dict()

def authenticate():
    username = request.vars.username
    password = request.vars.password

    if not auth.login_bare(username, password):
        session.flash = "Login failed. Try again with correct credentials"
        redirect(URL('login'))

    session.flash = "Login Successful"
    redirect(URL('home'))

def login():
    return dict()