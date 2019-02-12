from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)

db.define_table("uploads",              
               Field('db_upload', 'upload'),
               Field('db_details'),
               Field('db_profile'),
               Field('db_house_type'),
               Field('db_title'),
               Field('db_location'),
               Field('db_amount'),
                Field('db_contact'))


auth.settings.logout_next = URL('home')
auth.settings.login_url = URL('login')
