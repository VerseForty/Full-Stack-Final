var lambda = new AWS.Lambda();
function alertBox(){
  var entered = document.getElementById("sendNum");
  var asdf = (entered.elements[0].value);
  var enteredInt = (parseInt(entered.elements[0].value));
  //alert(entered.toString());
  alert(entered.elements[0].value);
  alert(typeof asdf); //entered defaults to string
  alert(enteredInt + 1);
};

/*
exports.handler = function(on)
lambda.addLayerVersionPermission(params, function (err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
});
*/
