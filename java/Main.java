class Main {
        
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "AND123", "email@dominio.com" ));
        car.passenger = 4;
        car.printDataCar();
        
        Car car2 = new Car("LSP12D", new Account("Angel Peraza", "LSP12D", "email@dominio.com"));
        car2.passenger = 2;
        car2.printDataCar();
        
    }
}