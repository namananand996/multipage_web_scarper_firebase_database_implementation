import bs4
import requests
import urllib
import os
import webbrowser
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



#  Firebase Initilization
# Use a service account
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()







inputdata =  ['Internship in Bangalore','Internship in Delhi','Internship in Hyderabad','Internship in Mumbai',
        'Internship in Pune','Internship in Kolkata','Internship in Jaipur','Work from Home Jobs',
        'Marketing Internship','Finance Internship','Computer Science Internship',
        'Mechanical Internship','Hr Internship','Digital Marketing Internship','Electronics Internship',
        'Content Writing Internship','Campus Ambassador Internship','Civil Internship','Engineering Internship',
        'Part Time Jobs']


data1 = ['internship-in-bangalore','internship-in-delhi','internship-in-hyderabad','internship-in-mumbai',
        'internship-in-pune','internship-in-kolkata','internship-in-jaipur','work-from-home-jobs',
         'marketing-internship','finance-internship','computer%20science-internship',
        'mechanical-internship','hr-internship','digital%20marketing-internship','electronics-internship',
        'content%20writing-internship','campus%20ambassador-internship','civil-internship','engineering-internship',
        'part-time-jobs']
for a in range(len(data1)):
    print(a+1," : ",inputdata[a])
    print()
    

find = int(input("What type of intership you want : "))
    
det = 0   
for ul in range(1):
    z = str(ul+1)
    url = "https://internshala.com/internships/"+ data1[find-1]+"/page-"+(z)+""
    url = str(url)
    print(url)
    
    print("\n\n\n")
    
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')





    data = soup.find_all("div","internship_meta")
    T = len(data)
    i = 0 
    # print(data[1].prettify())

    while i+1 :

        header = data[i].find_all("div","individual_internship_header")
        # print(header[0].prettify())
        head_data = header[0].find_all("a")
        

        head_data1 = header[0].find_all("a","link_display_like_text")
        

        details = data[i].find_all("div","individual_internship_details")

        # print(details[0].prettify())
        location = details[0].find_all("p",{"id": "location_names"})
        # print(location[0].prettify())
        location_name =  location[0].find_all("a")
        location_data = []
        x = len(location_name)
        for j in range(x):
#             print("Loctaion : ", j ,location_name[j].text)
            location_data.append(location_name[j].text)
        print("Location : ", location_data)


        main_details = details[0].find_all("td")


        print("Company : ", head_data1[0].text)
        print("Type of Job : ", head_data[0].text)
        print("Start Date : ", main_details[0].text)
        print("Duration : ", main_details[1].text)
        print("Stipend " , main_details[2].text)
        print("Posted_on : ", main_details[3].text)
        print("Apply By : ", main_details[4].text)


        type_of_job = head_data[0].text
        company = head_data1[0].text
        start_date = main_details[0].text
        duration = main_details[1].text
        stipend = main_details[2].text
        posted_on  = main_details[3].text
        apply_by = main_details[4].text

        det = str(det)

        doc_ref = db.collection(u''+ data1[find-1]).document(u'job_details'+det)
        doc_ref.set({
            u'type_of_job' : type_of_job,
            u'company' : company,
            u'location' : location_data,
            u'start_date' : start_date,
            u'duration' : duration,
            u'stipend' : stipend,
            u'posted_on' : posted_on,
            u'apply_by' : apply_by

        })

        det = int(det)
        det = det + 1
        print("\n\n")
        i = i + 1
        if i == T:
            break
    if ul == 0:
        webbrowser.open_new("http://127.0.0.1:4500/fetch.html")

