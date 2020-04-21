import simple_chalk


class Sezar:
    def __init__(self):
        self.alfabe = [
            "a",
            "b",
            "c",
            "ç",
            "d",
            "e",
            "f",
            "g",
            "ğ",
            "h",
            "ı",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "ö",
            "p",
            "r",
            "s",
            "ş",
            "t",
            "u",
            "ü",
            "v",
            "w",
            "x",
            "y",
            "z",
            "!",
            ".",
            "-",
            "?",
            "+",
            "*",
            "1","2","3","4","5","6","7","8","9","0"
        ]
        self.index_limit = len(self.alfabe)
    def index_fazlasi_al(self,index):
        harf = ''
        if index == 0:
            harf = self.alfabe[1]
        else:
            harf = self.alfabe[index]
        return harf 
    def encrypt(self, kelime, kaydirma=4):
        sifre = ""
        for harf in kelime:
            if harf.isupper():
                index = self.alfabe.index(harf.lower()) + kaydirma
                if index >= self.index_limit:
                    fazlalik = index - self.index_limit
                    sifre+= self.index_fazlasi_al(fazlalik)
                else:
                    sifre += self.alfabe[index].upper()
            else:
                index = self.alfabe.index(harf) + kaydirma
                if index >= self.index_limit:
                    fazlalik = index - self.index_limit
                    sifre+= self.index_fazlasi_al(fazlalik)
                else:
                    sifre += self.alfabe[index]
        return sifre

    def decrypt(self, kelime, kaydirma=4):
        parola = ""
        for harf in kelime:
            if harf.isupper():
                index = self.alfabe.index(harf.lower()) - kaydirma
                parola += self.alfabe[index].upper()
            else:
                index = self.alfabe.index(harf) - kaydirma
                parola += self.alfabe[index]
        return parola


sezar = Sezar()
flag = True
while flag:
    print(simple_chalk.black.bold("************************"))
    print(
        simple_chalk.green.bold(
            """1-) Sezar algoritması ile bir parolayı encrypt et\n"""
        )
        + simple_chalk.magenta.bold(
            """2-) Sezar algoritması ile şifrelenmiş bir parolayı decrypt et\n"""
        )
        + simple_chalk.blue.bold("""3-) Önce encrypt sonra decrypt\n""")
        + simple_chalk.red.bold("""q-) Çıkış\n""")
        + simple_chalk.yellow.bold(
            """
*********** Programımızda kullanılabilen özel karakterler:
            '!' / '.' / '-' / '?' / '+' / '*'
"""
        )
    )
    islem = input("İşlem girin:")
    if islem == "1":
        parola = input(simple_chalk.green.bold("Encrypt etmek için bir parola girin:"))
        kaydirma = int(
            input(
                simple_chalk.green.bold(
                    "Sezar algoritmasını için kaç karakter kaydırmak istersiniz:"
                )
            )
        )
        print(
            simple_chalk.green.bold(
                f"*****\n{kaydirma} basamak kaydırılarak encrypt edilen şifre -> {sezar.encrypt(parola,kaydirma)}\n*****\n"
            )
        )
    elif islem == "2":
        sifre = input(
            simple_chalk.magenta.bold(
                "Sezar algoritmasıyla encrypt edilen şifreyi girin:"
            )
        )
        kaydirma = int(
            input(
                simple_chalk.magenta.bold(
                    "Encrypt edilen şifre kaç basamak kaydırılmış:"
                )
            )
        )
        print(
            simple_chalk.magenta.bold(
                f"*****\n{kaydirma} basamak kaydırılarak encrypt edilen şifre -> {sezar.decrypt(sifre,kaydirma)}\n*****\n"
            )
        )
    elif islem == "3":
        parola = input(simple_chalk.blue.bold("Encrypt etmek için bir parola girin:"))
        kaydirma = int(
            input(
                simple_chalk.blue.bold(
                    "Sezar algoritmasını için kaç karakter kaydırmak istersiniz:"
                )
            )
        )
        sifre = sezar.encrypt(parola, kaydirma)
        parola = sezar.decrypt(sifre, kaydirma)
        print(
            simple_chalk.blue.bold(
                f"*****\n{kaydirma} basamak kaydırılarak encrypt edilen şifre -> {sifre}\nGirilen parola -> {parola}\n*****\n"
            )
        )
    elif islem == "q":
        print(simple_chalk.red.bold("Programdan çıkılıyor..."))
        flag = False


