let button = document.getElementById("color-toggle")

button.addEventListener("click", matchCommentsToTheme);
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
function matchCommentsToTheme() {
    console.log("Matchnig!");
    if(button.getAttribute("title") == "Activate Light Mode") {
        let message = {
          type: 'set-theme',
          theme: 'github-light' // 'github-light', etc.. 
        };
        let iframe = document.querySelector('.utterances-frame');
        iframe.contentWindow.postMessage(message, 'https://utteranc.es');
    } else {
        let message = {
          type: 'set-theme',
          theme: 'github-dark' // 'github-light', etc.. 
        };
        let iframe = document.querySelector('.utterances-frame');
        iframe.contentWindow.postMessage(message, 'https://utteranc.es');
    }

}

