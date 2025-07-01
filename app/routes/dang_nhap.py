from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas
from helper.security import hash_password
from helper.security import verify_password
router = APIRouter()

@router.post("/dang-nhap/", response_model=schemas.DangNhap)
def create_dang_nhap(dang_nhap: schemas.DangNhapCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một thông tin đăng nhập.
    """
    return crud.create_dang_nhap(db=db, dang_nhap=dang_nhap)

@router.get("/dang-nhap/", response_model=list[schemas.DangNhap])
def get_all_dang_nhap(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả thông tin đăng nhập.
    """
    db_dang_nhap = crud.get_all_dang_nhap(db=db)
    return db_dang_nhap

@router.get("/dang-nhap/search/", response_model=list[schemas.DangNhap])
def search_dang_nhap(
    dang_nhap_id: str | None = None,
    username: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm thông tin đăng nhập theo ID hoặc tên người dùng.
    """
    if dang_nhap_id:
        db_dang_nhap = crud.get_dang_nhap(db=db, dang_nhap_id=dang_nhap_id)
        return [db_dang_nhap] if db_dang_nhap else []
    
    if username:
        db_dang_nhap = crud.get_dang_nhap(db=db, username=username)
        return [db_dang_nhap] if db_dang_nhap else []

    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên người dùng để tìm kiếm")


@router.delete("/dang-nhap/{dang_nhap_id}")
def delete_dang_nhap(dang_nhap_id: str, db: Session = Depends(get_db)):
    """
    Xóa thông tin đăng nhập theo ID.
    """
    return crud.delete_dang_nhap(db=db, dang_nhap_id=dang_nhap_id)

@router.put("/dang-nhap/{dang_nhap_id}", response_model=schemas.DangNhap)
def update_dang_nhap(dang_nhap_id: str, dang_nhap: schemas.DangNhapCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin đăng nhập.
    """
    return crud.update_dang_nhap(db=db, dang_nhap_id=dang_nhap_id, dang_nhap=dang_nhap)

# Thêm endpoint đăng nhập
@router.post("/login")
async def login(dang_nhap: schemas.DangNhapBase, db: Session = Depends(get_db)):
    # Tìm user theo tên đăng nhập
    db_dang_nhap = crud.get_dang_nhap(db=db, username=dang_nhap.Ten_dang_nhap)
    if not db_dang_nhap:
        print("Không tìm thấy user:", dang_nhap.Ten_dang_nhap)
        raise HTTPException(status_code=401, detail="Tên đăng nhập hoặc mật khẩu không đúng")
    
    # Log mật khẩu nhập vào và mật khẩu trong DB (chú ý KHÔNG làm điều này trên môi trường thật)
    print("Mật khẩu nhập vào:", dang_nhap.Mat_khau)
    print("Mật khẩu trong DB:", db_dang_nhap.Mat_khau)
    print("Kết quả verify_password:", verify_password(dang_nhap.Mat_khau, db_dang_nhap.Mat_khau))
    
    # Kiểm tra mật khẩu
    if not verify_password(dang_nhap.Mat_khau, db_dang_nhap.Mat_khau):
        print("Sai mật khẩu cho user:", dang_nhap.Ten_dang_nhap)
        raise HTTPException(status_code=401, detail="Tên đăng nhập hoặc mật khẩu không đúng")
    
    # Đăng nhập thành công
    print("Đăng nhập thành công cho user:", dang_nhap.Ten_dang_nhap)
    return {"success": True, "message": "Đăng nhập thành công", "user_id": db_dang_nhap.id}