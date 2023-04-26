public class Monitor extends InputDevice {
    private static int count = 0;
    private int size;

    public Monitor(String inputType, String brand, int size) {
        super(inputType, brand);
        if (count < 2) {
            this.size = size;
            count++;
        } else {
            throw new RuntimeException("Cannot create more than 2 monitors");
        };
    };

    public int getSize() {
        return size;
    };
};