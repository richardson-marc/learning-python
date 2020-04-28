def up_low(s):
    upper_count = 0
    lower_count = 0
    for i in s:
#        print(i)
        if i.isupper():
            upper_count = upper_count + 1
        if i.islower():
            lower_count = lower_count +1
    lower_output = 'lower count is {}'.format(lower_count)
    output = 'upper count is {}'.format(upper_count)
    print(output)
    print(lower_output)
