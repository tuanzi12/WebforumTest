from tests import ForumRegister
from tests import ForumLogin
from tests import ForumPersonal

from common.Utils import forumDriver

if __name__ == "__main__":
    # ForumRegister.ForumRegister().RegisterFailTest()
    # ForumRegister.ForumRegister().RegisterSucTest()
    # ForumLogin.ForumLogin().LoginFailTest()
    ForumLogin.ForumLogin().LoginSucTest()
    # ForumPersonal.ForumPersonal().ChangeProfilePhoto()
    ForumPersonal.ForumPersonal().ChangePersonalProfile()
    forumDriver.driver.quit()