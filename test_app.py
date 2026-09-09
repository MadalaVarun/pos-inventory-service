import os,tempfile,unittest
from app import add_product,sell,stock
class TestPOS(unittest.TestCase):
 def setUp(self): self.p=tempfile.mktemp(); add_product("A","Widget",2.5,5,self.p)
 def tearDown(self): os.path.exists(self.p) and os.remove(self.p)
 def test_sale(self): self.assertEqual(sell("A",2,self.p)["total"],5); self.assertEqual(stock("A",self.p),3)
 def test_no_oversell(self):
  with self.assertRaises(ValueError): sell("A",6,self.p)
  self.assertEqual(stock("A",self.p),5)
if __name__=="__main__": unittest.main()
