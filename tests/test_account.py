import unittest
from graphenebase.base58 import Base58
from graphenebase.account import BrainKey, Address, PublicKey, PrivateKey, PasswordKey


class Testcases(unittest.TestCase):
    def test_B85hexgetb58_btc(self):
        self.assertEqual(["5HqUkGuo62BfcJU5vNhTXKJRXuUi9QSE6jp8C3uBJ2BVHtB8WSd",
                          "5JWcdkhL3w4RkVPcZMdJsjos22yB5cSkPExerktvKnRNZR5gx1S",
                          "5HvVz6XMx84aC5KaaBbwYrRLvWE46cH6zVnv4827SBPLorg76oq",
                          "5Jete5oFNjjk3aUMkKuxgAXsp7ZyhgJbYNiNjHLvq5xzXkiqw7R",
                          "5KDT58ksNsVKjYShG4Ls5ZtredybSxzmKec8juj7CojZj6LPRF7",
                          "02b52e04a0acfe611a4b6963462aca94b6ae02b24e321eda86507661901adb49",
                          "5b921f7051be5e13e177a0253229903c40493df410ae04f4a450c85568f19131",
                          "0e1bfc9024d1f55a7855dc690e45b2e089d2d825a4671a3c3c7e4ea4e74ec00e",
                          "6e5cc4653d46e690c709ed9e0570a2c75a286ad7c1bc69a648aae6855d919d3e",
                          ],
                         [format(Base58("02b52e04a0acfe611a4b6963462aca94b6ae02b24e321eda86507661901adb49"), "WIF"),
                          format(Base58("5b921f7051be5e13e177a0253229903c40493df410ae04f4a450c85568f19131"), "WIF"),
                          format(Base58("0e1bfc9024d1f55a7855dc690e45b2e089d2d825a4671a3c3c7e4ea4e74ec00e"), "WIF"),
                          format(Base58("6e5cc4653d46e690c709ed9e0570a2c75a286ad7c1bc69a648aae6855d919d3e"), "WIF"),
                          format(Base58("b84abd64d66ee1dd614230ebbe9d9c6d66d78d93927c395196666762e9ad69d8"), "WIF"),
                          repr(Base58("5HqUkGuo62BfcJU5vNhTXKJRXuUi9QSE6jp8C3uBJ2BVHtB8WSd")),
                          repr(Base58("5JWcdkhL3w4RkVPcZMdJsjos22yB5cSkPExerktvKnRNZR5gx1S")),
                          repr(Base58("5HvVz6XMx84aC5KaaBbwYrRLvWE46cH6zVnv4827SBPLorg76oq")),
                          repr(Base58("5Jete5oFNjjk3aUMkKuxgAXsp7ZyhgJbYNiNjHLvq5xzXkiqw7R")),
                          ])

    def test_B85hexgetb58(self):
        self.assertEqual(['CREA2CAbTi1ZcgMJ5otBFZSGZJKJenwGa9NvkLxsrS49Kr8JsiSGc',
                          'CREAhL45FEyUVSVV1LXABQnh4joS9FsUaffRtsdarB5uZjPsrwMZF',
                          'CREA7DQR5GsfVaw4wJXzA3TogDhuQ8tUR2Ggj8pwyNCJXheHehL4Q',
                          'CREAqc4QMAJHAkna65i8U4b7nkbWk4VYSWpZebW7JBbD7MN8FB5sc',
                          'CREA2QAVTJnJQvLUY4RDrtxzX9jS39gEq8gbqYMWjgMxvsvZTJxDSu'
                          ],
                         [format(Base58("02b52e04a0acfe611a4b6963462aca94b6ae02b24e321eda86507661901adb49"), "CREA"),
                          format(Base58("5b921f7051be5e13e177a0253229903c40493df410ae04f4a450c85568f19131"), "CREA"),
                          format(Base58("0e1bfc9024d1f55a7855dc690e45b2e089d2d825a4671a3c3c7e4ea4e74ec00e"), "CREA"),
                          format(Base58("6e5cc4653d46e690c709ed9e0570a2c75a286ad7c1bc69a648aae6855d919d3e"), "CREA"),
                          format(Base58("b84abd64d66ee1dd614230ebbe9d9c6d66d78d93927c395196666762e9ad69d8"), "CREA")])

    def test_Address(self):
        self.assertEqual([format(Address("CREAFN9r6VYzBK8EKtMewfNbfiGCr56pHDBFi", prefix="CREA"), "CREA"),
                          format(Address("CREAdXrrTXimLb6TEt3nHnePwFmBT6Cck112", prefix="CREA"), "CREA"),
                          format(Address("CREAJQUAt4gz4civ8gSs5srTK4r82F7HvpChk", prefix="CREA"), "CREA"),
                          format(Address("CREAFPXXHXXGbyTBwdKoJaAPXRnhFNtTRS4EL", prefix="CREA"), "CREA"),
                          format(Address("CREA3qXyZnjJneeAddgNDYNYXbF7ARZrRv5dr", prefix="CREA"), "CREA"),
                          ],
                         ["CREAFN9r6VYzBK8EKtMewfNbfiGCr56pHDBFi",
                          "CREAdXrrTXimLb6TEt3nHnePwFmBT6Cck112",
                          "CREAJQUAt4gz4civ8gSs5srTK4r82F7HvpChk",
                          "CREAFPXXHXXGbyTBwdKoJaAPXRnhFNtTRS4EL",
                          "CREA3qXyZnjJneeAddgNDYNYXbF7ARZrRv5dr",
                          ])

    def test_PubKey(self):
        self.assertEqual([format(PublicKey("CREA6UtYWWs3rkZGV8JA86qrgkG6tyFksgECefKE1MiH4HkLD8PFGL", prefix="CREA").address, "CREA"),
                          format(PublicKey("CREA8YAMLtNcnqGNd3fx28NP3WoyuqNtzxXpwXTkZjbfe9scBmSyGT", prefix="CREA").address, "CREA"),
                          format(PublicKey("CREA7HUo6bm7Gfoi3RqAtzwZ83BFCwiCZ4tp37oZjtWxGEBJVzVVGw", prefix="CREA").address, "CREA"),
                          format(PublicKey("CREA6676cZ9qmqPnWMrm4McjCuHcnt6QW5d8oRJ4t8EDH8DdCjvh4V", prefix="CREA").address, "CREA"),
                          format(PublicKey("CREA7u8m6zUNuzPNK1tPPLtnipxgqV9mVmTzrFNJ9GvovvSTCkVUra", prefix="CREA").address, "CREA")
                          ], [
                            'CREADXi9tQ6Pjf1SEv3m4jn2U5M2YgMPpHy2V',
                            'CREAQ1AEncFQ9ddRU1jfrieomX8RgTnSGgUwj',
                            'CREABkT8dGRrbbYpqCXovCBoZDNiVq3XXMyLG',
                            'CREA3U2ok8z392o6BXYu75PGxohEH9boCx3dy',
                            'CREACpkigUBxSLfK2Ldgah9QpoLFftL11k8wW'])

    def test_btsprivkey(self):
        self.assertEqual([format(PrivateKey("5HqUkGuo62BfcJU5vNhTXKJRXuUi9QSE6jp8C3uBJ2BVHtB8WSd").address, "CREA"),
                          format(PrivateKey("5JWcdkhL3w4RkVPcZMdJsjos22yB5cSkPExerktvKnRNZR5gx1S").address, "CREA"),
                          format(PrivateKey("5HvVz6XMx84aC5KaaBbwYrRLvWE46cH6zVnv4827SBPLorg76oq").address, "CREA"),
                          format(PrivateKey("5Jete5oFNjjk3aUMkKuxgAXsp7ZyhgJbYNiNjHLvq5xzXkiqw7R").address, "CREA"),
                          format(PrivateKey("5KDT58ksNsVKjYShG4Ls5ZtredybSxzmKec8juj7CojZj6LPRF7").address, "CREA")
                          ], [
                            'CREAGu2U7Q3rmkCUCkQH2SToLMjEVUr86GrpA',
                            'CREA9YgTfC8EfkgDG7DoRXJpMVKRougo64Lop',
                            'CREABXqRucGm7nRkk6jm7BNspTJTWRtNcx7k5',
                            'CREA5tTDDR6M3mkcyVv16edsw8dGUyNQZrvKU',
                            'CREA8G9ATJbJewVjTgTGmLGLNe1uP5XDWzaKX'])

    def test_PublicKey(self):
        self.assertEqual([str(PublicKey("CREA6UtYWWs3rkZGV8JA86qrgkG6tyFksgECefKE1MiH4HkLD8PFGL", prefix="CREA")),
                          str(PublicKey("CREA8YAMLtNcnqGNd3fx28NP3WoyuqNtzxXpwXTkZjbfe9scBmSyGT", prefix="CREA")),
                          str(PublicKey("CREA7HUo6bm7Gfoi3RqAtzwZ83BFCwiCZ4tp37oZjtWxGEBJVzVVGw", prefix="CREA")),
                          str(PublicKey("CREA6676cZ9qmqPnWMrm4McjCuHcnt6QW5d8oRJ4t8EDH8DdCjvh4V", prefix="CREA")),
                          str(PublicKey("CREA7u8m6zUNuzPNK1tPPLtnipxgqV9mVmTzrFNJ9GvovvSTCkVUra", prefix="CREA"))
                          ],
                         ["CREA6UtYWWs3rkZGV8JA86qrgkG6tyFksgECefKE1MiH4HkLD8PFGL",
                          "CREA8YAMLtNcnqGNd3fx28NP3WoyuqNtzxXpwXTkZjbfe9scBmSyGT",
                          "CREA7HUo6bm7Gfoi3RqAtzwZ83BFCwiCZ4tp37oZjtWxGEBJVzVVGw",
                          "CREA6676cZ9qmqPnWMrm4McjCuHcnt6QW5d8oRJ4t8EDH8DdCjvh4V",
                          "CREA7u8m6zUNuzPNK1tPPLtnipxgqV9mVmTzrFNJ9GvovvSTCkVUra"
                          ])

    def test_Privatekey(self):
        self.assertEqual([str(PrivateKey("5HvVz6XMx84aC5KaaBbwYrRLvWE46cH6zVnv4827SBPLorg76oq")),
                          str(PrivateKey("5Jete5oFNjjk3aUMkKuxgAXsp7ZyhgJbYNiNjHLvq5xzXkiqw7R")),
                          str(PrivateKey("5KDT58ksNsVKjYShG4Ls5ZtredybSxzmKec8juj7CojZj6LPRF7")),
                          repr(PrivateKey("5HvVz6XMx84aC5KaaBbwYrRLvWE46cH6zVnv4827SBPLorg76oq")),
                          repr(PrivateKey("5Jete5oFNjjk3aUMkKuxgAXsp7ZyhgJbYNiNjHLvq5xzXkiqw7R")),
                          repr(PrivateKey("5KDT58ksNsVKjYShG4Ls5ZtredybSxzmKec8juj7CojZj6LPRF7")),
                          ],
                         ["5HvVz6XMx84aC5KaaBbwYrRLvWE46cH6zVnv4827SBPLorg76oq",
                          "5Jete5oFNjjk3aUMkKuxgAXsp7ZyhgJbYNiNjHLvq5xzXkiqw7R",
                          "5KDT58ksNsVKjYShG4Ls5ZtredybSxzmKec8juj7CojZj6LPRF7",
                          '0e1bfc9024d1f55a7855dc690e45b2e089d2d825a4671a3c3c7e4ea4e74ec00e',
                          '6e5cc4653d46e690c709ed9e0570a2c75a286ad7c1bc69a648aae6855d919d3e',
                          'b84abd64d66ee1dd614230ebbe9d9c6d66d78d93927c395196666762e9ad69d8'
                          ])

    def test_BrainKey(self):
        self.assertEqual([str(BrainKey("COLORER BICORN KASBEKE FAERIE LOCHIA GOMUTI SOVKHOZ Y GERMAL AUNTIE PERFUMY TIME FEATURE GANGAN CELEMIN MATZO").get_private()),
                          str(BrainKey("NAK TILTING MOOTING TAVERT SCREENY MAGIC BARDIE UPBORNE CONOID MAUVE CARBON NOTAEUM BITUMEN HOOEY KURUMA COWFISH").get_private()),
                          str(BrainKey("CORKITE CORDAGE FONDISH UNDER FORGET BEFLEA OUTBUD ZOOGAMY BERLINE ACANTHA STYLO YINCE TROPISM TUNKET FALCULA TOMENT").get_private()),
                          str(BrainKey("MURZA PREDRAW FIT LARIGOT CRYOGEN SEVENTH LISP UNTAWED AMBER CRETIN KOVIL TEATED OUTGRIN POTTAGY KLAFTER DABB").get_private()),
                          str(BrainKey("VERDICT REPOUR SUNRAY WAMBLY UNFILM UNCOUS COWMAN REBUOY MIURUS KEACORN BENZOLE BEMAUL SAXTIE DOLENT CHABUK BOUGHED").get_private()),
                          str(BrainKey("HOUGH TRUMPH SUCKEN EXODY MAMMATE PIGGIN CRIME TEPEE URETHAN TOLUATE BLINDLY CACOEPY SPINOSE COMMIE GRIECE FUNDAL").get_private()),
                          str(BrainKey("OERSTED ETHERIN TESTIS PEGGLE ONCOST POMME SUBAH FLOODER OLIGIST ACCUSE UNPLAT OATLIKE DEWTRY CYCLIZE PIMLICO CHICOT").get_private()),
                          ],
                         ["5JfwDztjHYDDdKnCpjY6cwUQfM4hbtYmSJLjGd9KTpk9J4H2jDZ",
                          "5JcdQEQjBS92rKqwzQnpBndqieKAMQSiXLhU7SFZoCja5c1JyKM",
                          "5JsmdqfNXegnM1eA8HyL6uimHp6pS9ba4kwoiWjjvqFC1fY5AeV",
                          "5J2KeFptc73WTZPoT1Sd59prFep6SobGobCYm7T5ZnBKtuW9RL9",
                          "5HryThsy6ySbkaiGK12r8kQ21vNdH81T5iifFEZNTe59wfPFvU9",
                          "5Ji4N7LSSv3MAVkM3Gw2kq8GT5uxZYNaZ3d3y2C4Ex1m7vshjBN",
                          "5HqSHfckRKmZLqqWW7p2iU18BYvyjxQs2sksRWhXMWXsNEtxPZU",
                          ])

    def test_BrainKey_normalize(self):
        b = "COLORER BICORN KASBEKE FAERIE LOCHIA GOMUTI SOVKHOZ Y GERMAL AUNTIE PERFUMY TIME FEATURE GANGAN CELEMIN MATZO"
        self.assertEqual([BrainKey(b + "").get_brainkey(),
                          BrainKey(b + " ").get_brainkey(),
                          BrainKey(b + "  ").get_brainkey(),
                          BrainKey(b + "\t").get_brainkey(),
                          BrainKey(b + "\t\t").get_brainkey(),
                          BrainKey(b.replace(" ", "\t")).get_brainkey(),
                          BrainKey(b.replace(" ", "  ")).get_brainkey(),
                          ],
                         [b, b, b, b, b, b, b])

    def test_BrainKey_sequences(self):
        b = BrainKey("COLORER BICORN KASBEKE FAERIE LOCHIA GOMUTI SOVKHOZ Y GERMAL AUNTIE PERFUMY TIME FEATURE GANGAN CELEMIN MATZO")
        keys = ["5Hsbn6kXio4bb7eW5bX7kTp2sdkmbzP8kGWoau46Cf7en7T1RRE",
                "5K9MHEyiSye5iFL2srZu3ZVjzAZjcQxUgUvuttcVrymovFbU4cc",
                "5JBXhzDWQdYPAzRxxuGtzqM7ULLKPK7GZmktHTyF9foGGfbtDLT",
                "5Kbbfbs6DmJFNddWiP1XZfDKwhm5dkn9KX5AENQfQke2RYBBDcz",
                "5JUqLwgxn8f7myNz4gDwo5e77HZgopHMDHv4icNVww9Rxu1GDG5",
                "5JNBVj5QVh86N8MUUwY3EVUmsZwChZftxnuJx22DzEtHWC4rmvK",
                "5JdvczYtxPPjQdXMki1tpNvuSbvPMxJG5y4ndEAuQsC5RYMQXuC",
                "5HsUSesU2YB4EA3dmpGtHh8aPAwEdkdhidG8hcU2Nd2tETKk85t",
                "5JpveiQd1mt91APyQwvsCdAXWJ7uag3JmhtSxpGienic8vv1k2W",
                "5KDGhQUqQmwcGQ9tegimSyyT4vmH8h2fMzoNe1MT9bEGvRvR6kD"]
        for i in keys:
            p = b.next_sequence().get_private()
            self.assertEqual(str(p), i)

    def test_PasswordKey(self):
        a = ["Aang7foN3oz1Ungai2qua5toh3map8ladei1eem2ohsh2shuo8aeji9Thoseo7ah",
             "iep1Mees9eghiifahwei5iidi0Sazae9aigaeT7itho3quoo2dah5zuvobaelau5",
             "ohBeuyoothae5aer9odaegh5Eeloh1fi7obei9ahSh0haeYuas1sheehaiv5LaiX",
             "geiQuoo9NeeLoaZee0ain3Ku1biedohsesien4uHo1eib1ahzaesh5shae3iena7",
             "jahzeice6Ix8ohBo3eik9pohjahgeegoh9sahthai1aeMahs8ki7Iub1oojeeSuo",
             "eiVahHoh2hi4fazah9Tha8loxeeNgequaquuYee6Shoopo3EiWoosheeX6yohg2o",
             "PheeCh3ar8xoofoiphoo4aisahjiiPah4vah0eeceiJ2iyeem9wahyupeithah9T",
             "IuyiibahNgieshei2eeFu8aic1IeMae9ooXi9jaiwaht4Wiengieghahnguang0U",
             "Ipee1quee7sheughemae4eir8pheix3quac3ei0Aquo9ohieLaeseeh8AhGeM2ew",
             "Tech5iir0aP6waiMeiHoph3iwoch4iijoogh0zoh9aSh6Ueb2Dee5dang1aa8IiP"
             ]
        b = ["CREA5NyCrrXHmdikC6QPRAPoDjSHVQJe3WC5bMZuF6YhqhSsfYfjhN",
             "CREA8gyvJtYyv5ZbT2ZxbAtgufQ5ovV2bq6EQp4YDTzQuSwyg7Ckry",
             "CREA7yE71iVPSpaq8Ae2AmsKfyFxA8pwYv5zgQtCnX7xMwRUQMVoGf",
             "CREA5jRgWA2kswPaXsQNtD2MMjs92XfJ1TYob6tjHtsECg2AusF5Wo",
             "CREA6XHwVxcP6zP5NV1jUbG6Kso9m8ZG9g2CjDiPcZpAxHngx6ATPB",
             "CREA59X1S4ofTAeHd1iNHDGxim5GkLo2AdcznksUsSYGU687ywB5WV",
             "CREA6BPPL4iSRbFVVN8v3BEEEyDsC1STRK7Ba9ewQ4Lqvszn5J8VAe",
             "CREA7cdK927wj95ptUrCk6HKWVeF74LG5cTjDTV22Z3yJ4Xw8xc9qp",
             "CREA7VNFRjrE1hs1CKpEAP9NAabdFpwvzYXRKvkrVBBv2kTQCbNHz7",
             "CREA7ZZFhEBjujcKjkmY31i1spPMx6xDSRhkursZLigi2HKLuALe5t",
             ]
        for i, pwd in enumerate(a):
            p = format(PasswordKey("jared", pwd, "posting").get_public(), "CREA")
            self.assertEqual(p, b[i])

    def test_btcprivkey(self):
        self.assertEqual([format(PrivateKey("5HvVz6XMx84aC5KaaBbwYrRLvWE46cH6zVnv4827SBPLorg76oq").bitcoin.address, "BTC"),
                          format(PrivateKey("5Jete5oFNjjk3aUMkKuxgAXsp7ZyhgJbYNiNjHLvq5xzXkiqw7R").bitcoin.address, "BTC"),
                          format(PrivateKey("5KDT58ksNsVKjYShG4Ls5ZtredybSxzmKec8juj7CojZj6LPRF7").bitcoin.address, "BTC"),
                          ],
                         ["1G7qw8FiVfHEFrSt3tDi6YgfAdrDrEM44Z",
                          "12c7KAAZfpREaQZuvjC5EhpoN6si9vekqK",
                          "1Gu5191CVHmaoU3Zz3prept87jjnpFDrXL",
                          ])
