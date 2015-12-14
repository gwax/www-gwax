<?php
if(isset($_GET['delay']) && is_numeric($_GET['delay']))
	$delay = max((int)$_GET['delay'], 1);
else
	$delay = 10;

if(isset($_GET['width']) && is_numeric($_GET['width']))
	$width = max(min((int)$_GET['width'], 1920), 1);
else
	$width = 320;

if(isset($_GET['height']) && is_numeric($_GET['height']))
	$height = max(min((int)$_GET['height'], 1080), 1);
else
	$height = 240;

$out = new Imagick();
$out->newImage($width, $height, '#FF0000', 'gif');
$out->setImageDelay($delay);
$out->newImage($width, $height, '#00FF00', 'gif');
$out->setImageDelay($delay);
$out->newImage($width, $height, '#0000FF', 'gif');
$out->setImageDelay($delay);

header('Content-type: image/gif');
echo $out->getImagesBlob();
?>
