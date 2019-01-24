/* Javascript for GeogebraXBlock. */
function GeogebraXBlock(runtime, element) {

    var ggbApp = new GGBApplet({
        "appName": "graphing", 
        "width": 800, 
        "height": 600, 
        "showToolBar": true, 
        "showAlgebraInput": true, 
        "showMenuBar": true 
    }, true);
    
    window.addEventListener("load", function() { 
        ggbApp.inject('ggb-element');
    });


    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
