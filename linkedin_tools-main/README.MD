# Tool linkedin
Download project về máy

# Chạy tools:
``````
Mở file LinkedinTools.exe
``````

# Chức năng auto login:
B1: Thay đổi thông tin trong file Account.cfg
```python
[API_KEYS]
hunter = API KEYS hunter

[CREDS]
linkedin_username = ( Điền tên đăng nhập vào ) 
linkedin_password =  ( Điền password vào ) 
```

B2: Nhấn vào nút "Login LinkedIn"
(Note: Nếu xuất hiện trang check bot của LinkedIn, người dùng cần giải puzzle trong vòng 60s)

# Chức năng auto connect
```
B1: Nhập linkedin các user khác mà người dùng muốn connect vào file 'input/url_linkedin.csv'
B2: Nhấn vào nút "Auto connect LinkedIn"
```

# Chức năng auto get groups
```
B1: Nhập keywords để tìm các group cần join vào file 'input/keywords.csv'
B2: Nhấn vào nút "Auto get groups LinkedIn"
```

# Chức năng auto join groups
```
B1: Nhập keywords để tìm các group cần join vào file 'input/keywords.csv'
B2: Thêm hoặc bỏ bớt các nhóm cần join ở các file '{keyword}_linkedin_group.csv'
B2: Nhấn vào nút "Join groups LinkedIn"
```

# Chức năng auto post
```
B1: Nhập content và link linkedin các group vào file 'input/Content.csv'
B2: Nhấn vào nút "Auto post LinkedIn"
```
*********** lƯU Ý **********************************************************************************************
Giãn cách số lần đăng nhập ra vì LinkedIn sẽ check lần đăng nhập bất thường, có thể bị tạm thời khóa tài khoản
# Thoát
Nhấn vào nút "Quit"
