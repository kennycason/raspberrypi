/*
 * Sketch     Crawl function example
 * Platform   Freenove Hexapod Robot (Compatible with Arduino/Genuino Mega 2560)
 * Brief      This sketch is used to show how to control Freenove Hexapod Robot with code.
 *            You can easily achieve custom function by using FNHR library we provide.
 * Note       Keep the power off when uploading the code to prevent the robot from suddenly moving 
 *            after the upload is complete. Before turning on the power, disconnect the USB cable 
 *            and place the robot on a smooth surface that has no other objects.
 * Author     Ethan Pan @ Freenove (support@freenove.com)
 * Date       2020/04/24
 * Copyright  Copyright © Freenove (http://www.freenove.com)
 * License    Creative Commons Attribution ShareAlike 3.0
 *            (http://creativecommons.org/licenses/by-sa/3.0/legalcode)
 * -----------------------------------------------------------------------------------------------*/

#ifndef ARDUINO_AVR_MEGA2560
#error Wrong board. Please choose "Arduino/Genuino Mega or Mega 2560"
#endif

// Include FNHR (Freenove Hexapod Robot) library
#include <FNHR.h>

FNHR robot;

void setup() {
  // Custom setup code start

  // Custom setup code end
  // Start Freenove Hexapod Robot
  robot.Start();
}

void loop() {
  // Custom loop code start

  delay(2000);

  // Crawl forward
  robot.Crawl(0, 21, 0);
  robot.Crawl(0, 21, 0);
  robot.Crawl(0, 21, 0);
  robot.Crawl(0, 21, 0);
  delay(1000);

  // Crawl backward
  robot.Crawl(0, -42, 0);
  robot.Crawl(0, -42, 0);
  robot.Crawl(0, -42, 0);
  robot.Crawl(0, -42, 0);
  delay(1000);

  // Crawl left
  robot.Crawl(21, 0, 0);
  robot.Crawl(21, 0, 0);
  robot.Crawl(21, 0, 0);
  robot.Crawl(21, 0, 0);
  delay(1000);

  // Crawl right
  robot.Crawl(-42, 0, 0);
  robot.Crawl(-42, 0, 0);
  robot.Crawl(-42, 0, 0);
  robot.Crawl(-42, 0, 0);
  delay(1000);

  // Turn left
  robot.Crawl(0, 0, -9);
  robot.Crawl(0, 0, -9);
  robot.Crawl(0, 0, -9);
  robot.Crawl(0, 0, -9);
  delay(1000);

  // Turn right
  robot.Crawl(0, 0, 18);
  robot.Crawl(0, 0, 18);
  robot.Crawl(0, 0, 18);
  robot.Crawl(0, 0, 18);
  delay(1000);

  // Crawl forward and turn left
  robot.Crawl(0, 28, -12);
  robot.Crawl(0, 28, -12);
  robot.Crawl(0, 28, -12);
  robot.Crawl(0, 28, -12);
  delay(1000);

  // Crawl backward and turn right
  robot.Crawl(0, -28, 12);
  robot.Crawl(0, -28, 12);
  robot.Crawl(0, -28, 12);
  robot.Crawl(0, -28, 12);
  delay(1000);

  // Crawl left and turn left
  robot.Crawl(28, 0, -12);
  robot.Crawl(28, 0, -12);
  robot.Crawl(28, 0, -12);
  robot.Crawl(28, 0, -12);
  delay(1000);

  // Crawl right and turn right
  robot.Crawl(-28, 0, 12);
  robot.Crawl(-28, 0, 12);
  robot.Crawl(-28, 0, 12);
  robot.Crawl(-28, 0, 12);
  delay(1000);

  // Sleep mode
  robot.SleepMode();

  while (true);
  // Custom loop code end
}
