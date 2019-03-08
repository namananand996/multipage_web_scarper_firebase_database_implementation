var data1 = document.getElementById("cafe-list");
data1.style.display = "none"

function getData(){
    var test = document.getElementById("bt");
    var te = document.getElementById("btn");
    console.log(te.value);
    test.style.display = "none";
    data1.style.display = "block";
    
}

function getData1(){
    var test = document.getElementById("bt");
    var te = document.getElementById("btn1");
    console.log(te.value)
    test.style.display = "none";
    data1.style.display = "block";
}

function getData2(){
    var test = document.getElementById("bt");
    var te = document.getElementById("btn2");
    console.log(te.value)
    test.style.display = "none";
    data1.style.display = "block";
}

// $(document).ready(function(){
//     $("#btn").click(function(){
//       $("p").hide();
//     });
//     $("#cafe-list").click(function(){
//       $("ul").show();
//     });
//   });