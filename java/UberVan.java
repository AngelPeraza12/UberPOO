import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, ArrayList<String>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    private Integer passenger;

    public UberVan(String license, Account driver){
        super(license, driver);
    }

    public UberVan(String license, Account driver, 
    Map<String, ArrayList<String>> typeCarAccepted,
    ArrayList<String> seatsMaterial){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }

    public Integer getPassenger(){
        return passenger;
    }

    @Override
    public void setPassenger(Integer passenger) {
        if(passenger == 6){
            this.passenger = passenger;
        }else{
            System.out.println("Necesitas asignar 6 pasajeros");
        }
    }

    
}