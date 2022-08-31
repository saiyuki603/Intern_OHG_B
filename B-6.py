import re
import mojimoji

def yure(address):
    address_han = mojimoji.zen_to_han(address)

    re_kenshi = r'.*?市'
    re_ku = r'市.*?区'
    re_machi = r'区.*?\d'
    re_numbers = r'\D\d+'

    ken = re.search(re_kenshi, address).group()
    ku = re.search(re_ku, address).group()
    ku = ku[1:]
    machi = re.search(re_machi, address).group()
    machi = machi[1:-1]
    numbers = re.findall(re_numbers, address)

    address_list = []

    address_list.append(ken)
    address_list.append(ku)
    address_list.append(machi)

    for i in numbers:
        address_list.append(mojimoji.han_to_zen(i[1:]))

    return(address_list)

list = yure('千葉県千葉市中央区千葉港20-13')

print(list)