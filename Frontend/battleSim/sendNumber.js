
//import * as AWS "https://sdk.amazonaws.com/js/aws-sdk-2.558.0.min.js";
//var AWS = require('aws-sdk');
//require does not need to be done for browser JS, only if JS is used as a source code
var lambda = new AWS.Lambda();
alert("made lambda... yay?")
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
exports.handler = function(event, context){

}
*/

/*
console.log('Loading function');

exports.handler = (event, context, callback) => {

};
*/
