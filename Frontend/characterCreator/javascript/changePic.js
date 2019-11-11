function changePic(){

  var inputHTML = document.getElementById("class");
  var inputString = inputHTML.options[inputHTML.selectedIndex].value;

  //alert(inputString);


  if(inputString == "fighter"){
    document.getElementById('characterPic').src = '../assets/alan.png';
  }

  else if(inputString == "rogue"){
    document.getElementById('characterPic').src = '../assets/simon.png';
  }

  else if(inputString == "wizard"){
    document.getElementById('characterPic').src = '../assets/ivan.png';
  }
}
