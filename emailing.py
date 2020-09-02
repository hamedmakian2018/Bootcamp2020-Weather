def email_function(email_input, message_text):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from tkinter import messagebox


    gmailUser = 'aaaaaaa@gmail.com'
    gmailPassword = 'xxxxxxx'
    recipient = 'bbbbb@gmail.com'

    message = message_text

    msg = MIMEMultipart()
    msg['From'] = f'"Your Name" <{gmailUser}>'
    msg['To'] = recipient
    msg['Subject'] = "Subject here..."
    msg.attach(MIMEText(message))

    try:
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmailUser, gmailPassword)
        mailServer.sendmail(gmailUser, recipient, msg.as_string())
        mailServer.quit()
        messagebox.showinfo('Email','Information hasn been sentto ' + email_input)
    except:
        messagebox.showerror('Error','Cannot send email to ' + email_input)
        
