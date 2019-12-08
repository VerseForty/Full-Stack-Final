/*
Constant stats that will not be changed, HP will though so it is checked
every time it is called. Stats need to be parsed to ints for calculation
and then returned as strings for html to display, as shown in takeDmg()
*/
var playerName = document.getElementById("playerName").innerHTML
var race = document.getElementById("race").innerHTML
var playerClass = document.getElementById("playerClass").innerHTML
var strength = parseInt(document.getElementById("strength").innerHTML)
var dexterity = parseInt(document.getElementById("dexterity").innerHTML)
var constitution = parseInt(document.getElementById("constitution").innerHTML)
var intelligence = parseInt(document.getElementById("intelligence").innerHTML)
var wisdom = parseInt(document.getElementById("wisdom").innerHTML)
var charisma = parseInt(document.getElementById("race").innerHTML)


var level = parseInt(document.getElementById("level").value)
var proficiency = level

var attack
//long switch to determine player's attack stat
switch (playerClass) {
  case "Fighter":
    switch (strength){
      case 11:
        attack = 1
        break;
      case 12:
        attack = 2
        break;
      case 13:
        attack = 3
        break;
      case 14:
        attack = 5
        break;
      case 15:
        attack = 7
        break;
      case 16:
        attack = 10
        break;
      case 17:
        attack = 13
        break;
      case 18:
        attack = 14
        break;

      default: attack = 0

    }

    break;

  case "Rogue":
    switch (dexterity){
      case 11:
        attack = 1
        break;
      case 12:
        attack = 2
        break;
      case 13:
        attack = 3
        break;
      case 14:
        attack = 5
        break;
      case 15:
        attack = 7
        break;
      case 16:
        attack = 10
        break;
      case 17:
        attack = 13
        break;
      case 18:
        attack = 14
        break;

      default: attack = 0
        break;
    }

    break;


  default: alert("why dont you have stats")
    break;
}



var monsterName = document.getElementById("monsterName").innerHTML
var monsterAC = parseInt(document.getElementById("monsterAC").innerHTML)
var special = document.getElementById("special").innerHTML

//helper function courtesy of Mozilla web docs https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

/*
actual meat and bones functions doing calculations
takeDmg() is just a placeholder/example at the moment to decrement playerHP
*/
function takeDmg(){
  var playerHP = document.getElementById("playerHP").innerHTML;
  var playerHPInt = parseInt(playerHP);
  playerHPInt--;
  var playerHPString = playerHPInt.toString();
  document.getElementById("playerHP").innerHTML = playerHPString;

}

function playerAttack(){

  var monsterHP = document.getElementById("monsterHP").innerHTML;
  var weapon = document.getElementById("weapon").value;


  var weaponDamage;

  if(playerClass == "Fighter" || playerClass == "Rogue"){
    switch(weapon) {
      case "Club":
        weaponDamage = (getRandomInt(5)+1)
        alert("You rolled a " + weaponDamage + " out of 6 for your weapon roll")
        break;
      case "Dagger":
      alert("You rolled a " + weaponDamage + " out of 4 for your weapon roll")
        break;
      default:
        alert("why don't you have a weapon?")
        break;
    }

    //just as long switch to determine class damage buff
    var classDamage
    switch (playerClass) {
      case "Fighter":
        classDamage = level
        break;

      case "Rogue":
        switch(level){
          case 1:
            classDamage = 0
            break;
          case 2:
            classDamage = 1
            break;
          case 3:
            classDamage = 2
            break;
          case 4:
            classDamage = 3
            break;
          case 5:
            classDamage = 3
            break;
          case 6:
            classDamage = 4
            break;
          case 7:
            classDamage = 5
            break;
          case 8:
            classDamage = 6
            break;
          case 9:
            classDamage = 6
            break;
          case 10:
            classDamage = 7
            break;
          case 11:
            classDamage = 8
            break;
          case 12:
            classDamage = 9
            break;
          case 13:
            classDamage = 9
            break;
          case 14:
            classDamage=10
            break;
          case 15:
            classDamage = 11
            break;
          case 16:
            classDamage = 12
            break;
          case 17:
            classDamage = 12
            break;
          case 18:
            classDamage = 13
            break;
          case 19:
            classDamage = 14
            break;
          case 20:
            classDamage = 15
            break;
          default:
            alert("why do you have no class damage")
            break;
          }
        break;

      case "Wizard":
        alert("lmao Wizard")
        break;

      default: alert("why don't you have a class")

    }
    var acRoll = getRandomInt(20)+1
    var playerAC = (acRoll + proficiency)
    alert("You rolled a " + playerAC + " out of " + (20 + proficiency) + " for your accuracy roll (d20 plus Proficiency)")
    var totalDamage
    if(playerAC >= monsterAC){
      totalDamage = classDamage + weaponDamage + attack
      alert("You hit the monster for " + totalDamage + "! " + " (Attack stat: " + attack + " + " + "weapon roll: " + weaponDamage + " + " + "class damage: " + classDamage + ")")
    }
    else{
      totalDamage = 0
      alert("You missed!")
    }
    var newMonsterHP = monsterHP - totalDamage
    var newMonsterHPString = newMonsterHP.toString()
    document.getElementById("monsterHP").innerHTML = newMonsterHPString


    if(newMonsterHP <= 0){
      alert("You win!")
    }
    else{
      //monster attack goes here
    }

  }//end if for fighter or rogue
  else{
    //if Wizard
  }


}//end playerattack
