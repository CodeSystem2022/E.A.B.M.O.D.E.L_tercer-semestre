public class InputDevice {
    private String inputType;
    private String brand;

    public InputDevice(String inputType, String brand) {
        this.inputType = inputType;
        this.brand = brand;
    };

    public String getInputType() {
        return inputType;
    };

    public String getBrand() {
        return brand;
    };
};