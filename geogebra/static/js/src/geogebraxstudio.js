/* Javascript for GeoGebraxStudio. */
function GeoGebraxStudio(runtime, element, question) {
    // Stub notify so xblock doesnt crash in dev
    if( typeof runtime.notify === "undefined" ){
        runtime.notify = function(){ console.info(arguments); }
    }
 
    var handlerUrl = runtime.handlerUrl(element, 'save_question');

    $('.save-button', element).click(function(eventObject) {
        var data = {
            ggb_url : $('#ggb_url', element).val(),
        }

        runtime.notify('save', {state:'start'});
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify(data),
            success: null
        }).done( function(response){
            runtime.notify('save', {state:'end'});
        });
    });

    $('.cancel-button', element).click(function(eventObject) {
        runtime.notify('cancel', {});
    });
 
    /* PAGE LOAD EVENT */
    $(function ($) {
    });

}
