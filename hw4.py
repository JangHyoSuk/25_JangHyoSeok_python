def rep_char(b, n) :
    print(b * n)
def draw_line_string(text) :
    a = input(text)
    msg1 = 'Hello ' + a + ', '
    msg2 = 'Welcome to Seoul. '
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr)
    print(f' {msg1} ' + '\n' + f' {msg2} ')
    rep_char('-', nstr)
    return msg1, msg2
draw_line_string('input his/her name: ')
