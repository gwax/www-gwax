<?php
$img = imageCreateTrueColor(512,512);
for($i=0; $i<512; $i++)
{
		for($j=0; $j<512; $j++)
		{
				$c = mt_rand(0,255);
				$col = imageColorAllocate($img, $c, $c, $c);
				imagesetpixel($img, $i, $j, $col);
		}
}

header("Content-Type: image/png");
imagepng($img);
imagedestroy($img);
?>
