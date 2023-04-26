public class CreatingnNews_Example {
    public void createInputDevices() {
        // Create new instances of each input device
        Keyboard keyboard = new Keyboard("Wired", "Dell", 1);
        String keyboard_input = keyboard.getInputType();
        String keyboard_brand = keyboard.getBrand();
        System.out.println("Keyboard input type: " + keyboard_input);
        System.out.println("Keyboard brand: " + keyboard_brand);

        Mouse mouse = new Mouse("Wireless", "Logitech", 1);
        String mouse_input = mouse.getInputType();
        String mouse_brand = mouse.getBrand();
        System.out.println("Mouse input type: " + mouse_input);
        System.out.println("Mouse brand: " + mouse_brand);

        Monitor monitor = new Monitor("HDMI", "Samsung", 16);
        String monitor_input = monitor.getInputType();
        String monitor_brand = monitor.getBrand();
        int monitor_size = monitor.getSize();
        System.out.println("Monitor input type: " + monitor_input);
        System.out.println("Monitor brand: " + monitor_brand);
        System.out.println("Monitor size: " + monitor_size);

        // Adittional
        AdditionalInput additionalInput = new AdditionalInput("USB", "Sony");
        additionalInput.addInput("Headphones");
        additionalInput.addInput("USB");
        additionalInput.addInput("Sony");
    };
};