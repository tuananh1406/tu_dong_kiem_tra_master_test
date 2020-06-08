import os
import pyautogui
from time import process_time
from kiem_tra_phan_mem import kiem_tra_phan_mem
from kiem_tra_phan_mem import cai_dat_phan_mem
from lay_thong_tin_ban_quyen import chay_chuong_trinh
from lay_thong_tin_ban_quyen import lay_ten_ban_quyen


pyautogui.PAUSE = 0
duong_dan_goc = os.getcwd()
danh_sach_bo_cai = os.path.join(duong_dan_goc,
                        r'danhsachbocai.txt')
def danh_sach_duong_dan(duong_dan_goc, ten_danh_sach):
    duong_dan_danh_sach = os.path.join(duong_dan_goc,
            ten_danh_sach)
    if os.path.exists(duong_dan_danh_sach):
        with open(duong_dan_danh_sach, 'r', encoding='utf16') as danhsach:
            noi_dung = danhsach.read()
        return noi_dung.split('\n')


if __name__ == '__main__':
    thoigian = process_time()
    danh_sach = danh_sach_duong_dan(duong_dan_goc, danh_sach_bo_cai)
    for i in danh_sach:
        if os.path.exists(i):
            if kiem_tra_phan_mem(r'Master Test'):
                print(r'Cài đặt bộ cài: %s' % (i))
                cai_dat_phan_mem(i)
                chay_chuong_trinh()
                link_tenbanquyen = os.path.join(duong_dan_goc,
                        r'anhbanquyen',
                        r'%s.png' % (
                            i.split('\\')[-2],
                        ))
                lay_ten_ban_quyen(link_tenbanquyen)
    thoigian_xuly = process_time() - thoigian
    print(r'Thời gian xử lý: %s' % (thoigian_xuly))
