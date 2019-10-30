function myFunction() {


    let z = document.getElementById("user_form");
    let w = document.getElementById("register_form");
    if(w.style.display === "none")
    {

        z.style.display="none";
        w.style.display="block";
    }
    else {

        w.style.display="none";
        z.style.display="block";
    }
}
function form_toggle(ele){
    console.log(ele.id+"_form"+"2");
    let a = document.getElementById("caretaker_form");
    let b = document.getElementById("admin_form");
    let c = document.getElementById("user_form");
    let d = document.getElementById("register_form");
    d.style.display="none";

    a.style.display="none";b.style.display="none";c.style.display="none";
    let e = document.getElementById(ele.id+"_form")
    e.style.display="block";
}