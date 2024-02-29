class Member():
    def __init__(self, name, id, nickname, password):
        self.name = name
        self.id = id
        self.nickname = nickname
        self.password = password
    

    def display(self):
        print(f"회원 이름: {self.name}, 회원 아이디: {self.id}")
        

class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


members = []

members.append(Member("김땡땡", "kimdd", "김땡", "1234"))
members.append(Member("박땡땡", "parkdd", "박땡", "4567"))
members.append(Member("이땡땡", "leedd", "이땡", "7890"))


def printmembername():
    for member in members :
        print(member.name)


posts = []
for member in members :
    for i in range(3):
        title = f"{member.nickname}의 게시물 {i+1}"
        content = f"{member.nickname}의 내용 {i+1}"
        author = member.nickname
        post = Post(title, content, member.nickname)
        posts.append(post)

def searchid():
    member.nickname = input("\n검색할 유저 닉네임을 입력해주세요: ")

    print("\n특정 유저가 작성한 게시글 제목:")
    for post in posts:
        if post.author == member.nickname:
            print(f'\n{post.title}')

def searchcontent():
    text= input("\n검색할 내용을 입력해주세요: ")
    for post in posts:
        if text in post.content:
            print(f"\n{post.title}")

def sighin():
    name = input("\n이름을 입력해주세요: ")
    id = input("\n사용하실 아이디를 입력해주세요: ")
    password = input("\n사용하실 비밀번호를 입력해주세요: ")
    nickname = input("\n사용하실 닉네임을 입력해주세요: ")
    members.append(Member(name, id, nickname, password))
    print("\n회원가입이 완료되었습니다")

def login():
    id = input("아이디: ")
    password = input("비밀번호: ")
    
    for member in members:
        if member.id == id and member.password == password:
            print("\n로그인 되었습니다")
            return member
    print("\n아이디 또는 비밀번호를 확인해주세요\n")
    return None
    
def createpost(loginaccount):
    title = input("\n게시글 제목을 입력해주세요: ")
    content = input("\n게시글 내용을 입력해주세요: ")
    post = Post(title, content, loginaccount.nickname)
    posts.append(post)
    print("\n게시글이 작성되었습니다")

def test():
    loginaccount = None
    
    while True:
        print("\n환영합니다! 아래의 숫자들을 입력하여 원하는 기능을 실행해주세요\n")
        print("\n1. 로그인")
        print("\n2. 회원가입")
        print("\n3. 종료")

        select = input('\n')

        if select == '1' and not loginaccount:
            loginaccount = login()
        elif select == '2' and not loginaccount:
            sighin()
        elif select == '3':
            print("\n안녕히가세요!")
            break
        else:
            print("\n아래에 보이는 숫자들을 입력해주세요")

        if loginaccount:
            while True:
                print(f"\n어서오세요 {loginaccount.nickname} 님!")
                print("\n1. 게시글 작성")
                print("\n2. 닉네임으로 게시물 검색")
                print("\n3. 내용으로 게시물 검색")
                print("\n4. 로그아웃")
                
                loginselect = input('\n')

                if loginselect == '1':
                    createpost(loginaccount)
                elif loginselect == '2':
                    searchid()
                    
                elif loginselect == '3':
                    searchcontent()
                
                elif loginselect == '4':
                    loginaccount = None

                    print("\n안녕히가세요!")
                    break
                else:
                    print("\n올바른 숫자를 입력해주세요")


test()