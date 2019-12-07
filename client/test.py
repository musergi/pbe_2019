import coms

if __name__ == '__main__':
    url = coms.parse.parse_url()
    print(url)
    coms.core.login(url, {'uid': '5D7D9529'}, print)
    while True:
        pass