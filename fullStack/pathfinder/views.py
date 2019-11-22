from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
#from polls.models import Poll

def index(request):

    html = '''

    <html lang="en">

<head>
  <link href = "static/css/bootstrap.min.css" rel = "stylesheet">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Placeholder Page Title</title> <!-- Placeholder-->

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>

  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading"> Options: </div>
      <div class="list-group list-group-flush">
        <a href="index.html" class="list-group-item list-group-item-action bg-dark">Home</a>
        <a href="http://localhost:8000/characterCreator/" class="list-group-item list-group-item-action bg-light">Character Creator</a>
        <a href="http://localhost:8000/battleSim/" class="list-group-item list-group-item-action bg-light">Battle Simulator</a>
        <a href="http://localhost:8000/beginnersGuide/" class="list-group-item list-group-item-action bg-light">Beginner's Guide</a>
        <a href="http://localhost:8000/info/" class="list-group-item list-group-item-action bg-light">Info</a>

      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <!-- Menu Toggle Button -->
        <button class="btn btn-primary" id="menu-toggle"> ≡ </button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost:8000/login/">Login</a>
            </li>

          </ul>
        </div>
      </nav>
      <!-- main area of page -->
      <div class="container-fluid">

        <h1 class="mt-4">Placeholder Project Title</h1>
        <p style = "color: red;"> Matt Varelli, Christopher Cruz, Derek Windahl, and Isaac Freshour, with special thanks to Zach Taylor</p>
        <p> Some extra text or a nice picture or something goes here </p>
        <!-- <img src = "https://mpng.pngfly.com/20180127/eyq/kisspng-ink-chinese-dragon-ink-dragon-5a6c48012ffd17.0315307415170457611966.jpg"> -->
        <!--<p>The starting state of the menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will change.</p>
        <p>Make sure to keep all page content within the <code>#page-content-wrapper</code>. The top navbar is optional, and just for demonstration. Just create an element with the <code>#menu-toggle</code> ID which will toggle the menu when clicked.</p> -->
      </div>
    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->

</body>

</html>

    '''

    return HttpResponse(html)

