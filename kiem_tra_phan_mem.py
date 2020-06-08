import os
import subprocess
import re


duong_dan_goc = os.getcwd()
danh_sach_phan_mem = os.path.join(duong_dan_goc, r'danhsachphanmem.txt')

def go_cai_dat(ten_phan_mem):
    print(r'Gỡ cài đặt phần mềm %s' % (ten_phan_mem.strip()))
    p = subprocess.call(
            r'wmic product where name="%s" call uninstall' % (
                ten_phan_mem.strip(),
                ))

def kiem_tra_phan_mem(ten_can_kiem_tra):
    #Lấy danh sách phần mềm có trong máy
    print(r'Lấy danh sách các phần mềm có trong máy')
    with open(danh_sach_phan_mem, 'w') as danhsach:
        p = subprocess.call(
            r'wmic product get name',
            stdout=danhsach,
            )

    #Tìm phần mềm Master Test
    print(r'Tìm phần mềm Master Test')
    with open(danh_sach_phan_mem, 'r', encoding='utf16') as danhsach:
        noi_dung = danhsach.read()
    os.remove(danh_sach_phan_mem)
    mautimkiem = re.compile(ten_can_kiem_tra)
    noi_dung_theo_dong = noi_dung.split('\n')
    for noi_dung_dong in noi_dung_theo_dong:
        if mautimkiem.match(noi_dung_dong):
            go_cai_dat(noi_dung_dong)
            return True
    return False

def cai_dat_phan_mem(duong_dan_phan_mem):
    p = subprocess.call(r'%s /passive' % (duong_dan_phan_mem))
    return 0

if __name__ == '__main__':
    if kiem_tra_phan_mem(r'Master Test'):
        print(r'Đã gỡ bản cũ')
    else:
        print(r'Chưa cài đặt Master Test')
        print(r'Tiến hành cài đặt')
        phan_mem = os.path.join(duong_dan_goc, r'MasterTest.exe')
        cai_dat_phan_mem(phan_mem)
        print(r'Đã cài xong phần mềm')
    exit(1)
