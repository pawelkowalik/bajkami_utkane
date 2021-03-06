$(document).ready(function() {
	$('img').hide();
	$('img').fadeIn(1500);

//////////Bootstrap Selecters //////////
$("[rel=tooltip]").tooltip();
$("[rel=popover]").hover(function(){
	$(this).popover('toggle');
	});


////////// Function for client image rollovers //////////
imgclientHover();
function imgclientHover() {		
	$('a.client-link').hover(function(){		
			$(this).stop('true','true').fadeTo("normal",.8);
	},
		function(){
			$(this).stop('true','true').fadeTo("normal",1);
	});
}

////////// Function for footer image feed rollovers //////////
imgfeedHover();
function imgfeedHover() {		
	$('.img-feed a').hover(function(){		
			$(this).stop('true','true').fadeTo("normal",.6);
	},
		function(){
			$(this).stop('true','true').fadeTo("normal",1);
	});
} 

////////// CSS Fix //////////
 $(".post-list li:first-child").css("padding-top", "0px");
 $(".page-sidebar h5:first, .page-left-sidebar h5:first, .page-right-sidebar h5:first").css("margin-top", "0px");
 $('h5.title-bg').has('button').css("padding-bottom", "12px");

}); // End document.ready