def characterCreator(request):
    html ='''
    <!-- see index.html for in depth comments, this is just a reimplementation of that at the moment -->


<!DOCTYPE html>
<!-- Open Source Template Credit: StartBootstrap -->
<html lang="en">
<meta charset="utf-8">


<!-- AWS SDK stuff -->
<script src="https://sdk.amazonaws.com/js/aws-sdk-2.558.0.min.js"></script>

<script type="text/javascript">
  AWS.config.update({region: 'us-east-1'});
  AWS.config.credentials = new AWS.CognitoIdentityCredentials({IdentityPoolId: 'us-east-1:7f58ba06-4893-483c-a60b-2576e66168ae'});

</script>


<!-- API stuff -->
<script type="text/javascript" src="../apiGateway-js-sdk/lib/axios/dist/axios.standalone.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/CryptoJS/rollups/hmac-sha256.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/CryptoJS/rollups/sha256.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/CryptoJS/components/hmac.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/CryptoJS/components/enc-base64.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/url-template/url-template.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/apiGatewayCore/sigV4Client.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/apiGatewayCore/apiGatewayClient.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/apiGatewayCore/simpleHttpClient.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/lib/apiGatewayCore/utils.js"></script>
<script type="text/javascript" src="../apiGateway-js-sdk/apigClient.js"></script>

<!-- local js stuff -->
<script src = "./javascript/formToJSON.js"></script>
<script src = "./javascript/changePic.js"></script>


<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Character Creator</title> <!-- Placeholder-->

  <!-- Bootstrap core CSS -->
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>

  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading"> Options: </div>
      <div class="list-group list-group-flush">
        <a href="http://localhost:8000/" class="list-group-item list-group-item-action bg-dark">Home</a>
        <a href="http://localhost:8000/characterCreator/" class="list-group-item list-group-item-action bg-light">Character Creator</a>
        <a href="http://localhost:8000/battleSim/" class="list-group-item list-group-item-action bg-light">Battle Simulator</a>
        <a href="http://localhost:8000/beginnersGuide/" class="list-group-item list-group-item-action bg-light">Beginner's Guide</a>
        <a href="http://localhost:8000/info/" class="list-group-item list-group-item-action bg-light">Info</a>

      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <!-- Menu Toggle Button -->
        <button class="btn btn-primary" id="menu-toggle"> ≡ </button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost:8000/login/">Login</a>
            </li>

          </ul>
        </div>
      </nav>

      <div class="container-fluid">

        <h1 class="mt-4">Character Creator Stuff Here</h1>

        <div id = "divBox">
          <div id = "formArea">
            <form name = "characterForm" id = "characterForm">
              Character Name:<br>
              <input type="text" name="characterName" id ="characterName">
              <br>

              Race:<br>
              <select name = "race" id = "race">
                <option value = "human"> Human </option>
                <option value = "elf"> Elf </option>
                <option value = "dwarf"> Dwarf </option>
                <option value = "gnome"> Gnome </option>
                <option value = "halfling"> Halfling </option>
                <option value = "halfElf"> Half-Elf </option>
                <option value = "halfOrc"> Half-Orc </option>
              </select>
              <br>

              Class:<br>
              <select name = "class" id = "class" onchange="changePic()">
                <option value = "fighter"> Fighter </option>
                <option value = "rogue"> Rogue </option>
                <option value = "wizard"> Wizard </option>
              </select>
              <br>

              Strength:<br>
              <input type = "number" name = "strength">
              <br>

              Dexterity:<br>
              <input type = "number" name = "dexterity">
              <br>

              Constitution:<br>
              <input type = "number" name = "constitution">
              <br>

              Intelligence:<br>
              <input type = "number" name = "intelligence">
              <br>

              Wisdom:<br>
              <input type = "number" name = "wisdom">
              <br>

              Charisma:<br>
              <input type = "number" name = "charisma">
              <br>

              <br><br>

              <!-- <input type="submit" value="Submit" onclick="makeJSON()"> -->
            </form>
            <button type="button" name="button"  onclick="makeJSON()">Submit</button>

          </div>

          <div id = "pictureBox">
            <img id = "characterPic" src = ""> </img>
          </div>
        </div>
        <!--<p>The starting state of the menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will change.</p>
        <p>Make sure to keep all page content within the <code>#page-content-wrapper</code>. The top navbar is optional, and just for demonstration. Just create an element with the <code>#menu-toggle</code> ID which will toggle the menu when clicked.</p> -->
      </div>
    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->

  <!-- Bootstrap core JavaScript -->
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Menu Toggle Script -->
  <script>
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  </script>

</body>

</html>
'''
    return HttpResponse(html)


