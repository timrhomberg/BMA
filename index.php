<?php
  /* Functions for redis operations starts here   */

  $redisObj = new Redis();

  function openRedisConnection( $hostName, $port){
        global $redisObj;
        // Opening a redis connection
        $redisObj->connect( $hostName, $port );
        return $redisObj;
  }



  function getValueFromKey( $key ){
        try{
                global $redisObj;
                // getting the value from redis
                return $redisObj->get( $key);
        }catch( Exception $e ){
                echo $e->getMessage();
        }
  }

  openRedisConnection( 'localhost', 6379 );
  $varvorne = getValueFromKey( 'vorne' );
  $varhinten = getValueFromKey( 'hinten' );
?>
<html>
  <head>
    <title>Sensor Daten</title>
  </head>
  <body>
   <h1>Ultraschall Sensor Daten</h1>
   <p>Sensor Vorne: <?php echo "<b>$varvorne</b>"; ?> </p>
   <p>Sensor Hinten: <?php echo "<b>$varhinten</b>"; ?>  </p>
  </body>
</html>