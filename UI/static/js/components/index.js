function include(file) {
    const script = document.createElement('script');
    script.src = file;
    script.type = 'text/javascript';
    script.defer = true;

    document.getElementsByTagName('head').item(0).appendChild(script);
}

/* include all the Chat components js file */

var rootPath="https://diwakarojha.github.io/aiviveka_bot/UI"

include(rootPath+'/static/js/components/chat.js');
include(rootPath+'/static/js/constants.js');
include(rootPath+'/static/js/components/cardsCarousel.js');
include(rootPath+'/static/js/components/botTyping.js');
include(rootPath+'/static/js/components/charts.js');
include(rootPath+'/static/js/components/collapsible.js');
include(rootPath+'/static/js/components/dropDown.js');
include(rootPath+'/static/js/components/location.js');
include(rootPath+'/static/js/components/pdfAttachment.js');
include(rootPath+'/static/js/components/quickReplies.js');
include(rootPath+'/static/js/components/suggestionButtons.js');

// include('./static/js/components/chat.js');
// include('./static/js/constants.js');
// include('./static/js/components/cardsCarousel.js');
// include('./static/js/components/botTyping.js');
// include('./static/js/components/charts.js');
// include('./static/js/components/collapsible.js');
// include('./static/js/components/dropDown.js');
// include('./static/js/components/location.js');
// include('./static/js/components/pdfAttachment.js');
// include('./static/js/components/quickReplies.js');
// include('./static/js/components/suggestionButtons.js');

