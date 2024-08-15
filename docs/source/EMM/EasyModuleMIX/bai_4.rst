**Bài 4: Nút bấm**
=============

1. **Button - Nút bấm**

   Button là nút bấm, bạn có thể tìm thấy nó ở mọi thứ trong cuộc sống, chẳng hạn như cái nút trong bàn phím của bạn.

   .. image:: ../media/image20.jpeg
      :width: 0.7697in
      :height: 0.82425in
      :align: center
   |

2. **Thông số kỹ thuật**

   -  Số chân: 4 chân
   -  Kiểu chân: chân cắm
   -  Chất liệu: nhựa, kim loại.

3. **Sơ đồ kết nối**

   Dùng dây jump cái cái để kết nối chân S của D2 với chân SW1 (hoặc có thể nối chân D2 với một trong các chân còn lại từ 2 - 5)

   +-----------------------------------+-----------------------------------+
   | **NÚT NHẤN**                      | **ARDUINO**                       |
   +===================================+===================================+
   | SW1                               | D2                                |
   +-----------------------------------+-----------------------------------+

   .. image:: ../media/image21.png
      :width: 5.77065in
      :height: 3.5in
      :align: center
   |

4. **Hướng dẫn lập trình**

   ~~~C++
   
   int button = 2;

   void setup() {
      Serial.begin(9600); //Mở cổng Serial ở baudrate 9600 để giao tiếp với máy tính
      pinMode(button, INPUT_PULLUP ); //Cài đặt chân D2 ở trạng thái đọc dữ liệu
   }
   void loop() {
      int buttonStatus = digitalRead(button); //Đọc trạng thái button
      Serial.println(buttonStatus); //Xuất trạng thái button
      delay(200); //Chờ 200ms
   }

   ~~~
.. 