<?php

$xmlstr = 'https://as.com/rss/motor/formula_1.xml';
$xml = simplexml_load_file($xmlstr);

foreach ($xml->channel->item as $item) {
   
    echo $item->title . "<br>";
}

?>
