<?php
require_once('account.php');

class Car {
    public $license;
    public $driver;
    public $passenger;
    public $id;

    public function __construct($license, $driver){
        $this->license = $license;
        $this->driver = $driver;
    }

    public function printDataCar(){
        echo "Licencia: $this->license Driver " .$this->driver->name;
    }

}

?>