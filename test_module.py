from budget import Category


class TestCategory:

    def test_1(self):
        assert 1 == 1
        pass

    def test_create_category_without_name(self):
        cat = Category("")
        assert isinstance(cat, Category)
        pass

    def test_deposit(self):
        cat = Category("Computers")
        cat.deposit(247, "")
        assert dict(cat.ledger[len(cat.ledger) - 1])["description"] == ""
        assert dict(cat.ledger[len(cat.ledger) - 1])["amount"] == 247
        pass

    def test_withdraw(self):
        cat = Category("Childrens")
        cat.withdraw(296, "Buying candies")
        assert len(cat.ledger) == 0
        cat.deposit(1000, "Initial deposit")
        cat.withdraw(296, "Buying candies")
        assert cat.get_balance() == (1000 - 296)
        assert dict(cat.ledger[len(cat.ledger) - 1])["amount"] == -296
        pass

    def test_transfer(self):
        cat = Category("Childrens")
        cat.deposit(1000, "Initial deposit")
        catego = Category("Computers")
        catego.deposit(1000, "Initial deposit")
        assert cat.transfer(500, catego)
        assert not cat.transfer(1001, catego)
        assert catego.get_balance() == 1500
        pass

    def test_check_funds(self):
        cat = Category("Childrens")
        cat.deposit(1000, "Initial deposit")
        assert cat.check_funds(900)
        assert not cat.check_funds(1050)
        pass
    pass
