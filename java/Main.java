class Main {
        
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123", "email@dominio.com" ), "Chevrolet","Spark");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("ABC556", new Account("alexis campo", "1033888", "programacion@hotmail.com"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();

        
    }
}