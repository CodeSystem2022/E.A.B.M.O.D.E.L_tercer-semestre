public class Mouse extends InputDevice {
    private int mouseId;

    public Mouse (String inputType, String brand, int mouseId) {
        super(inputType, brand);
        this.mouseId = mouseId;
    };

    public int getMouseId() {
        return mouseId;
    };
};