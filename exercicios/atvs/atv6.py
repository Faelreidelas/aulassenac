emails = [["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]]
def filtrar_emails(emails):
    emails_filtrados = []
    for email in emails[0]:
        if email.endswith("@senac.df"):
            emails_filtrados.append(email)
    return emails_filtrados

print (filtrar_emails(emails))