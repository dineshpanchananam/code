class Test:
  def call_me(self):
    return {
      "d": u'ko\u017eu\u0161\u010dek',
      "c": "d",
      "yu": "hu"
    }
  
  def test_me(self, snapshot):
    snapshot.assert_match(self.call_me())
    
  @staticmethod
  def abcd():
    return {"ab": "cd"}
  
  def test_abcd(self, snapshot):
    snapshot.assert_match(Test.abcd())