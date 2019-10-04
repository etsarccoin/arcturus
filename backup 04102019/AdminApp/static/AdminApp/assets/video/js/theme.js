// JavaScript Document

// For Banner
var $owl = $('.baner-slider');
$owl.on('initialized.owl.carousel resized.owl.carousel', function(e) {
	"use strict";
	$(e.target).toggleClass('hide-nav', e.item.count <= e.page.size);
});
$owl.owlCarousel({ 
	items: 1,
	loop:false,
	dots:false,
	nav:false,
	autoplay:false,
	margin:0,
	thumbs:false,
	navText:['',''],//['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
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


















// For Product Slider
var $sync1 = $("#sync1"),
	$sync2 = $("#sync2"),
	duration = 300;

$sync1.owlCarousel({
		items: 1,
		navText:['',''],
		mouseDrag: false,
		touchDrag: false,
		loop:false,
		dots:false,
		nav:false,
	}).on('changed.owl.carousel', function (e) {
		"use strict";
		var syncedPosition = syncPosition(e.item.index);
		if ( syncedPosition !== "stayStill" ) {
			$sync2.trigger('to.owl.carousel', [syncedPosition, duration, true]);
		}
	});
$sync2.on('initialized.owl.carousel resized.owl.carousel', function(e) {
		"use strict";
		$(e.target).toggleClass('hide-nav', e.item.count <= e.page.size);
	}).owlCarousel({
		loop:false,
		dots:false,
		nav:true,
		items: 4,
		margin: 5,
		stagePadding: 0,
		navText:['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
	}).on('click', '.owl-item', function () {
		"use strict";
		$sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);
	});
function addClassCurrent(index) {
	"use strict";
	$sync2.find(".owl-item").removeClass("current").eq( index ).addClass("current");
}
function syncPosition(index) {
	"use strict";
	addClassCurrent(index);
	var itemsNo = $sync2.find(".owl-item").length;
	var visibleItemsNo = $sync2.find(".owl-item.active").length;
	if (itemsNo === visibleItemsNo) {
		return "stayStill";
	}
	var visibleCurrentIndex = $sync2.find(".owl-item.active").index( $sync2.find(".owl-item.current") );
	if (visibleCurrentIndex === 0 && index !== 0) {
			return index - 1;
	}
	if (visibleCurrentIndex === (visibleItemsNo - 1) && index !== (itemsNo - 1)) {
			return index - visibleItemsNo + 2;
	}
	return "stayStill";
}

// For Data Table
$(document).ready(function() {	
	"use strict";
	$('#demo-table').DataTable( {
		responsive: true,
		"pagingType": "full_numbers",
		"lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]]
	});
});

// For Date Picker
$('#delivery-date').datepicker({
	todayBtn: true,
	autoclose: true,
	todayHighlight: true
});

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

















