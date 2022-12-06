"""تبدیل میلادی به شمسی  فایل پاس داده شده به ویو ها و مدل ها """


"""edit jalali date"""

from . import jalali



ir_month = [
"فروردین",
"اردیبهشت,"
" خرداد",
" تیر",
" امرداد",
" شهریور",
" مهر",
"آبان",
" آذر",
" دی",
"بهمن",
"اسفند ",
]
def jalali_converter(date):
    date_to_str = "{},{},{}".format(date.year,date.month,date.day)
    date_to_tuple = jalali.Gregorian(date_to_str).persian_tuple()
    date_to_list = list(date_to_tuple)

    for index , month in enumerate(ir_month):
        if date_to_list[1] == index+1:
            date_to_list[1]= month
            break

    output = f" ||  {date_to_list[2]} {date_to_list[1]} {date_to_list[0]}"  
    output2 = f"    {date.hour}:{date.minute} "
    retu = [output,output2]


    return retu[1] + retu[0]



# def eng_to_per(str):
#     nums = {
#         "0":"0",
#         "1":"",
#         "2":"",
#         "3":"",
#         "4":"",
#         "5":"",
#         "6":"",
#         "7":"",
#         "8":"",
#         "9":""
#     }