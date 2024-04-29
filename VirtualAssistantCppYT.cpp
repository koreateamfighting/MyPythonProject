#include <ArduinoGraphics.h>
#include <Arduino_MKRRGB.h>
#include "thingProperties.h"

void setup() {
    Serial.begin(9600);
    delay(1500);

    MATRIX.begin();
    MATRIX.brightness(10);

    initProperties();

    ArduinoCloud.begin(ArduinoIoTPreferredConnection);

    setDebugMessageLevel(2);
    ArduinoCloud.printDebugInfo();
}

void loop() {
    ArduinoCloud.update();
    // No code required in the loop for this setup
}


void onLoungeAreaChange() {
    uint8_t r, g, b;
    loungeArea.getValue().getRGB(r, g, b);
    if (loungeArea.getSwitch()) {
        Serial.println("R:" + String(r) + " G:" + String(g) + " B:" + String(b));  //prints the current R, G, B values
        MATRIX.beginDraw();                                                        //starts a new "drawing" on the RGB shield's pixels
        MATRIX.clear();                                                            //clears the RGB shield's pixels
        MATRIX.noStroke();
        MATRIX.fill(r, g, b);                                //the r, g, b values are fed into the shield's pixels
        MATRIX.rect(0, 0, MATRIX.width(), MATRIX.height());  //creates a rectangle (this covers the entire matrix)
        MATRIX.endDraw();                                    // ends the draw, and displays the new "drawing"

    }
    else {
        Serial.println("Lamp Off");
        //the following code simply turns everything off
        MATRIX.beginDraw();
        MATRIX.clear();
        MATRIX.noStroke();
        MATRIX.fill(0, 0, 0);
        MATRIX.rect(0, 0, MATRIX.width(), MATRIX.height());
        MATRIX.endDraw();
    }
}