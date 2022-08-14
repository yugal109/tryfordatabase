const user = window.localStorage.getItem("username");
if (user) {
  console.log(user);
  document.getElementById("showname_id").innerText = user;
} else {
  console.log(user);
}
