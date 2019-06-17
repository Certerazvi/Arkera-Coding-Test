import unittest


# Assume all elements are positive since they represent prices.
def get_largest_possible_loss(pricesList):

    assert len(pricesList) > 1
    assert all(x >= 0 for x in pricesList)

    losses = [None] * (len(pricesList) - 1)
    curr_max = pricesList[len(pricesList) - 1]

    for i in range(len(pricesList) - 2, -1, -1):

        losses[i] = curr_max - pricesList[i]

        if curr_max < pricesList[i]:
            curr_max = pricesList[i]

    return max(losses)


class TestLargestPossibleLoss(unittest.TestCase):

    def test_general_largest_loss(self):
        l = [2, 1, 7, 3, 5, 6]
        loss = get_largest_possible_loss(l)
        self.assertEqual(loss, 6)

    def test_one_elem_assert(self):
        l = [5]
        with self.assertRaises(AssertionError):
            get_largest_possible_loss(l)

    def test_negative_elem(self):
        l = [-1, 6, 8]
        with self.assertRaises(AssertionError):
            get_largest_possible_loss(l)

    def test_loss_with_duplicates(self):
        l = [3, 3, 3, 3, 3]
        loss = get_largest_possible_loss(l)
        self.assertEqual(loss, 0)

    def test_loss_is_consistent(self):
        l = [4, 3, 7, 10, 2, 20]
        loss1 = get_largest_possible_loss(l)
        loss2 = get_largest_possible_loss(l)
        self.assertEqual(loss1, loss2)