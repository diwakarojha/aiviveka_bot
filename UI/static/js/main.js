function loadBot() {
  const content = '<!--Import Google Icon Font-->\
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />\
      <!-- <link rel="preconnect" href="https://fonts.gstatic.com" />\
     <!--Import Font Awesome Icon Font-->\
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous"/>\
     <!--Import materialize.css-->\
     <link rel="stylesheet" type="text/css" href="./static/css/materialize.min.css" />\
     <!--Main css-->\
     <link rel="stylesheet" type="text/css" href="./static/css/style.css" />\
     <meta name="viewport" content="width=device-width, initial-scale=1" />\
      <div class="chat_container">\
       <!-- Modal for rendering the charts, declare this if you want to render charts, \
          else you remove the modal -->\
       <div id="modal" class="modal">\
         <canvas id="modal-chart"></canvas>\
       </div>\
       <!--chatbot widget -->\
       <div class="widget">\
         <div class="chat_header">\
           <!--Add the name of the bot here -->\
           <span class="chat_header_title">Welcome at AIViveka!</span>\
           \
           <span class="close-trigger" href="#" id="close">\
            <i class="material-icons"> close </i>\
           </span>\
           <!-- <span class="dropdown-trigger" href="#" data-target="dropdown1">\
             <i class="material-icons"> more_vert </i>\
           </span> -->\
           <!-- Dropdown menu-->\
           <!-- <ul id="dropdown1" class="dropdown-content">\
             <li><a href="#" id="clear">Clear</a></li>\
             <li><a href="#" id="restart">Restart</a></li>\
             <li><a href="#" id="close">Close</a></li>\
           </ul> -->\
         </div>\
         <!--Chatbot contents goes here -->\
         <div class="chats" id="chats">\
           <div class="clearfix"></div>\
         </div>\
         <!--keypad for user to type the message -->\
         <div class="keypad">\
           <textarea id="userInput" placeholder="Say \'Hi\' to get Started..." class="usrInput">\
           </textarea>\
           <div id="sendButton">\
             <i class="fa fa-paper-plane" aria-hidden="true"></i>\
           </div>\
         </div>\
       </div>\
       <!--bot profile-->\
       <div class="profile_div" id="profile_div">\
         <img class="imgProfile" src="./static/img/botAvatar.png" />\
       </div>\
       <!-- Bot pop-up intro -->\
       <div class="tap-target" data-target="profile_div">\
         <div class="tap-target-content">\
           <h5 class="white-text">Welcome!👋</h5>\
           <p class="white-text">\
             Tap me for help...\
           </p>\
         </div>\
       </div>\
     </div>'
  var rootPath="."
  let chatBotDiv = document.createElement('div')
  chatBotDiv.innerHTML = content

  let jqueryScript = document.createElement('script')
  jqueryScript.src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
  chatBotDiv.appendChild(jqueryScript)

  let materializeScript = document.createElement('script')
  materializeScript.src=rootPath+"/static/js/lib/materialize.min.js"
  chatBotDiv.appendChild(materializeScript)

  let uuidMinScript = document.createElement('script')
  uuidMinScript.src=rootPath+"/static/js/lib/uuid.min.js"
  chatBotDiv.appendChild(uuidMinScript)

  let scScript = document.createElement('script')
  scScript.src=rootPath+"/static/js/script.js"
  chatBotDiv.appendChild(scScript)

  let chartMinScript = document.createElement('script')
  chartMinScript.src=rootPath+"/static/js/lib/chart.min.js"
  chatBotDiv.appendChild(chartMinScript)

  let showDownScript = document.createElement('script')
  showDownScript.src=rootPath+"/static/js/lib/showdown.min.js"
  chatBotDiv.appendChild(showDownScript)

  document.getElementsByTagName('body')[0].appendChild(chatBotDiv)
}


document.addEventListener("DOMContentLoaded", function () {
  loadBot()
});
