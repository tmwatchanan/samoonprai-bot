## Generated Story 7888212846449165396
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9012498096536122969
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1981545419537980195
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4786648730354714990
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5738313586498652858
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3337194167481506532
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5412468112299908209
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4413449590979301039
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5798917063246222278
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -6253097014738709148
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1776550950622508536
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6066139322439809976
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 4753491034792306970
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -460519074573284780
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 4798591973824294057
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8413092992711742846
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1047170611679175405
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -6167045319712995766
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2972602901005215652
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 9165982432664329735
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7934595303862710741
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3786946215394484777
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4763797119234472167
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -1181617559784827815
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -5857588663078662840
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -5371305760912738738
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 8873730275593864463
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -6608856286335428049
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2684358222029153992
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6008572498013737439
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3904191010929262258
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3260527604478904021
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -708615866665845599
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -7998725157490761355
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -895164547775300801
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 8833630985331513536
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8590881164089167326
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4815038043413158402
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 668997533546289913
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3576666824606029052
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -14217656660697144
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8081839853089814949
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1120628159143530559
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2784949621460081002
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6213989565193565105
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3077130496170669720
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8089111848439475955
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 35979262793127267
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3095396676403710439
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7419548886332140688
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1546498625449334765
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1511545637460234295
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1182655453363104317
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2907255927302746749
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3950484350760743935
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3814614931678479418
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6208339188979845024
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9200172418389830525
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6858882122002429718
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2462651427126311905
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2887671133199574240
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5838860283646314380
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2821208134996956213
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2283210063848628633
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3159016361064694395
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6398251152461544574
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8791772793933878416
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8430200124900083846
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 665431063089070716
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6380732359210996995
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4334130337713379998
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8670340749090884278
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5901354123993771461
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 544773322646335012
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6345466794617534652
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 841810900267387871
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -535451629773814123
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4858298533292321415
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1480640441336450406
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4150823859352995206
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1878490949501630063
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8716936927773637366
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3904210785999908254
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4102091208654893704
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7199872346313234720
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8712917499329137619
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7023891507238114878
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -2229209260149410000
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1059102297565192416
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3918731911360670497
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4669798424131299028
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3089083154818821985
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4925938923109340147
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -566163185130312177
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3029594219595806352
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6203219941987209250
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 2930027812508204067
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -5135791728454257789
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 172971586167120375
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 6272532597949624127
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2275921454315680553
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 6770699427152756138
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -5478705960911130502
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 544970546976295542
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -4155973276600786906
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -3667622776596462890
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 2264151238356031233
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5970166561666919261
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 7632308174103241013
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5658552574433412588
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -7296568876629637666
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 2611296152526140860
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 2304549583201985095
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -9215828247362912202
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 7183640152827409561
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 377940031834808558
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -5094834623908693751
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2825578903235169390
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6942240751570579774
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1032688691902152023
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2963522126994994000
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7542573522597745023
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8349527120215254197
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2331045352251558300
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5765398599985396946
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2540935259020545165
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7542016958725679667
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5735890209727668136
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9043626058240815017
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1982478655369485729
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4001536443166300922
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2071526923493009896
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8142603698208962031
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2566990018948286798
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6716293296389661387
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8359827287965671815
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1082694176688236707
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2941150514765231687
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5538699060460274086
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5745239351020860091
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1721306082051043542
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8111122482929925065
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8419538958435224549
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2241525632029898801
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2634470587414836536
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5231835130877467920
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2427304981012106751
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2383670225351434307
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1886801042700627309
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7163046402067672084
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1490066830576182196
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7811494673478112126
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7329663355800625737
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1435061961781172278
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7297156575616737716
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8491554320558715036
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8905969982233502941
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8454399667547353573
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9116265188464751439
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1555359828579207102
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 577757321587776636
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3791293357945334614
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2528122844732938552
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2214423331553760513
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4733176144179568421
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6872008657756063652
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1393102986652863298
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8219259737250272263
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7746844570410814670
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1832274620684699475
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5612741134404638622
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3932492568316194026
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1598096506565074452
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6016202434851538139
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7164864572628645367
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7916079356052645725
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8766726062836864838
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3322692688176352695
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1819894659990920616
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5329506159171763223
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2516432967729893284
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6033427002803364084
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5495175160206608265
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6673468608312171236
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3863513061795940427
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3176214637046217955
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4736861993685604642
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7499281094556676332
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3559936337523459194
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -589041781868994190
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4627935761443527648
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1125683337609211199
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9169602998628709940
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2097357756369685949
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8878006550486919282
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5499271248545638210
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4185487119370683233
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 643474875508549424
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2443830556157392093
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4367472030890898748
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5918523150432156286
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7449132936235874980
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8828548226439713638
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3098339552362799278
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -6090649772376304053
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2933532455795615840
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3297191340453958097
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3915751762167881063
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8024919371710347406
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5755679898506951278
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -26570825204381502
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4736960813066304934
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 6377782921955571337
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4435394634208568428
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3287805380538879905
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3505539730971397353
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3729883385056937219
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4341469750887978001
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -626787437328134437
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3990279292012815810
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -9223231761761979489
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1213868213446796810
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 9085179980759879624
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5628686374216750060
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7455209045265919980
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4313373867727337697
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -5258359730898991658
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4118625978410633300
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 789185346108449309
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8705534742012607695
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 7323517382033633608
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 7878105156163307732
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3466378132938605081
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3154515784420288613
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 7778161581198046741
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5599970058513501284
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3364007960584954624
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -26126036333113666
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8388567991636190262
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5534640020437142980
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4386313859923176210
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5950304471850902412
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -452912401870179032
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6376620824022684526
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6976862957487815847
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5276411511467475523
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8106822797034045073
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 659741762576175078
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4591668777101864684
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 6558282085091258806
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7379300181921039128
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3647473757888121518
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5729975036795530365
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -2885240835547496599
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4425370400586637042
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4880053308341616228
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8179754794219398054
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4367532135470149664
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 7005602027167061477
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 6152420409002479763
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -5608342045841939792
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -6873597336632295194
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 6847120027950792101
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 1547603350622008176
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -4761855141209686618
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -5338911139601380115
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -76223537905912357
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 3303906203233293785
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 7888735114689018572
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -2808102336483183400
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -2196052966559079435
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 8435810155897793375
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 8367519671888915326
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 9168606952677900990
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 6807488960501543812
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -3484067784844974703
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -6767055854884822208
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -231220963085728706
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 979377197285617361
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3826125664485479467
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -7257553840616894316
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -6212785714318624114
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -558779929190265334
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -4577537149920588973
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5683210101666766520
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 5069418801138825278
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -6892063704859751813
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1480198010533139996
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -4984662390696461104
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -6375458311709648778
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -56722089145420123
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -2512899335276846624
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3754477662340919160
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 5019139115094978030
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4357784920711833516
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3090640378530625110
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 5322687855500514731
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -7755658744263478820
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 8644715179917151125
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -5470556608313611087
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 3997204854528887060
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -4522406314681943832
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -8649624146960192820
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 7148814167239969514
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 7872724610187779007
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -1017085698722265975
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -8611235616031509941
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -3375440323710767941
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -894078667387901970
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 7970696811467097959
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 6496158274023737223
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -403800492237190256
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -110482905131507178
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -6887996069610174393
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -3718235955484455851
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 25084238289309716
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 2145597298756419693
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 8703921632523168771
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8715483266913641015
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2108582206989733685
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2580075651624405250
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7122861346774729223
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5259768208918528872
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2456191259450832327
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4388281268738072335
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1927368432879088552
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 659761276531277130
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4921956530967220638
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7544901904649359411
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1236172074897436611
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2879341173922616163
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -778022706910271751
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3464003348625757110
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -726087190358601650
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4400160591802948998
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9087086520756460361
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1872839306360749262
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9178276896906847849
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1351413624156146983
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3918303275438177141
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7239935597697184924
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 9170509747783962880
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 2342218954239240574
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5072889900827901118
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 7699456857733595761
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -709251417573940988
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4691303287302394402
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 9021339562072102022
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 9111767254033019675
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4884155305933983486
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3083082540029642051
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 2928556506510172643
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1359454516800835584
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -6954580215822575154
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -5469357560332668650
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 1263633711787234331
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4849025655309522456
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7092051246922873918
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 8181510406634907650
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 7460307766321938700
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 2703082996205158387
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -6900475502611134632
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -7590151632684088371
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 5575776436818620718
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2016044484558553289
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2736737561236440102
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -6168085197727517282
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -1425515193125117164
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2170723508968546831
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 7931726886060006517
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -788142091321116071
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -6547844236527218274
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 4335408591309792811
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 5677787006233831926
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -7422173261841781339
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -4634604388527151725
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 1501418546753407200
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -3278883871633831517
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2685864019562581286
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1357330183465000857
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2154480027392859364
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7797480947255606547
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9090010115950010161
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3238559417726235814
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 236891672430635421
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6624618430067258925
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4791214308129093020
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3474402327573643037
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6077445256660787959
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3531322012859874826
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5351101310203197834
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7419456004319182769
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6099226979616141877
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7426139879295550377
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7737919366093534712
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8788696714166604491
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4087674673651058305
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9111705687113784364
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 2084649045266153540
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5388286911481943309
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 7598647461075837302
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2525913370783617762
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -5964142042510656415
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 1430961914265111073
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -614124501973873143
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 555212130936387690
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2311657804910036916
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -9153391910518476374
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2199989309822379740
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -1118919016128080531
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 2903638003684514618
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -9177938209582013311
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -5757241014001363794
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -1507655484042513462
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 2184540220367521966
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 3995173329298425709
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 2060722895122173344
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -5049156255181001211
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8727067551669232264
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6908804231559124043
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1834518981247433352
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7718823867142959679
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 1766417829679513308
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6940762097132650513
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3092188956742737629
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 2658552635855991410
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1867924188439408444
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8748116637977732595
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1272547611719725918
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 2498700401516953105
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5948651591693480376
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6705990211282549721
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3785970061282563847
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -991612109193741588
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -674056107969204388
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4247070402152549398
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6960115531868079783
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1202234242624702469
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5361224899251757333
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -6800624703635923336
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 6155740438620400308
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -992795222724089120
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -6279825431768208380
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -154379220360851414
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3333665723710946185
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 2095028567722150895
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1775835042275410039
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8241652566602630579
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 1602855355019001950
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4761415044200604138
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8178696104420046059
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3095692328964728537
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3103350832616519144
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2532366751566547761
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -574279843225600360
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 7154464474803785255
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -5792652296548330525
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8548073519660939463
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8216115335085195635
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8566076928493358385
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 4071813716540897004
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5439480447195706556
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3025346321641574636
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3479745313740863438
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8954071545389154241
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7745970199100537981
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 414056813432705915
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3551991193751410005
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 1109925999275052293
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -236105835452157850
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1753584490132337974
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5594752992915721695
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7872206831395676600
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6677216569130584828
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8334959720061828299
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6819942996841172597
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8085154109033926099
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7634244216628890235
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7592052208396446725
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7631586765809116983
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 5323209947004059713
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -8034319269474207802
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 6913601706807994618
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 304563213695013092
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 1465827986143516707
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 8324759606736697090
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -6940140912037479465
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -828176573883417932
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -5349822828847538021
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -4287375427928527090
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7489852398830233602
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 5546606503373298911
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -7093590153073421168
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 6275124092780491706
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -2930846959181546107
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -7143404461883445744
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -5150169870619445014
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -2042149593580867794
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 118476043403210528
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -1272222636664708535
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 5288649490821847611
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -5375191582993632314
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7304607712666303609
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 1557935321349926031
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -3652825099107504571
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -5208334435372639249
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -6959534016210937272
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 3193126854692001455
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -2374926875060284410
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 3581925114045968896
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -3614477585633561464
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 912862150357482065
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -6114924229542124899
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -3600126889726275263
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -3344421083996250653
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -8633837500738774172
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -59225665265543811
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 5377963459208735273
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -2167432850590751214
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3802862137954845842
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7445618617818312210
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5540368250651305134
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3680112936678017779
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7337934780444161284
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 141701283722765390
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 4475109504335782872
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8226078458568512008
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8187207588588392178
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8177474682387363780
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8815631225167061398
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3307278818916069019
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8350886898315064420
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -492841215456808602
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7205165167581066804
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 4422332254752324865
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4166192273428811175
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8687679817447159669
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6792787227929729179
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1807659416103033869
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5376777033999500219
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 6558859563939765618
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4837285966347423213
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -8129147070282354664
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -7055459063670468514
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -882619561834692125
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5099018178976394540
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 9080766764168190951
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4908911867000572343
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -2777803641139605266
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1760068542929123689
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -7100921893006362984
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -3695643206780951926
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1473303514689237248
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -2989136495267438512
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 5828671677298883779
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3377548889727944584
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5740369337372214981
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5802446367454896644
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -3940889879074875238
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 6088796355746984742
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -4144471918912225440
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5212414629888261325
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4420941992253489235
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1193792373677146319
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -8827527100537507222
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5423243692161083826
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -526937834629658007
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -3227531855376553165
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -7880026923611447909
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 1872910016121000852
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -4406809331669766669
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 8863101962639025919
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -6986880615559177151
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 570100165232988116
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 7799916104823067064
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 7594328179507746301
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 8817865136850910655
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 8653753310405132164
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3989836904892112006
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3161774560336407665
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3231171555851340904
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8076254001343552900
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2572629543509529454
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5943971745456657787
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4698894253841550908
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 916034417536692437
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3473122382638497462
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7540106069712467892
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8070312354748185762
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4352286099266401000
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6354537323474000290
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5776025275090583249
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1343706746929834161
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6998100419118081559
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2314342058232470355
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -97332859559302865
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4211176827412842078
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2628733950560634202
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 2035659862978120881
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1906378372253123652
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 67718056460106609
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4117494367918686158
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1127688055974849659
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5018061900346185001
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -96654987522808123
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7345774897280436372
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4580856161468598968
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 1030471674018452522
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5255845179450591315
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8485713929613804719
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 4262622472298857731
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6386365243386742027
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 4470777288375803155
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3567918066419038404
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5221966991977755437
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8085312980410587077
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8609977657345895008
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3255645645584956844
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 7859981468746698103
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 6477542169134726623
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6608663232334409594
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3209620935965848601
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 362378541096574573
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3761185498770714264
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4600869404084315143
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1873600256812235638
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4561727221287360291
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8262643892419396872
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8686358090552935845
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1071230809895222688
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 367426908580904180
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -33269034122906681
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6867888631116809405
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3440832990627237992
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3789675007628694265
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 6209384872244976065
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3984503492055588394
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5503082082113655412
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1245074444238540577
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 534625725310640137
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 9189979310125975386
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2808637318751557997
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7023957781005846714
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 2396675180169879881
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8499285062961646963
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4770919557434969177
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 7535553068150531349
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 6710372494144402085
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2989819751415210614
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2986382436211870410
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4884310687762013285
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -5582495923238049546
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1708932174428257214
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4015106784810689526
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8267213277153716061
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 6130602864619316387
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 2345937129595398019
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -579055301750188063
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 6877503603733716316
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 1257952358837765381
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 1223443358247165100
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -1203346991007013891
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8176788754317720348
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 1376999507631071964
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 7833767896961361193
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 502043901961315857
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -1077940681689537024
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4826653445587442875
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -3711904761729555767
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 3005738417053437123
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 4034405593690592367
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4041475453574442611
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4722410505335303675
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 65079155145551748
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 1213741480725210086
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -9038966588575293849
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -3397180530129566016
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4808739039405834469
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 4039968935988062180
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 3227548343919067094
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 4396181648356775080
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2272940670541374651
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 3074675874832358076
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -5182076186706474306
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -5489117786405202047
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 2686238277692321652
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -8596090284362383561
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -1543524460371557987
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 7115181239448906100
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 4221170047316815843
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 3813329484400736713
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -3741234352903151937
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -8192558261656725629
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -5701462465215056996
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 6546743503841559508
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 4050912798252103146
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 5420598950340244463
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -539206050340980531
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8805789145971939050
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5003859578248265081
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7526481912398036470
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -74960445846143772
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4324626641570361444
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5111191656385935833
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7227407163841469964
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5857565646003752808
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5759295843768555042
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 58125650450531470
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1329756745297064435
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1915930241116791842
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6015245970508838511
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5111665879979120931
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5555974643837225185
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5512042714742099935
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3832098053634071174
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5977413230629532040
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -817842858961437334
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7816938586053333136
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 8125953393733436762
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -2676617553644665560
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7077132932078787438
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 3181888658942718594
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -2550960696981730324
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 841517131638230226
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 6868783002995571735
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -6380590402711859844
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7154305549703686017
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 8918526137058851842
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -2991681662304990416
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -3346318477381924104
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 2360437796905457917
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -2856356931802502468
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -8048273403960247518
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -8964957977810695538
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 3648839544739641873
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 5351382637367746096
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -1171218794135673734
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 3566966122643931555
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3200860904966589511
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1436818368949453044
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8761199531037910642
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5366513933168271223
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8691244916050183788
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 302481218440896815
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5996451713917464390
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1123099626753222628
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5479569602745589828
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5151168990624763754
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5580674883129184421
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -864705147879827360
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 832491521786492384
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8816288254056305187
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2674267545825791773
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7706210624062003312
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2991351480096250958
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 467203690769470004
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1914340979359346281
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 340081274567076425
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 1014762918481256849
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -6068178894506501357
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 6551789537893434972
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 6025261339558991969
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 7009036472197077882
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -139988066811146416
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 179092105743153593
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 5220798062109539510
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -731139622570880769
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -925732031672474215
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 2983013099043299562
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 7599726153651878905
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -2011290002150984994
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -5354284428936366168
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 2360407565606172569
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 5716948946206702162
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8526729230936721365
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 6604339524935441253
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8742014827183274212
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 2220211729470235053
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5310314083963255755
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3515579421902923527
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6927134554020138136
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3901020037117116530
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3761515332617421336
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8184032881426150701
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8324142625471329152
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3926614822745886562
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9079454349338865352
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6467839031943417800
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -551050867181605151
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5138759417502611550
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5222805492057094189
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4414895110957272278
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 639699782727465967
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3034955987625714167
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2665062762711856051
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -948002767188161715
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2379238652280042146
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ขอบคุณ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1424525162925756860
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1070321076669898957
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9181546458382873874
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 669087725922512937
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5722960129378197240
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -908109492368660611
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2637458431341322682
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -539211222019674747
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4143283702836495090
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7314510755154107510
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7060224742720924912
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2573122658772769768
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8571366054558541999
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3851561262687357728
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9167795394395164444
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6785747205894051221
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 639329416452099716
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5865480641220604254
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9221468370565885912
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1456826867510313815
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 578904041062055887
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -960734813714121126
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -285393125813129137
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5103450499853284074
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4238373410007361498
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1078486731133517616
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5437233452348209675
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6662139678343570417
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 30880673817806208
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1677956125725043253
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4108312290284023066
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1865636879427020755
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4338710055217198849
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8932707823616263010
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -5944161269308635402
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8070763691752273373
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4455539069800341742
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8249245967898489267
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4572564210336191239
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8140976456460435131
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3312211666604832358
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 6587358894152500363
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -8462897448094275238
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 6003297147158811991
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5120664267404292098
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 6679777069803053977
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -1016693129361306847
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 8095859186401369767
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -4192466591706584627
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -1035031512372194978
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 3368985544568306642
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 8885853158103125473
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 1479720554827783843
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5464874007493470540
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 8152697616829336716
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 3788753102975983515
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 388115262942946964
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 3780903021251476531
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 234595771189890105
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -8052574970628446194
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 6307572387495059578
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4846712744501474026
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8133192062853920106
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1112047865306336922
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3338824889445586108
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6257921252426942665
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -492844996921529681
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1037419878469605482
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 387324120589909868
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6136199778313476075
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1849679873189037294
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4432518047056409389
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1792072551321125571
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6896101201058733915
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4360385426168669055
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2033102987558801147
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7606230459312523680
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5101753387898311908
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7460865803035518222
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 944624395004237483
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3022378234335655630
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8827714733589879041
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6827597042909012748
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9050690169646042722
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7847088311048613892
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1680187774365894778
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5005949538376621551
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1375127209242980317
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5079059660971483691
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8405990268483889456
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1897905573129121578
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6250961563853468021
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8975482348701748708
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1643074837289822278
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9178243414354161606
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8635835175821841558
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 971198829103380926
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7603003802708714466
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -846546799625365573
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4932124872034472592
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6014709823737002264
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4669099385417265947
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5073331873844057233
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9150365026129667462
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2827676706273642253
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8036663649932658921
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2920227317917855906
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5776626905451074858
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -9182762754977815651
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5195994295638262194
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6979160753694047179
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4805699055839246369
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 584231214510943900
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5341811344477328225
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2595030722488128806
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1986580092932893202
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -616202891872955808
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1082082630127816983
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9177518518949673267
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5121431731733207529
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2176622383238021357
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6638788655635195467
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7521257308950405825
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5472550033172446635
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2001585896797206207
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8738362499225312718
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7304967863104918583
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5503130673147682960
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7602797281995850621
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 565904028011366382
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2204872335036705542
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2786807421768386958
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6229592857146074441
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -445934663034261747
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2683025055243912989
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5472948910500970452
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4872113934344831234
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -978666474563975422
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5519729233994593700
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6111475422825292303
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6046091085452140104
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -6744823393051709289
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7732395457783703587
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1210712387471070134
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2825196619535975237
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3249094329499758817
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 6513980881136543638
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 9200295699402282734
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 213523076944121748
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -170027139647605776
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2842982508441774979
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 1521368355868920345
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 940309244955861226
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3929575149163812116
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4063653135617625570
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -595121814900791241
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8560305121350895991
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4808987686936724761
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8395185072609393482
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4632688151091105792
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1411792972238514582
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3086198734793502706
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8884123990324044371
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6412881845116896605
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -5568545493367186884
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7949206601433690036
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8738937396391192361
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7145570303812863705
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -2698305722524796839
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -5703993356196855874
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4613347966262378878
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6758260027686349730
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -5551873680560179113
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4226779475932806765
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4697094934500805151
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 450717403803337283
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5959247787415289589
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7785088578916787041
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3069182336343871250
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1491013329583984628
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3041941315009013786
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 2200847107443566789
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1394300689758450595
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -7475470054047825602
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3113584475220559602
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1972866032606398445
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8444832463982120214
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 8410820549774319820
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 2494115621886347411
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 7723331288684932185
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4972161992569162281
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4191218070914755877
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -8869830321828059913
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 6235279775122794260
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1614692034322404310
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -622175449452776362
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 4899359882687900893
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 6807337697692740203
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1418366232506044644
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -2667506859083220142
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -5235544301771956078
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 7141347812606674059
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -8163364749460078935
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 2019514683049915729
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -7205301957027028719
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -341305582188951376
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 3557171929864817648
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -3588215068029319668
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -6711209800793666054
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 8541930671749703566
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 5703108373822621344
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -7081547298898223119
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 6593822135363921500
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -2571879714991051838
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 8351957251682585645
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 4644253765889951071
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -8977544172068968926
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 4729885716730587886
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -5865490946228539256
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story 2285747887178772581
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset

## Generated Story -2251946474308974306
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3989471381991907478
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -6795576246354667017
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1011665867416684117
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -581188251203556374
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -3100711816353519163
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3306237668377157430
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -8264694195671335694
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3857444624902195129
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4682854818247561042
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3153677979042896199
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 2123234126093719835
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -8422404824183504209
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5757211898151468003
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5823608570551646266
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4179375783716555572
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 8904179714110964936
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 826706326112750833
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 7598642497481944488
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3708472434511919187
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 5932109237156854670
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -4306610609229838321
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7532492332114293714
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -5498080975880033847
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 6192567620241327727
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7139361397610993044
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 4878451182521929962
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 3922225891915224027
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -6071788228812310535
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -444392102591292439
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 5775676728689276472
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7985738721594410635
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -5818101234805136637
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -5168977688580584040
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7218175897062430845
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -473013809169103757
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -1208902961035140790
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -4215848890014656840
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 1649491891786387425
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 3144513022977631688
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -4164554854362716946
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7373461889200246673
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3762834786398569065
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4523408304107778800
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2246007921942875746
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2087836328927689023
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8101210348578734408
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2509935933521437138
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8690334584823212138
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5925240943618192053
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -632285383935848041
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7236615856365616474
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8425944022154980700
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5058151056071035922
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1526619996459732485
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5429204545223225655
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -255976768088827209
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8281356534362492877
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 759090600718408435
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -276097486158904542
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3081349363099600463
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7281822686376937015
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8878147203325197172
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7777423464072133267
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 2919793791133956897
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8568649320324770392
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 632056696735294156
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 843635923161376727
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1957153406361632279
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2886747627777120475
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 7435523824044840956
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3117898770922019840
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 1622251612581072028
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 572972056611201680
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -5518091032926857483
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 2260904644011790394
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8492136007260598164
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5327153237217353309
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3598952089458860753
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2515269181886724373
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
    - bot.utter.herb_feature.not_found
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 4377361318209043463
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -8753707317452170491
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -436975820244383921
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -8877744293308800190
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -5729950832679936845
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 8247753650667713870
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -5086995430406644129
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 5641250357049684760
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -3288184345491895258
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2634281366535069203
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2917908022055221225
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 2871520965993192337
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -8257395070480433875
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 113414843344211367
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 274415786943907608
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -9210856901445440633
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 9083303007808767827
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 5374647053696344158
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2944088566373822599
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 3614309907762185789
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -5345502413731043027
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8163267365093555387
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8067076638489680629
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6853434967155736010
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4684323919934130270
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8446100464923833755
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5243761111558593136
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3861823897712684622
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7664692979055127396
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1088933288694526001
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -812087729137848649
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7394638358183568908
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1921827355163432194
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1846844600965213641
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7418037584816169024
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 9188490434396795017
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2482126249169907252
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6433066440748569958
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4516458847828726619
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3247053031392025619
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7409240964828114944
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5941447841938732931
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -8861492998156847598
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 748198592102795111
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -7386781233944495052
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -3863751085183962288
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -4431863650225972696
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -8294585491320471573
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 3991595830266895318
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -4984521315201050193
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -5781834832674032851
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2002748358742322712
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 9191971040126181952
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 8210276623280040800
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -7031645548940659585
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5245184113375979038
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2929924362095324723
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -1042952902814856091
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 5032448783637067470
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story -2396593796530822957
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset

