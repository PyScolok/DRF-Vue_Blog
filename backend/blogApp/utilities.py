# def send_new_comment_notification(comment):
#     """Отправка уведомления о новом посте на почту"""
#     if ALLOWED_HOSTS:
#         host = 'http://' + ALLOWED_HOSTS[0]
#     else:
#         host = 'http://127.0.0.1:8000'
#     author = comment.ad.author
#     context = {'author': author, 'host': host, 'comment': comment}
#     subject = render_to_string('email/new_comment_letter_subject.txt', context)
#     body_text = render_to_string('email/new_comment_letter_body.txt', context)
#     author.email_user(subject, body_text)