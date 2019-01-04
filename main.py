# -*- coding: utf-8 -*-

import pandas as pd
from postbox import Postbox


def check_input(msg):

    _input = input(msg + ' Y/n? ')

    if _input.lower() in 'y' or _input == '':
        return True


def check_table(df):

    if not {'student_no', 'student_name'}.issubset(set(df.columns.values)):
        raise Exception('檔案格式不符')

    if 'score' in df.columns.values:
        if check_input('要計算名次嗎'):
            df['rank'] = df.rank(method='min', ascending=False)[
                'score'].astype('int')
            df['rank'] = df['rank'].astype('str') + '/' + str(df.shape[0])

    return df


def convert_to_mail(sender, subject, text, sign_off, df):

    columns = list(df.columns.values)[2:]
    mails = []

    for _, row in df.iterrows():
        contents = []
        for col in columns:
            contents.append(col + ': ' + str(row[col]))
        content = '\r\n\r\n'.join(contents)
        body = 'Hi ' + row['student_name'] + \
            ',\r\n\r\n' + text + '\r\n\r\n' + content + \
            '\r\n\r\n' + sign_off + '\r\n' + sender

        addr = row['student_no'] + '@mail.ntust.edu.tw'
        mails.append({'addr': addr, 'subject': subject, 'body': body})

    return mails


if __name__ == "__main__":

    try:
        df = pd.read_csv('data.csv')
    except UnicodeDecodeError:
        df = pd.read_csv('data.csv', encoding='big5')

    df = check_table(df)
    print(df)

    if check_input('確定寄送至學生信箱'):

        sender = input('寄件者姓名: ')
        subject = input('信件標題: ')
        text = input('信件內容: ')
        sign_off = input('結尾敬語: ')

        mails = convert_to_mail(sender, subject, text, sign_off, df)

        for m in mails:
            print(m)

        if check_input('確定寄送'):
            print('請輸入台科的信箱(xxx@mail.ntust.edu.tw)')
            mail = Postbox(host='mail.ntust.edu.tw:25', tls=False)
            for m in mails:
                mail.send(
                    to=m['addr'],
                    subject=m['subject'],
                    body=m['body']
                )
            print('finsh')

        mail.close()