## Generated Story 3624134964408625899
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6165302602997913777
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -5018267320221297142
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 2548483175585723202
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6654356994134184739
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 9145479750310428149
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -2551708464793424430
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3646035655272039255
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -9135897988856780820
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6432671338548118041
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -439365892209522126
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4048280731700077748
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8567787681807604749
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6915631380005506191
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4249286253440988127
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 9114796527354815700
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7188811245731249565
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6148717586157475579
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7460002932626583299
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3563630624879232890
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 2219178373570744633
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1584491425461193663
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8267486925390247940
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 7163186327064684172
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7912058403967610037
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1893536315128830663
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4912624915026995417
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -5870192014942362157
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 1344860967963034414
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 1419373200902997050
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4499462338099700704
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -5763310662266589402
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3056579630886882839
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4438640167060158330
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5100617123754693108
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 764715800823224097
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -3081409696158807877
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -6523137310471482355
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8419429025127873414
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5490222220518611367
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - slot{"feature": "\u0e1c\u0e34\u0e27\u0e41\u0e2b\u0e49\u0e07"}
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -457377463986249193
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6782188394669289842
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5227092087848747124
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7292544865740763520
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 1153237769858653439
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3902551856383997563
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7438817627307243599
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7227981999290447634
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6361151525507445568
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3796573924894270349
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4135311135578259963
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -9022618606666978514
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6377324729537680208
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5423783455234131715
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7204485582630638728
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6662003110309687214
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8416018724264858673
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -344162548260192840
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4905914936184961007
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -5462125404444788886
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -167501833763293669
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 6916804085338270449
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -4413019496623710141
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -453843362285067901
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 843432266341837635
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -914490567450039710
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 4511234965784915283
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -1117289607346282805
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 6926874352569170587
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -1563733341177813934
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 4567390800957727528
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 1172811463389650060
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 8872462023779938364
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7779385672220196632
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -6798334055525707994
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -1892044149912800508
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -1285947333221045355
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 5014591108402958334
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 6591844628240231363
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 226893647387858381
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -3368445371290924321
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -7920310071244050409
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 874018853243366169
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -3490048720671906850
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7129278151575251074
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -5239645983270472115
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7224035963983351016
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -259790747653817356
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -1833173618583966052
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -7528742037503369869
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -9017767676226620588
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -2607401396690678926
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 225383318649378564
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7591004541124290442
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -7691174001284364772
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -5451292968462593009
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 7072138122853546537
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -7425427328774694000
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story 4598949171314419511
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -398490150205622905
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset

