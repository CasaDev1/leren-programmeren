var fotos_lijst = ["python.png","react.jpg","php.png","mysql.png","javascript.jpg","java.png","html.jpg","css.png","c++.png","csharp.jpg"];
var achtergrond = "background.png";
var galerijElement = document.getElementById("afbeeldingen");


for (var i = 0; i < fotos_lijst.length; i++) {
  var fotoUrl = fotos_lijst[i];
  var fotoElement = document.createElement("img");
  fotoElement.src = fotoUrl;
  galerijElement.appendChild(fotoElement);
}
for (var i = 0; i < 20; i++) {
    var img = document.createElement("img");
    img.src = achtergrond;
    document.getElementById("afbeeldingen").appendChild(img);
  }

fotos_lijst = shuffle(fotos_lijst)

function shuffle(fotos_lijst) {
    let huidigeIndex = fotos_lijst.length, randomIndex;

    while (huidigeIndex != 0) {

        randomIndex = Math.floor(Math.random() * huidigeIndex);
        huidigeIndex--;

        [fotos_lijst[huidigeIndex], fotos_lijst[randomIndex]] = [fotos_lijst[randomIndex], fotos_lijst[huidigeIndex]];
    }

    return fotos_lijst
}

