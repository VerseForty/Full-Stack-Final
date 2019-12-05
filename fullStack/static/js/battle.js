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

var monsterName = document.getElementById("monsterName").innerHTML
var monsterAC = parseInt(document.getElementById("monsterAC").innerHTML)
var special = document.getElementById("special").innerHTML



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