## Generated Story -4682515366051819519
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7862921593273982575
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6212425976676990833
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 4494940960725202697
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -7389068621901012433
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -2077317953736526828
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -5973460098235737331
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3681087108948520123
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8543301424524814902
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 4232850577432098717
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3681411419841327663
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3314572923256429356
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4308302759995281023
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8855489209699149054
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6677147457064891423
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 7428180421852029417
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3182328897500912444
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 425920522796822045
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 8173381397532210661
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3652659368201583038
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 857475647559704742
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 2900013006617142067
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 5152506310203539309
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 7602098777887555015
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 7672957902065834345
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 485079522221924777
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -2424044789171709318
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 981302840462958291
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 6142216763467912095
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -6909917437272135715
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -3642398663286633410
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1547300395068930890
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 8765446608953985399
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 71096179450677703
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 1590133438250504296
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4484081068343201296
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5973726380036310951
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -7267532245371070146
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -8270477809340040658
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -4754999129230076442
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -3459831272843140982
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5449744411420608662
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -5143355740055979100
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -8765112769276735589
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -2654895403854316706
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -727530634928173866
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -2971153671462795058
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 2559463292285771283
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 4154787524189979392
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 3608538536756112887
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -276793507932595625
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -142603204017852189
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -1183988870554166602
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 7108204063857845002
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -2886218058763022816
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 6222234549395843977
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 8408473388663870504
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story -8174983221420344005
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 2528603064435239308
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 5329496216837811029
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset

