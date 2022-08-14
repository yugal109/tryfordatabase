const p = document.querySelectorAll(".title_class")[0];
const des = document.querySelectorAll(".description_class")[0];
if (p !== null && des !== null) {
  p.style.color = "black";
  des.style.display = "block";
  p.style.borderBottom="3px solid black";
}
const handle = (id) => {
  const p = document.querySelectorAll(".title_class");
  const description = document.querySelectorAll(".description_class");
  for (let i = 0; i < p.length; i++) {
    p[i].style.color = "black";
    description[i].style.display = "none";
    p[i].style.borderBottom="none";
  }
  const indi_title = document.getElementById(`title-${id}`);
  const indi_desc = document.getElementById(`description-${id}`);
  indi_title.style.color = "black";
  indi_desc.style.display = "block";
  indi_title.style.borderBottom="3px solid black";
};
