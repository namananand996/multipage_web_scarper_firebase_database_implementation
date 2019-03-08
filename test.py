import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'player').document(u'player_details')
doc_ref.set({
    u'type_of_job' : '1',
    u'company' : '1',
    u'location' : ['1','2'],
    u'start_date' : '1',
    u'duration' : '1',
    u'stipend' : '1',
    u'posted_on' : '1',
    u'apply_by' : '1'

})

        # type_of_job = head_data[0].text
        # company = head_data1[0].text
        # start_date = main_details[0].text
        # duration = main_details[1].text
        # stipend = main_details[2].text
        # posted_on  = main_details[3].text
        # apply_by = main_details[4].text