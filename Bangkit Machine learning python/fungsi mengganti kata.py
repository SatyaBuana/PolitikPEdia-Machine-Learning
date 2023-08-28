def Replace_age(Detail, Old_age ,  New_age):

    if Old_age in Detail:
        New_detail = Detail.replace(Old_age, New_age)
        return New_detail
    return Detail

print(Replace_age("Satya Was 19 years old", "19", "20"))
print(Replace_age("I do remember that alfan was 20 years old", "20", "22"))
print(Replace_age("In july sultan was 17", "17", "18"))