
// Generate a username string
function randString(id){
  var dataSet = $(id).attr('data-character-set-u').split(',');  
  var possible = '';
  var intYear = dteNow.getFullYear();

  if($.inArray('0-9', dataSet) >= 0){
    possible += '0123456789';
  }

  var text = '';
  for(var i=0; i < $(id).attr('data-size-u'); i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return intYear+text;
}

// Create a new password on page load
$('input[rel="gp"]').each(function(){
  $(this).val(randString($(this)));
});

// Create a new password
$(".getNewPass").click(function(){
  var field = $(this).closest('div').find('input[rel="gp"]');
  field.val(randString(field));
});

// Auto Select Pass On Focus
$('input[rel="gp"]').on("click", function () {
   $(this).select();
});


