function toonPlaatjes() {
    var afbeeldingen = document.getElementById('afbeeldingen');
    
    }
  }
  
  toonPlaatjes();
  

let program_lijst = ['python','c++','c#','java','javascript','html','css','php','mysql','react'];
program_lijst = shuffle(program_lijst)

function shuffle(array) {
    let huidigeIndex = array.length, randomIndex;

    while (huidigeIndex != 0) {

        randomIndex = Math.floor(Math.random() * huidigeIndex);
        huidigeIndex--;

        [array[huidigeIndex], array[randomIndex]] = [array[randomIndex], array[huidigeIndex]];
    }

    return array
}

