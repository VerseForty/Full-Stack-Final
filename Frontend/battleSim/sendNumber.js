//dont use classroom for anything!
//require does not need to be done for browser JS, only if JS is used as a source code

//creates lambda object
var lambda = new AWS.Lambda();

//dummy parameters, note the name of the function is specified and is included in the parameters so that it calls upon that specific function
var myParams = {
  FunctionName : 'lambda_test',
  InvocationType : 'RequestResponse',
  LogType : 'None'
}

//function to open alert box when top button pressed
function alertBox(){
  //gets element from the field "sendNum" in the document (battleSim.html)
  var entered = document.getElementById("sendNum");

  //getting the element returns an HTML object that we need to take the main value of (at index 0)
  var asdf = (entered.elements[0].value);

  //last step gave us a string so we have to parse it
  var enteredInt = (parseInt(entered.elements[0].value));

  //opens text box and displays the number plus one
  alert(enteredInt + 1);


}

//function to call upon a lambda function
function initiateLambda(){

  //invokes the lambda function with teh parameters
  lambda.invoke(myParams, function(err, data){

    //if it errors, prompts an error message
    if (err) {
            prompt(err);
         }
         //otherwise puts up a message that it didnt error. the lambda function presently doesnt do anything
         //in the future the lambda function should produce a json file for the JavaScript here to do something with
         else {
            alert("Invoked Lambda function without erroring!");
         }
  });
}
