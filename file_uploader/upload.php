<?php
	error_reporting(0);
	if(isset($_FILES['file']))
	{
		$errors = array();

		$file_name = $_FILES['file']['name'];
		$file_tmp = $_FILES['file']['tmp_name'];
		$file_ext = strtolower(end(explode(".", $_FILES['file']['name'])));

		$file_dest = "uploads/";

		$rozszerzenia = array("jpeg", "jpg", "png");
		$vallidation = true;

		if(in_array($file_ext, $rozszerzenia) == false)
		{
			// echo "Plik posiada błędne rozszerzenie!";
			$vallidation = false;
		}

		if($vallidation == true)
		{
			$movefile = move_uploaded_file($file_tmp, $file_dest . $file_name);
		}
		else
		{
			echo "Plik nie przeszedł walidacji! spróbuj ponownie lub skontaktuj się z administratorem";
		}
	}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>file_upload</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<main>
		<header>
			<h2>File Uploader</h2>
		</header>

		<br />

		<section id="sekcja1">
			<form action="upload.php" method="POST" enctype="multipart/form-data">
				<input type="file" name="file" id="send_file">
				<br /> <br /> <br />
				<input type="submit" value="WYŚLIJ" name="submit" id="przycisk">
				&nbsp;&nbsp;
				<button id="przycisk"><a href="index.php">POWRÓT</a></button>
				<br />
				<?php
					if($movefile)
					{
						echo '<h3 style="color: green;">file was sent successfully :)</h3>';
					}
				?>
			</form>
		</section>
	</main>
</body>
</html>