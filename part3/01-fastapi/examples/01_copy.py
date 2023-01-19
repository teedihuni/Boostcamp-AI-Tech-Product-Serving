from fastapi import FastAPI
import uvicorn 

#Fast api 객체 생성
app = FastAPI()

#"/"로 접근하면 return을 보여줌
@app.get("/")
def read_root():
    return {"Hello" : "World"}

#실행할때 uvicorn을 입력해주기 매번 귀찮으니 아래처럼 설정
if __name__ =='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)