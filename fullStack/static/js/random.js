//simple randomizer for character creation

//helper function courtesy of Mozilla web docs https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function randomize(){
var randRace = getRandomInt(7)

switch (randRace) {
  case 0:
    document.getElementById("race").value = "Human"
    break;

  case 1:
    document.getElementById("race").value = "Elf"
    break;
  case 2:
    document.getElementById("race").value = "Dwarf"
    break;
  case 3:
    document.getElementById("race").value = "Gnome"
    break;
  case 4:
    document.getElementById("race").value = "Halfling"
    break;
  case 5:
    document.getElementById("race").value = "Half-Elf"
    break;
  case 6:
    document.getElementById("race").value = "Half-Orc"
    break;

  default:
    document.getElementById("race").value = "Human"
    break;

}


var randClass = getRandomInt(3)

switch (randClass) {
  case 0:
    document.getElementById("class").value = "Fighter"

    break;
  case 1:
    document.getElementById("class").value = "Rogue"
    break;
  case 2:
    document.getElementById("class").value = "Wizard"
    break;
  default:
    document.getElementById("class").value = "Fighter"
    break;
}


var randStr = getRandomInt(18) +1
document.getElementById("strength").value = randStr

var randDex = getRandomInt(18) +1
document.getElementById("dexterity").value = randDex

var randCon = getRandomInt(18) +1
document.getElementById("constitution").value = randCon

var randInt = getRandomInt(18) +1
document.getElementById("intelligence").value = randInt

var randWis = getRandomInt(18) +1
document.getElementById("wisdom").value = randWis

var randCha = getRandomInt(18) +1
document.getElementById("charisma").value = randCha
}
