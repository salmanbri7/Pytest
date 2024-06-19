class Orders:
    order_lines = [
        {
            "description": "SET-KASTRON SPLIT 2 TON",
            "quantity": 2,
            "unit_price": 180,
            "tax_percentage": 0.1,
            "subtotal": 360,
            "total": 396,
        },
        {
            "description": "SET-KASTRON AQUACHILL 1.5 TON",
            "quantity": 1,
            "unit_price": 200,
            "tax_percentage": 0.1,
            "subtotal": 200,
            "total": 220,
        },
        {
            "description": 'SAMSUNG 43" CU-7000',
            "quantity": 1,
            "unit_price": 119,
            "tax_percentage": 0.1,
            "subtotal": 119,
            "total": 130.9,
        },
    ]

    # add discount defualt 10,5,1
    def addDiscount(self):
        self.order_lines[0]["discount_amount"] = 10
        self.order_lines[1]["discount_amount"] = 5
        self.order_lines[2]["discount_amount"] = 1

    # in the below function the user can specify the discount he wants for each order
    # if we want 10,5,1 he should pass them as parameters
    # ex: order.addDiscountManual(10,5,1)
    def addDiscountManual(self, discount1, discount2, discount3):
        self.order_lines[0]["discount_amount"] = discount1
        self.order_lines[1]["discount_amount"] = discount2
        self.order_lines[2]["discount_amount"] = discount3

    # assuming the discount affects the "unit price"
    def calculateNewValues(self):
        for order in self.order_lines:
            order["unit_price"] = order["unit_price"] - order["discount_amount"]
            order["subtotal"] = order["unit_price"] * order["quantity"]
            order["total"] = order["subtotal"] * (1 + order["tax_percentage"])


order = Orders()
# order.addDiscount()
order.addDiscountManual(10, 5, 1)
print(order.order_lines)
print("\n")
order.calculateNewValues()
print(order.order_lines)
