<html>
<head>
<title>UCLA Loneliness Scale</title>
</head>

<?php
$questions =
	array(
		"How often do you feel unhappy doing so many things alone?",
		"How often do you feel you have nobody to talk to?",
		"How often do you feel you cannot tolerate being so alone?",
		"How often do you feel as if nobody really understands you?",
		"How often do you find yourself waiting for people to call or write?",
		"How often do you feel completely alone?",
		"How often do you feel you are unable to reach out and communicate with those around you?",
		"How often do you feel starved for company?",
		"How often do you feel it is difficult for you to make friends?",
		"How often do you feel shut out and excluded by others?");

$answers = array();
for($i=0; $i<count($questions); $i++)
{
	if(isset($_GET[$i]))
		$answers[$i] = $_GET[$i];
}
?>

<body>
<h1>UCLA Loneliness Scale</h1>

<p>This form is dynamic and stores no information.</p>

<form method="get">
<table>
<tr>
<td>Question</td><td>Often</td><td>Sometimes</td><td>Rarely</td><td>Never</td>
</tr>
<?php
for($i=0; $i<count($questions); $i++)
{
	?>
	<tr>
	<td><?php echo $questions[$i]; ?></td>
	<?php
	for($j=4; $j>0; $j--)
	{
		?>
		<td align="center"><input type="radio" name="<?php echo $i;?>" value="<?php echo $j; ?>" <?php if($answers[$i]==$j) echo "checked" ; ?> /></td>
		<?php
	}
	?>
	</tr>
	<?php
}
?>
</table>
<input type="submit" value="Calculate Score" />
</form>

<?php
if(count($questions)==count($answers))
{
	?>
	<p>
	You scored: <?php echo array_sum($answers); ?>
	</p>

	<p>
	Scoring:<br />
	Often => 4<br />
	Sometimes => 3<br />
	Rarely => 2<br />
	Never => 1<br />
	</p>

	<p>
	Scores between 15 and 20 are considered normal. Scores above 30 indicate severe loneliness.
	</p>
	<?php
}
?>
</body>
</html>
