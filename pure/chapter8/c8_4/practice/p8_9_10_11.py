def show_magicians(magicians):
    '''
    打印列表magicians中的全部元素
    '''
    for magician in magicians:
        print(magician)

def make_great(magicians, changed_magicians):
    '''
    将 magicains 中的 magicians前加入 "the Great xxx"
    并将其存放在changed_magicians中
    '''
    for magician in magicians:
        changed_magicians.append('the Great ' + magician)
    magicians = changed_magicians



magicians = ['fzx', 'fsd', 'fde']
changed_magicians = []

make_great(magicians, changed_magicians)
show_magicians(changed_magicians)
show_magicians(magicians)
