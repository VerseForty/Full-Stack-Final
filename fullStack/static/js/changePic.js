//function for updating picture on character creator
function changePic(){

  var inputHTML = document.getElementById("class");
  var inputString = inputHTML.options[inputHTML.selectedIndex].value;

  //alert(inputString);


  if(inputString == "Fighter"){
    document.getElementById('characterPic').src = '/static/assets/alan.png';
  }

  else if(inputString == "Rogue"){
    document.getElementById('characterPic').src = '/static/assets/simon.png';
  }

  else if(inputString == "Wizard"){
    document.getElementById('characterPic').src = '/static/assets/ivan.png';
  }
}
