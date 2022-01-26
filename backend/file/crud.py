
from sqlalchemy.orm import Session
from file import models, schemas

def get_file_path(db: Session, filename: str):
    try:
        return db.query(models.Pdf_File).filter(models.Pdf_File.filename == filename, models.Pdf_File.is_delete == False ).first()
    except:
        return False

def insert_file(db: Session, filename: str, file_path: str):
    db_tmp_file_obj = models.Pdf_File(filename = filename, file_path = file_path)
    db.add(db_tmp_file_obj)
    db.commit()
    db.refresh(db_tmp_file_obj)
    return db_tmp_file_obj

def delete_file(db: Session, filename: str):
    try:
        db_tmp_file_obj = db.query(models.Pdf_File).filter(models.Pdf_File.filename == filename)
        db_tmp_file_obj.is_delete = True
        db.commit()
        return True
    except:
        return False