## Generated Story 6471245688546417322
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8215947215113746372
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2899696174449936467
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 473625173458605805
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -2536704101865957129
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2476207528011562302
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5004615183031459008
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3588985630549863250
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5957019506853569072
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3234415165231266517
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -773465310082616495
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 239048846607349775
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1982838480825265635
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -502397151900890818
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5502547538848890976
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5920581959244727999
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5843458025586741556
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5161580669718879283
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6136333842775164357
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5014224946573281876
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2311900226868702978
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3617271015415070767
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 3365528614915864131
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6999465188666403035
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -5053434999577567112
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -4228358746691908863
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 1040517129179764638
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8285451220188953696
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3088584911506011338
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6201634850968659033
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -1418222664358369172
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 1740376347085065755
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -5459753716642525258
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -8721294040136584860
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3715896898390623752
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -2830236760568363223
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 5878649135436059339
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -2222999196094112436
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -3187441609555358711
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story -6659451609244832151
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset

## Generated Story 6524703105974562647
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -1226823909885881259
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1114600776303998250
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3350863910790602015
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3061225086363700523
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -2027645873513268885
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -3857551865329975780
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6053438730611694980
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4151606650726065466
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 3574343497398517320
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4905624134296004433
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -827072867281323846
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 1278839843628284119
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 874932228484811881
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6831651580834906126
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6266891228485943666
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -4820932717354215606
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 369378332773035190
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -2388667105119191826
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story -6324632241241370545
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset

