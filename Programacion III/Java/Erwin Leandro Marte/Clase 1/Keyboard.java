public class Keyboard extends InputDevice {
    private int keyboardId;

    public Keyboard(String inputType, String brand, int keyboardId) {
        super(inputType, brand);
        this.keyboardId = keyboardId;
    };

    public int getKeyboardId() {
        return keyboardId;
    };
};