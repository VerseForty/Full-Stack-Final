
//import * as AWS "https://sdk.amazonaws.com/js/aws-sdk-2.558.0.min.js";
//var AWS = require('aws-sdk');
//require does not need to be done for browser JS, only if JS is used as a source code

var lambda = new AWS.Lambda();
var myParams = {
  FunctionName : 'lambda_handler',
  InvocationType : 'RequestResponse',
  LogType : 'None'
}
//alert("made lambda... yay?");
function alertBox(){
  //var entered = document.getElementById("sendNum");
  //var asdf = (entered.elements[0].value);
  //var enteredInt = (parseInt(entered.elements[0].value));
  //alert(entered.toString());
  //alert(entered.elements[0].value);
  //alert(typeof asdf); //entered defaults to string
  //alert(enteredInt + 1);


}


function initiateLambda(){
  lambda.invoke(myParams, function(err, data){
    if (err) {
            prompt(err);
         } else {
            alert("eyyy");
         }
  });
}


/*
var myParams = {
  FunctionName : 'lambda_handler',
  InvocationType : 'RequestResponse',
  LogType : 'None'
}

lambda.invoke(myParams, function(err, data)){
  if (err) {
   prompt(err);
} else {
   alert("eyyy");
}
}


/*
console.log('Loading function');

exports.handler = (event, context, callback) => {

};
*/
