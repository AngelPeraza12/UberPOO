class Main {
        
    public static void main(String[] args) {
        System.out.prinln("Hola Mundo")  
        Car car = new Car("AMQ123", new Account("Andres Herrera", "AND123" ));
        car.passenger = 4;
        car.printDataCar();
        
        Car car2 = new Car("LSP12D", new Account("Angel Peraza", "LSP12D"));
        car2.passenger = 2;
        car2.printDataCar();
        
    }
}