## Generated Story 5984323090395000123
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -7175422601518890294
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -1660647701870945622
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 1685996654619838045
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5926598945337852427
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8732465048228140409
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3424814220789675328
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 3208617346116667860
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 6329109868140744134
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 7574829070278820900
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -93174811478404061
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -729737667021049995
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4099490388392416297
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -8825704401446643453
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 8497884087020977896
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5107502418134733871
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -4953778584766809636
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2919302060054053015
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -565250923801128313
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story -2893687908393678522
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.หาสมุนไพรจากสรรพคุณ{"feature": null}
    - slot{"feature": null}
    - bot.ask.feature_to_herb.feature
* None
    - bot.action.feature_to_herb
* user.พบสมุนไพร
    - bot.utter.herb_feature
    - bot.default.ask_more
    - action_slot_reset

## Generated Story 5806525888774301186
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 3883536346763854936
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4776892035608406729
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8977194362051574690
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4774499465795972227
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 793705094594455549
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8804263663187887410
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 7027802893891174815
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -6475526165547692016
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 6740934147421078955
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 7931507277609210402
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 8088687955198555652
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -2373111956399181843
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4852023539293007464
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4834404250277358250
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8887535648323023962
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 4559090116767936064
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 8197841953332690870
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -5400561970982672764
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -6335335903780723974
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -6289913322243511477
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 2824769942338764786
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -660864551314012886
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -2384397308041966884
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 1754511155762232593
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -6955678051012192343
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -4485439332121498856
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 5292305278641761106
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -4599786305438322172
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -3439228230934183439
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -8943054985542177395
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 3646379480267320016
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 5539722011178162783
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -4117912882049551071
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 589295181071117619
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 6141576486499331735
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 3017851064305070958
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 4007311034910768483
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story 1994544657174954918
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -1333803809115065623
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset

