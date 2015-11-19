$(".icon").click(function() {
	var icon = $(this),
			input = icon.parent().find("#search"),
			submit = icon.parent().find(".submit"),
			is_submit_clicked = false;
	
	// Animate the input field
	input.animate({
		"width": "165px",
		"padding": "10px",
		"opacity": 1
	}, 300, function() {
		input.focus();
	});
	
	submit.mousedown(function() {
		is_submit_clicked = true;
	});
	
	// Now, we need to hide the icon too
	icon.fadeOut(300);
	
	// Looks great, but what about hiding the input when it loses focus and doesnt contain any value? Lets do that too
	input.blur(function() {
		if(!input.val() && !is_submit_clicked) {
			input.animate({
				"width": "0",
				"padding": "0",
				"opacity": 0
			}, 200);
			
			// Get the icon back
			icon.fadeIn(200);
		};
	});
});









