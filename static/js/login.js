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
const loginFunction = (e) => {
  e.preventDefault();
  let submitable = true;
  // const fullnameElement = document.getElementById("fullname");
  // const emailElement = document.getElementById("email");
  // const phoneNumberElement = document.getElementById("phonenumber");
  const elements = document.getElementsByClassName("input");
  const datas = ["username is required!!!", "password is required!!!"];
  for (let i = 0; i < elements.length; i++) {
    if (elements[i].value === "") {
      insertParagraph(datas[i], elements[i]);
      submitable = false;
    }
  };

  if (submitable === true) {
    document.getElementById("LoginForm").submit();
  }
};

const loginForm = document
  .getElementById("LoginForm")
  .addEventListener("submit", loginFunction);
