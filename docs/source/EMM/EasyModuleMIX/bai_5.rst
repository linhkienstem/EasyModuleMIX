**Bài 5: LED 7 đoạn**
=============

1. **LED 7 đoạn**

   Màn hình LED 7 đoạn là một thiết bị hiển thị điện tử đơn giản, thường dùng để hiển thị các chữ số và một số ký tự chữ cái. Nó gồm có bảy đoạn LED nhỏ, sắp xếp theo hình dạng của một số "8". Mỗi đoạn có thể được điều khiển riêng biệt để phát sáng, cho phép tạo ra các con số từ 0 đến 9 và một vài ký tự như A, F (thường dùng trong hệ thập lục phân).

   Các đoạn này thường được đánh dấu từ "A" đến "G", mỗi đoạn tương ứng với một phần của chữ số. Khi bật hoặc tắt các đoạn cụ thể, màn hình có thể hiển thị một loạt các số và ký tự khác nhau. Đây là một thiết bị cơ bản nhưng rất phổ biến trong các ứng dụng điện tử như đồng hồ kỹ thuật số, máy tính cầm tay và các bảng điều khiển.

   .. image:: ../media/image24.png
      :width: 4.76594in
      :height: 4.43213in
      :align: center
   |

2. **Ứng dụng**

   -  Bảng thiết thị
   -  Hiển thị chung
   -  Hiển thị tỷ giá
   -  Hiển thị đồng hồ

3. **Thông số kỹ thuật**

   -  Loại màn hình : LED 7 đoạn
   -  Số chữ số : 4 chữ số
   -  Chiều cao chữ số : Thông thường khoảng 0,56 inch (14,2mm)
   -  Loại phổ biến : Cathode chung hoặc Anode chung
   -  Màu sắc : Đỏ (các màu khác như xanh lá, xanh dương cũng có thể tùy theo nhà sản xuất)
   -  Đặc điểm điện từ:
      +  Điện áp chuyển tiếp (Vf) : Thường là 1,8V đến 2,2V trên mỗi phân đoạn (Đỏ)
      +  Dòng chuyển tiếp (Nếu) : Thông thường 10mA đến 20mA trên mỗi phân đoạn
      +  Điện áp ngược (Vr) : tối đa 5V
      +  Tản điện : Phụ thuộc vào số lượng đoạn được thắp sáng

   -  Cấu hình chân:
      +  Chân 1 : Cathode số 1/Anode chung
      +  Chân 2 : Đoạn E
      +  Chân 3 : Cathode số 2/Anode chung
      +  Chân 4 : Đoạn D
      +  Chân 5 : Đoạn C
      +  Chân 6 : Dấu thập phân (DP)
      +  Chân 7 : Đoạn G
      +  Chân 8 : Cathode số 3/Anode chung
      +  Chân 9 : Đoạn B
      +  Chân 10 : Đoạn A
      +  Chân 11 : Cathode số 4/Anode chung
      +  Chân 12 : Đoạn F

   .. image:: ../media/image24.png
      :width: 4.76594in
      :height: 4.43213in
      :align: center
   |

4. **Sơ đồ kết nối**

   -  Sơ đồ kết nối

   +----------------------------------+-----------------------------------+
   | **LED 7 THANH**                  | **ARDUINO**                       |
   +==================================+===================================+
   | CLK                              | D3                                |
   +----------------------------------+-----------------------------------+
   | DIN                              | D2                                |
   +----------------------------------+-----------------------------------+

   .. image:: ../media/image25.png
      :width: 6.5in
      :height: 3.94236in
      :align: center
   |

5. **Hướng dẫn lập trình**

.. code-block:: cpp
   // Bao gồm thư viện TM1637Display để điều khiển màn hình 7 đoạn
   #include <TM1637Display.h>

   // Định nghĩa các chân kết nối
   #define CLK 3 // Định nghĩa CLK là chân 3 (chân Clock kết nối với chân D3 của Arduino)
   #define DIO 2 // Định nghĩa DIO là chân 2 (chân Data In kết nối với chân D2 của Arduino)

   // Tạo một thể hiện của TM1637Display với các chân CLK và DIO đã được định nghĩa
   TM1637Display display(CLK, DIO);

   void setup() {
      // Thiết lập độ sáng của màn hình
      // 0x0f thiết lập độ sáng tối đa (phạm vi từ 0-7 cho độ sáng)
      display.setBrightness(0x0f);
   }
   void loop() {
      // Vòng lặp để hiển thị các số từ 0-9 tuần tự trên màn hình 7 đoạn
      for (int i = 0; i < 10; i++) {
         // Hiển thị số hiện tại (i) trên màn hình
         display.showNumberDec(i);
         delay(1000); // Chờ 1 giây trước khi hiển thị số tiếp theo
      }

      // Hiển thị một số cụ thể, ví dụ, 1234
      // Số 1234 sẽ được hiển thị trên màn hình 7 đoạn
      display.showNumberDec(1234);

      // Chờ 2 giây để giữ số được hiển thị
      delay(2000);

      // Xóa màn hình
      // Điều này sẽ tắt tất cả các đoạn của màn hình 7 đoạn
      display.clear();
      
      // Chờ 1 giây trước khi bắt đầu lại vòng lặp
      delay(1000);
   }

.. 