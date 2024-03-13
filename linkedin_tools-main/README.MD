# Tool linkedin
Download project về máy

```bash
git clone https://github.com/TAHKInteractingAI/bot_auto_connect_linkedin
```

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
linkedin_username = 
linkedin_password = 
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

# Thoát
Nhấn vào nút "Quit"