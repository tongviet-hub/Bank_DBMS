# Hướng dẫn chạy dự án FastAPI

## 1. Tạo môi trường ảo Python (virtual environment)

Mở terminal (bash hoặc cmd) tại thư mục dự án, chạy:

```bash
python -m venv myfastapi
```
- Lệnh này sẽ tạo một thư mục `myfastapi` chứa môi trường Python riêng biệt cho dự án.

## 2. Kích hoạt môi trường ảo

- **Windows (cmd):**
    ```bash
    myfastapi\Scripts\activate
    ```
- **Windows (PowerShell):**
    ```bash
    .\myfastapi\Scripts\Activate.ps1
    ```
- **Linux/macOS:**
    ```bash
    source myfastapi/bin/activate
    ```
- Khi kích hoạt thành công, bạn sẽ thấy tên môi trường (ví dụ: `(myfastapi)`) ở đầu dòng lệnh.

## 3. Cài đặt các thư viện cần thiết

Chạy lệnh sau để cài đặt các package từ file `requirements.txt`:

```bash
pip install -r requirements.txt
```
- Đảm bảo file `requirements.txt` nằm trong thư mục dự án.

## 4. Di chuyển vào thư mục `app`

```bash
cd app
```
- Thư mục này chứa file `main.py` của FastAPI.

## 5. Chạy server FastAPI với Uvicorn

```bash
uvicorn main:app --reload
```
- Tham số `--reload` giúp tự động tải lại server khi có thay đổi mã nguồn.

## 6. Truy cập ứng dụng

- Mở trình duyệt và truy cập: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Để xem tài liệu Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 7. Trải nghiệm thành quả
- Mở 1 file html bất kì
---

**Lưu ý:**  
- Nếu gặp lỗi thiếu thư viện, hãy kiểm tra lại file `requirements.txt` hoặc cài đặt thủ công bằng `pip install <tên_thư_viện>`.
- Để thoát môi trường ảo, dùng lệnh `deactivate`.

---
