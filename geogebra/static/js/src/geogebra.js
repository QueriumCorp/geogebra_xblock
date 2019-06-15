/* Javascript for GeoGebraXBlock. */
function GeoGebraXBlock(runtime, element, data) {

    var ggb_url;

    // it might be an older xblock instance without this field
    if (data.ggb_url == null) {
        ggb_url = "";
    } else {
        ggb_url = data.ggb_url;
    };

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
        ggbApp.inject('ggb-element');	// This just works on the initial page load, not on the initialization of each xblock 
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });

    ggbApp.inject('ggb-element');	// Try to get the ggbApp to load for every GeoGebra xblock on this page
}
