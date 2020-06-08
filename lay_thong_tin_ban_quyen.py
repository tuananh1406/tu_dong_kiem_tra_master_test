import pyautogui
import os
from time import process_time

pyautogui.PAUSE = 0
link_anh = os.getcwd()

def dang_nhap(link_icon, noi_dung):
    hop_thong_tin = pyautogui.locateOnScreen(link_icon)
    while hop_thong_tin is None:
        hop_thong_tin = pyautogui.locateOnScreen(link_icon)
    pyautogui.doubleClick(x=hop_thong_tin.left+hop_thong_tin.width+10,
                            y=(hop_thong_tin.top
                            +hop_thong_tin.height
                            +(hop_thong_tin.height/2)))
    pyautogui.typewrite([r'delete',])
    pyautogui.typewrite(noi_dung)

def click_nut(link_anh):
    nut_can_click = pyautogui.locateOnScreen(link_anh)
    while nut_can_click is None:
        nut_can_click = pyautogui.locateOnScreen(link_anh)
    pyautogui.click(pyautogui.center(nut_can_click))

def chay_chuong_trinh():
    #Chay phan mem, nhap thong tin dang nhap
    print(r'Ấn icon phần mềm')
    link_icon_test = os.path.join(link_anh, r'icon_mastertest.png')
    icon_test = pyautogui.locateOnScreen(link_icon_test)
    while icon_test is None:
        icon_test = pyautogui.locateOnScreen(link_icon_test)
    icon_test_trung_tam = pyautogui.center(icon_test)
    while icon_test_trung_tam is None:
        icon_test_trung_tam = pyautogui.center(icon_test)
    pyautogui.doubleClick(icon_test_trung_tam)

    #Nhap thong tin dang nhap he thong
    print(r'Nhập tên đăng nhập')
    icon_tendangnhap = os.path.join(link_anh, r'tendangnhap.png')
    link_tendangnhapnull = os.path.join(link_anh, r'tendangnhap_null.png')
    tendangnhap_noidung = r'admin'
    dang_nhap(icon_tendangnhap,
                       tendangnhap_noidung)
    print(r'Nhập mật khẩu')
    icon_matkhau = os.path.join(link_anh, r'nhapmatkhau.png')
    link_matkhaunull = os.path.join(link_anh, r'matkhau_null1.png')
    matkhau_noidung = r'admin'
    dang_nhap(icon_matkhau,
                       matkhau_noidung)

    #Dang nhap he thong
    print(r'Ấn nút đồng ý')
    link_dong_y = os.path.join(link_anh, r'dongy.png')
    click_nut(link_dong_y)

def lay_ten_ban_quyen(duong_dan_luu_anh):
    print(r'Lấy vị trí bản quyền')
    link_anh_banquyen = os.path.join(link_anh, r'banquyen.png')
    link_banquyen = pyautogui.locateOnScreen(link_anh_banquyen)
    while link_banquyen is None:
        link_banquyen = pyautogui.locateOnScreen(link_anh_banquyen)
    print(r'Vị trí bản quyền')
    banquyen_left = link_banquyen.left + link_banquyen.width
    banquyen_top = link_banquyen.top
    banquyen_width = 300
    banquyen_height = link_banquyen.height
    banquyen = pyautogui.screenshot(duong_dan_luu_anh,
                                    region = (
                                        banquyen_left,
                                        banquyen_top,
                                        banquyen_width,
                                        banquyen_height,
                                        ))
    print(r'Thoát chương trình')
    link_nut_thoat = os.path.join(link_anh, r'nutthoat.png')
    click_nut(link_nut_thoat)


if __name__ == '__main__':
    thoi_gian = process_time()
    chay_chuong_trinh()
    link_tenbanquyen = os.path.join(link_anh,
                                    r'anhbanquyen',
                                    r'tenbanquyen.png')
    lay_ten_ban_quyen(link_tenbanquyen)
    #Tổng thời gian chạy chương trình
    thoi_gian_xu_ly = process_time() - thoi_gian
    print(r'Tổng thời gian xử lý: %s' % (thoi_gian_xu_ly))
    exit(1)
