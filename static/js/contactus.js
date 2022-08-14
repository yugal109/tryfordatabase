const navElement = document.getElementById("NavContact");
navElement.style.borderBottom = "3px solid black";
navElement.style.marginTop = "5px";

const insertParagraph = (text, element) => {
  let p = document.createElement("p");
  element.style.border="2px solid red"
  p.className+="error_class_node"
  p.textContent = text;
  p.style.color = "red";
  p.style.fontSize = "15px";
  p.style.marginTop = "-4px";
  p.style.marginBottom = "-4px";
  element.after(p);
   setTimeout(() => {
    p.style.display = "none";
    element.style.border="none"
  }, 3000);
};



const contactUsFunction = (e) => {
  e.preventDefault();
  document.querySelectorAll(".error_class_node").forEach(el => el.remove());
  const elements = document.getElementsByClassName("input");
  let submitable = true;
  const datas = [
    "fullname is required!!!",
    "email is required!!!",
    "phonenumber is required!!!",
    "description is required!!!",
  ];
  for (let i = 0; i < elements.length; i++) {
    if (elements[i].value === "") {
      insertParagraph(datas[i], elements[i]);
        // makeBorderRed(elements[i])
      submitable = false;
    }
  }
  if (submitable === true) {
    document.getElementById("ContactUsForm").submit();
  }
};

const contactUsForm = document
  .getElementById("ContactUsForm")
  .addEventListener("submit", contactUsFunction);
