/*
g++ -L/usr/local/include/ tank.cpp -o tank -lrf24 -lgpiod && ./tank

https://circuitpython-nrf24l01.readthedocs.io/en/latest/
*/
#include <iostream>
#include <RF24/RF24.h>
#include <gpiod.h>

#ifndef	CONSUMER
#define	CONSUMER	"Consumer"
#endif

// RF24
#define PIN_CE 22
#define PIN_CSN 0

// GPIO
#define PIN_LED 2

#define RT_PIN_ENABLE_A 25
#define RT_PIN_IN1 24
#define RT_PIN_IN2 23

#define LT_PIN_ENABLE_A 16
#define LT_PIN_IN1 20
#define LT_PIN_IN2 26


using namespace std;


// Format:  [transStart] [order] [data 0] [data 1] ... [data n] [transEnd]
//          [x] is byte type and the range of [order] and [data x] is 0~127
// Process: The requesting party send the order, then the responding party respond the order.
//          The non blocking order will be responded immediately, and the blocking order will
//          be responded orderStart immediately, then respond orderDone after completion.

class Orders {
public:
    // Data stream control orders, range is 128 ~ 255
    // These orders are used to control data stream.

    static const uint8_t transStart = 128;
    static const uint8_t transEnd = 129;

    // Orders, range is 0 ~ 127
    // Orders are used to control target.
    // Some orders have proprietary response orders, others use orderStart and orderDone.
    // The even orders is sent by the requesting party, and the odd orders is sent by the responding party.

    // Simple action
    static const uint8_t requestCrawlForward = 80;       // [order]
    static const uint8_t requestCrawlBackward = 82;      // [order]
    static const uint8_t requestCrawlLeft = 84;          // [order]
    static const uint8_t requestCrawlRight = 86;         // [order]
    static const uint8_t requestTurnLeft = 88;           // [order]
    static const uint8_t requestTurnRight = 90;          // [order]
    static const uint8_t requestActiveMode = 92;         // [order]
    static const uint8_t requestSleepMode = 94;          // [order]
    static const uint8_t requestSwitchMode = 96;         // [order]

    // Complex action
    static const uint8_t requestCrawl = 110;             // [order] [64 + x] [64 + y] [64 + angle]
    static const uint8_t requestChangeBodyHeight = 112;  // [order] [64 + height]
    static const uint8_t requestMoveBody = 114;          // [order] [64 + x] [64 + y] [64 + z]
    static const uint8_t requestRotateBody = 116;        // [order] [64 + x] [64 + y] [64 + z]
    static const uint8_t requestTwistBody = 118;         // [order] [64 + xMove] [64 + yMove] [64 + zMove] [64 + xRotate] [64 + yRotate] [64 + zRotate]
};



// RF24
uint8_t pipeNumber;
uint8_t payloadSize;

uint8_t rf24Address[6] = { 'F', 'N', 'K', '2', '9' };

// GPIO
const char* chipname = "gpiochip0";
struct gpiod_chip *chip;
struct gpiod_line *ledLine;
struct gpiod_line *ltLine;
struct gpiod_line *rtLine;

