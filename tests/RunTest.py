from tests import ForumRegister
from tests import ForumLogin
from tests import ForumPersonal
from tests import ForumPost
from common.Utils import forumDriver

if __name__ == "__main__":
    username = "tuanzi_test5"
        # 注册失败/注册成功
    ForumRegister.ForumRegister().RegisterFailTest()
    ForumRegister.ForumRegister().RegisterSucTest()
         # 登录失败/登录成功
    ForumLogin.ForumLogin().LoginFailTest()
    ForumLogin.ForumLogin().LoginSucTest()

        # 修改个人信息
    ForumPersonal.ForumPersonal(). PersonalProfileChange()
        # 个人页面修改密码成功/失败
    ForumPersonal.ForumPersonal().PasswordFailChangeTest()
    ForumPersonal.ForumPersonal().PasswordSucChangeTest()

        # 发帖失败/发帖成功
    ForumPost.ForumPost().PostMessageFailTest()
    ForumPost.ForumPost().PostMessageSucTest()
        # 帖子互动
    ForumPost.ForumPost().PostInteraction()
    # ForumPost.ForumPost().sort()
    forumDriver.driver.quit()