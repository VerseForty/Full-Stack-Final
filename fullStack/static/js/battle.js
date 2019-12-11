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
var weapon = document.getElementById("weapon").value;
var level = parseInt(document.getElementById("level").innerHTML)
var proficiency = level
var savingThrowMod = 0;
var acMod = 0;
var spellsLeft = 3
//helper function to make sure weapon stays updated

function updateWeapon(){
  weapon = document.getElementById("weapon").value;

}
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

  case "Wizard":

      attack = 0;
      document.getElementById("spell1").innerHTML = "Acid Splash"
      document.getElementById("spell2").innerHTML = "Ray of Frost"
      document.getElementById("spell3").innerHTML = "Jolt"
      document.getElementById("spell4").innerHTML = "Resistance"
      document.getElementById("spell5").innerHTML = "Stunning Barrier"
      document.getElementById("spell6").innerHTML = "Corrosive Touch"
      document.getElementById("spell7").innerHTML = "Stone Call"
      switch (level) {
        case 1:
          spellsLeft = 3

          break;

        default:
          spellsLeft = 4

          break;
    }
    break;
  default: alert("why dont you have stats")
    break;
}



var monsterName = document.getElementById("monsterName").innerHTML
var monsterAC = parseInt(document.getElementById("monsterAC").innerHTML)
var special = document.getElementById("special").innerHTML
var monsterCR = parseInt(document.getElementById("monsterCR").innerHTML)
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

function monsterAttack(){
  var playerHP = document.getElementById("playerHP").innerHTML;
  var acRoll = getRandomInt(20)+1
  var playerAC = (acRoll + proficiency)

  var monsterACRoll = (getRandomInt(20)+1)
  if(monsterACRoll >= playerAC){
    var playerHP = document.getElementById("playerHP").innerHTML;
    var playerHPInt = parseInt(playerHP);
    playerHPInt = playerHPInt - monsterCR;
    var playerHPString = playerHPInt.toString();
    document.getElementById("playerHP").innerHTML = playerHPString;
    alert(monsterName + " rolled a " + monsterACRoll + " to your " + playerAC + " and hit you for " + monsterCR + " damage!")


    if(playerHPInt <=0){
      alert("Make a saving throw!")
      var playerSave = getRandomInt(20)+1+savingThrowMod
      var monsterSave = getRandomInt(20)+1
      if(playerSave == 1|| playerSave < monsterSave){
        alert("You rolled a " + playerSave + " to the monster's " + monsterSave +", you lose!")
      }
      else{
        alert("You rolled a " + playerSave + " to the monster's " + monsterSave + " and lived with 1HP!")
        document.getElementById("playerHP").innerHTML = "1";
      }

    }
  }
  else{
    alert(monsterName + " rolled a " + monsterACRoll + " to your " + playerAC + " and missed!")
  }
}


function playerAttack(){

  var monsterHP = document.getElementById("monsterHP").innerHTML;


  var weaponDamage;

  if(playerClass == "Fighter" || playerClass == "Rogue" || playerClass == "Wizard"){

    switch(weapon) {

      case "Club":
        weaponDamage = (getRandomInt(5)+1)
        alert("You rolled a " + weaponDamage + " out of 6 for your weapon roll")
        break;
      case "Dagger":
      weaponDamage = (getRandomInt(3)+1)

      alert("You rolled a " + weaponDamage + " out of 4 for your weapon roll")
        break;
      default:
        alert("why don't you have a weapon? weapon: " + weapon)
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
        classDamage =0
        break;

      default: alert("why don't you have a class")

    }
    var acRoll = getRandomInt(20)+1
    var playerAC = (acRoll + proficiency + acMod)
    alert("You rolled a " + playerAC + " out of a possible " + (20 + proficiency + acMod) + " for your accuracy roll (d20 plus Proficiency and Modifiers)")
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
      monsterAttack()
    }

  }//end if for fighter or rogue EDUT wuzard too


}//end playerattack

function spell1(){
  switch (playerClass) {
    case "Wizard":
      if(spellsLeft > 0){
        var spellRoll = getRandomInt(3)+1
        var monsterHP = document.getElementById("monsterHP").innerHTML;
        var newMonsterHP = monsterHP - spellRoll

        var newMonsterHPString = newMonsterHP.toString()
        spellsLeft--
        document.getElementById("monsterHP").innerHTML = newMonsterHPString
        alert("You hit the " + monsterName + " with an orb of acid for " + spellRoll + " damage! You have " + spellsLeft + " spells remaining.")

        if(newMonsterHP <= 0){
          alert("You win!")
          }
        else{
          monsterAttack()
          }
        }
      else{
        alert("You have no remaining spells!")
      }
      break;

    default:
      alert("Your class cannot use spells!")
      break;
  }
}

