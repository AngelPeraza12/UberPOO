<?php
require_once('car.php');
require_once('UberX.php');
require_once('UberPool.php');
require_once('account.php');

$uberX = new UberX("CVB123", new Account("Andres herrera", "1033888999"), "Chevrolet", "Spark");
$uberX->printDataCar();

$uberPool = new UberPool("RTS486", new Account("Nairu Perez", "52069582"), "Mazda", "Mazda3");
$uberPool->printDataCar();

?>