int main() {
    RF24 radio(PIN_CE, PIN_CSN);

    radio.begin();
    radio.setChannel(125);
    radio.setPALevel(RF24_PA_HIGH);
    radio.setDataRate(RF24_1MBPS);
    radio.enableDynamicPayloads();
    //radio.openReadingPipe(0, 0x7878787878LL);
    radio.openReadingPipe(0, rf24Address);;
    radio.printDetails();
    radio.startListening();

    cout << "Start listening..." << endl;

    chip = gpiod_chip_open_by_name(chipname);
    if (!chip) {
        cout <<"Open chip failed" << endl;
        return 1;
    }

    ledLine = gpiod_chip_get_line(chip, PIN_LED);
    if (!ledLine) {
        cout << "Get ledLine line failed" << endl;
        gpiod_chip_close(chip);
        return 1;
    }
    int ledLineOutputRequestReturn = gpiod_line_request_output(ledLine, CONSUMER, 0);
	if (ledLineOutputRequestReturn < 0) {
		cout << "Request ledLine line as output failed" << endl;
		gpiod_chip_close(chip);
		return 1;
	}


    ltLine = gpiod_chip_get_line(chip, LT_PIN_ENABLE_A);
    if (!ltLine) {
        cout << "Get ltLine[" << LT_PIN_ENABLE_A << "] line failed (" << ltLine << ")" << endl;
        gpiod_chip_close(chip);
        return 1;
    }
    int ltLineOutputRequestReturn = gpiod_line_request_output(ltLine, CONSUMER, 0);
	if (ltLineOutputRequestReturn < 0) {
		cout << "Request ltLine line as output failed" << endl;
		gpiod_chip_close(chip);
		return 1;
	}


    rtLine = gpiod_chip_get_line(chip, RT_PIN_ENABLE_A);
    if (!rtLine) {
        cout << "Get rtLine[" << RT_PIN_ENABLE_A << "] line failed (" << rtLine << ")" << endl;
        gpiod_chip_close(chip);
        return 1;
    }
    int rtLineOutputRequestReturn = gpiod_line_request_output(rtLine, CONSUMER, 0);
	if (rtLineOutputRequestReturn < 0) {
		cout << "Request rtLine line as output failed" << endl;
		gpiod_chip_close(chip);
		return 1;
	}

    int bytes = 0;
    int led_flash = 0;
    int i = 0;
    while (true) {
        if (radio.available(&pipeNumber)) {
            payloadSize = radio.getDynamicPayloadSize();
            char payload[payloadSize];
//            string receivedData;
            radio.read(&payload, sizeof(payload));

            int direction = 0; // 0=stop,1=up,2=right,3=down,4=left
            if (payloadSize > 0) {
                if (payload[0] == Orders::transStart) {
                    cout << "Transmission Start" << endl;
                    if (payload[1] == Orders::requestCrawl) {
                        cout << "Drive" << endl;
                        //int trackOn = (i % 10 < 5) ? 0 : 1;

                        /*
                        joystick left
                        � 128 n 110 j 106 A 65 @ 64 � 129
                        */
                        if (payload[2] == 106 && payload[3] == 65) {
                            cout << "Turn Left" << endl;
                            direction = 4;
                        }
                        /*
                        joystick right
                        � 128 n 110  23 A 65 @ 64 � 129
                        */
                        else if (payload[2] == 23 && payload[3] == 65) {
                            cout << "Turn Right" << endl;
                            direction = 2;
                        }
                        /*
                        joystick up
                        � 128 n 110 A 65 j 106 @ 64 � 129
                        */
                        else if (payload[2] == 65 && payload[3] == 106) {
                            cout << "Drive Forward" << endl;
                            direction = 1;
                        }
                        /*
                        joystick down
                        � 128 n 110 A 65  23 @ 64 � 129
                        */
                        else if (payload[2] == 65 && payload[3] == 23) {
                            cout << "Stop" << endl;
                            direction = 3;
                        }
                    }
                    else {

                    }
                }

                for (uint8_t i = 0; i < payloadSize; i++) {
                    cout << (uint8_t) payload[i] << " ";
                    cout << (static_cast<unsigned int>(payload[i]) & 0xFF) << " ";
//                    receivedData += payload[i];
                }
                cout << endl;
                cout << "Pipe : " << (int) pipeNumber << " ";
                cout << "Size : " << (int) payloadSize << " ";
//                cout << "Data : " << receivedData << endl;
            }

            // flash led
			cout << "Set line output led " << led_flash << endl;
            int lineOutputRequestReturn = gpiod_line_set_value(ledLine, led_flash);
            if (lineOutputRequestReturn < 0) {
			    cout << "Set line output failed" << endl;
		        gpiod_chip_close(chip);
		        return 1;
		    }
		    led_flash = !led_flash;


		    if (direction == 0) { // nothing pressed

		    }
		    else if (direction == 1) { // up
		        int lineOutputRequestReturn = gpiod_line_set_value(ltLine, 1);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set ltLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
                lineOutputRequestReturn = gpiod_line_set_value(rtLine, 1);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set rtLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
		    }
		    else if (direction == 2) { // right
                int lineOutputRequestReturn = gpiod_line_set_value(ltLine, 1);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set ltLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
                lineOutputRequestReturn = gpiod_line_set_value(rtLine, 0);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set rtLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
		    }
		    else if (direction == 3) { // down
                int lineOutputRequestReturn = gpiod_line_set_value(ltLine, 0);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set ltLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
                lineOutputRequestReturn = gpiod_line_set_value(rtLine, 0);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set rtLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
		    }
		    else if (direction == 4) { // left
                int lineOutputRequestReturn = gpiod_line_set_value(ltLine, 0);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set ltLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
                lineOutputRequestReturn = gpiod_line_set_value(rtLine, 1);
                if (lineOutputRequestReturn < 0) {
                    cout << "Set rtLine output failed" << endl;
                    gpiod_chip_close(chip);
                    return 1;
                }
		    }

            delay(20);
            i++;
        }
    }

    return 0;
}

/*

record raw traffic

joystick up
Transmission Start
� 128 n 110 A 65 j 106 @ 64 � 129

joystick right
Transmission Start
� 128 n 110  23 A 65 @ 64 � 129
Pipe : 0 Size : 6 Set line output led 1

joystick down
Transmission Start
� 128 n 110 A 65  23 @ 64 � 129
Pipe : 0 Size : 6 Set line output led 1

joystick left
Transmission Start
� 128 n 110 j 106 A 65 @ 64 � 129
Pipe : 0 Size : 6 Set line output led 0

*/