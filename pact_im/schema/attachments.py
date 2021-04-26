from pydantic import BaseModel, AnyHttpUrl


class FileUpload(BaseModel):
    file_url: AnyHttpUrl

