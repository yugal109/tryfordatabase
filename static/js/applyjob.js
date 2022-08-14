const insertParagraph = (text, element) =>{
  element.style.border="2px solid red"
    let p = document.createElement('p');
        p.className+="error_class_node"
        p.textContent = text;
        p.style.color = 'red';
        p.style.fontSize= '15px';
        p.style.marginTop='-4px';
        p.style.marginBottom='-4px';
        element.after(p);
        setTimeout(()=>{
            p.style.display ='none';
            element.style.border="none"
        },3000);
}
const applyJobFunction = (e) =>{
    e.preventDefault();
  document.querySelectorAll(".error_class_node").forEach(el => el.remove());
    // const firstnameElement = document.getElementById("firstname");
    // const lastnameElement = document.getElementById("lastname");
    // const emailElement = document.getElementById("email");
    // const addressElement = document.getElementById("address");
    // const phonenumberElement = document.getElementById("phonenumber");
    // const educationElement = document.getElementById("educationStatus");
    // const jobTypeElement = document.getElementById("")
    const elements = document.getElementsByClassName("Career_InputBox_Input");
    const datas = [
        "firstname is required !!!",
        "lastname is required!!!",
        "email is required!!!",
        "address is required!!!",
        "phonenumber is required!!!",
        "education status is required!!!",
        "jobtype is required!!!",
        "job is required!!!",
        "description is required!!!",
        "CV is required!!!"

    ]
    for(let i=0; i<elements.length; i++){
        if(elements[i].value === ""){
            insertParagraph(datas[i],elements[i]);
        } 
    }
}
const applyJobForm = document.getElementById("applyJobForm").addEventListener("submit",applyJobFunction);