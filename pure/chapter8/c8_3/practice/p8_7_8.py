def make_album(album, singer="fang zixuan", num=''):
    oops = {'album': album, 'singer': singer}
    if num:
        oops['num'] = str(num)
    return(oops)



while True:
    print("\nPlease input your favorite album: ")
    print("(Type 'q' at any time to quit)")
    i_album = input("album: ")
    if i_album == 'q':
        break
    i_singer = input("singer: ")
    if i_singer == 'q':
        break

    user_favorite_album = make_album(i_album, i_singer, num='')
    print(user_favorite_album)
