def apply_discount(product, discount):
    price = (product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'] , (
 'This should never happen, but it does occasionally. '
 'We are currently trying to figure out why. '
 'Email dbader if you encounter this in the wild. Thanks!')
    return price

shoes  = {'name' : 'Fancy', 'price' : 14900}

print(apply_discount(shoes, 0.25))
print(apply_discount(shoes, 2))

