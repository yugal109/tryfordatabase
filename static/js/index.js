const colors = ["red", "blue", "green", "yellow", "red","darkgreen","orange"];

function randomIntFromInterval(min, max) {
  // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min);
}

const rndInt = randomIntFromInterval(1, 6);
document.getElementById("title").addEventListener("click", (event) => {
  document.getElementById("title").style.color = colors[randomIntFromInterval(
    0,
    colors.length
  )];
});
