// JavaScript Document

// For Rating Star
$('.rating-star').raty({
	number: function() {
		"use strict";
		return $(this).attr('data-number');
	},
	score: function() {
		"use strict";
		return $(this).attr('data-score');
	},
	readOnly: false,
});

//Date picker
$('#date-picker').datepicker({
	todayBtn: true,
	autoclose: true,
	todayHighlight: true
});

//Timepicker
$('#time-picker').timepicker({
	showInputs: false,
	showSeconds: true,
});

//Colorpicker
$('#color-picker').colorpicker();

// Form Validation
(function() {
  'use strict';
  window.addEventListener('load', function() {
	  console.log(1);
	// Fetch all the forms we want to apply custom Bootstrap validation styles to
	var forms = document.getElementsByClassName('needs-validation');
	// Loop over them and prevent submission
	var validation = Array.prototype.filter.call(forms, function(form) {
		console.log(2);
	  form.addEventListener('submit', function(event) {
		  console.log(3);
		if (form.checkValidity() === false) {
			console.log(4);
		  event.preventDefault();
		  event.stopPropagation();
		}
		form.classList.add('was-validated');
	  }, false);
	});
  }, false);
})();

// For Banner
var $owl = $('.live-slider');
$owl.on('initialized.owl.carousel resized.owl.carousel', function(e) {
	"use strict";
	$(e.target).toggleClass('hide-nav', e.item.count <= e.page.size);
});
$owl.owlCarousel({ 
	items: 1,
	loop:true,
	dots:true,
	nav:false,
	autoplay:false,
	margin:60,
	navText:false,
	responsiveClass:true,
	responsive:{
		0:{
			items:1					
		},
		600:{
			items:1
		},
		1000:{
			items:1
		}
	},

});

// For Data Table
$(document).ready(function() {	
	"use strict";
	$('#coinHistoryTable').DataTable( {
		responsive: true,
		"pagingType": "full_numbers",
		"lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]]
	});
});