## Generated Story -7405176775466359481
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6299376871049138319
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5665624069221598571
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4533212969465521116
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -7162798145649380965
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8860963984576047681
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5278630152090822718
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 391076326695756658
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7439057506178685112
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3194303856554536568
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 5024858890850027633
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8676962286369045237
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5830386149614913924
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -5100075082381124553
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3372780975230683939
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 3959350420185769612
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -1410787682892635788
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4076713117506228610
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1613744316036236084
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8532911557208515721
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -246435307781911562
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 8371545508346098702
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -2479026886469868915
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 9021770593498689003
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 7934421860526245154
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 2055014487230192769
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 2029972382227477554
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -8889217033758131945
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -3897655946507877919
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 2172449678715958556
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -6722236730706690760
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7369131841706682719
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -8409499793740883250
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 7568988866254779606
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 5572576884335158656
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 353397401138422532
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 4961256303724546873
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 1284549659679688033
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -7518121176965663783
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story 3815863784792790593
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset

## Generated Story -5157380385726546689
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8157215244301049330
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3712928482643516352
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -4224409923547720963
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6294492050300648692
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 7114439839203160534
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 6649494849803006752
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4506923190712220752
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6696407267203245836
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 647791087927822496
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -8637062926727909116
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -478944932790608030
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -6924019833448647652
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 2529354139748924421
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 319482418836520413
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 1271073054557328628
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8933397271376144103
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 4129947358276901305
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story -3125849826289331867
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8490845783060415010
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่ใช่
    - bot.utter.thankyou
    - action_slot_reset

