import unittest
import lab6

class TestDLLPriorityQueue(unittest.TestCase):
    def test_unsortedpq_basic(self):
        pq = lab6.UnsortedPQ()
        self.assertTrue(pq.is_empty())
        self.assertEqual(repr(pq), "{}", "Empty UnsortedPQ repr should be '{}'")

        pq.insert(5, 'a')
        self.assertFalse(pq.is_empty())
        self.assertEqual(pq.min(), 'a', "UnsortedPQ.min() returned wrong value after first insert")

        pq.insert(3, 'b')
        pq.insert(7, 'c')
        self.assertEqual(pq.min(), 'b', "UnsortedPQ.min() did not find the smallest key")

        # remove_min should return the removed value (spec requirement)
        removed = pq.remove_min()
        # explicit check to point out missing return
        self.assertIsNotNone(removed, "UnsortedPQ.remove_min did not return the removed value (returned None). It should return the removed entry's value.")
        self.assertEqual(removed, 'b', "UnsortedPQ.remove_min returned incorrect value")

        # after removing min, new min should be 'a'
        self.assertEqual(pq.min(), 'a', "After removing min, UnsortedPQ.min() returned incorrect value")

        # remove remaining items
        pq.remove_min()
        pq.remove_min()
        self.assertTrue(pq.is_empty())

        # operations on empty queue should raise
        with self.assertRaises(Exception, msg="UnsortedPQ.min() should raise Exception on empty queue"):
            pq.min()
        with self.assertRaises(Exception, msg="UnsortedPQ.remove_min() should raise Exception on empty queue"):
            pq.remove_min()

    def test_sortedpq_basic(self):
        pq = lab6.SortedPQ()
        self.assertTrue(pq.is_empty())

        # first insert may trigger the empty-branch bug (uses new_node before creation).
        try:
            pq.insert(10, 'x')
        except Exception as e:
            self.fail(f"SortedPQ.insert raised an exception on empty queue. Likely bug: the empty-branch references 'new_node' before it's created. Exception: {e}")

        pq.insert(2, 'y')
        pq.insert(7, 'z')
        self.assertEqual(pq.min(), 'y', "SortedPQ.min() returned wrong smallest value after inserts")

        # remove_min should return and remove the smallest value
        val = pq.remove_min()
        self.assertEqual(val, 'y', "SortedPQ.remove_min() returned incorrect value")
        self.assertEqual(pq.min(), 'z', "After removing min, SortedPQ.min() returned incorrect next-min value")

        # emptying the queue then raising exceptions
        pq.remove_min()
        pq.remove_min()
        self.assertTrue(pq.is_empty())
        with self.assertRaises(Exception, msg="SortedPQ.min() should raise Exception on empty queue"):
            pq.min()
        with self.assertRaises(Exception, msg="SortedPQ.remove_min() should raise Exception on empty queue"):
            pq.remove_min()

if __name__ == "__main__":
    unittest.main()