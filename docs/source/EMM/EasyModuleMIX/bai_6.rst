**Bài 6: Hệ thống đèn giao thông**
=============


1. **Hệ thống đèn giao thông**

    Việc sử dụng Arduino làm hệ thống đèn giao thông là một ứng dụng rất thú vị trong việc hỗ trợ quá trình học tập. Với Easy Module Mix for Arduino Nano, học sinh, sinh viên có thể tự thiết kế và lập trình hệ thống đèn giao thông như một dự án thực tế, giúp rèn luyện kỹ năng lập trình và kỹ năng tư duy logic. Đồng thời, việc thực hiện các thí nghiệm với hệ thống đèn giao thông cũng giúp các bạn hiểu rõ hơn về cơ chế hoạt động và quy trình điều khiển của hệ thống đèn giao thông. Ngoài ra, sử dụng Arduino còn giúp giảm thiểu chi phí và đơn giản hóa quy trình thiết kế và lắp ráp.

2. **Sơ đồ kết nối**

   Sơ đồ kết nối:

   - Đèn LED 7 thanh

         +----------------------------------+-----------------------------------+
         | **LED 7 THANH**                  | **ARDUINO**                       |
         +==================================+===================================+
         | CLK                              | D3                                |
         +----------------------------------+-----------------------------------+
         | DIN                              | D2                                |
         +----------------------------------+-----------------------------------+

   - LED

         +----------------------------------+-----------------------------------+
         | **LED**                          | **ARDUINO**                       |
         +==================================+===================================+
         | LED 1                            | D3                                |
         +----------------------------------+-----------------------------------+
         | LED 2                            | D4                                |
         +----------------------------------+-----------------------------------+
         | LED 3                            | D5                                |
         +----------------------------------+-----------------------------------+

         .. image:: ../media/image26.png
            :width: 6.5in
            :height: 3.94236in
            :align: center
         |


3. **Hướng dẫn lập trình**

   .. code-block:: cpp

      #include <TM1637Display.h> // Bao gồm thư viện TM1637Display để điều khiển hiển thị 7 đoạn LED

      #define CLK 3 // Chân CLK được kết nối với chân 2 của Arduino
      #define DIO 2 // Chân DIO được kết nối với chân 3 của Arduino
      #define RED_LED_PIN 4 // Đèn LED đỏ được kết nối với chân 4 củamArduino
      #define YELLOW_LED_PIN 5 // Đèn LED màu vàng được kết nối với chân 5 của Arduino
      #define GREEN_LED_PIN 6 // Đèn LED màu xanh được kết nối với chân 6 của Arduino

      TM1637Display display(CLK, DIO); // Tạo một thể hiện của lớp TM1637Display

      void setup() {
         // Khởi tạo các đèn LED
         pinMode(RED_LED_PIN, OUTPUT);
         pinMode(YELLOW_LED_PIN, OUTPUT);
         pinMode(GREEN_LED_PIN, OUTPUT);

         // Khởi tạo hiển thị
         display.setBrightness(0x0f); // Đặt độ sáng của hiển thị (0-7)
      }

      void loop() {
         // Đèn xanh sáng trong 20 giây
         greenLight();
         countdownTimer(20);

         // Đèn vàng sáng trong 3 giây
         yellowLight();
         countdownTimer(3);

         // Đèn đỏ sáng trong 20 giây
         redLight();
         countdownTimer(20);
      }

      void redLight() {
         digitalWrite(RED_LED_PIN, LOW);
         digitalWrite(YELLOW_LED_PIN, HIGH);
         digitalWrite(GREEN_LED_PIN, HIGH);
      }

      void yellowLight() {
         digitalWrite(RED_LED_PIN, HIGH);
         digitalWrite(YELLOW_LED_PIN, LOW);
         digitalWrite(GREEN_LED_PIN, HIGH);
      }

      void greenLight() {
         digitalWrite(RED_LED_PIN, HIGH);
         digitalWrite(YELLOW_LED_PIN, HIGH);
         digitalWrite(GREEN_LED_PIN, LOW);
      }

      void countdownTimer(int seconds) {
         for (int i = seconds; i > 0; i--) {
            // Cập nhật hiển thị 7 đoạn với giá trị đếm ngược
            display.showNumberDec(i);
            // Trễ một giây
            delay(1000);
         }
         // Xóa hiển thị sau khi đếm ngược kết thúc
         display.clear();
      }

.. 