def battleSim(request):

    #coding for python for battle sim goes here

    html ='''
    <!-- see index.html for in depth comments, this is just a reimplementation of that at the moment -->


<!DOCTYPE html>
<!-- Open Source Template Credit: StartBootstrap -->
<html lang="en">

<script src="https://sdk.amazonaws.com/js/aws-sdk-2.558.0.min.js"></script>

<script type="text/javascript">
  AWS.config.update({region: 'us-east-1'});
  AWS.config.credentials = new AWS.CognitoIdentityCredentials({IdentityPoolId: 'us-east-1:6954362b-23fd-4348-9c16-59ac206e543e'});
  //alert("done")
  //hi
</script>
<script src="sendNumber.js"></script>
<script src = "getCharacter.js"></script>


<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Battle Simulator</title> <!-- Placeholder-->

  <!-- Bootstrap core CSS -->
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>

  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading"> Options: </div>
      <div class="list-group list-group-flush">
        <a href="http://localhost:8000/" class="list-group-item list-group-item-action bg-dark">Home</a>
        <a href="http://localhost:8000/characterCreator/" class="list-group-item list-group-item-action bg-light">Character Creator</a>
        <a href="http://localhost:8000/battleSim/" class="list-group-item list-group-item-action bg-light">Battle Simulator</a>
        <a href="http://localhost:8000/beginnersGuide/" class="list-group-item list-group-item-action bg-light">Beginner's Guide</a>
        <a href="http://localhost:8000/info/" class="list-group-item list-group-item-action bg-light">Info</a>

      <!--  <a href="#" class="list-group-item list-group-item-action bg-light">Profile</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Status</a> -->
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <!-- Menu Toggle Button -->
        <button class="btn btn-primary" id="menu-toggle"> ≡ </button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost:8000/login/">Login</a>
            </li>

          </ul>
        </div>
      </nav>


      <div class="container-fluid">

        <h1 class="mt-4">Battle Simulator Stuff Here</h1>
        <p> Some extra text or a nice picture or something goes here </p>
        <!--<p>The starting state of the menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will change.</p>
        <p>Make sure to keep all page content within the <code>#page-content-wrapper</code>. The top navbar is optional, and just for demonstration. Just create an element with the <code>#menu-toggle</code> ID which will toggle the menu when clicked.</p> -->

        <!-- form with text field and buttons for doing things in sendNumber.js -->
        <form id ="sendNum" action="./sendNumber.js">
          <input type = "number" name = "Enter"
          <br>
          <button type = "button" onclick="alertBox()"> Click </button>
          <br>
        </form>
        <br>
        <button type = "button" onclick = "initiateLambda()"> Lambda </button>
        <button type ="button" onclick = "getCharacterSheet()"> Query </button>
      </div>
    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->

  <!-- Bootstrap core JavaScript -->
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Menu Toggle Script -->
  <script>
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  </script>

</body>

</html>
'''
    return HttpResponse(html);

def beginnersGuide(request):
    html = '''
    <!-- see index.html for in depth comments, this is just a reimplementation of that at the moment -->


<!DOCTYPE html>
<!-- Open Source Template Credit: StartBootstrap -->
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Beginners Guide</title> <!-- Placeholder-->

  <!-- Bootstrap core CSS -->
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>

  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading"> Options: </div>
      <div class="list-group list-group-flush">
        <a href="http://localhost:8000/" class="list-group-item list-group-item-action bg-dark">Home</a>
        <a href="http://localhost:8000/characterCreator/" class="list-group-item list-group-item-action bg-light">Character Creator</a>
        <a href="http://localhost:8000/battleSim/" class="list-group-item list-group-item-action bg-light">Battle Simulator</a>
        <a href="http://localhost:8000/beginnersGuide/" class="list-group-item list-group-item-action bg-light">Beginner's Guide</a>
        <a href="http://localhost:8000/info/" class="list-group-item list-group-item-action bg-light">Info</a>

      <!--  <a href="#" class="list-group-item list-group-item-action bg-light">Profile</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Status</a> -->
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <!-- Menu Toggle Button -->
        <button class="btn btn-primary" id="menu-toggle"> ≡ </button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost:8000/login/">Login</a>
            </li>

          </ul>
        </div>
      </nav>


      <div class="container-fluid">

        <h1 class="mt-4">Beginners Guide Stuff Here</h1>
        <p> Some extra text or a nice picture or something goes here </p>
        <!-- <img src = "https://mpng.pngfly.com/20180127/eyq/kisspng-ink-chinese-dragon-ink-dragon-5a6c48012ffd17.0315307415170457611966.jpg"> -->
        <!--<p>The starting state of the menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will change.</p>
        <p>Make sure to keep all page content within the <code>#page-content-wrapper</code>. The top navbar is optional, and just for demonstration. Just create an element with the <code>#menu-toggle</code> ID which will toggle the menu when clicked.</p> -->
      </div>
    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->

  <!-- Bootstrap core JavaScript -->
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Menu Toggle Script -->
  <script>
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  </script>

</body>

</html>
'''

    return HttpResponse(html)

