

function makeJSON(){
  var userID = "";
  var name = document.forms["characterForm"]["characterName"].value;
  //alert(name);
  //alert(typeof name);
  var race = document.forms["characterForm"]["race"].value;
  var playerClass = document.forms["characterForm"]["class"].value;
  var strength = document.forms["characterForm"]["strength"].value;
  var dexterity = document.forms["characterForm"]["dexterity"].value;
  var constitution = document.forms["characterForm"]["constitution"].value;
  var intelligence = document.forms["characterForm"]["intelligence"].value;
  var wisdom = document.forms["characterForm"]["wisdom"].value;
  var charisma = document.forms["characterForm"]["charisma"].value;


  //alert(name + race + playerClass + strength, dexterity, constitution, intelligence, wisdom, charisma);

  characterSheetObj = {userID: userID, name: name, race: race, class: playerClass, strength: strength, dexterity: dexterity, constitution: constitution, intelligence: intelligence, wisdom: wisdom, charisma: charisma}
  characterSheetJSON = JSON.stringify(characterSheetObj);
//?  localStorage.setItem("testJSON", characterSheetJSON);
  alert(characterSheetJSON);
}
