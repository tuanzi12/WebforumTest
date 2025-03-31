from tests import ForumRegister
from tests import ForumLogin
from tests import ForumPersonal
from tests import ForumPost
from common.Utils import forumDriver

if __name__ == "__main__":
    # ForumRegister.ForumRegister().RegisterFailTest()
    # ForumRegister.ForumRegister().RegisterSucTest()
    # ForumLogin.ForumLogin().LoginFailTest()
    ForumLogin.ForumLogin().LoginSucTest()
    # ForumPersonal.ForumPersonal().Change_ProfilePhoto()
    # ForumPersonal.ForumPersonal(). PersonalProfileSucChange()
    # ForumPersonal.ForumPersonal().PasswordSucChangeTest()
    # ForumPersonal.ForumPersonal().PasswordFailChangeTest()
    # ForumPost.ForumPost().PostMessageSucTest()
    ForumPost.ForumPost().PostMessageFailTest()
    forumDriver.driver.quit()