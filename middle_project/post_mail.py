import os
from django.core.mail import send_mail, EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'middle_project.settings'
if __name__ == '__main__':
    # send_mail(
    # 'HELLO',
    # 'HAHAHAHA！',
    # '18500872740@sina.cn',
    # ['18500872740@163.com'],
    # )
    subject, from_email, to = 'hello', '18500872740@sina.cn', '18500872740@163.com'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target = blank > www.baidu.com </a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html"),
    msg.send()



















