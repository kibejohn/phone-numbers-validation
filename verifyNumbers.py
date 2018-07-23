import phonenumbers
import re
def converter(number):
    print(number)
    raw_phone = number
    raw_phone = re.sub(r'[^\w]', '',raw_phone)
    raw_phone.strip()
    if not raw_phone:
        phn = raw_phone
    if raw_phone[0] == '+':
        parse_type = None
    else:
        parse_type = "KE"
    phone_representation = phonenumbers.parse(raw_phone, parse_type)
    phn = phonenumbers.format_number(phone_representation,
        phonenumbers.PhoneNumberFormat.E164)
    print(phn)
    return phn
def checkphn(num):
	global sa1
	if num !=None:
		sa1 = num
		sa1.strip()
		if not (sa1.isnumeric()) and not ((sa1[1:].isnumeric())):
			print("bad num",sa1)
		elif (len(sa1) < 10) or \
			(not ((sa1.startswith("07")) or (sa1.startswith("+254"))) ):
		else:
			converter(sa1)
checkphn('')