def info(request):
    html = '''
    <!-- see index.html for in depth comments, this is just a reimplementation of that at the moment -->

<!DOCTYPE html>
<!-- Open Source Template Credit: StartBootstrap -->
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Info</title> <!-- Placeholder-->

  <!-- Bootstrap core CSS -->
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>

  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading"> Options: </div>
      <div class="list-group list-group-flush">
        <a href="http://localhost:8000/" class="list-group-item list-group-item-action bg-dark">Home</a>
        <a href="http://localhost:8000/characterCreator/" class="list-group-item list-group-item-action bg-light">Character Creator</a>
        <a href="http://localhost:8000/battleSim/" class="list-group-item list-group-item-action bg-light">Battle Simulator</a>
        <a href="http://localhost:8000/beginnersGuide/" class="list-group-item list-group-item-action bg-light">Beginner's Guide</a>
        <a href="http://localhost:8000/info/" class="list-group-item list-group-item-action bg-light">Info</a>

      <!--  <a href="#" class="list-group-item list-group-item-action bg-light">Profile</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Status</a> -->
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <!-- Menu Toggle Button -->
        <button class="btn btn-primary" id="menu-toggle"> ≡ </button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost:8000/login/">Login</a>
            </li>

          </ul>
        </div>
      </nav>


      <div class="container-fluid">

        <h1 class="mt-4">Info Page Stuff Here</h1>
        <p> Some extra text or a nice picture or something goes here </p>

        <!--<p>The starting state of the menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will change.</p>
        <p>Make sure to keep all page content within the <code>#page-content-wrapper</code>. The top navbar is optional, and just for demonstration. Just create an element with the <code>#menu-toggle</code> ID which will toggle the menu when clicked.</p> -->
      </div>
    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->

  <!-- Bootstrap core JavaScript -->
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Menu Toggle Script -->
  <script>
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  </script>

</body>

</html>
'''
    return HttpResponse(html)

def login(request):
    html = '''
    <!-- NOTE: when uploading to the repo, you must do a few folders at a time instead of the whole thing!! -->

<!DOCTYPE html>
<!-- Open Source Template Credit: StartBootstrap -->
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Placeholder Page Title</title> <!-- Placeholder-->

  <!-- Bootstrap core CSS -->
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>

  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading"> Options: </div>
      <div class="list-group list-group-flush">
        <a href="http://localhost:8000/" class="list-group-item list-group-item-action bg-dark">Home</a>
        <a href="http://localhost:8000/characterCreator/" class="list-group-item list-group-item-action bg-light">Character Creator</a>
        <a href="http://localhost:8000/battleSim/" class="list-group-item list-group-item-action bg-light">Battle Simulator</a>
        <a href="http://localhost:8000/beginnersGuide/" class="list-group-item list-group-item-action bg-light">Beginner's Guide</a>
        <a href="http://localhost:8000/info/" class="list-group-item list-group-item-action bg-light">Info</a>

      <!--  <a href="#" class="list-group-item list-group-item-action bg-light">Profile</a>
        <a href="#" class="list-group-item list-group-item-action bg-light">Status</a> -->
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <!-- Menu Toggle Button -->
        <button class="btn btn-primary" id="menu-toggle"> ≡ </button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost:8000/login/">Login</a>
            </li>

          </ul>
        </div>
      </nav>


      <!-- main area of page -->
      <div class="container-fluid">

        <h1 class="mt-4">Placeholder for login</h1>

        <form name = "credentials" id = "credentials">
          <br><br>
          Username:
          <br>
          <input type="text" name="username" id ="username">
          <br><br>
          Password:
          <br>
          <input type="text" name= "password" id ="password">
          <br><br>
          <input type="submit" value="Submit" onclick= ""> <!-- JS function goes in quotes after onlick -->
          <br><br>
        <!--<p>The starting state of the menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will change.</p>
        <p>Make sure to keep all page content within the <code>#page-content-wrapper</code>. The top navbar is optional, and just for demonstration. Just create an element with the <code>#menu-toggle</code> ID which will toggle the menu when clicked.</p> -->
      </div>
    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->

  <!-- Bootstrap core JavaScript -->
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Menu Toggle Script -->
  <script>
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  </script>

</body>

</html>
'''
    return HttpResponse(html)
