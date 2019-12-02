var lambda = new AWS.Lambda();


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
  //alert(characterSheetJSON);

  var myParams = {
    FunctionName : 'addCharacterSheet',
    InvocationType : 'RequestResponse',
    LogType : 'None',
    //Payload : '{"userID": userID, "name": name, "race": race, "class": playerClass, "strength": strength, "dexterity": dexterity, "constitution": constitution, "intelligence": intelligence, "wisdom": wisdom, "charisma" : charisma}'
    Payload : characterSheetJSON
  }

  lambda.invoke(myParams, function(err, data){
      //if it errors, prompts an error message
      if (err) {
              alert("Error");
              prompt(err);
           }
           //otherwise puts up a message that it didnt error. the lambda function presently doesnt do anything
           //in the future the lambda function should produce a json file for the JavaScript here to do something with
           else {
              alert("Invoked Lambda function without erroring!");
           }
    });

}
