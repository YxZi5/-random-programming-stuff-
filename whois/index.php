<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>WHO.is</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<main>
		<header id="glowa">
			<h1>WHO IS</h1>
		</header>
		<br />
		<section id="sekcja1">
			<br />
			<form method="GET" action="index.php">
				<input id="formularz" type="text" name="ip"/>
				<input id="przycisk" type="submit" value="SZUKAJ"/>
			</form>
			<br />
		</section>
		<section id="sekcja2">
			<br />
			<?php
				error_reporting(0);
				function only_numbers_check($text)
				{
					$bad_chars = "asdfghjklzxcvbnmqwertyuiop";

					$bads = -1;

					for ($i = 0; $i <= strlen($text); $i++)
					{
						for ($k = 0; $k <= strlen($bad_chars); $k++)
						{
							if($text[$i] == $bad_chars[$k])
							{
								$bads += 1;
							}
						}
					}
					if($bads > 1)
					{
						return 1;
					}
					else
					{
						return 0;
					}
				}
				if(isset($_GET['ip']))
				{
					$vallidation = true;
					$ip = $_GET['ip'];

					if(only_numbers_check($ip) == 1)
					{
						$vallidation = false;
						// echo '<h2 style="color: red;">Enter valid IP address</h2>';
					}

					if(strlen($ip) < 7 || strlen($ip) > 15)
					{
						$vallidation = false;
						unset($ip);
					}
					
					if($vallidation == true)
					{
						$output = shell_exec("curl -s http://ipinfo.io/".$ip);

						echo '<h2>'. $output. '</h2>';

					}
					else
					{
						echo '<h2 style="color: red;">Enter valid IP address</h2>';
						unset($ip);
					}
				}
				else
				{
					echo "<h2>Wypełnij formularz</h2>";
				}
			?>
		</section>
		<footer>
			<br />
			<p>Wszelkie prawa zastrzeżone - 0000000000000000000000</p>
		</footer>
	</main>
</body>
</html>