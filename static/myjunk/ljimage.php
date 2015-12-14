<h1>Taken from <a href="http://adcott.net/ljimages/">LJImages</a></h1><br />

<?php

$n = 60; // this is the number of images displayed on the page, the maximum is 250

// The following is needed to comply with LJ's bot policy (livejournal.com/bots/)

$s = 'http://www.adcott.net/ljimages/'; // the address of your page
$e = 'adcott@livejournal.com'; // your email address

$fp = fsockopen('www.livejournal.com', 80);
if ($fp) {
  fputs($fp, "GET /stats/latest-img.bml HTTP/1.0\r\n".
      "Host: www.livejournal.com\r\n".
      "User-Agent: ".$s."; ".$e."\r\n\r\n");
  $data = '';
  while(!feof($fp)) {
    $data .= fgets($fp);
  }
  fclose($fp);

  preg_match_all("<recent-image img=\'([^\']+)\' url=\'([^\']+)\' />", $data, $out);
  
  for ($i=0; $i<$n; $i++) {
    echo "<a href='".$out[2][$i]."'><img src='".$out[1][$i]."' alt='' /></a><br /><br />\n";
  }
} else {
  echo 'connecting to LJ failed';
}

?>