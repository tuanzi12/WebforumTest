from tests import ForumRegister
from tests import ForumLogin
from common.Utils import forumDriver
from tests.ForumPersonal import ForumPersonal

if __name__ == "__main__":
    # ForumRegister.ForumRegister().RegisterFailTest()

    # ForumRegister.ForumRegister().RegisterSucTest()
    # ForumLogin.ForumLogin().LoginFailTest()
    ForumLogin.ForumLogin().LoginSucTest()
    # ForumPersonal.ForumPersonal().ChangeProfilePhoto()
    forumDriver.driver.quit()