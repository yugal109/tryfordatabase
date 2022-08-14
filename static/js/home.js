const home_img_array = [1, 2, 3]
let a = 0;
setInterval(() => {
    const ptag = document.getElementById("homepage_slider")
    let home = `home${home_img_array[a]}`
    ptag.innerHTML = `<img src="/media/images/${home}.png" widht="800" height="800" />`
    if (a == 2) {
        a = 0;
    }
    else {
        a++;
    }
}, 3000);
