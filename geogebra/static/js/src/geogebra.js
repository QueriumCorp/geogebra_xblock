/* Javascript for GeoGebraXBlock. */
function GeoGebraXBlock(runtime, element, data) {

    var ggb_url = data.ggb_url;

    var ggbApp = new GGBApplet({
        "appName": "graphing", 
        "width": 800, 
        "height": 600, 
        "showToolBar": true, 
        "showAlgebraInput": true, 
        "showMenuBar": true,
        "filename": ggb_url
    }, true);
    
    window.addEventListener("load", function() { 
        ggbApp.inject('ggb-element');
    });


    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
