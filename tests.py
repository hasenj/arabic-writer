from harf import *
from iterator import *
from main import *

import unittest

class TestIterator( unittest.TestCase ):
    def test_range(self):
        a = [1,4,7]        
        iter = Iterator(a)
        self.assertEqual( 1, iter.get() )
        self.assertEqual( 4, iter.peek_next() )
        self.assertEqual( None, iter.peek_prev() )
        self.assert_( not iter.in_range( -1 ) )
        self.assert_( iter.in_range() )
        self.assert_( iter.in_range( 0 ) )
        self.assert_( iter.in_range( 1 ) )
        self.assert_( iter.in_range( 2 ) )
        self.assert_( not iter.in_range( 3 ) )
        self.assertEqual( None, iter.peek_index(-1) )
        self.assertEqual( 1, iter.peek_index(0) )
        self.assertEqual( 4, iter.peek_index(1) )
        self.assertEqual( 7, iter.peek_index(2) )
        self.assertEqual( None, iter.peek_index(3) )
        iter.move()
        iter.move()
        self.assert_( iter.in_range() )
        iter.move()
        self.assert_( not iter.in_range() )
        iter.reset()
        self.assert_( iter.in_range() )
        
        
        
class TestHarf( unittest.TestCase ):
    def test_is_harf( self ):
        self.assert_( Harf.is_harf( u'\u0600' ) )
        self.assert_( Harf.is_harf( u'\u06FF' ) )
        self.assert_( Harf.is_harf( u'\uFE70' ) )
        self.assert_( Harf.is_harf( u'\uFEFF' ) )
        self.assert_( Harf.is_harf( u'أ' ) )
        self.assert_( Harf.is_harf( u'ب' ) )
        self.assert_( Harf.is_harf( u'ت' ) )
        self.assert_( Harf.is_harf( u'ع' ) )
        self.assert_( Harf.is_harf( u'ح' ) )
        self.assert_( Harf.is_harf( u'ي' ) )
        self.assert_( not Harf.is_harf( u'a' ) )
        self.assert_( not Harf.is_harf( u'v' ) )
        self.assert_( not Harf.is_harf( u'z' ) )
        self.assert_( not Harf.is_harf( u' ' ) )
        self.assert_( not Harf.is_harf( u'!' ) )
        self.assert_( not Harf.is_harf( u'=' ) )
    
    
if __name__ == '__main__':
    unittest.main()
    