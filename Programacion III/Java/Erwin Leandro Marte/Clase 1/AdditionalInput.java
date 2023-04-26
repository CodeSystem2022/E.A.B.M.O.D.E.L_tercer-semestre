public class AdditionalInput extends InputDevice {
    private static int count = 0;
    private String[] inputs = new String[3];

    public AdditionalInput(String inputType, String brand) {
        super(inputType, brand);
    };

    public void addInput(String input) {
        if (count < 3) {
            inputs[count] = input;
            count++;
        } else {
            throw new RuntimeException("Cannot add more than 3 inputs");
        }
    };

    public String[] getInputs() {
        return inputs;
    };
};