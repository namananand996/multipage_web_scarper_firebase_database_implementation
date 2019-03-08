
  // Initialize Cloud Firestore through Firebase
  var db = firebase.firestore();
  
  // Disable deprecated features
  db.settings({
    timestampsInSnapshots: true
  });


// var docRef = db.collection("internship-in-delhi").doc("job_details0");

const cafeList = document.querySelector('#cafe-list');

// var data = document.getElementById("cafe-list");
// data.style.display = "none";
// var test = document.getElementById("btn");

input_data = "";

// function getData(){
    
//     console.log(test.value);
//     test.style.display = "none";
//     data.style.display = "block"
// }




// send to web page

function renderCafe(doc){
    let li = document.createElement('li');
    let Type_of_job  = document.createElement('span');
    let Company = document.createElement('span');
    let Locations = document.createElement('span');
    let Start_date = document.createElement('span');
    let Duration = document.createElement('span');
    let Stipend = document.createElement('span');
    let Posted_on = document.createElement('span');
    let Apply_by = document.createElement('span');


    li.setAttribute('data-id',doc.id);
    Type_of_job.textContent = doc.data().type_of_job;
    Company.textContent = doc.data().company;
    Locations.textContent = doc.data().location;
    Start_date.textContent = doc.data().start_date;
    Duration.textContent = doc.data().duration;
    Stipend.textContent = doc.data().stipend;
    Posted_on.textContent = doc.data().posted_on;
    Apply_by.textContent  = doc.data().apply_by;


    li.append(Type_of_job);
    li.append(Company);
    li.append(Locations);
    li.append(Start_date);
    li.append(Duration);
    li.append(Stipend);
    li.append(Posted_on);
    li.append(Apply_by);
    cafeList.appendChild(li);

}




var data1 = document.getElementById("cafe-list");
data1.style.display = "none"

function getData(){
    var test = document.getElementById("bt");
    var te = document.getElementById("btn");
    input_data = te.value
    console.log(te.value);
    db.collection(input_data).get().then(function(querySnapshot) {
        querySnapshot.docs.forEach(function(doc) {
            // doc.data() is never undefined for query doc snapshots
            // console.log(doc.id, " => ", doc.data());
            renderCafe(doc);
    
        });
    });
    test.style.display = "none";
    data1.style.display = "block";
    
}

function getData1(){
    var test = document.getElementById("bt");
    var te = document.getElementById("btn1");
    input_data = te.value
    console.log(te.value)
    db.collection(input_data).get().then(function(querySnapshot) {
        querySnapshot.docs.forEach(function(doc) {
            // doc.data() is never undefined for query doc snapshots
            // console.log(doc.id, " => ", doc.data());
            renderCafe(doc);
    
        });
    });
    test.style.display = "none";
    data1.style.display = "block";
}

function getData2(){
    var test = document.getElementById("bt");
    var te = document.getElementById("btn2");
    input_data = te.value
    console.log(te.value)
    db.collection(input_data).get().then(function(querySnapshot) {
        querySnapshot.docs.forEach(function(doc) {
            // doc.data() is never undefined for query doc snapshots
            // console.log(doc.id, " => ", doc.data());
            renderCafe(doc);
    
        });
    });
    test.style.display = "none";
    data1.style.display = "block";
}








console.log("Hello");