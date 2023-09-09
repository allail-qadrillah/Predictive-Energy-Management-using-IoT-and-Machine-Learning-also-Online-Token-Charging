from firebase_admin import credentials, initialize_app, db



class RTDB:
    def __init__(self) -> None:
        cred = credentials.Certificate('./firebase/credentials.json')
        initialize_app(cred, {
            'databaseURL': 'https://i3o-new-default-rtdb.asia-southeast1.firebasedatabase.app'
        })
        
    def update(self, path:str, data):
        return db.reference(path).update(data)

    def read(self, path:str):
        return db.reference(path).get()
    
    def ignore_first_call(self, fn):
        """
        mengabaikan panggilan awal ketika listen ke salah satu value
        """
        called = False
        def wrapper(*args, **kwargs):
            nonlocal called
            if called: return fn(*args, **kwargs);
            else: called = True; return None;
        return wrapper
    
    def listen(self, path:str, func):
        """
        membaca ketika da perubahan value pada database
        """
        return db.reference(path).listen(func)
