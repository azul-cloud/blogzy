//Javascript that should be included on all pages will be placed in this file
$(document).ready(function(){

   /*
   get the csrftoken value and set it on all AJAX Posts. General requirement
   for all django applications.
   */
   function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
   }
   var csrftoken = getCookie('csrftoken');
   function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
   }
   $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
   });


   /*
   ACTIVATE TOOLTIPS - Bootstrap advises to only turn on tooltip for
   items that it is needed for performance reasons
   */
   $('.add-favorite').tooltip()
   $('.remove-favorite').tooltip()


   /*
   TOGGLE FAVORITE - user will see icons and they will be able
   to click the icon and toggle if the post should be included
   in their favorites
   */
   $( '.favorite' ).click( function() {
     // get shared variables
     post_id = $( this ).data( 'id' )
     var data = JSON.stringify({
        "post": "/api/v1/post/"+ post_id + "/"
     });

     // perform add/remove tasks
     if ($( this ).hasClass( 'add-favorite')) {
         var action = 'add'
         $.ajax({
            url: '/api/v1/userfavorite/',
            type: 'POST',
            contentType: 'application/json',
            data: data,
            dataType: 'json',
            processData: false
         })
         $( this ).attr( "data-original-title", "Remove Favorite" );
     }
     else if ($( this ).hasClass( 'remove-favorite' )) {
         var action = 'remove'
         $.ajax({
            url: '/api/v1/userfavorite/',
            type: 'DELETE',
            contentType: 'application/json',
            data: data,
            dataType: 'json',
            processData: false,
         })
         $( this ).attr( "data-original-title", "Add Favorite" );
     }

     // change attributes at the end
     $( this ).toggleClass( 'glyphicon-star remove-favorite glyphicon-star-empty add-favorite' )
   });


   /*
   TOGGLE WAVE - add or remove a blog to someone's personal wave
   */
   $( '.wave' ).click( function() {
     /*
     add a blog wave for the current user. Current user is defaulted in the server code.
     */
     blog_id = $( this ).data( 'id' );

     if ($( this ).hasClass( "add-wave" )) {
         // add the blog to the user's wave
         $.post(
            "/wave/add/" + blog_id + "/"
         );

         $( this ).removeClass( "add-wave btn-default" ).addClass( "remove-wave btn-danger" );
         $( this ).html("<span class='glyphicon glyphicon-trash'></span> Remove from Wave" );
     }
     else if ($( this ).hasClass( "remove-wave" )) {
         // remove the blog from the user's wave
         $.post(
            "/wave/remove/" + blog_id + "/"
         );

         $( this ).addClass( "add-wave btn-default" ).removeClass( "remove-wave btn-danger" );
         $( this ).html("<span class='glyphicon glyphicon-plus'></span> Add to Wave" );
     }
   });


   /*
   SUBMIT FEEDBACK - This feedback is submitted from the
   header which can be submitted from any page. Need to hit the submit
   page with the POST
   */
   $( '#contact-submit').click( function() {
     console.log("contact pushed");
     var message = $( '#id_message' ).val()
     var type = $( '#id_type' ).val()

     var data = JSON.stringify({
        message:message,
        type:type

     });

     if ( message != "" ) {
        if ( type != "" ) {
         $.post( "/sendcontact/", { 
            "message": message,
            "type": type
         } );

         // clean up on success
         console.log(data);
         $( "#form-message" ).html("<h4 style='color:green;'>Your contact has been sent successfully</h4>");
         $( "#id_contact" ).val("");
        }
        else {
          $( "#form-message" ).html("<h4 style='color:red;'>Please choose a type</h4>");   
        }
     }
     else {
        $( "#form-message" ).html("<h4 style='color:red;'>Please enter message above</h4>");
     }
   });


   /*
   OVERLAY REPOSITION - When on an xs screen on home page, need to reposition the
   position absolute search overlay box
   */
   $( '.navbar-toggle').click( function() {
     overlay = $( '.search-overlay' );
     overlay.toggleClass( 'drop' );
   });


   /*
   SOCIAL SHARE SHOW/HIDE - The social share buttons should only be visible
   when you hover over the Share button. When leaving the area with the mouse,
   the buttons should be hidden again and the Share button be visible


   $( ".social-share-start" ).hover( function() {
     $( this ).addClass( 'hidden' );
     $( '.social-share' ).removeClass( 'hidden' );
   });
   $( ".social-share" ).mouseleave( function() {
     $( this ).addClass( 'hidden' );
     $( '.social-share-start' ).removeClass( 'hidden' );
   });
   */
});