## Generated Story 8179187469497890870
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8596438681407474243
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -916792252985661639
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
    - bot.action.name_to_detail
* user.พบสมุนไพร
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 8296521251977531419
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8734779815304843963
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -5526685467953591940
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 790485399327457195
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.พบสมุนไพร
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 2858677021261766275
* user.ทักทาย
    - bot.utter.greeting
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -207834208903282030
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 8878897277108646853
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 8675293134847867588
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -2172399628428208730
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 6306047774642161414
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 5594684370566985750
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.detail
    - action_slot_reset
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_detail.herb_name
* None
* user.ดูข้อมูลทั่วไปของสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.detail.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 4783099217534485656
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
    - bot.utter.herb_photo.not_found
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -8775107470662471927
* user.สรรพคุณสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_benefit.herb_name
* None
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ไม่
    - bot.utter.benefit.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story 7545971905824418650
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
    - bot.utter.herb_name.not_found
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -5864026121804515776
* user.สรรพคุณสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
    - bot.ask.validate.herb
* user.ใช่
    - bot.utter.benefit
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่แน่ใจ
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4601347270438507230
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_name
    - action_slot_reset
* user.ค้นหาสมุนไพรจากรูป
    - bot.ask.photo
* user.ส่งรูปภาพ
    - bot.action.photo_to_name
* user.พบสมุนไพร
    - bot.utter.herb_name
    - bot.validation.herb_name
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

## Generated Story -4166722018470253088
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ใช่
    - bot.utter.thankyou
    - action_slot_reset
* user.ดูรูปสมุนไพร{"herb": null}
    - slot{"herb": null}
    - bot.ask.name_to_photo.herb_name
* None
    - bot.action.validate.herb
* user.พบสมุนไพร
    - bot.action.name_to_photo
* user.พบสมุนไพร
    - bot.utter.herb_photo
    - bot.validation.herb_photo
* user.ไม่
    - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร{"herb": " "}
    - slot{"herb": " "}
    - bot.validation.get_data.herb_photo
    - action_slot_reset

