## ค้นหาชื่อจากรูป_ผิด
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.แจ้งข้อมูลสมุนไพร {"herb":"มะนาว"}
 - bot.validation.get_data.herb_name

## ค้นหาชื่อจากรูป_ถูก
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ใช่
 - bot.utter.thankyou
 
## ขอดูรูปจากชื่อสมุนไพร_ผิด
* user.ดูรูปสมุนไพร {"herb":"ขมิ้นชัน"}
 - bot.action.name_to_photo
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.แจ้งข้อมูลสมุนไพร {"herb":"มะนาว"}
 - bot.validation.get_data.herb_photo
  
## ขอดูรูปจากชื่อสมุนไพร_ถูก
* user.ดูรูปสมุนไพร {"herb":"ขมิ้นชัน"}
 - bot.action.name_to_photo
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ใช่
 - bot.utter.thankyou
 
## ข้อมูลทั่วไป
* user.สรรพคุณสมุนไพร {"herb":"มะนาว"}
 - bot.action.name_to_benefit
 - bot.utter.benefit

## ข้อมูลทั่วไป
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb":"มะนาว"}
 - bot.action.name_to_detail
 - bot.utter.detail