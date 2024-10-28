function getUrlParameters(paramDelimiter){
    console.log("getUrlParameters");
    // grab current URL
    //var sPageURL = window.location.href;
    var sPageURL = 'http://34.121.126.205:8080/dropInRegistration/success.html?code=YHRD62KSIHZM3TLQFYOF';
    console.log("getUrlParameters sPageURL="+sPageURL);

    var sUrlVariables = sPageURL.split(paramDelimiter);

    for (var i=0; i<sUrlVariables.length; i++){
        console.log(sUrlVariables[1]);
    }

}



console.log(getUrlParameters('code='))