function spell2(){
  switch (playerClass) {
    case "Wizard":
      if(spellsLeft > 0){
        var spellRoll = getRandomInt(3)+1
        var monsterHP = document.getElementById("monsterHP").innerHTML;
        var newMonsterHP = monsterHP - spellRoll

        var newMonsterHPString = newMonsterHP.toString()
        spellsLeft--

        document.getElementById("monsterHP").innerHTML = newMonsterHPString
        alert("You hit the " + monsterName + " with a beam of ice for " + spellRoll + " damage! You have " + spellsLeft + " spells remaining.")

        if(newMonsterHP <= 0){
          alert("You win!")
          }
        else{
          monsterAttack()
          }
        }
      else{
        alert("You have no remaining spells!")
      }
      break;

    default:
      alert("Your class cannot use spells!")
      break;
  }
}


function spell3(){
  switch (playerClass) {
    case "Wizard":
      if(spellsLeft > 0){
        var spellRoll = getRandomInt(3)+1
        var monsterHP = document.getElementById("monsterHP").innerHTML;
        var newMonsterHP = monsterHP - spellRoll

        var newMonsterHPString = newMonsterHP.toString()
        spellsLeft--

        document.getElementById("monsterHP").innerHTML = newMonsterHPString
        alert("You hit the " + monsterName + " with an bolt of electricity for " + spellRoll + " damage! You have " + spellsLeft + " spells remaining.")

        if(newMonsterHP <= 0){
          alert("You win!")
          }
        else{
          monsterAttack()
          }
        }
      else{
        alert("You have no remaining spells!")
      }
      break;

    default:
      alert("Your class cannot use spells!")
      break;
  }
}


function spell4(){
  switch (playerClass) {
    case "Wizard":
      if(spellsLeft>0){
        savingThrowMod++
        spellsLeft--

        alert("You added 1 to your saving throw bonus! You have " + spellsLeft + " spells remaining.")
        monsterAttack()
      }
      else{
        alert("You have no remaining spells!")
      }
        break;
      default:
        alert("Your class cannot use spells!")
      break;
  }
}

function spell5(){
  switch (playerClass) {
    case "Wizard":
      if(spellsLeft>0 && level >=2){
        savingThrowMod++
        acMod++
        spellsLeft--

        alert("You added 1 to your saving throw bonus and AC! You have " + spellsLeft + " spells remaining.")
        alert("Your stunning barrier blocked the monster's attack!")
      }
      else{
        if(spellsLeft<=0){
          alert("You have no remaining spells!")
        }
        else alert("Your level is too low!")
      }
        break;
      default:
        alert("Your class cannot use spells!")
      break;
  }
}

function spell6(){
  switch (playerClass) {
    case "Wizard":
      if(spellsLeft > 0 && level>=2){
        var spellRoll = getRandomInt(4)+1
        var monsterHP = document.getElementById("monsterHP").innerHTML;
        var newMonsterHP = monsterHP - spellRoll

        var newMonsterHPString = newMonsterHP.toString()
        document.getElementById("monsterHP").innerHTML = newMonsterHPString
        spellsLeft--

        alert("You hit the " + monsterName + " with a touch of corrosion for " + spellRoll + " damage! You have " + spellsLeft + " spells remaining.")

        if(newMonsterHP <= 0){
          alert("You win!")
          }
        else{
          monsterAttack()
          }
        }
        else{
          if(spellsLeft<=0){
            alert("You have no remaining spells!")
          }
          else alert("Your level is too low!")
        }
      break;

    default:
      alert("Your class cannot use spells!")
      break;
  }
}

function spell7(){
  switch (playerClass) {
    case "Wizard":
      if(spellsLeft > 0 && level > 2){
        var spellRoll = getRandomInt(12)+1
        var monsterHP = document.getElementById("monsterHP").innerHTML;
        var newMonsterHP = monsterHP - spellRoll

        var newMonsterHPString = newMonsterHP.toString()
        document.getElementById("monsterHP").innerHTML = newMonsterHPString
        spellsLeft--

        alert("You hit the " + monsterName + " with a large stone for " + spellRoll + " damage! You have " + spellsLeft + " spells remaining.")

        if(newMonsterHP <= 0){
          alert("You win!")
          }
        else{
          monsterAttack()
          }
        }
        else{
          if(spellsLeft<=0){
            alert("You have no remaining spells!")
          }
          else alert("Your level is too low!")
        }
      break;

    default:
      alert("Your class cannot use spells!")
      break;
  }
}
