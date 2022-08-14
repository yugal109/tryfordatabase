const navElement = document.getElementById("NavCareer");
navElement.style.borderBottom= '3px solid black';
navElement.style.marginTop = '5px';

const handleshowmore=(vacancy_id)=>{
    const showmorep=document.getElementById(`showmore${vacancy_id}`);
    const showless=document.getElementById(`showless${vacancy_id}`);
    showmorep.style.display="none"
    showless.style.display="block"
}
const handleshowless=(vacancy_id)=>{
    const showmorep=document.getElementById(`showmore${vacancy_id}`);
    const showless=document.getElementById(`showless${vacancy_id}`);
    showmorep.style.display="block"
    showless.style.display="none"
}