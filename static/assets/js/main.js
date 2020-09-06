$(document).ready(function () {
	flashed_messages();
});


/*
Alerts modal
*/

function flashed_messages() {
	let messages = parseInt($("#messages p").length);
	if (messages) {
		$("#alerts").slideDown(1500);
		setTimeout(() => {
			$("#alerts").slideUp(1500);
		}, 7000);
	}
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });

  // Initialize collapsible (uncomment the lines below if you use the dropdown variation)
  // var collapsibleElem = document.querySelector('.collapsible');
  // var collapsibleInstance = M.Collapsible.init(collapsibleElem, options);