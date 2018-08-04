## default greeting
* user.ทักทาย
 - bot.utter.greeting

## default thankyou
* user.ขอบคุณ
  - bot.utter.thankyou

## ค้นหาชื่อจากรูป_ผิด
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ไม่
 - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร {"herb":"มะนาว"}
 - bot.validation.get_data.herb_name
 
## ค้นหาชื่อจากรูป_ถูก
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ใช่
 - bot.utter.thankyou
## ค้นหาชื่อจากรูป_ไม่พบรูป
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
 - bot.utter.herb_name.not_found

## ค้นหาชื่อจากรูป_ผิด
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ไม่
 - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร {"herb":"มะนาว"}
 - bot.validation.get_data.herb_name
## ค้นหาชื่อจากรูป_ถูก
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ใช่
 - bot.utter.thankyou
## ค้นหาชื่อจากรูป_ไม่พบรูป
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
 - bot.utter.herb_name.not_found


## ขอดูรูปจากชื่อสมุนไพร_ผิด
* user.ดูรูปสมุนไพร {"herb":"ขมิ้นชัน"}
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ไม่
 - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร {"herb":"มะนาว"}
 - bot.validation.get_data.herb_photo
## ขอดูรูปจากชื่อสมุนไพร_ถูก
* user.ดูรูปสมุนไพร {"herb":"ขมิ้นชัน"}
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ใช่
 - bot.utter.thankyou
## ขอดูรูปจากชื่อสมุนไพรไม่พบ
* user.ดูรูปสมุนไพร {"herb":"ขมิ้นชัน"}
 - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
 - bot.utter.herb_photo.not_found
 
## ข้อมูลทั่วไป
* user.สรรพคุณสมุนไพร {"herb":"มะนาว"}
 - bot.action.name_to_benefit
 - bot.utter.benefit

## ข้อมูลทั่วไป
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb":"มะนาว"}
 - bot.action.name_to_detail
 - bot.utter.detail