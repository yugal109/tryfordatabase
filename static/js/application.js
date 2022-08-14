const insertParagraph = (text, element) => {
  let p = document.createElement("p");
  p.textContent = text;
  p.style.color = "red";
  p.style.fontSize = "15px";
  p.style.marginTop = "-4px";
  p.style.marginBottom = "-4px";
  element.after(p);
  setTimeout(() => {
    p.style.display = "none";
  }, 2000);
};
const applicationFunction = (e) => {
    e.preventDefault();
  // const fullnameElement = document.getElementById("fullname");
  // const emailElement = document.getElementById("email");
  // const phoneNumberElement = document.getElementById("phonenumber");
  const elements = document.getElementsByClassName(
    "input"
  );
  const datas = [
    "fullname is required!!!",
    "email is required!!!",
    "phonenumber is required!!!",
    "description is required!!!"
  ];
  for (let i = 0; i < elements.length; i++) {
    if (elements[i].value === "") {
      insertParagraph(datas[i], elements[i]);
    }
  }
};

const applicationForm = document
  .getElementById("ApplicationForm")
  .addEventListener("submit", applicationFunction);