import os
nmap_command = "nmap -sT -F -A -O -sV -sC -v 183.81.34.136"
os.system(nmap_command)

# -sT thực hiện TCP connect scan
# -F chỉ quét cổng nhanh (top 1000)
# -A kết hợp các tùy chọn -O (OS detection)
# -sV (service/version detection)
# -sC (script scan)
# -O thực hiện phát hiện hệ điều hành
# -sV thực hiện phát hiện phiên bản phần mềm và dịch vụ
# -sC thực hiện script scan để kiểm tra các lỗ hổng của ứng dụng
# -v in ra thông tin chi tiết hơn