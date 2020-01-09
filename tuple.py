# expression tuple as hash

if __name__ == '__main__':
    _ = int(input())
    
    integer_list = map(int, input().split())
    tpl = tuple(integer_list)
    
    print(hash(tpl))